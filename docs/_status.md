---
type: Status
title: Docs Status
description: Current state of the docs system, including what is already in place and which parts remain unsettled.
tags:
  - docs
  - status
  - current-state
  - gaps
---

# Docs Status

The repository is using the indexed docs model under `docs/`.

Current reality:

- `index.md` is the navigation layer.
- `README.md` is the human mental-model entrypoint for each docs folder.
- `_status.md` and `_decisions.md` are now part of the folder-level docs shape when their information is needed.
- `docs/DICTIONARY.md` is the canonical terminology file for this template's own docs and should be adapted as destination repositories grow their own stable terminology.
- `docs/` targets OKF v0.2, with a root version declaration, no nested-index frontmatter, and metadata on all thirteen current concept documents.
- Both hierarchical indexes remain: the root discovers resources and the process area; the process index discovers its nine concepts. Dictionary discovery is maintained only at the root.
- Concept descriptions and tags are projected into indexes; reading conditions and area metadata remain index-owned.
- Structural validation and CI enforce the repository's metadata, routing, coverage, and local-link conventions.
- Obsidian compatibility is checked statically. An interactive vault smoke check has not been performed; the workflow remains usable without Obsidian.

Open questions:

- Destination repositories still need to decide which template workflow terms to keep, rename, or replace with their own repository vocabulary.
