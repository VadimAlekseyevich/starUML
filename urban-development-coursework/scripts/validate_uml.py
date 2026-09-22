#!/usr/bin/env python3
"""Validate legacy StarUML XPD/XML projects used by this coursework."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

XPD_NS = "http://www.staruml.com"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def direct_name(obj: ET.Element) -> str | None:
    for child in obj:
        if local(child.tag) == "ATTR" and child.get("name") == "Name":
            return child.text or ""
    return None


def direct_ref(obj: ET.Element, field: str) -> str | None:
    for child in obj:
        if local(child.tag) == "REF" and child.get("name") == field:
            return (child.text or "").strip()
    return None


def collect_objects(root: ET.Element) -> tuple[dict[str, ET.Element], list[str]]:
    by_guid: dict[str, ET.Element] = {}
    duplicates: list[str] = []
    for el in root.iter():
        guid = el.get("guid")
        if not guid:
            continue
        if guid in by_guid:
            duplicates.append(guid)
        else:
            by_guid[guid] = el
    return by_guid, duplicates


def validate_refs(root: ET.Element, guids: set[str]) -> list[str]:
    missing: set[str] = set()
    for el in root.iter():
        if local(el.tag) != "REF":
            continue
        ref = (el.text or "").strip()
        if ref and ref not in guids:
            missing.add(ref)
    return sorted(missing)


def validate_collection_counts(root: ET.Element) -> list[str]:
    """Validate #Collection counters against direct Collection[i] children.

    Old StarUML files occasionally contain unusual constructs, so these are
    warnings by default and become errors only with --strict-counts.
    """
    warnings: list[str] = []
    for obj in root.iter():
        if local(obj.tag) != "OBJ":
            continue
        children = list(obj)
        counters: dict[str, int] = {}
        for ch in children:
            if local(ch.tag) != "ATTR":
                continue
            name = ch.get("name") or ""
            if not name.startswith("#"):
                continue
            try:
                counters[name[1:]] = int((ch.text or "0").strip())
            except ValueError:
                warnings.append(f"non-integer counter {name!r} on {obj.get('guid')}")
        for collection, expected in counters.items():
            rx = re.compile(rf"^{re.escape(collection)}\[(\d+)\]$")
            indices: list[int] = []
            for ch in children:
                child_name = ch.get("name") or ""
                m = rx.match(child_name)
                if m:
                    indices.append(int(m.group(1)))
            if len(indices) != expected:
                warnings.append(
                    f"{obj.get('guid')}: #{collection}={expected}, "
                    f"but {len(indices)} direct items found"
                )
            if indices and sorted(indices) != list(range(len(indices))):
                warnings.append(
                    f"{obj.get('guid')}: {collection} indices are not contiguous: "
                    f"{sorted(indices)}"
                )
    return warnings


def validate_registry(
    by_guid: dict[str, ET.Element], registry_path: Path
) -> list[str]:
    errors: list[str] = []
    data = json.loads(registry_path.read_text(encoding="utf-8"))

    for section in ("views", "entities", "diagrams"):
        for item in data.get(section, []):
            guid = item["guid"]
            expected_name = item["name"]
            obj = by_guid.get(guid)
            if obj is None:
                errors.append(f"registry {section}: missing GUID {guid} ({expected_name})")
                continue
            actual_name = direct_name(obj)
            if actual_name != expected_name:
                errors.append(
                    f"registry {section}: {guid} name mismatch: "
                    f"{actual_name!r} != {expected_name!r}"
                )

    for rel in data.get("relationships", []):
        guid = rel["guid"]
        obj = by_guid.get(guid)
        if obj is None:
            errors.append(f"registry relationship missing GUID {guid}")
            continue
        kind = rel["kind"]
        expected_type = "UMLInclude" if kind == "include" else "UMLExtend"
        actual_type = obj.get("type")
        if actual_type != expected_type:
            errors.append(
                f"relationship {guid}: type {actual_type!r} != {expected_type!r}"
            )
            continue
        base = direct_ref(obj, "Base")
        target_field = "Addition" if kind == "include" else "Extension"
        target = direct_ref(obj, target_field)
        if base != rel["base_guid"] or target != rel["target_guid"]:
            errors.append(
                f"relationship {guid}: registry endpoints do not match XML"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("uml", type=Path, help="StarUML .uml file")
    parser.add_argument("--registry", type=Path, help="model/registry.json")
    parser.add_argument(
        "--forbid",
        action="append",
        default=[],
        help="case-insensitive forbidden substring; may be repeated",
    )
    parser.add_argument("--strict-counts", action="store_true")
    args = parser.parse_args()

    raw = args.uml.read_bytes()
    errors: list[str] = []
    warnings: list[str] = []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        print(f"ERROR: XML parse failed: {exc}")
        return 2

    by_guid, duplicates = collect_objects(root)
    if duplicates:
        errors.append("duplicate GUIDs: " + ", ".join(sorted(set(duplicates))))

    missing = validate_refs(root, set(by_guid))
    if missing:
        errors.append("unresolved XPD:REF GUIDs: " + ", ".join(missing))

    counter_issues = validate_collection_counts(root)
    if args.strict_counts:
        errors.extend(counter_issues)
    else:
        warnings.extend(counter_issues)

    lower = raw.decode("utf-8", errors="replace").lower()
    for term in args.forbid:
        if term.lower() in lower:
            errors.append(f"forbidden substring found: {term!r}")

    if args.registry:
        errors.extend(validate_registry(by_guid, args.registry))

    type_counts = Counter(
        el.get("type")
        for el in root.iter()
        if local(el.tag) == "OBJ" and el.get("type")
    )

    print(f"File: {args.uml}")
    print(f"GUID objects: {len(by_guid)}")
    print(
        "Diagrams: "
        + ", ".join(
            f"{t}={type_counts[t]}"
            for t in (
                "UMLUseCaseDiagram",
                "UMLActivityDiagram",
                "UMLStatechartDiagram",
                "UMLClassDiagram",
                "UMLComponentDiagram",
                "UMLDeploymentDiagram",
                "UMLSequenceDiagram",
            )
            if type_counts[t]
        )
    )

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
