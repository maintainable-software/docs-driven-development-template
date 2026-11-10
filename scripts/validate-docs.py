#!/usr/bin/env python3
"""Validate this repository's docs contract, not universal OKF conformance."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml


MARKDOWN = MarkdownIt("commonmark").enable("table")
RESERVED = {"index.md", "log.md"}


def normalize(value):
    return " ".join(value.split())


def inline_text(tokens):
    """Visible text, preserving breaks for index field labels; ignore markup."""
    return "".join(
        "\n" if token.type in {"softbreak", "hardbreak"} else token.content
        for token in tokens
        if token.type in {"text", "code_inline", "softbreak", "hardbreak"}
    )


def valid_tags(value):
    return (
        isinstance(value, list)
        and bool(value)
        and all(
            isinstance(tag, str)
            and bool(tag)
            and all(char.isalnum() or char in "_-/" for char in tag)
            and all(tag.split("/"))
            and not tag.isdecimal()
            for tag in value
        )
    )


def frontmatter(text, path, errors):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return False, None, text
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        errors.append(f"{path}: unclosed YAML frontmatter")
        return True, None, ""
    try:
        metadata = yaml.safe_load("".join(lines[1:end]))
    except yaml.YAMLError as error:
        errors.append(f"{path}: malformed YAML: {error}")
        metadata = None
    return True, metadata, "".join(lines[end + 1:])


def heading_anchors(tokens):
    """GitHub-style anchors for this repository's Markdown headings."""
    anchors = set()
    for i, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        text = inline_text(tokens[i + 1].children or []).strip().lower()
        base = re.sub(r"[^\w\- ]", "", text).replace(" ", "-")
        anchor = base
        suffix = 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{base}-{suffix}"
        anchors.add(anchor)
    return anchors


def local_target(source, href, errors):
    try:
        url = urlsplit(href)
    except ValueError:
        errors.append(f"{source}: invalid link {href!r}")
        return None
    if url.scheme or url.netloc:
        return None
    path = unquote(url.path)
    if path.startswith("/"):
        errors.append(f"{source}: use a file-relative link: {href}")
        return None
    return (source.parent / path).resolve() if path else source


def check_links(source, tokens, documents, errors):
    for token in tokens:
        for child in token.children or []:
            if child.type not in {"link_open", "image"}:
                continue
            href = child.attrGet("href" if child.type == "link_open" else "src")
            target = local_target(source, href, errors)
            if target is None:
                continue
            if not target.is_file():
                errors.append(f"{source}: missing local file target: {href}")
                continue
            fragment = unquote(urlsplit(href).fragment)
            if fragment and target.suffix == ".md":
                if target not in documents:
                    # Links may leave the bundle without extending its metadata rules.
                    _, _, body = frontmatter(target.read_text(encoding="utf-8"), target, errors)
                    documents[target] = MARKDOWN.parse(body)
                if fragment not in heading_anchors(documents[target]):
                    errors.append(f"{source}: missing heading fragment: {href}")


def index_entries(path, tokens, errors):
    """Read top-level Markdown list items, not links inside illustrative code."""
    entries = []
    heading_seen = False
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            heading_seen = True
        if token.type != "list_item_open" or token.level != 1:
            continue
        end = next(j for j in range(i + 1, len(tokens))
                   if tokens[j].type == "list_item_close" and tokens[j].level == 1)
        item = tokens[i + 1:end]
        inlines = [t for t in item if t.type == "inline"]
        children = inlines[0].children if inlines else []
        if not heading_seen or token.markup not in {"-", "*", "+"}:
            errors.append(f"{path}: discovery entries must be bullet lists under headings")
        if not children or children[0].type != "link_open":
            errors.append(f"{path}: discovery entry must start with a Markdown link")
            continue
        close = next(j for j, child in enumerate(children) if child.type == "link_close")
        label = inline_text(children[1:close])
        href = children[0].attrGet("href")
        rest = inline_text(children[close + 1:])
        rest += "".join("\n" + inline_text(t.children or []) for t in inlines[1:])
        match = re.fullmatch(
            r"\s*[—-]\s+(.+?)\nRead when:\s*(.+?)\nTags:\s*(.+?)\s*", rest, re.DOTALL
        )
        if not match:
            errors.append(f"{path}: {href}: expected description, Read when, and Tags in the same list item")
            continue
        description, read_when, tag_text = (normalize(v) for v in match.groups())
        tags = [tag.strip() for tag in tag_text.split(",")]
        if not description or not read_when or not valid_tags(tags):
            errors.append(f"{path}: {href}: empty routing hint or invalid Tags")
        entries.append((href, normalize(label), description, tags))
    return entries


