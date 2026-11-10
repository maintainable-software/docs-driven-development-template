---
type: Status
title: Process Status
description: Current reality for the documentation-process area, including which workflow rules are active and where adoption is still incomplete.
tags:
  - docs
  - process
  - status
  - current-state
---

# Process Status

Current reality:

- Global docs are routed through `docs/index.md` and area `index.md` files.
- Linked-list entries preserve descriptions, primary `Read when` hints, and secondary tags. Routing reads concept frontmatter only after selection.
- All process concepts have metadata; their index projections are validated. Area metadata is maintained independently in the parent index.
- The validator and focused regression cases cover metadata parsing, index structure, coverage, projection drift, and local links. These checks enforce repository conventions beyond OKF's permissive conformance rules.
- The normal docs workflow now treats `README.md` as the mandatory human entrypoint in each docs folder.
- The docs process now explicitly routes conceptual-simplicity guidance for
  boundary, decomposition, terminology, and docs-structure tasks.
- The dictionary now separates repository concepts from meta/internal
  terminology instead of flattening both into one glossary section.
- The docs workflow now requires a dictionary coverage pass over an affected
  docs area after substantive docs changes, rather than only updating
  explicitly mentioned terms.
- Contradictions noticed during docs routing should be surfaced even when contradiction-finding was not explicitly requested.
- [Co-located docs](../DICTIONARY.md#co-located-docs) remain optional and conservative by default, and new ones are created manually rather than by a creator skill.
- [Demand-Driven Context](../DICTIONARY.md#demand-driven-context) is wired into the shared policy, activation rules, and existing skills: agents assess task-relative [context sufficiency](../DICTIONARY.md#context-sufficiency), ask before blocking dependent work and ambiguous high-impact decisions, and may defer non-blocking clarification.
- Validated reusable answers can trigger updates to existing canonical global or co-located docs during authorized editing tasks, even without a corresponding source-file edit. New co-located docs still require an explicit user request.
- DDC uses the existing indexed docs model and review workflow; no separate knowledge base, provenance or knowledge-ownership tracking, or mandatory cycle log is introduced.

Known gaps:

- The process is defined, but only a small number of docs areas currently exist, so some folder-shape rules are established ahead of broader adoption.
- DDC instructions have received structural checks and scenario walkthroughs; end-to-end behavior in an adopting product repository has not yet been exercised.
