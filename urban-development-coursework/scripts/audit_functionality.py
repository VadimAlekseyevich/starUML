#!/usr/bin/env python3
"""Methodology-oriented audit of the current functionality model."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def direct_name(obj: ET.Element) -> str:
    for ch in obj:
        if local(ch.tag) == "ATTR" and ch.get("name") == "Name":
            return ch.text or ""
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("uml", type=Path)
    parser.add_argument("--traceability", type=Path)
    args = parser.parse_args()

    raw = args.uml.read_text(encoding="utf-8")
    root = ET.fromstring(raw)

    by_guid: dict[str, ET.Element] = {}
    parents: dict[ET.Element, ET.Element] = {}
    for parent in root.iter():
        for child in parent:
            parents[child] = parent
        guid = parent.get("guid")
        if guid:
            by_guid[guid] = parent

    diagrams = [
        x for x in root.iter()
        if local(x.tag) == "OBJ" and x.get("type") == "UMLUseCaseDiagram"
    ]
    main_diagram = next((x for x in diagrams if direct_name(x) == "UrbanDevelopment"), None)
    if main_diagram is None:
        print("ERROR: UrbanDevelopment main Use Case Diagram not found")
        return 2

    model_guids: set[str] = set()
    view_type_counts: dict[str, int] = {}
    for x in main_diagram.iter():
        if local(x.tag) == "OBJ":
            t = x.get("type") or ""
            view_type_counts[t] = view_type_counts.get(t, 0) + 1
        if local(x.tag) == "REF" and x.get("name") == "Model":
            if x.text:
                model_guids.add(x.text.strip())

    main_use_cases = []
    for guid in model_guids:
        obj = by_guid.get(guid)
        if obj is not None and obj.get("type") == "UMLUseCase":
            main_use_cases.append((guid, direct_name(obj)))
    main_use_cases.sort(key=lambda x: x[1])

    documentation_count = raw.count('<XPD:ATTR name="Documentation"')
    attachment_count = raw.count('<XPD:ATTR name="Attachments"')
    condition_count = raw.count('<XPD:ATTR name="Condition"')
    generic_condition_count = raw.count("Выполнение дополнительного условия сценария")

    print("Methodology functionality audit")
    print(f"Main diagram: UrbanDevelopment")
    print(f"Main Use Cases: {len(main_use_cases)}")
    for guid, name in main_use_cases:
        print(f"  - {name} [{guid}]")

    warnings: list[str] = []
    if not 3 <= len(main_use_cases) <= 9:
        warnings.append(
            "P0104: main diagram normally contains 3-9 relatively independent Use Cases"
        )

    include_views = view_type_counts.get("UMLIncludeView", 0)
    extend_views = view_type_counts.get("UMLExtendView", 0)
    if include_views or extend_views:
        warnings.append(
            "P0105: main diagram contains dependency views "
            f"(include={include_views}, extend={extend_views}); review partial decomposition"
        )

    if documentation_count == 0:
        warnings.append("P0149: no Documentation attributes found")

    if attachment_count == 0:
        warnings.append("P0164: no Attachments attributes found")

    if generic_condition_count:
        warnings.append(
            "P0161-P0163: generic extend Condition placeholders remain: "
            f"{generic_condition_count}/{condition_count}"
        )

    if args.traceability:
        tr = json.loads(args.traceability.read_text(encoding="utf-8"))
        declared = {x["guid"]: x for x in tr["main_diagram"]["entries"]}
        actual = {guid for guid, _ in main_use_cases}
        for guid in actual:
            if guid not in declared:
                warnings.append(f"traceability: main Use Case {guid} missing from traceability.json")
        for guid, item in declared.items():
            if guid not in actual:
                warnings.append(
                    f"traceability: {item['name']} declared as main entry but not rendered on main diagram"
                )
        for item in tr["main_diagram"]["entries"]:
            if item.get("classification") == "top_level":
                if not item.get("decomposition_diagram"):
                    warnings.append(
                        "P0139: top-level Use Case lacks decomposition mapping: "
                        + item["name"]
                    )
                if not item.get("behavior_diagram"):
                    warnings.append(
                        "P0220/P0225: top-level Use Case lacks behavior mapping: "
                        + item["name"]
                    )

    print()
    if warnings:
        print(f"WARNINGS: {len(warnings)}")
        for w in warnings:
            print("  * " + w)
    else:
        print("OK: no methodology warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
