# Colocated Docs

[Co-located docs](../DICTIONARY.md#co-located-docs) are optional Markdown
files that live next to one concrete source or configuration file.

Naming convention:

- `src/foo.ts` -> `src/foo.docs.md`
- `src/bar/baz.ts` -> `src/bar/baz.docs.md`

Purpose:

- describe a public interface that matters beyond the code
- record non-obvious intent for why the file exists
- capture important invariants, constraints, or integration expectations

Rules:

- not every file needs co-located docs
- read a co-located docs file when it exists and is relevant to a task involving the documented file
- when the documented file is modified, update its co-located docs file if it exists and is affected
- do not create a new co-located docs file as part of normal maintenance
- new co-located docs are created manually and only when the user explicitly requests them
- co-located docs do not participate in the global `docs/_index.md` index system
- when validated new context supplied during an authorized editing task changes an existing relevant adjacent `*.docs.md`, update it even if its concrete source/config file was not modified; follow [Demand-Driven Context](demand-driven-context.md) for validation and curation
- user-supplied context does not authorize automatic creation of a new co-located docs file; if none exists, recommend one only when useful and obtain explicit user instruction before creating it
- route cross-cutting knowledge to the appropriate [global doc](../DICTIONARY.md#global-docs) rather than duplicating it across unrelated co-located docs
