---
type: Reference
title: Docs Routing
description: Defines global docs discovery through linked index.md entries and distinguishes successful retrieval from sufficient task context.
tags:
  - docs
  - routing
  - indexing
  - read-when
  - discovery
---

# Docs Routing

Preferred shape:

1. root `docs/index.md`
2. area `index.md`
3. area `README.md`
4. optional area `_status.md`
5. optional area `_decisions.md`
6. focused topic docs

## Index Entries

Use standard Markdown linked lists under headings in each `index.md`:

```markdown
- [Docs Routing](docs-routing.md) — Defines global docs discovery through linked index.md entries and distinguishes successful retrieval from sufficient task context.
  **Read when:** The task changes doc discovery, routing behavior, index shape,
  selection of the minimum relevant docs, or the transition from discovery to context assessment.
  **Tags:** docs, routing, indexing, read-when, discovery
```

The link supplies the title and file-relative destination; the text beside it
is the description. Keep **Read when:** and **Tags:** visibly labelled within
the same list item, even when text wraps. These three signals support initial
selection without opening each target's frontmatter:

1. **Read when** is the primary selection signal, curated in the containing index.
2. **Description** supports relevance assessment using the concept's canonical description.
3. **Tags** provide secondary semantic matching using the concept's tag collection.

For example, `indexing` or `discovery` can support selecting this document before
opening it. On opening a selected concept, read its frontmatter with its body.
Do not scan every concept's metadata as a preliminary routing step.

An [area entry](../DICTIONARY.md#area-entry) points explicitly to a child
`index.md`, such as [the process index](index.md) from [the root index](../index.md).
Follow that index before selecting its individual concepts. Area descriptions,
reading conditions, and tags are maintained directly in the parent index;
nested indexes have no frontmatter. Concept projections follow the
[metadata ownership rules](docs-system.md#metadata-ownership).

## Routing Rules

- `docs/index.md` is the only always-read entry point for global docs when global docs are needed
- area `index.md` files define local discoverability
- `README.md` is the human entrypoint for a docs folder and should explain what the area is, why it exists, and the core mental model
- `_status.md` captures present-state context, active uncertainty, known gaps, and open questions when that information matters
- `_decisions.md` captures important rationale and tradeoffs when that information matters
- each `index.md` discovery entry has a linked title, description, `Read when`, and `Tags`
- `docs/process/conceptual-simplicity.md` should be read when the task affects conceptual boundaries, module responsibilities, terminology boundaries, system decomposition, or docs structure
- `docs/DICTIONARY.md` should be read when the task depends on repository terminology or terminology consistency
- `Read when` is the primary routing hint for deciding relevance
- the description explains the document's scope and intended use
- `Tags` provide compact secondary routing signals
- topic docs should stay focused and small
- `README.md` is mandatory in every docs folder under `docs/`
- for each substantive prompt, global docs routing happens first
- global docs routing may correctly conclude that zero global docs need to be read
- if routing or reading reveals a meaningful contradiction or mismatch, it should be surfaced clearly even when contradiction-finding was not the user's primary request
- co-located docs are not part of the global routing tree and are discovered by adjacency when concrete files are opened
- after routing and consulting task-relevant existing context, assess [context sufficiency](../DICTIONARY.md#context-sufficiency) for the task's material decisions; successfully finding documents does not by itself establish sufficiency
- distinguish a failure to discover existing knowledge from knowledge that is actually missing, incomplete, stale, or contradictory; repair the relevant `index.md` routing instead of duplicating existing facts when routing is the real problem
- when a material [context gap](../DICTIONARY.md#context-gap) is encountered, use [Demand-Driven Context](demand-driven-context.md) to decide whether to ask, continue with a limited scope, or curate validated new context; do not read the entire docs tree merely to hunt for hypothetical gaps

This pattern exists to minimize prompt noise while preserving discoverability.
The default is selective reading; the repository's analyst profile may expand
reading for lower omission risk. Neither mode requires a preliminary metadata scan.
