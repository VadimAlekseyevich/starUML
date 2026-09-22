#!/usr/bin/env python3
"""Validate the canonical StarUML 7 project and coursework behavior model."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path


TOP_LEVEL_ACTIVITIES = {
    "ProjectCreation",
    "DataManagement",
    "ScenarioConfiguration",
    "ScenarioLaunch",
    "ScenarioComparison",
    "ResultExport",
}
DECOMPOSED_ACTIVITIES = {
    "DatasetImport",
    "DataQualityValidation",
    "ScenarioValidation",
    "GenerationExecution",
}
REQUIRED_ACTIVITIES = TOP_LEVEL_ACTIVITIES | DECOMPOSED_ACTIVITIES
REQUIRED_TOP_LEVEL = {
    "Создать проект",
    "Управление исходными геоданными",
    "Настроить сценарий развития",
    "Запустить сценарий развития",
    "Просмотр и сравнение сценариев",
    "Экспортировать результаты",
}
REQUIRED_RUN_STATES = {
    "Draft", "Validated", "Queued", "Running", "Completed", "Failed", "Cancelled"
}
REQUIRED_CALLS = {
    "DataManagement": {"DatasetImport", "DataQualityValidation"},
    "ScenarioConfiguration": {"ScenarioValidation"},
    "ScenarioLaunch": {"ScenarioValidation", "GenerationExecution"},
}

ACTION_TYPES = {"UMLAction", "UMLCallBehaviorAction"}
ACTIVITY_NODE_VIEW_TYPES = {"UMLActionView", "UMLControlNodeView"}
STATE_NODE_VIEW_TYPES = {"UMLStateView", "UMLPseudostateView"}


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def activity_nodes(activity):
    result = list(activity.get("nodes", []))
    for group in activity.get("groups", []):
        result.extend(group.get("nodes", []))
    return result


def rect(view):
    left = float(view.get("left", 0))
    top = float(view.get("top", 0))
    width = float(view.get("width", 0))
    height = float(view.get("height", 0))
    return left, top, left + width, top + height


def overlaps(a, b, pad=0.0):
    al, at, ar, ab = rect(a)
    bl, bt, br, bb = rect(b)
    return (
        al < br + pad
        and ar > bl - pad
        and at < bb + pad
        and ab > bt - pad
    )


def node_gap(a, b):
    al, at, ar, ab = rect(a)
    bl, bt, br, bb = rect(b)
    hgap = max(0.0, max(bl - ar, al - br))
    vgap = max(0.0, max(bt - ab, at - bb))
    return math.hypot(hgap, vgap)


def visible_edge_labels(diagram, edge_type):
    labels = []
    for edge_view in diagram.get("ownedViews", []):
        if edge_view.get("_type") != edge_type:
            continue
        for sub in edge_view.get("subViews", []):
            if (
                sub.get("_type") == "EdgeLabelView"
                and sub.get("visible") is not False
                and str(sub.get("text") or "").strip()
            ):
                labels.append(sub)
    return labels


def check_diagram_spacing(errors, name, diagram, node_types, edge_type):
    views = diagram.get("ownedViews", [])
    nodes = [v for v in views if v.get("_type") in node_types]
    labels = visible_edge_labels(diagram, edge_type)

    # Deliberately conservative: label rectangles must not touch model nodes.
    for label in labels:
        for node in nodes:
            if overlaps(label, node, pad=4):
                errors.append(
                    f"{name}: edge label {label.get('text')!r} overlaps a node view"
                )

    for index, left in enumerate(labels):
        for right in labels[index + 1 :]:
            if overlaps(left, right, pad=2):
                errors.append(
                    f"{name}: edge labels overlap: "
                    f"{left.get('text')!r} / {right.get('text')!r}"
                )

    # Prevent the layout from drifting back to the very dense first version.
    for index, left in enumerate(nodes):
        for right in nodes[index + 1 :]:
            if node_gap(left, right) < 40:
                errors.append(f"{name}: node views are closer than 40 px")
                return


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mdj", type=Path)
    ap.add_argument("--traceability", type=Path, required=True)
    args = ap.parse_args()

    project = json.loads(args.mdj.read_text(encoding="utf-8"))
    trace = json.loads(args.traceability.read_text(encoding="utf-8"))
    objects = list(walk(project))

    errors: list[str] = []

    ids = [o["_id"] for o in objects if isinstance(o, dict) and "_id" in o]
    counts = Counter(ids)
    duplicates = sorted(x for x, n in counts.items() if n > 1)
    if duplicates:
        errors.append(f"duplicate _id values: {len(duplicates)}")

    known = set(ids)
    refs = [
        o["$ref"]
        for o in objects
        if isinstance(o, dict) and isinstance(o.get("$ref"), str)
    ]
    unresolved = sorted(set(refs) - known)
    if unresolved:
        errors.append(f"unresolved $ref values: {len(unresolved)}")

    logical = next(
        (
            o
            for o in project.get("ownedElements", [])
            if o.get("_type") == "UMLModel" and o.get("name") == "Logical View"
        ),
        None,
    )
    if logical is None:
        errors.append("Logical View not found")
        activities = []
        state_machines = []
    else:
        activities = [
            x for x in logical.get("ownedElements", [])
            if x.get("_type") == "UMLActivity"
        ]
        state_machines = [
            x for x in logical.get("ownedElements", [])
            if x.get("_type") == "UMLStateMachine"
        ]

    activity_by_name = {a.get("name"): a for a in activities}
    activity_by_id = {a.get("_id"): a for a in activities}

    missing = sorted(REQUIRED_ACTIVITIES - set(activity_by_name))
    if missing:
        errors.append("missing Activity models: " + ", ".join(missing))

    for name in sorted(REQUIRED_ACTIVITIES & set(activity_by_name)):
        activity = activity_by_name[name]
        diagrams = [
            x for x in activity.get("ownedElements", [])
            if x.get("_type") == "UMLActivityDiagram"
        ]
        if len(diagrams) != 1:
            errors.append(f"{name}: expected exactly one UMLActivityDiagram")

        nodes = activity_nodes(activity)
        edges = activity.get("edges", [])
        node_ids = {n.get("_id") for n in nodes}

        if not any(x.get("_type") == "UMLInitialNode" for x in nodes):
            errors.append(f"{name}: no initial node")
        if not any(x.get("_type") == "UMLActivityFinalNode" for x in nodes):
            errors.append(f"{name}: no activity final node")
        if len(activity.get("groups", [])) < 2:
            errors.append(f"{name}: expected at least two swimlane partitions")

        incoming = Counter(
            edge.get("target", {}).get("$ref")
            for edge in edges
            if edge.get("target", {}).get("$ref") in node_ids
        )
        for node in nodes:
            node_name = node.get("name") or node.get("_id")
            doc = (node.get("documentation") or "").strip()
            if not doc:
                errors.append(f"{name}: undocumented node {node_name}")

            if node.get("_type") in ACTION_TYPES:
                if incoming.get(node.get("_id"), 0) != 1:
                    errors.append(
                        f"{name}: Action {node_name!r} must have exactly one incoming "
                        f"control flow, got {incoming.get(node.get('_id'), 0)}"
                    )
                if len(doc) < 80:
                    errors.append(
                        f"{name}: Action {node_name!r} documentation is too terse "
                        f"({len(doc)} chars; expected implementation-level explanation)"
                    )

            if node.get("_type") == "UMLCallBehaviorAction":
                behavior_id = node.get("behavior", {}).get("$ref")
                if behavior_id not in activity_by_id:
                    errors.append(
                        f"{name}: call behavior {node_name!r} points to "
                        f"unknown Activity {behavior_id!r}"
                    )

        for edge in edges:
            doc = (edge.get("documentation") or "").strip()
            if not doc:
                errors.append(f"{name}: undocumented control flow {edge.get('_id')}")
            elif len(doc) < 100:
                errors.append(
                    f"{name}: control-flow documentation is too terse "
                    f"for {edge.get('_id')} ({len(doc)} chars)"
                )

            guard = (edge.get("guard") or "").strip().lower()
            if guard in {"да", "нет", "yes", "no"}:
                errors.append(f"{name}: non-semantic guard {guard!r}")

        decision_ids = {
            x.get("_id") for x in nodes if x.get("_type") == "UMLDecisionNode"
        }
        for decision_id in decision_ids:
            outgoing = [
                e for e in edges
                if e.get("source", {}).get("$ref") == decision_id
            ]
            if len(outgoing) >= 2:
                guards = [(e.get("guard") or "").strip() for e in outgoing]
                if any(not guard for guard in guards):
                    errors.append(
                        f"{name}: decision {decision_id} has an outgoing flow "
                        "without a guard"
                    )
                if sum(guard.lower() == "else" for guard in guards) > 1:
                    errors.append(
                        f"{name}: decision {decision_id} has more than one else branch"
                    )

        if len(diagrams) == 1:
            check_diagram_spacing(
                errors,
                name,
                diagrams[0],
                ACTIVITY_NODE_VIEW_TYPES,
                "UMLControlFlowView",
            )

    # Check that the intended decompositions are actually called, not merely present.
    for caller_name, required_targets in REQUIRED_CALLS.items():
        caller = activity_by_name.get(caller_name)
        if caller is None:
            continue
        called_ids = {
            node.get("behavior", {}).get("$ref")
            for node in activity_nodes(caller)
            if node.get("_type") == "UMLCallBehaviorAction"
        }
        called_names = {
            activity_by_id[target].get("name")
            for target in called_ids
            if target in activity_by_id
        }
        missing_calls = sorted(required_targets - called_names)
        if missing_calls:
            errors.append(
                f"{caller_name}: missing call-behavior decomposition(s): "
                + ", ".join(missing_calls)
            )

    lifecycle = next(
        (x for x in state_machines if x.get("name") == "GenerationRunLifecycle"),
        None,
    )
    if lifecycle is None:
        errors.append("GenerationRunLifecycle state machine not found")
    else:
        states = {
            v.get("name")
            for region in lifecycle.get("regions", [])
            for v in region.get("vertices", [])
            if v.get("_type") == "UMLState"
        }
        missing_states = sorted(REQUIRED_RUN_STATES - states)
        if missing_states:
            errors.append(
                "GenerationRunLifecycle missing states: " + ", ".join(missing_states)
            )

        for region in lifecycle.get("regions", []):
            for transition in region.get("transitions", []):
                if not (transition.get("documentation") or "").strip():
                    errors.append(
                        "GenerationRunLifecycle: undocumented transition "
                        + str(transition.get("_id"))
                    )

        state_diagrams = [
            x for x in lifecycle.get("ownedElements", [])
            if x.get("_type") == "UMLStatechartDiagram"
        ]
        if len(state_diagrams) != 1:
            errors.append(
                "GenerationRunLifecycle: expected exactly one UMLStatechartDiagram"
            )
        else:
            check_diagram_spacing(
                errors,
                "GenerationRunLifecycle",
                state_diagrams[0],
                STATE_NODE_VIEW_TYPES,
                "UMLTransitionView",
            )

    entries = trace.get("main_diagram", {}).get("entries", [])
    entry_names = {e.get("name") for e in entries}
    if REQUIRED_TOP_LEVEL - entry_names:
        errors.append("traceability is missing top-level Use Cases")
    for entry in entries:
        if entry.get("name") in REQUIRED_TOP_LEVEL:
            behavior = entry.get("behavior_diagram")
            if not behavior:
                errors.append(
                    f"traceability: {entry.get('name')} has no behavior_diagram"
                )
            elif behavior not in activity_by_name:
                errors.append(
                    f"traceability: {entry.get('name')} points to unknown Activity "
                    f"{behavior}"
                )

    decomposition_names = {
        item.get("name")
        for item in trace.get("algorithm_model", {}).get("decompositions", [])
    }
    missing_trace_decompositions = sorted(
        DECOMPOSED_ACTIVITIES - decomposition_names
    )
    if missing_trace_decompositions:
        errors.append(
            "traceability is missing algorithm decompositions: "
            + ", ".join(missing_trace_decompositions)
        )

    print("StarUML 7 coursework audit")
    print(f"  model ids: {len(known)}")
    print(f"  references: {len(refs)}")
    print(f"  activities: {len(activities)}")
    print(
        "  required algorithm activities: "
        f"{len(REQUIRED_ACTIVITIES & set(activity_by_name))}/{len(REQUIRED_ACTIVITIES)}"
    )
    print(
        "  top-level behavior mappings: "
        f"{sum(1 for e in entries if e.get('name') in REQUIRED_TOP_LEVEL and e.get('behavior_diagram'))}/"
        f"{len(REQUIRED_TOP_LEVEL)}"
    )
    print(f"  lifecycle state machine: {'yes' if lifecycle else 'no'}")

    if errors:
        print(f"ERRORS: {len(errors)}")
        for error in errors:
            print("  * " + error)
        return 2

    print(
        "OK: canonical MDJ, decomposition, documentation, layout and "
        "traceability are consistent"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
