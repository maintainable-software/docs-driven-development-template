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

No entries yet.

## Meta And Internal Terms

No entries yet.
