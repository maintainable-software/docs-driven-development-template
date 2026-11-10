---
type: Glossary
title: Dictionary
description: Canonical definitions for the repository terminology used by this repository's own `docs/` tree.
tags:
  - docs
  - dictionary
  - terminology
  - glossary
  - repository-language
---

# Dictionary

This file is the canonical dictionary for the repository terminology used by
this repository's own `docs/` tree.

It has two sections on purpose:

- `Repository Concepts` is for actual things, parts, artifacts, states,
  workflows, properties, and relations that belong to the repository's
  documented domain model itself.
- `Meta And Internal Terms` is for terms the repository uses to scope, design,
  implement, operate, or document those concepts.

Use it to keep terminology understandable, consistent, and linkable from
anywhere in `docs/`.

## Maintenance Rules

- Keep entries sorted alphabetically within their section.
- Put a term in `Repository Concepts` when it names an actual thing, artifact,
  part, state, workflow, property, or relation intrinsic to the repository's
  documented domain model.
- Put a term in `Meta And Internal Terms` when it names how the repository
  classifies, scopes, designs, implements, operates, or documents repository
  concepts.
- Do not add vague principle language, taste labels, or one-off grouping labels
  to the dictionary unless they are stable reference terms used repeatedly
  across docs and need canonical meaning.
- If a term only labels a category of concepts rather than a concept the
  repository actually has, prefer documenting the actual concepts instead of
  adding the category label as a dictionary entry.
- Add or update entries when the project's terminology changes, when a term
  gains a new meaning, or when a newly introduced term becomes important to
  understanding the repository.
- After substantively changing docs in an area, do a dictionary coverage pass
  over the affected docs. Scan for stable terms the updated docs now rely on,
  add missing entries for terms that meet the criteria, link important uses,
  and remove stale links to removed entries.
- Remove entries when the term is removed from the product or repository model
  entirely.
- Write entries for readers with little domain knowledge. An entry should
  explain what the term is, why it exists in this model, and how it relates to
  surrounding terms.
- If a term is easy to misunderstand, easy to misuse, or can mean more than one
  thing in everyday language, include a short usage example that shows how a
  tool consumer would actually use it in a managed project. If using the term
  depends on a command, prefer a concrete example command and explain what that
  enables.
- If an entry describes a planned concept rather than a live implemented one,
  say that explicitly so the dictionary does not blur target behavior with
  current behavior.
- In `docs/` prose, link repository terms to the matching entry in this
  dictionary unless the term is being used as code, CLI syntax, or a file path
  in backticks.

## Repository Concepts

### Area Entry

A discovery entry in a parent `index.md` that links to a child area's
`index.md`. Its description, reading conditions, and tags are maintained in
the parent index; there is no concept frontmatter to project from a nested
index. It directs the reader to local routing before individual concepts.

### Co-Located Docs

Optional Markdown files named `*.docs.md` that live next to one concrete
source or configuration file and capture local guidance that would be hard to
recover quickly from code alone.

