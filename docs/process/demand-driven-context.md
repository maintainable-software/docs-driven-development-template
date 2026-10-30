# Demand-Driven Context

## Purpose

[Demand-Driven Context (DDC)](../DICTIONARY.md#demand-driven-context) complements the repository's
[Docs-Driven Product Development (DPD)](../DICTIONARY.md#docs-driven-product-development)
workflow. DPD routes to and maintains established knowledge;
DDC identifies material knowledge that a real task still needs, obtains or
investigates it, and curates validated reusable information into the existing
documentation system.

DDC is **not** a separate knowledge base, framework, entity schema, or mandatory
log. It follows the existing routing, documentation boundaries, terminology,
and maintenance rules.

## Principles

- Discover before asking: inspect relevant existing docs, code, and tests.
- Assess [context sufficiency](../DICTIONARY.md#context-sufficiency) on each substantive task, but interrupt only when
  an important unresolved question warrants it.
- Distinguish missing knowledge from failed retrieval, implementation defects,
  transient investigation needs, and decisions that have not yet been made.
- Ask targeted questions. Never fabricate domain-specific rules.
- User choice controls how unresolved context affects the task, but does not
  make an unsupported assumption true.
- When validated reusable information resolves a gap, prepare updates to
  existing canonical docs automatically as part of an authorized editing task.
- Keep [provisional assumptions](../DICTIONARY.md#provisional-assumption) and unimplemented desired behavior visibly
  separate from established current behavior.
- New co-located `*.docs.md` files are never created automatically.
- Use ordinary repository validation and review processes, not a new mandatory
  DDC publication process.
- Do not introduce provenance or knowledge-ownership tracking fields or files.

## When To Run

For every substantive task:

1. Route through relevant global docs according to `docs-routing.md`. Routing
   may correctly identify zero global docs to read.
2. When reading concrete source/config files, inspect relevant adjacent
   `*.docs.md` files using the existing co-located docs rules.
3. Consider relevant code, tests, contracts, and repository instructions.
4. Before a materially dependent decision, assess whether the necessary
   information is actually sufficient.
5. Reassess when further work uncovers a new material unknown.

Do not load all documentation or run a comprehensive gap-scanning pass for
ordinary tasks. A successful routing step does not prove context sufficiency.
When context is sufficient, proceed without a user-facing DDC ceremony.

## Diagnose The Need

Distinguish these situations before asking for information:

- **Routing/discovery failure**: the answer exists but was not found; fix
  discovery and, when appropriate, the relevant `_index.md` entry.
- **Knowledge gap**: a [context gap](../DICTIONARY.md#context-gap) where relevant knowledge is absent, partial, stale, conflicting,
  or only available outside canonical docs.
- **Undecided requirement**: a design or business policy has not been decided.
  Ask for a decision rather than implying an established fact exists.
- **Implementation defect**: context is sufficient but code is incorrect;
  fix code rather than manufacturing new documentation.
- **Transient evidence gap**: obtain the needed current observation without
  necessarily publishing it as durable documentation.
- **Tool/access limitation**: disclose the limitation instead of guessing.

For a knowledge gap, classify current documentation state independently of
severity:

| State | Meaning | Appropriate reaction |
| --- | --- | --- |
| CLEAN | Existing docs correctly answer the relevant question | Proceed |
| INCOMPLETE | Docs contain partial but insufficient information | Extend existing docs after resolution |
| STALE | Docs misdescribe current known reality | Correct existing docs |
| TRIBAL | Relevant knowledge exists outside canonical docs | Inspect/curate when appropriate |
| MISSING | Needed knowledge cannot be established from known sources | Request targeted clarification |

Do not label information MISSING merely because the first index did not show it.
For conflicting information, identify the contradiction rather than deciding
by confidence alone. Source code reflects *actual implementation*, not always
*intended policy*.

## Severity And Interruptions

Severity is task-relative and separate from knowledge state:

- **Blocking**: unresolved information materially affects correctness, safety,
  irreversibility, or a required choice. Ask and wait for the user's answer
  before dependent work. In particular, stop and ask before making an ambiguous
  high-impact decision.
- **Non-blocking**: useful work can proceed and a clear, reversible assumption
  or a deferred subtask is acceptable. Continue, preserve the specific
  question in the task context, and surface it at completion if still material.
- **Informational**: the detail does not affect task correctness. Continue
  without interruption or durable documentation churn.

Do not rely on an agent's numerical confidence score to determine severity.

When interrupting for a blocking gap, explain concisely:

1. What exact information or decision is needed.
2. What is already established and what remains uncertain.
3. Why the gap affects the requested task.
4. Which relevant areas of docs/code/tests were examined (briefly).
5. Safe next actions: provide an answer; investigate further; defer or narrow
   dependent work; or approve one explicit provisional assumption only when
   that assumption is safe and appropriate.

Ask the smallest sufficient question. Avoid repeated or speculative questions.
Do not ask the user to restate information they already supplied.

### If the user chooses to continue without an answer

Continue only in a defensible form:

- Perform independent work, leaving the uncertain part undone; or
- Use an explicitly stated, user-approved *provisional* assumption within a
  reversible/safe scope; or
- Reduce scope and report what was excluded; or
- Stop the dependent action if there is no responsible way forward.

Never convert an unverified assumption into a canonical business rule.

### Non-blocking and late-discovered gaps

Track a concise task-local unresolved question. Continue with independent
work and disclose consequential provisional assumptions. At task completion,
raise only outstanding questions that materially affect the result or reusable
knowledge. If an answer arrives after work was performed, re-evaluate the work,
change implementation where necessary, and retest before declaring completion.
If the task was already closed, treat a later resolution as follow-up work.
Persist important long-lived unknowns in the relevant `_status.md` when useful;
do not create a durable record for every minor question.

## When The User Provides Missing Context

A response to an identified gap automatically triggers **assessment and
curation consideration**. It does not automatically establish permanent truth.

1. Match the answer to the unresolved question; identify anything still unclear.
2. Distinguish explicit confirmed requirements/current-state clarification from
   tentative statements, temporary assumptions, and one-off preferences.
3. Reconcile with relevant code, tests, existing docs, and other requirements.
   Existing code describes current behavior; a new requirement can describe a
   desired future behavior. Do not silently collapse the two.
4. Determine whether the information is stable, reusable, and appropriate for
   canonical docs.
5. For an authorized repository-editing task, automatically prepare an update
   to the smallest suitable **existing** canonical document when justified.
   Do not request redundant permission merely to edit an existing affected doc.
6. If a new focused global topic doc is justified but no current doc fits,
   propose the new document and follow the user's documentation-scope choices.
   Do not silently expand the documentation system.
7. Never create a new co-located `*.docs.md` without explicit user instruction.
8. Validate affected implementation and docs together. Publish through the
   existing repository workflow; do not treat an unreviewed draft as accepted
   canonical truth.

If the task is analytical, read-only, or otherwise not authorized to edit the
repository, describe or propose the appropriate documentation change instead.
If the user explicitly instructs the agent not to edit docs, obey and call out
meaningful resulting drift where useful.

A user may introduce a new intended requirement. Document it as **planned** or
**proposed** until it is implemented; after implementation, describe current
behavior accurately. A tentative statement such as "I think..." must remain
provisional and must not be presented as established fact.

## Documentation Placement

Use the existing [indexed docs system](../DICTIONARY.md#indexed-docs-system) categories:

- Existing focused [global doc](../DICTIONARY.md#global-docs) under `docs/`: reusable system/business
  rules, cross-cutting contracts, architecture, behavior.
- Existing adjacent [co-located doc](../DICTIONARY.md#co-located-docs) (`<file>.docs.md`): file/module-specific non-obvious intent,
  public interface, invariant, or integration constraint.
- `docs/DICTIONARY.md`: important stable terminology, following existing
  concept/meta sections and dictionary coverage rules.
- Relevant `_status.md`: consequential current uncertainty, unresolved gap,
  or known difference between intended and implemented behavior.
- Relevant `_decisions.md`: rationale and tradeoffs of meaningful decisions.
- Relevant `_index.md`: navigation updates when discovery changes.

Choose the place by **conceptual scope**, not by the file the agent happened to
have open. Avoid duplicating the same canonical rule across global and local
docs. Co-located files remain excluded from the global `_index.md` tree.

### Existing co-located docs without a source-code edit

If validated newly supplied knowledge changes the meaning of an **existing**
relevant adjacent `*.docs.md`, update that document in the authorized task even
when its source/config file is unchanged. Only inspect co-located docs adjacent
to relevant concrete files. Do not change unrelated co-located docs and never
create a new one automatically.

## Validate And Close The Loop

After resolving a gap:

1. Reattempt the affected question or development step using the clarified
   information. No deliberately incorrect "before" implementation is needed.
2. Validate with relevant tests, checks, or human acceptance as appropriate.
3. If the result fails, correct the work and draft docs and repeat validation.
4. Check documentation for contradictions, duplicate facts, outdated terms,
   incorrect current/planned status, and broken links.
5. Follow normal global index maintenance and
   [dictionary coverage pass](../DICTIONARY.md#dictionary-coverage-pass) rules when
   relevant docs change.
6. Report changes made, any assumptions still in force, and unresolved material
   questions. A mandatory DDC cycle log is not required.

For information that changes frequently, use a modest review reminder or
relevant `_status.md` note only when it provides real value. Reading a doc is
not evidence that it was verified. Do not require provenance, person/team
ownership, or universal freshness metadata.

## Boundaries

- DDC is task-driven; no top-down requirement to document an entire domain.
- Do not create new DDC entities, ontology, graph, or second knowledge base.
- Do not create new co-located docs automatically.
- Do not turn temporary assumptions into established facts.
- Do not interrupt for optional trivia.
- Do not introduce mandatory scores, logs, new subagents, or tooling.
- Keep existing conceptual-simplicity, routing, and maintenance rules intact.

## Related Documentation

- [docs-routing.md](docs-routing.md): selecting existing global documentation.
- [docs-system.md](docs-system.md): global docs, maintenance, and canonical scope.
- [colocated-docs.md](colocated-docs.md): adjacent documentation boundaries.
- [conceptual-simplicity.md](conceptual-simplicity.md): focused responsibility boundaries.
- [Dictionary](../DICTIONARY.md): shared terminology.
