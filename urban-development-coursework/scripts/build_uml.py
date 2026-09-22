#!/usr/bin/env python3
"""Assemble the coursework StarUML project from ordered safe fragments."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_basic(raw: bytes) -> tuple[int, int]:
    root = ET.fromstring(raw)
    guids: set[str] = set()
    duplicate_count = 0
    for el in root.iter():
        guid = el.get("guid")
        if not guid:
            continue
        if guid in guids:
            duplicate_count += 1
        guids.add(guid)

    unresolved: set[str] = set()
    for el in root.iter():
        if local(el.tag) != "REF":
            continue
        ref = (el.text or "").strip()
        if ref and ref not in guids:
            unresolved.add(ref)

    if duplicate_count or unresolved:
        raise ValueError(
            f"basic validation failed: duplicate GUIDs={duplicate_count}, "
            f"unresolved refs={len(unresolved)}"
        )
    return len(guids), len(unresolved)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "manifest",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "fragments" / "manifest.json",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    manifest = args.manifest.resolve()
    cfg = json.loads(manifest.read_text(encoding="utf-8"))
    fragment_dir = manifest.parent

    chunks: list[bytes] = []
    for rel in cfg["parts"]:
        part = fragment_dir / rel
        if not part.exists():
            raise FileNotFoundError(part)
        chunks.append(part.read_bytes())

    raw = b"".join(chunks)
    guid_count, _ = validate_basic(raw)

    output = args.output.resolve() if args.output else (fragment_dir / cfg["output"]).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(raw)

    print(f"Built: {output}")
    print(f"Parts: {len(chunks)}")
    print(f"Bytes: {len(raw)}")
    print(f"GUID objects: {guid_count}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, ET.ParseError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