They are discovered by adjacency rather than through the global docs index.
Files outside `docs/` are outside the [OKF bundle](DICTIONARY.md#okf-bundle) and do not
require OKF frontmatter.

### Concept Document

A Markdown unit of knowledge within the [OKF bundle](DICTIONARY.md#okf-bundle), excluding
the reserved `index.md` and `log.md` filenames. This includes overviews,
status docs, decision records, the Dictionary, and focused topic documents.
Its YAML frontmatter owns type, title, description, and tags; its body retains
its existing documentation responsibility.

### Global Docs

The canonical documentation files under `docs/` that define repository-wide
facts, workflow rules, routing metadata, and shared terminology.

They are routed through `docs/index.md` and area `index.md` files.

### Index Projection

A concept's title, description, or tags copied from its frontmatter into its
containing index's discovery entry. This deliberate duplication makes initial
selection possible without opening every concept. Description/tag changes
update their projections in the same change; `Read when` is independently
curated and is not a projection. [Area entries](DICTIONARY.md#area-entry) also own their
metadata independently.

### Indexed Docs System

The repository documentation model that separates [global docs](DICTIONARY.md#global-docs)
under `docs/` from optional [co-located docs](DICTIONARY.md#co-located-docs) and uses
linked-list `index.md` files for hierarchical discoverability. Each discovery
entry supplies a linked title, description, primary `Read when` condition,
and secondary tags.

### OKF Bundle

The directory tree distributed as Open Knowledge Format knowledge. In this
repository it is exactly `docs/`, targeting OKF v0.2, not the repository root
or whichever folder is opened as an Obsidian vault. Repository instructions,
agent skills, and co-located docs elsewhere are outside this boundary.

The root `index.md` declares the version; nested indexes have no frontmatter.
Other Markdown files are [concept documents](DICTIONARY.md#concept-document), except for
the reserved optional `log.md`, which this template does not use.

### Skill

A reusable set of agent instructions in a directory containing `SKILL.md`.
Shared repository skills are authored in `.agents/skills/` and copied into
`.claude/skills/` with `bash scripts/sync-skills.sh` so Claude Code can discover
them. See [Shared Skills](process/skills.md) for the workflow.

### Synchronization Manifest

The generated `.claude/skills/.sync-skills-manifest` file records which skill
copies the synchronizer owns and their last generated fingerprints. It lets
sync detect manual edits and remove stale copies while preserving unrelated
Claude skills. Commit it together with the generated skill directories.

## Meta And Internal Terms

### Context Gap

A specific piece of information, rule, relationship, or decision needed by a
real task but not yet sufficiently established from relevant available context.
The agent distinguishes a genuine gap from a routing failure, an implementation
defect, or a temporary need for evidence. Gaps are assessed by documentation
state and task-relative severity.

Example: a cancellation task requires the permitted cutoff, but the relevant
documentation and code do not establish the intended business rule.

### Context Sufficiency

A task-relative judgment that the information available from relevant
documents, code, tests, and user requirements is adequate for the decisions the
task actually requires. It is not a claim that the entire repository has
complete documentation. The agent checks sufficiency after discovery and again
when new consequential uncertainty appears.

### Demand-Driven Context

Demand-Driven Context (DDC) complements
[Docs-Driven Product Development](DICTIONARY.md#docs-driven-product-development) by improving
repository documentation when real tasks reveal material missing, incomplete,
stale, contradictory, or undecided knowledge. It identifies precise
[context gaps](DICTIONARY.md#context-gap), obtains clarification when needed, validates the
resulting work, and curates reusable knowledge into the existing
[indexed docs system](DICTIONARY.md#indexed-docs-system) rather than creating a separate
knowledge base.

### Dictionary Coverage Pass

A review of the affected docs area after a substantive docs change to ensure
stable terms used by that area are present in `docs/DICTIONARY.md`, important
uses are linked where needed, and stale removed-term links are cleaned up.

### Docs-Driven Product Development

Docs-Driven Product Development (DPD) is this template's workflow for organizing,
routing, reading, and maintaining repository documentation. It uses the
[indexed docs system](DICTIONARY.md#indexed-docs-system), optional
[co-located docs](DICTIONARY.md#co-located-docs), and a shared dictionary to keep documented
knowledge discoverable and consistent as the repository changes.
[Demand-Driven Context](DICTIONARY.md#demand-driven-context) complements it when a task needs
information that the available context does not yet establish.

### Provisional Assumption

An explicitly limited, unverified statement used to allow safe, reversible
progress on a task while a needed answer remains unresolved. It must be stated
clearly, used only within its approved scope, and must not be recorded as
established canonical behavior.

### System-Part Doc

A focused doc that explicitly documents one system part.

When this kind of doc is used, it should include `Responsibility`,
`Not responsible for`, `Inputs`, `Outputs`, and `Adjacent parts`.
