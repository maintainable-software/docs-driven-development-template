# Process

Process docs define how repository documentation is structured, routed, and maintained, including how task-driven context gaps are resolved.

## Area Context

- [Process Overview](README.md) — Human entrypoint for the documentation-process area, explaining what this area covers and how its documents fit together.
  **Read when:** You need the mental model for the repository's documentation workflow before going into detailed process rules.
  **Tags:** docs, process, overview, mental-model

- [Process Status](_status.md) — Current reality for the documentation-process area, including which workflow rules are active and where adoption is still incomplete.
  **Read when:** You need the present-state view of the docs process, known gaps, or active uncertainty.
  **Tags:** docs, process, status, current-state

- [Process Decisions](_decisions.md) — Rationale for separating documentation roles and integrating context sufficiency and validated curation into the existing workflow.
  **Read when:** You need to understand the docs process boundaries, its file roles, or the choices behind demand-driven context integration.
  **Tags:** docs, process, decisions, rationale

## Focused Rules

- [Conceptual Simplicity](conceptual-simplicity.md) — Defines the repository's anti-complecting rules for code, terminology, docs structure, and system-part boundaries.
  **Read when:** The task affects architecture, module boundaries, terminology boundaries, system decomposition, or how docs should be structured to preserve conceptual simplicity.
  **Tags:** docs, process, simplicity, complexity, boundaries

- [Docs Routing](docs-routing.md) — Defines global docs discovery through linked index.md entries and distinguishes successful retrieval from sufficient task context.
  **Read when:** The task changes doc discovery, routing behavior, index shape, selection of the minimum relevant docs, or the transition from discovery to context assessment.
  **Tags:** docs, routing, indexing, read-when, discovery

- [Demand-Driven Context](demand-driven-context.md) — Defines task-driven context sufficiency checks, missing-knowledge handling, targeted user clarification, and validated curation into existing documentation.
  **Read when:** The task requires assessing missing or contradictory context, deciding whether to interrupt for a knowledge gap, handling user answers or provisional assumptions, or curating knowledge discovered during development.
  **Tags:** docs, process, demand-driven-context, context-gap, sufficiency, clarification, curation

- [Docs System](docs-system.md) — Defines the global OKF bundle, optional co-located docs, metadata ownership, and maintenance of canonical knowledge, including validated context supplied during development.
  **Read when:** The task changes the documentation model, canonical placement, index maintenance, knowledge curation, or the relationship between global and co-located docs.
  **Tags:** docs, system, maintenance, global-docs, colocated-docs

- [Colocated Docs](colocated-docs.md) — Defines naming, purpose, and conservative maintenance of optional adjacent `*.docs.md` files, including corrections from validated context without source edits.
  **Read when:** The task involves creating, reading, or updating co-located docs, correcting local knowledge even without a source edit, or deciding whether file-specific documentation belongs next to code instead of in `docs/`.
  **Tags:** docs, colocated, module-docs, file-docs, maintenance

- [Transitional Docs](transitional-docs.md) — Explains how to work safely in repositories whose documentation structure is only partially normalized toward the indexed global docs model.
  **Read when:** The repository has legacy docs locations, missing docs indexes, or mixed documentation patterns that need to be interpreted or normalized.
  **Tags:** docs, transitional, legacy, migration, normalization
