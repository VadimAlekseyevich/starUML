#!/usr/bin/env python3
"""Validate the canonical StarUML 7 MDJ and phase-2 behavior coverage."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_ACTIVITIES = {
    "ProjectCreation",
    "DataManagement",
    "ScenarioConfiguration",
    "ScenarioLaunch",
    "ScenarioComparison",
    "ResultExport",
    "GenerationExecution",
}
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


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


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
    refs = [o["$ref"] for o in objects if isinstance(o, dict) and isinstance(o.get("$ref"), str)]
    unresolved = sorted(set(refs) - known)
    if unresolved:
        errors.append(f"unresolved $ref values: {len(unresolved)}")

    logical = next(
        (o for o in project.get("ownedElements", [])
         if o.get("_type") == "UMLModel" and o.get("name") == "Logical View"),
        None,
    )
    if logical is None:
        errors.append("Logical View not found")
        activities = []
        state_machines = []
    else:
        activities = [x for x in logical.get("ownedElements", []) if x.get("_type") == "UMLActivity"]
        state_machines = [x for x in logical.get("ownedElements", []) if x.get("_type") == "UMLStateMachine"]

    activity_by_name = {a.get("name"): a for a in activities}
    missing = sorted(REQUIRED_ACTIVITIES - set(activity_by_name))
    if missing:
        errors.append("missing Activity models: " + ", ".join(missing))

    for name in sorted(REQUIRED_ACTIVITIES & set(activity_by_name)):
        activity = activity_by_name[name]
        diagrams = [x for x in activity.get("ownedElements", []) if x.get("_type") == "UMLActivityDiagram"]
        if len(diagrams) != 1:
            errors.append(f"{name}: expected exactly one UMLActivityDiagram")
        nodes = list(activity.get("nodes", []))
        for group in activity.get("groups", []):
            nodes.extend(group.get("nodes", []))
        edges = activity.get("edges", [])

        if not any(x.get("_type") == "UMLInitialNode" for x in nodes):
            errors.append(f"{name}: no initial node")
        if not any(x.get("_type") == "UMLActivityFinalNode" for x in nodes):
            errors.append(f"{name}: no activity final node")
        if len(activity.get("groups", [])) < 2:
            errors.append(f"{name}: expected at least two swimlane partitions")

        for node in nodes:
            if not (node.get("documentation") or "").strip():
                errors.append(f"{name}: undocumented node {node.get('name') or node.get('_id')}")
        for edge in edges:
            if not (edge.get("documentation") or "").strip():
                errors.append(f"{name}: undocumented control flow {edge.get('_id')}")
            guard = (edge.get("guard") or "").strip().lower()
            if guard in {"да", "нет", "yes", "no"}:
                errors.append(f"{name}: non-semantic guard {guard!r}")

        decision_ids = {x.get("_id") for x in nodes if x.get("_type") == "UMLDecisionNode"}
        for did in decision_ids:
            outgoing = [e for e in edges if e.get("source", {}).get("$ref") == did]
            if len(outgoing) >= 2 and any(not (e.get("guard") or "").strip() for e in outgoing):
                errors.append(f"{name}: decision {did} has an outgoing flow without a guard")

    lifecycle = next((x for x in state_machines if x.get("name") == "GenerationRunLifecycle"), None)
    if lifecycle is None:
        errors.append("GenerationRunLifecycle state machine not found")
    else:
        states = {
            v.get("name")
            for r in lifecycle.get("regions", [])
            for v in r.get("vertices", [])
            if v.get("_type") == "UMLState"
        }
        missing_states = sorted(REQUIRED_RUN_STATES - states)
        if missing_states:
            errors.append("GenerationRunLifecycle missing states: " + ", ".join(missing_states))

    entries = trace.get("main_diagram", {}).get("entries", [])
    entry_names = {e.get("name") for e in entries}
    if REQUIRED_TOP_LEVEL - entry_names:
        errors.append("traceability is missing top-level Use Cases")
    for e in entries:
        if e.get("name") in REQUIRED_TOP_LEVEL:
            behavior = e.get("behavior_diagram")
            if not behavior:
                errors.append(f"traceability: {e.get('name')} has no behavior_diagram")
            elif behavior not in activity_by_name:
                errors.append(f"traceability: {e.get('name')} points to unknown Activity {behavior}")

    print("StarUML 7 coursework audit")
    print(f"  model ids: {len(known)}")
    print(f"  references: {len(refs)}")
    print(f"  activities: {len(activities)}")
    print(f"  top-level behavior mappings: {sum(1 for e in entries if e.get('name') in REQUIRED_TOP_LEVEL and e.get('behavior_diagram'))}")
    print(f"  lifecycle state machine: {'yes' if lifecycle else 'no'}")

    if errors:
        print(f"ERRORS: {len(errors)}")
        for error in errors:
            print("  * " + error)
        return 2

    print("OK: canonical MDJ and algorithm coverage are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
