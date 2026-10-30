# Docs Routing

Preferred shape:

1. root `docs/_index.md`
2. area `_index.md`
3. area `README.md`
4. optional area `_status.md`
5. optional area `_decisions.md`
6. focused topic docs

Routing rules:

- `docs/_index.md` is the only always-read entry point for global docs when global docs are needed
- area `_index.md` files define local discoverability
- `README.md` is the human entrypoint for a docs folder and should explain what the area is, why it exists, and the core mental model
- `_status.md` captures present-state context, active uncertainty, known gaps, and open questions when that information matters
- `_decisions.md` captures important rationale and tradeoffs when that information matters
- each `_index.md` entry for an existing global doc should include `Path`, `Summary`, `Read when`, and `Tags`
- `docs/process/conceptual-simplicity.md` should be read when the task affects conceptual boundaries, module responsibilities, terminology boundaries, system decomposition, or docs structure
- `docs/DICTIONARY.md` should be read when the task depends on repository terminology or terminology consistency
- `Read when` is the primary routing hint for deciding relevance
- `Summary` explains the document's scope and intended use
- `Tags` provide compact secondary routing signals
- topic docs should stay focused and small
- `README.md` is mandatory in every docs folder under `docs/`
- for each substantive prompt, global docs routing happens first
- global docs routing may correctly conclude that zero global docs need to be read
- if routing or reading reveals a meaningful contradiction or mismatch, it should be surfaced clearly even when contradiction-finding was not the user's primary request
- co-located docs are not part of the global routing tree and are discovered by adjacency when concrete files are opened
- after routing and consulting task-relevant existing context, assess [context sufficiency](../DICTIONARY.md#context-sufficiency) for the task's material decisions; successfully finding documents does not by itself establish sufficiency
- distinguish a failure to discover existing knowledge from knowledge that is actually missing, incomplete, stale, or contradictory; repair the relevant `_index.md` routing instead of duplicating existing facts when routing is the real problem
- when a material [context gap](../DICTIONARY.md#context-gap) is encountered, use [Demand-Driven Context](demand-driven-context.md) to decide whether to ask, continue with a limited scope, or curate validated new context; do not read the entire docs tree merely to hunt for hypothetical gaps

This pattern exists to minimize prompt noise while preserving discoverability.
