---
type: Overview
title: Docs Overview
description: Human entrypoint for the repository docs tree, explaining what this documentation area is for and how to approach it.
tags:
  - docs
  - overview
  - mental-model
  - entrypoint
---

# Docs Overview

This `docs/` tree defines how documentation works in this repository.

It is the [OKF v0.2 bundle](DICTIONARY.md#okf-bundle). The
[root index](index.md) discovers global resources and the
[process index](process/index.md); that area index selects individual process
documents. Descriptions, reading conditions, and tags support selection before
opening a concept. Frontmatter is authoritative for concept metadata, with
descriptions and tags projected into indexes under the
[ownership rules](process/docs-system.md#metadata-ownership).

Use it to understand the documentation model, the agent-facing maintenance workflow, and the conventions that keep global docs, co-located docs, and terminology aligned.

Start with [process/README.md](process/README.md) if you want the mental model for the documentation workflow itself.

Read [process/conceptual-simplicity.md](process/conceptual-simplicity.md) when
a task affects boundaries, decomposition, terminology, or docs structure.

Indexes own navigation; READMEs explain the mental model. Status documents
describe current reality, decision documents retain rationale, topic documents
own focused rules, and the [Dictionary](DICTIONARY.md) owns terminology.
Optional adjacent file-specific docs remain outside the global routing tree.

For Obsidian, open `docs/` as an existing vault. In **Settings → Files and
links**, disable **Use Wikilinks** and set **New link format** to **Relative path
to file**. Use ordinary Markdown links with explicit file destinations. The
repository root is an alternative vault location when co-located docs elsewhere
should be visible; the OKF boundary remains `docs/`. Personal `.obsidian/`
configuration is ignored in either location. A Markdown editor or GitHub works
without Obsidian or community plugins. See Obsidian's
[link formats](https://help.obsidian.md/links) and
[settings](https://help.obsidian.md/settings).
