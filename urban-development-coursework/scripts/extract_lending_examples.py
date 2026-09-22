#!/usr/bin/env python3
"""Extract exact textual diagram fragments from legacy lending.uml.

The extractor deliberately uses a lightweight tag stack instead of
ElementTree serialization so the original StarUML text is preserved.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Node:
    start: int
    open_end: int
    end: int | None
    type: str
    guid: str


OBJ_RE = re.compile(r"<XPD:OBJ\b[^>]*>|</XPD:OBJ>")
TYPE_RE = re.compile(r'\btype="([^"]+)"')
GUID_RE = re.compile(r'\bguid="([^"]+)"')
NAME_RE = re.compile(
    r'<XPD:ATTR name="Name" type="string">([\s\S]*?)</XPD:ATTR>'
)

DEFAULT_SPECS = [
    ("use-case", "UMLUseCaseDiagram", "ApplyingForLoan", "applying_for_loan.fragment.xml"),
    ("activity", "UMLActivityDiagram", "ApplyingForLoan", "applying_for_loan.fragment.xml"),
    ("statechart", "UMLStatechartDiagram", "AuthorizationStatechartDiagramm", "authorization.fragment.xml"),
    ("class", "UMLClassDiagram", "ClassEntityDetailWithRelation", "entity_with_relation.fragment.xml"),
    ("component", "UMLComponentDiagram", "ClientServer", "client_server.fragment.xml"),
    ("deployment", "UMLDeploymentDiagram", "Lending", "lending.fragment.xml"),
    ("sequence", "UMLSequenceDiagram", "SequenceDiagram1", "sequence.fragment.xml"),
]


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
        stack.append(
            Node(
                start=m.start(),
                open_end=m.end(),
                end=None,
                type=type_match.group(1) if type_match else "",
                guid=guid_match.group(1) if guid_match else "",
            )
        )
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="path to lending.uml")
    parser.add_argument("output", type=Path, help="reference output directory")
    args = parser.parse_args()

    text = args.source.read_bytes().decode("utf-8")
    nodes = parse_nodes(text)

    source_map = []
    for directory, obj_type, wanted_name, filename in DEFAULT_SPECS:
        matches = [
            n
            for n in nodes
            if n.type == obj_type and node_name(text, n) == wanted_name
        ]
        if len(matches) != 1:
            raise ValueError(
                f"expected one {obj_type}/{wanted_name}, found {len(matches)}"
            )
        node = matches[0]
        assert node.end is not None
        target = args.output / directory / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        fragment = text[node.start : node.end] + "\n"
        target.write_text(fragment, encoding="utf-8", newline="")
        source_map.append(
            {
                "type": obj_type,
                "name": wanted_name,
                "guid": node.guid,
                "path": str(target.relative_to(args.output)),
                "chars": len(fragment),
            }
        )

    (args.output / "source-map.generated.json").write_text(
        json.dumps(
            {"source": str(args.source), "fragments": source_map},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Extracted {len(source_map)} reference fragments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
