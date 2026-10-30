# Process

Process docs define how repository documentation is structured, routed, and maintained, including how task-driven context gaps are resolved.

## Documents

### Process Overview
- Path: `docs/process/README.md`
- Summary: Human entrypoint for the documentation-process area, explaining what this area covers and how its documents fit together.
- Read when: You need the mental model for the repository's documentation workflow before going into detailed process rules.
- Tags: docs, process, overview, mental-model

### Process Status
- Path: `docs/process/_status.md`
- Summary: Current reality for the documentation-process area, including which workflow rules are active and where adoption is still incomplete.
- Read when: You need the present-state view of the docs process, known gaps, or active uncertainty.
- Tags: docs, process, status, current-state

### Process Decisions
- Path: `docs/process/_decisions.md`
- Summary: Rationale for separating documentation roles and integrating context sufficiency and validated curation into the existing workflow.
- Read when: You need to understand the docs process boundaries, its file roles, or the choices behind demand-driven context integration.
- Tags: docs, process, decisions, rationale

### Conceptual Simplicity
- Path: `docs/process/conceptual-simplicity.md`
- Summary: Defines the repository's anti-complecting rules for code, terminology, docs structure, and system-part boundaries.
- Read when: The task affects architecture, module boundaries, terminology boundaries, system decomposition, or how docs should be structured to preserve conceptual simplicity.
- Tags: docs, process, simplicity, complexity, boundaries

### Docs Routing
- Path: `docs/process/docs-routing.md`
- Summary: Defines global docs discovery through structured `_index.md` entries and distinguishes successful retrieval from sufficient task context.
- Read when: The task changes doc discovery, routing behavior, index shape, selection of the minimum relevant docs, or the transition from discovery to context assessment.
- Tags: docs, routing, indexing, read-when, discovery

### Demand-Driven Context
- Path: `docs/process/demand-driven-context.md`
- Summary: Defines task-driven context sufficiency checks, missing-knowledge handling, targeted user clarification, and validated curation into existing documentation.
- Read when: The task requires assessing missing or contradictory context, deciding whether to interrupt for a knowledge gap, handling user answers or provisional assumptions, or curating knowledge discovered during development.
- Tags: docs, process, demand-driven-context, context-gap, sufficiency, clarification, curation

### Docs System
- Path: `docs/process/docs-system.md`
- Summary: Defines global indexed docs, optional co-located docs, and maintenance of canonical knowledge, including validated context supplied during development.
- Read when: The task changes the documentation model, canonical placement, index maintenance, knowledge curation, or the relationship between global and co-located docs.
- Tags: docs, system, maintenance, global-docs, colocated-docs

### Dictionary
- Path: `docs/DICTIONARY.md`
- Summary: Defines the canonical repository terminology used by this repository's own docs tree and how terminology should stay consistent.
- Read when: The task depends on repository terminology, term consistency, ambiguous repository language, or docs changes that introduce, rename, redefine, or remove important terms.
- Tags: docs, dictionary, terminology, glossary, repository-language

### Colocated Docs
- Path: `docs/process/colocated-docs.md`
- Summary: Defines naming, purpose, and conservative maintenance of optional adjacent `*.docs.md` files, including corrections from validated context without source edits.
- Read when: The task involves creating, reading, or updating co-located docs, correcting local knowledge even without a source edit, or deciding whether file-specific documentation belongs next to code instead of in `docs/`.
- Tags: docs, colocated, module-docs, file-docs, maintenance

### Transitional Docs
- Path: `docs/process/transitional-docs.md`
- Summary: Explains how to work safely in repositories whose documentation structure is only partially normalized toward the indexed global docs model.
- Read when: The repository has legacy docs locations, missing docs indexes, or mixed documentation patterns that need to be interpreted or normalized.
- Tags: docs, transitional, legacy, migration, normalization
