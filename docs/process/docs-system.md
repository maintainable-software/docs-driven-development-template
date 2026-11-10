---
type: Reference
title: Docs System
description: Defines the global OKF bundle, optional co-located docs, metadata ownership, and maintenance of canonical knowledge, including validated context supplied during development.
tags:
  - docs
  - system
  - maintenance
  - global-docs
  - colocated-docs
---

# Indexed Docs System

The repository documentation system separates:

- [global docs](../DICTIONARY.md#global-docs) under `docs/`
- optional [co-located docs](../DICTIONARY.md#co-located-docs) in `*.docs.md`
  files next to specific source or configuration files

Recommended ownership:

- `docs/index.md`: root index file
- `docs/<area>/index.md`: local index file
- `docs/**/README.md`: mandatory human mental-model entrypoint for each docs folder
- `docs/**/_status.md`: optional present-state doc for current reality, active uncertainty, known gaps, or open questions
- `docs/**/_decisions.md`: optional rationale doc for important choices and tradeoffs
- `docs/DICTIONARY.md`: canonical repository terminology dictionary for the repository's docs tree
- topic docs under `docs/`: global canonical facts
- `<file>.docs.md`: optional local documentation for one concrete file or module

Conceptual-simplicity rules:

- preserve conceptual simplicity when choosing doc boundaries
- do not broaden one doc to cover multiple distinct responsibilities just because they are adjacent in workflow or implemented together
- prefer one focused doc per responsibility or system part plus a composition doc that explains how the parts fit together
- treat docs structure as part of the system design, not just as explanatory prose

System-part doc shape:

- `Responsibility`: what the part owns
- `Not responsible for`: what adjacent parts own instead
- `Inputs`: what comes into the part
- `Outputs`: what leaves the part
- `Adjacent parts`: which neighboring parts it composes with

## OKF Bundle And Concept Metadata

The [OKF bundle](../DICTIONARY.md#okf-bundle) root is `docs/`. The template targets
[Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/0b87c52c6ef999286c745e19998fdfcd03d5dbee/SPEC.md).
Repository-level Markdown, agent skills, and co-located documents outside
`docs/` are outside the bundle and have no OKF frontmatter requirement.

OKF reserves `index.md` and `log.md`. Every other Markdown file in the bundle is
a [concept document](../DICTIONARY.md#concept-document), including `README.md`,
`_status.md`, `_decisions.md`, and `DICTIONARY.md`. OKF requires parseable YAML
frontmatter with a non-empty string `type`. This template also requires
non-empty `title` and `description` strings and a non-empty `tags` list for
consistent discovery and interoperability. Preserve valid extension fields.

```yaml
---
type: Reference
title: Documentation Routing
description: Rules for selecting relevant global documentation.
tags:
  - docs
  - routing
  - indexing
  - discovery
---
```

Use `Overview` for READMEs, `Status` for status docs, `Decision Record` for
decision docs, `Glossary` for the Dictionary, and `Reference` for focused
process rules. Classify new concepts by their actual purpose; type names are
not a closed vocabulary. Use concise descriptions and meaningful tags. Our tag
convention uses letters, digits, underscores, hyphens, or slash-separated
segments, with at least one non-numeric character and no spaces or leading `#`;
it is compatible with [Obsidian tags](https://help.obsidian.md/tags).

Keep only `okf_version: "0.2"` in the root `index.md` frontmatter. Nested
indexes have no YAML frontmatter. Keep one canonical `index.md` per docs
directory. Status docs, decision docs, and Git history retain their roles;
no `log.md`, provenance, trust, lifecycle, or computation fields are needed.

## Metadata Ownership

| Information | Canonical location | Index representation |
| --- | --- | --- |
| Concept type | Document frontmatter | Normally omitted |
| Concept title | Document frontmatter | Human-readable link label |
| Concept description | Document frontmatter | Projected beside the link |
| Concept tags | Document frontmatter | Projected as `Tags` |
| Reading conditions | Containing index | Independently maintained `Read when` |
| Navigation destination | Containing index | Standard Markdown link |

The description and tag collection in a concept's discovery entry are
[index projections](../DICTIONARY.md#index-projection), not independent facts.
**A change to a concept's description or tags must update its discovery entry
in the same change.** Copy the description, allowing formatting and line
wrapping, and the same tag collection, allowing a different order. Keep the
link label aligned with the title. Preserve and maintain the separately curated
`Read when`; refreshing metadata must not erase its routing intent.

An [area entry](../DICTIONARY.md#area-entry) points to a child `index.md` and
represents the area rather than a concept. Its description, reading conditions,
and tags belong directly to the parent index, because nested indexes have no
frontmatter. Apply frontmatter consistency checks only to concept entries.
When the area's purpose changes, update this parent entry.

Indexes use the [linked-list routing contract](docs-routing.md#index-entries).
Use ordinary Markdown links with explicit file destinations and paths relative
to the linking file, including links with heading fragments. This keeps
navigation useful in GitHub and Obsidian. Keep illustrative paths in code
examples distinct from actual navigation.

## Maintenance

Global docs maintenance rules:

- update the canonical document that owns the changed fact
- keep `README.md` present in every docs folder under `docs/`, even if it is only a few lines long
- keep `README.md` focused on what the area is, why it exists, and the core mental model humans should use when reading it
- add or update `_status.md` when the area has meaningful current-state volatility, active uncertainty, known gaps, or open questions
- add or update `_decisions.md` when rationale or tradeoffs would not be obvious from the current docs shape alone
- add a new focused doc only when no current doc is a good fit
- preserve conceptual simplicity when choosing doc boundaries
- do not broaden one doc to cover multiple distinct responsibilities just because they are adjacent in workflow or implemented together
- when an area has multiple clear responsibility boundaries, prefer one focused doc per responsibility or system part plus a composition doc
- when a global doc changes, check the containing directory's `index.md` first
- then walk upward one folder at a time toward `docs/index.md`
- update or create parent routing `index.md` files only where routing or discoverability changed
- ensure each `index.md` discovery entry includes a linked title, description, `Read when`, and `Tags` under a heading
- when a concept is added, moved, or removed, update its containing index and affected links; each concept must be discoverable from its containing index, and each child area from its parent's index
- maintain Dictionary discovery through the root index only; meaningful direct links to definitions remain appropriate throughout process docs
- preserve concept metadata ownership and refresh description/tag projections in the same change, retaining independently curated reading conditions
- stop once the next parent `index.md` would not need any change
- update `docs/DICTIONARY.md` when important repository terms are introduced, renamed, redefined, or removed
- after substantively changing docs in an area, do a dictionary coverage pass over the affected docs so stable terms now relied on by those docs are present in `docs/DICTIONARY.md`, linked where important, and stripped of stale removed-term links

Demand-driven curation rules:

- when real development work reveals a material [context gap](../DICTIONARY.md#context-gap), follow [Demand-Driven Context](demand-driven-context.md) before inventing a missing rule
- when the user provides missing context during an authorized repository-editing task, automatically assess whether it is sufficiently clear, reusable, and consistent to warrant an update to an existing canonical doc
- prepare justified updates to existing canonical docs as part of the same task, subject to normal validation and repository review; do not automatically turn tentative answers or [provisional assumptions](../DICTIONARY.md#provisional-assumption) into established facts
- choose the smallest appropriate existing global doc, dictionary entry, status doc, decision doc, or adjacent existing co-located doc; do not duplicate one fact across several documents except for the deliberate index projections defined above
- if no focused global doc is suitable, propose a new topic document and follow the user's documentation-scope decisions rather than silently expanding the docs tree
- do not require knowledge provenance, person/team ownership tracking, a separate DDC knowledge base, or mandatory DDC cycle logs

Global docs reading rules:

- route through `docs/index.md` first when global docs are needed
- treat `index.md` as navigation, `README.md` as the human entrypoint, `_status.md` as present-state context, `_decisions.md` as rationale, and topic docs as focused mechanisms or rules
- read an area's `README.md` when you need to understand what the area is, why it exists, or how its docs are meant to be interpreted
- read an area's `_status.md` when current reality or active uncertainty matters
- read an area's `_decisions.md` when rationale or tradeoffs matter
- read only the minimum sufficient set of global docs
- read [Demand-Driven Context](demand-driven-context.md) when the task needs material gap resolution or knowledge curation, not automatically for every task
- if routing or reading reveals a meaningful contradiction or mismatch, surface it clearly even when contradiction-finding was not the user's primary request
- when a focused doc explicitly documents a system part, use the standard `Responsibility`, `Not responsible for`, `Inputs`, `Outputs`, and `Adjacent parts` sections

Co-located docs maintenance rules:

- when a concrete source or configuration file changes, check whether an adjacent co-located docs file exists
- if it exists and the change affects documented behavior, interface, intent, invariants, or constraints, update it in the same task
- when validated reusable context affects an existing relevant adjacent doc during an authorized editing task, update it even if its source/config file did not change; follow [Demand-Driven Context](demand-driven-context.md) for validation and scope
- if it does not exist, do not create one as part of normal maintenance
- new co-located docs are created manually and only when explicitly requested
- co-located docs do not participate in `docs/index.md` routing or `index.md` propagation

## Structural Validation

From the repository root, run `python3 scripts/validate-docs.py` after installing
the validation dependencies described in the repository README. The validator
uses PyYAML for YAML and markdown-it-py for Markdown parsing. It checks concept
metadata, index structure, coverage, routing hints, metadata projections, and
local link targets. It ignores external URLs and links illustrated in code;
fragments are checked against Markdown headings with GitHub-style anchors.

Index coverage, routing hints, metadata consistency, and link integrity are
**repository conventions**, not universal OKF conformance requirements. OKF
permits missing indexes and unresolved links. This validator enforces our
contract; it is not a general-purpose OKF conformance framework. Maintenance
and CI may scan all metadata without changing selective router behavior.
