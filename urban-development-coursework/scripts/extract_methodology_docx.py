#!/usr/bin/env python3
"""Extract a DOCX methodology into stable Markdown + JSON using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
W = f"{{{W_NS}}}"
R = f"{{{R_NS}}}"


def paragraph_text(p: ET.Element) -> str:
    out: list[str] = []
    for el in p.iter():
        if el.tag == W + "t":
            out.append(el.text or "")
        elif el.tag == W + "tab":
            out.append("\t")
        elif el.tag == W + "br":
            out.append("\n")
    return "".join(out).strip()


def paragraph_style_id(p: ET.Element) -> str | None:
    ppr = p.find(W + "pPr")
    if ppr is None:
        return None
    style = ppr.find(W + "pStyle")
    if style is None:
        return None
    return style.get(W + "val")


def load_style_names(zf: zipfile.ZipFile) -> dict[str, str]:
    try:
        root = ET.fromstring(zf.read("word/styles.xml"))
    except KeyError:
        return {}
    result: dict[str, str] = {}
    for style in root.findall(W + "style"):
        sid = style.get(W + "styleId")
        name = style.find(W + "name")
        if sid and name is not None:
            result[sid] = name.get(W + "val") or sid
    return result


def heading_level(style_name: str | None) -> int | None:
    if not style_name:
        return None
    s = style_name.strip().lower()
    for pattern in (r"^heading\s*([1-9])$", r"^заголовок\s*([1-9])$"):
        m = re.match(pattern, s)
        if m:
            return int(m.group(1))
    return None


def cell_text(tc: ET.Element) -> str:
    parts = [paragraph_text(p) for p in tc.findall(".//" + W + "p")]
    return " ".join(x for x in parts if x).strip()


def escape_md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>").strip()


def extract_media(zf: zipfile.ZipFile, output_dir: Path) -> list[dict[str, object]]:
    media_dir = output_dir / "media"
    if media_dir.exists():
        shutil.rmtree(media_dir)
    media_dir.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, object]] = []
    for name in sorted(zf.namelist()):
        if not name.startswith("word/media/") or name.endswith("/"):
            continue
        data = zf.read(name)
        target = media_dir / Path(name).name
        target.write_bytes(data)
        items.append({"zip_path": name, "file": f"media/{target.name}", "size_bytes": len(data)})
    return items


def extract_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    try:
        root = ET.fromstring(zf.read("word/_rels/document.xml.rels"))
    except KeyError:
        return {}
    result: dict[str, str] = {}
    for rel in root.findall(f"{{{REL_NS}}}Relationship"):
        rid = rel.get("Id")
        target = rel.get("Target")
        if rid and target:
            result[rid] = target
    return result


def drawing_refs(p: ET.Element) -> list[str]:
    refs: list[str] = []
    for blip in p.iter():
        if blip.tag.endswith("}blip"):
            rid = blip.get(R + "embed")
            if rid:
                refs.append(rid)
    return refs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = args.output_dir / "methodology-extract.md"
    index_path = args.output_dir / "methodology-index.json"

    with zipfile.ZipFile(args.docx) as zf:
        styles = load_style_names(zf)
        rels = extract_relationships(zf)
        media = extract_media(zf, args.output_dir)
        document = ET.fromstring(zf.read("word/document.xml"))

    body = document.find(W + "body")
    if body is None:
        raise RuntimeError("word/document.xml has no w:body")

    blocks: list[dict[str, object]] = []
    md: list[str] = [
        "# Извлечение методички",
        "",
        f"Источник: {args.docx.name}.",
        "",
        "> Этот файл создаётся автоматически. Интерпретация требований находится уровнем выше в methodology/*.md.",
        "",
    ]

    p_no = 0
    t_no = 0
    for child in list(body):
        if child.tag == W + "p":
            text = paragraph_text(child)
            refs = drawing_refs(child)
            if not text and not refs:
                continue
            p_no += 1
            pid = f"P{p_no:04d}"
            sid = paragraph_style_id(child)
            sname = styles.get(sid, sid or "")
            level = heading_level(sname)
            blocks.append({
                "id": pid,
                "type": "paragraph",
                "style_id": sid,
                "style_name": sname,
                "heading_level": level,
                "text": text,
                "drawing_rel_ids": refs,
                "drawing_targets": [rels.get(x) for x in refs if rels.get(x)],
            })
            if level and text:
                md.append(f"{'#' * min(level + 1, 6)} {text}")
                md.append(f"<!-- {pid}; style={sname} -->")
            else:
                if text:
                    md.append(f"**[{pid}]** {text}")
                if refs:
                    targets = ", ".join(rels.get(x, x) for x in refs)
                    md.append(f"<!-- {pid}; drawings: {targets} -->")
            md.append("")

        elif child.tag == W + "tbl":
            t_no += 1
            tid = f"T{t_no:04d}"
            rows: list[list[str]] = []
            for tr in child.findall(W + "tr"):
                row = [cell_text(tc) for tc in tr.findall(W + "tc")]
                rows.append(row)
            width = max((len(r) for r in rows), default=0)
            normalized = [r + [""] * (width - len(r)) for r in rows]
            blocks.append({"id": tid, "type": "table", "rows": normalized})
            md.extend([f"### Таблица {tid}", ""])
            if width:
                header = normalized[0]
                md.append("| " + " | ".join(escape_md_cell(x) for x in header) + " |")
                md.append("| " + " | ".join("---" for _ in range(width)) + " |")
                for row in normalized[1:]:
                    md.append("| " + " | ".join(escape_md_cell(x) for x in row) + " |")
            md.append("")

    markdown_path.write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")
    index = {
        "source_file": args.docx.name,
        "paragraph_count": p_no,
        "table_count": t_no,
        "media_count": len(media),
        "styles": styles,
        "relationships": rels,
        "blocks": blocks,
        "media": media,
    }
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        "# Автоматически извлечённая методичка\n\n"
        "- methodology-extract.md — последовательный текст и таблицы с ID абзацев.\n"
        "- methodology-index.json — структурированный индекс блоков/стилей.\n"
        "- media/ — встроенные изображения DOCX.\n\n"
        "Не редактировать эти файлы вручную: они пересоздаются extractor-скриптом.\n",
        encoding="utf-8",
    )

    print(f"Extracted paragraphs={p_no}, tables={t_no}, media={len(media)} to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
