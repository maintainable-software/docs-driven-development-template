---
type: Decision Record
title: Docs Decisions
description: Explains the key choices behind the current docs structure and why routing, mental-model, and status information are split across different files.
tags:
  - docs
  - decisions
  - rationale
  - tradeoffs
---

# Docs Decisions

## `_index.md` Owns Routing

Historical decision: the filename in this section is superseded by the OKF
v0.2 migration below; the separation of responsibilities remains in force.

The repository uses `_index.md` instead of `README.md` for docs navigation so routing metadata stays separate from human-oriented explanation.

## `README.md` Owns The Mental Model

Each docs folder now uses `README.md` as the human entrypoint. This makes the file name familiar and predictable without overloading it with routing duties.

## `_status.md` And `_decisions.md` Are Special-Purpose Docs

Current-state information and rationale change at different rates and for different reasons. Keeping them out of `README.md` reduces drift and makes it clearer where to update the truth.

## Adopt OKF v0.2 And Obsidian-Compatible Links

The global bundle is `docs/`. Rename the routing files to `index.md`, keep both
hierarchical indexes, and use Markdown linked lists so standard readers can
navigate the same discovery structure. Add concept frontmatter and declare
version `0.2` only at the root index. This changes the interchange convention
without merging navigation with explanation or changing DPD's document roles.

Frontmatter owns concept metadata. Descriptions and tags are deliberately
projected into indexes so agents can select documents before opening them;
reading conditions remain curated by the index. Child-area metadata stays in
the parent index because nested indexes have no frontmatter. These are distinct
ownership responsibilities, not a new knowledge-ownership tracking system.

File-relative Markdown links support GitHub and Obsidian without plugins.
Co-located docs keep their locations and adjacency discovery outside the global
routing tree. Status docs, decision docs, and Git history continue to record
reality and rationale; optional OKF tracking fields and `log.md` add no needed
responsibility in this migration.
