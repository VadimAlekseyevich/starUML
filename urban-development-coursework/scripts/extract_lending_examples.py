#!/usr/bin/env python3
"""Extract exact textual diagram fragments from legacy lending.uml.

Two layers are produced:
1. curated fragments in reference/<type>/ are maintained manually;
2. generated/all-diagrams/ contains every diagram object from lending.uml.

The extractor deliberately avoids XML re-serialization so StarUML text is
preserved exactly as it appears in the source file.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Node:
    start: int
    open_end: int
    end: int | None
    type: str
    guid: str
    parent: "Node | None" = None


OBJ_RE = re.compile(r"<XPD:OBJ\b[^>]*>|</XPD:OBJ>")
TYPE_RE = re.compile(r'\btype="([^"]+)"')
GUID_RE = re.compile(r'\bguid="([^"]+)"')
NAME_RE = re.compile(
    r'<XPD:ATTR name="Name" type="string">([\s\S]*?)</XPD:ATTR>'
)

DIAGRAM_TYPES = {
    "UMLUseCaseDiagram": "use-case",
    "UMLActivityDiagram": "activity",
    "UMLStatechartDiagram": "statechart",
    "UMLClassDiagram": "class",
    "UMLComponentDiagram": "component",
    "UMLDeploymentDiagram": "deployment",
    "UMLSequenceDiagram": "sequence",
}

OWNER_TYPES = {
    "UMLModel",
    "UMLPackage",
    "UMLActivityGraph",
    "UMLStateMachine",
    "UMLCollaborationInstanceSet",
    "UMLInteractionInstanceSet",
}


def parse_nodes(text: str) -> list[Node]:
    stack: list[Node] = []
    nodes: list[Node] = []
    for m in OBJ_RE.finditer(text):
        token = m.group(0)
        if token.startswith("</"):
            if not stack:
                raise ValueError(f"unbalanced closing tag at {m.start()}")
            node = stack.pop()
            node.end = m.end()
            nodes.append(node)
            continue

        type_match = TYPE_RE.search(token)
        guid_match = GUID_RE.search(token)
        parent = stack[-1] if stack else None
        node = Node(
            start=m.start(),
            open_end=m.end(),
            end=None,
            type=type_match.group(1) if type_match else "",
            guid=guid_match.group(1) if guid_match else "",
            parent=parent,
        )
        stack.append(node)

    if stack:
        raise ValueError("unclosed XPD:OBJ elements")
    return nodes


def node_name(text: str, node: Node) -> str:
    assert node.end is not None
    body = text[node.open_end : node.end]
    first_child = body.find("<XPD:OBJ")
    head = body if first_child < 0 else body[:first_child]
    m = NAME_RE.search(head)
    return m.group(1) if m else ""


def owner_chain(text: str, node: Node) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    p = node.parent
    while p is not None:
        if p.type in OWNER_TYPES:
            name = node_name(text, p)
            if name:
                result.append({"type": p.type, "name": name, "guid": p.guid})
        p = p.parent
    result.reverse()
    return result


def slug(value: str) -> str:
    ascii_value = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    ascii_value = re.sub(r"[^a-z0-9]+", "_", ascii_value).strip("_")
    return ascii_value or "unnamed"


def filename_for(text: str, node: Node, used: set[str]) -> str:
    name = node_name(text, node) or "Main"
    chain = owner_chain(text, node)
    owner = chain[-1]["name"] if chain else "root"
    base = f"{slug(owner)}__{slug(name)}"
    filename = base + ".fragment.xml"
    if filename in used:
        suffix = re.sub(r"[^A-Za-z0-9]", "", node.guid)[:8] or "dup"
        filename = f"{base}__{suffix}.fragment.xml"
    used.add(filename)
    return filename


def write_all(text: str, nodes: list[Node], output: Path) -> list[dict[str, object]]:
    generated = output / "generated" / "all-diagrams"
    if generated.exists():
        shutil.rmtree(generated)
    generated.mkdir(parents=True, exist_ok=True)

    catalog: list[dict[str, object]] = []
    used_by_dir: dict[str, set[str]] = {}

    diagrams = [n for n in nodes if n.type in DIAGRAM_TYPES]
    diagrams.sort(key=lambda n: n.start)

    for node in diagrams:
        assert node.end is not None
        category = DIAGRAM_TYPES[node.type]
        category_dir = generated / category
        category_dir.mkdir(parents=True, exist_ok=True)
        used = used_by_dir.setdefault(category, set())
        filename = filename_for(text, node, used)
        target = category_dir / filename
        fragment = text[node.start : node.end] + "\n"
        target.write_text(fragment, encoding="utf-8", newline="")

        catalog.append(
            {
                "category": category,
                "type": node.type,
                "name": node_name(text, node),
                "guid": node.guid,
                "owners": owner_chain(text, node),
                "path": str(target.relative_to(output)).replace("\\", "/"),
                "chars": len(fragment),
            }
        )

    counts: dict[str, int] = {}
    for item in catalog:
        counts[item["category"]] = counts.get(item["category"], 0) + 1

    (generated / "catalog.json").write_text(
        json.dumps(
            {"source": "lending.uml", "counts": counts, "diagrams": catalog},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    md = [
        "# Все диаграммы lending.uml",
        "",
        "Каталог создаётся автоматически из исходного lending.uml без XML-пересериализации.",
        "",
        "| Тип | Количество |",
        "|---|---:|",
    ]
    for category in sorted(counts):
        md.append(f"| {category} | {counts[category]} |")
    md += ["", "## Фрагменты", ""]
    for item in catalog:
        owners = " → ".join(x["name"] for x in item["owners"])
        md.append(
            f"- **{item['category']} / {item['name']}** — "
            f"[fragment](../../{item['path']}); "
            f"owner: {owners or 'root'}; GUID: `{item['guid']}`."
        )
    (generated / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return catalog


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="path to lending.uml")
    parser.add_argument("output", type=Path, help="reference output directory")
    args = parser.parse_args()

    text = args.source.read_bytes().decode("utf-8")
    nodes = parse_nodes(text)
    catalog = write_all(text, nodes, args.output)
    print(f"Extracted {len(catalog)} diagram fragments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
