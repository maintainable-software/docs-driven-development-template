---
name: global-docs-maintainer
description: Maintain this repository's global indexed documentation system under docs/ as repository truth changes, including validated reusable context supplied during authorized editing tasks.
---

# Global Docs Maintainer

Use this skill whenever work changes global repository documentation or repository truth that should be reflected in `docs/`.

## Workflow

1. Update the global canonical document that owns the changed fact.
2. Ensure the affected docs folder still has a `README.md` that explains what the area is, why it exists, and the core mental model humans should use when reading the area.
3. Update or create the folder's `_status.md` when the change affects current reality, active uncertainty, known gaps, or open questions.
4. Update or create the folder's `_decisions.md` when the change affects important rationale or tradeoffs that would not be obvious from the current docs shape alone.
5. Preserve conceptual simplicity: do not broaden one doc to cover multiple distinct responsibilities just because they are adjacent in workflow or implementation.
6. When an area has multiple clear responsibility boundaries, prefer one focused doc per responsibility or system part plus a composition doc that describes how the parts fit together.
7. When a focused doc explicitly documents a system part, include the standard `Responsibility`, `Not responsible for`, `Inputs`, `Outputs`, and `Adjacent parts` sections unless the doc is clearly not a system-part doc.
8. Add a new focused global doc only when no current doc in `docs/` is a good fit.
9. Check the containing directory's `index.md` first and update it if routing or discoverability changed, including changes to concept titles, descriptions, or tags.
10. Walk upward one folder at a time toward `docs/index.md`, updating or creating routing `index.md` files only where needed.
11. Stop once the next parent `index.md` would not need any change.
12. Ensure each `index.md` discovery entry is a Markdown list item under a heading with a linked title, description, labelled `Read when`, and `Tags`. Use correct file-relative links with explicit destinations. Enforce the metadata contract below.
13. If the change introduces, removes, renames, or redefines important repository terms, also update `docs/DICTIONARY.md`.
14. After substantively changing docs in an area, do a dictionary coverage pass over the affected docs area. Add missing stable terms that now matter, link important uses, and remove stale links to removed entries.
15. When a user's answer resolves a material context gap during an authorized editing task, assess whether it establishes stable reusable knowledge or corrects the existing documented truth. Do not automatically promote temporary assumptions or tentative claims.
16. When the information fits an existing global canonical document, prepare the minimal update as part of the current task without requiring a second instruction to maintain that existing doc. Preserve explicit planned-vs-current distinctions and validate the result against the task.
17. If no existing focused global doc fits, propose a new topic document and follow the user's documentation-scope choice; do not create unrelated or duplicative documents.
18. Apply the existing `index.md` propagation, `_status.md`, `_decisions.md`, and dictionary coverage rules to any resulting edits. Use ordinary repository validation and review; do not require DDC-specific logs or metadata.

## Metadata And Navigation Contract

- Treat `docs/` as the OKF v0.2 bundle root; repository Markdown, skills, and co-located docs outside it have no OKF frontmatter requirement.
- Keep one canonical `index.md` per docs directory. The root index has only `okf_version: "0.2"` in its YAML frontmatter; nested indexes have no frontmatter.
- Every non-reserved Markdown document under `docs/` is a concept. Require parseable YAML with non-empty string `type`, `title`, and `description`, plus a non-empty list of meaningful Obsidian-compatible tags. `type` is OKF's requirement; the additional fields are template conventions. Preserve valid existing metadata and unrelated extension fields.
- Concept frontmatter owns type, title, description, and tags. Project the title as the link label, copy the description beside it, and project the same tag collection as `Tags`. Type is normally omitted from the index.
- Update description/tag projections in the same change as their canonical metadata. Allow formatting, line wrapping, and tag order differences. Preserve and separately maintain `Read when` so metadata updates do not erase routing intent.
- Handle entries pointing to child `index.md` as areas, not concepts. Maintain their description, reading conditions, and tags directly in the parent index; never require nested-index frontmatter. Update that entry when the area's purpose changes.
- When a concept is added, moved, or removed, update affected indexes and links. Keep every concept discoverable in its containing index and every child area in its parent index. Maintain Dictionary discovery only in `docs/index.md` and retain meaningful direct definition links.
- Run `python3 scripts/validate-docs.py` from the repository root with the documented validation dependencies. Maintenance and CI may scan metadata; this does not authorize a preliminary full metadata scan during routing.
- Index coverage, routing hints, projection consistency, and local-link integrity are repository conventions, not universal OKF conformance requirements.

## Boundaries

- Do not duplicate canonical explanations across global docs. The deliberate metadata projections in discovery indexes are the exception, maintained from their frontmatter source.
- Maintain routing integrity only through `index.md` files in the `docs/` tree.
- Do not use `README.md` as a routing index in this repository. Keep it as the folder's human mental-model entrypoint.
- Do not use this skill for co-located `*.docs.md` files next to source files.
- Do not preserve stale wording when the correct scope is now known.
- Do not let implementation convenience or process adjacency justify a doc boundary that braids distinct responsibilities together.
- Do not treat dictionary maintenance as complete just because the explicitly mentioned terms were handled.
- Do not record provisional assumptions as established repository truth.
- Do not add knowledge-source, person/team ownership, verification-person, or mandatory expiry metadata as part of DDC curation.
- Do not treat a user answer to an analytical/read-only request as authorization to edit repository files.

## Canonical References

Read [docs/index.md](../../../docs/index.md) for the root global docs index.
Read [docs/DICTIONARY.md](../../../docs/DICTIONARY.md) when terminology changes are part of the task.
Read [docs/process/index.md](../../../docs/process/index.md) for process docs routing.
Read [docs/process/docs-system.md](../../../docs/process/docs-system.md) for the indexed global docs model.
Read [docs/process/colocated-docs.md](../../../docs/process/colocated-docs.md) to distinguish co-located docs from global docs.
Read [docs/process/demand-driven-context.md](../../../docs/process/demand-driven-context.md) for context-gap resolution and knowledge promotion rules.
