## Repo Rules

### Global Docs Routing

* For every substantive prompt, first use the `global-docs-router` skill.
* When global docs are needed, route through the indexed docs system under `docs/` and read only the minimum sufficient set.
* In each docs folder, treat `_index.md` as navigation, `README.md` as the mandatory human mental-model entrypoint, `_status.md` as present-state context, `_decisions.md` as rationale, and ordinary topic docs as focused mechanisms or rules.
* When a task affects architecture, implementation boundaries, system decomposition, terminology boundaries, or docs structure, include `docs/process/conceptual-simplicity.md` in the minimum sufficient context.
* When a task depends on repository business-domain terminology, terminology consistency, or docs prose that may introduce or change important terms, include `docs/DICTIONARY.md` in the minimum sufficient context.
* If `global-docs-router` notices a meaningful contradiction or mismatch while routing or reading global docs, surface it clearly even if the user did not explicitly ask for contradiction-finding.

### Colocated Docs Reading

* When reading a concrete source or configuration file, use the `colocated-docs-reader` skill to check for an adjacent `*.docs.md` file with the same basename.
* If the co-located docs file exists and is relevant, read it as part of the minimum sufficient context.
* If no co-located docs file exists, continue without treating that as a gap.
* Co-located docs are optional and do not participate in the global `docs/_index.md` routing system.

### Global Docs Maintenance

* Whenever a file under `docs/` is created, moved, renamed, deleted, or substantively updated, use the `global-docs-maintainer` skill.
* Every docs folder under `docs/` must have a `README.md`, even if it is only a few lines long.
* Use `_status.md` only for meaningful current-state volatility, active uncertainty, known gaps, or open questions.
* Use `_decisions.md` only when rationale or tradeoffs would not be obvious from the current docs shape alone.
* Do not create or update unrelated `_index.md` files outside the affected routing path in the `docs/` tree.
* Every `_index.md` entry for an existing global doc should explicitly include `Path`, `Summary`, `Read when`, and `Tags`.
* Do not broaden one doc to cover multiple distinct responsibilities just because they are adjacent in workflow or implementation.
* When an area has clear responsibility boundaries, prefer one focused doc per responsibility or system part plus a composition doc.
* When a focused doc explicitly documents a system part, include at least `Responsibility`, `Not responsible for`, `Inputs`, `Outputs`, and `Adjacent parts`.

### Business Dictionary Maintenance

* `docs/DICTIONARY.md` is the canonical dictionary for the business-domain language used by this repository's own `docs/` tree.
* When docs or repository instructions introduce, rename, redefine, or remove important business-domain terms, use the `business-dictionary-maintainer` skill.
* In `docs/` prose, link business-domain terms to the matching dictionary entry unless the term is being used as code, CLI syntax, or a file path in backticks.

### Colocated Docs Maintenance

* When modifying a source or configuration file, use the `colocated-docs-maintainer` skill to check for an adjacent `*.docs.md` file with the same basename.
* If that co-located docs file exists and the change affects documented behavior, interface, intent, invariants, or constraints, update it in the same task.
* If no co-located docs file exists, do not create one unless the user explicitly requests it.
* If the user explicitly requests creation of a new co-located docs file, use the `colocated-docs-creator` skill to decide whether creation is warranted and create it only when its criteria are met.