def validate(bundle):
    bundle = bundle.resolve()
    errors = []
    files = sorted(p for p in bundle.rglob("*.md") if ".obsidian" not in p.relative_to(bundle).parts)
    concepts = {}
    documents = {}
    indexes = []
    for path in files:
        has_metadata, metadata, body = frontmatter(path.read_text(encoding="utf-8"), path, errors)
        documents[path] = MARKDOWN.parse(body)
        if path.name == "index.md":
            indexes.append(path)
            if path == bundle / "index.md":
                if metadata != {"okf_version": "0.2"}:
                    errors.append(f"{path}: root frontmatter must contain only okf_version: \"0.2\"")
            elif has_metadata:
                errors.append(f"{path}: nested indexes must not have frontmatter")
        elif path.name not in RESERVED:
            if not has_metadata or not isinstance(metadata, dict):
                errors.append(f"{path}: concept requires a YAML frontmatter mapping")
                continue
            for field in ("type", "title", "description"):
                if not isinstance(metadata.get(field), str) or not metadata[field].strip():
                    errors.append(f"{path}: concept {field} must be a non-empty string")
            if not valid_tags(metadata.get("tags")):
                errors.append(f"{path}: concept tags must be a non-empty list of Obsidian-compatible strings")
            concepts[path] = metadata
        if path.name == "_index.md":
            errors.append(f"{path}: legacy index filename; migrate to index.md")

    # Every docs directory on a path to a document is an area, even if it only
    # contains child areas. Personal Obsidian config is outside this contract.
    areas = {bundle}
    for path in files:
        areas.update(parent for parent in path.parents if parent == bundle or bundle in parent.parents)
    for area in sorted(areas):
        if area / "index.md" not in indexes:
            errors.append(f"{area}: missing index.md")
        if area / "README.md" not in files:
            errors.append(f"{area}: missing README.md mental-model entrypoint")

    for index in indexes:
        covered = set()
        for href, label, description, tags in index_entries(index, documents[index], errors):
            target = local_target(index, href, errors)
            if target is None:
                errors.append(f"{index}: discovery destination must be a local concept or child index: {href}")
                continue
            if target in covered:
                errors.append(f"{index}: duplicate discovery entry: {href}")
            covered.add(target)
            if target.name == "index.md":
                if target.parent.parent != index.parent:
                    errors.append(f"{index}: area entry must point to an immediate child index: {href}")
                continue  # Area metadata has no frontmatter source.
            if target.parent != index.parent or target not in concepts:
                errors.append(f"{index}: expected a concept in the containing directory: {href}")
                continue
            metadata = concepts[target]
            for field, value in (("title", label), ("description", description)):
                canonical = metadata.get(field)
                if isinstance(canonical, str) and normalize(
                    inline_text(MARKDOWN.parseInline(canonical)[0].children or [])
                ) != value:
                    errors.append(f"{index}: {href}: {field} projection drift")
            if valid_tags(metadata.get("tags")) and set(metadata["tags"]) != set(tags):
                errors.append(f"{index}: {href}: tags projection drift")
        expected = {p for p in files if p.parent == index.parent and p.name not in RESERVED}
        expected.update(area / "index.md" for area in areas if area.parent == index.parent)
        for missing in sorted(expected - covered):
            errors.append(f"{index}: missing discovery entry for {missing.relative_to(index.parent)}")

    for source in files:
        check_links(source, documents[source], documents, errors)
    return errors, len(indexes), len([p for p in files if p.name not in RESERVED])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "docs")
    args = parser.parse_args()
    errors, indexes, concepts = validate(args.bundle)
    if errors:
        print("Documentation contract failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Documentation contract passed: {indexes} indexes, {concepts} concepts (OKF v0.2 target).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
