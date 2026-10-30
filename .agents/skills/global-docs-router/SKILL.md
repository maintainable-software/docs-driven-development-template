---
name: global-docs-router
description: Route into this repository's global indexed documentation system under docs/, load the smallest relevant set of global docs, and assess task-relative context sufficiency after discovery.
---

# Global Docs Router

Use this skill for every substantive prompt before implementation work starts.

## Workflow

1. Decide whether global repository docs are needed for the task.
2. If no global docs are needed, make that decision explicit in your reasoning and skip global-doc loading. Still assess task context in steps 15–18 after considering relevant available code, tests, and requirements.
3. If global docs are needed, read `docs/_index.md` first.
4. Use each structured `_index.md` entry's `Read when`, `Summary`, and `Tags` fields to identify the smallest relevant global docs area for the task.
5. Read that area's `_index.md` before opening documents inside the area.
6. Treat `_index.md` as navigation, `README.md` as the human mental-model entrypoint, `_status.md` as present-state context, `_decisions.md` as rationale, and ordinary topic docs as focused mechanisms or rules.
7. Read the area's `README.md` when you need to understand what the area is, why it exists, or how its docs are meant to be interpreted.
8. Read the area's `_status.md` when current reality, active uncertainty, known gaps, or open questions matter to the task.
9. Read the area's `_decisions.md` when rationale, tradeoffs, or historical intent matter to the task.
10. Read only the minimum sufficient set of topic docs after the relevant higher-level area docs are loaded.
11. Read `docs/process/conceptual-simplicity.md` when the task affects architecture, implementation boundaries, system decomposition, terminology boundaries, or docs structure.
12. Read `docs/DICTIONARY.md` when the task depends on repository terminology, terminology consistency, or docs prose that may introduce or redefine important terms.
13. If you notice a meaningful contradiction or mismatch while routing or reading global docs, surface it clearly even if the user did not explicitly ask for contradiction-finding.
14. If global docs and code disagree about current implementation, trust the code and note the mismatch. Distinguish that from an intended requirement that is not yet implemented.
15. After the relevant docs and available task-related code/test context have been considered, assess whether context is sufficient for the task's material decisions. Do not infer sufficiency merely from finding relevant documents.
16. Distinguish missing information from unsuccessful discovery, stale or contradictory docs, an undecided requirement, an implementation defect, and a transient evidence or tool-access gap.
17. For a material knowledge gap, follow `docs/process/demand-driven-context.md`: classify its documentation state and task severity, stop and ask before an ambiguous high-impact decision or blocking dependent work, and wait for the user's answer. Otherwise continue useful work while retaining consequential unresolved questions.
18. Reassess sufficiency if new code, tests, or design work exposes another material unknown. When context is adequate, continue silently without a DDC report.

## Boundaries

- Do not read the entire `docs/` tree by default.
- Do not treat this skill as a reason to spawn a subagent automatically.
- Do not use this skill to discover co-located `*.docs.md` files.
- Prefer the `Read when` field as the primary routing hint, with `Summary` and `Tags` as supporting signals.
- Do not treat `README.md` as a routing index. In this repository it is the human entrypoint for the folder.
- When a task depends on how the repository should decompose concepts, modules, or system parts, include the conceptual-simplicity rules rather than inferring structure ad hoc.
- When surfacing an incidental contradiction, identify the conflicting files and keep the contradiction note separate from the main answer.
- Use explicit file references when summarizing findings.
- Do not turn the context-sufficiency check into a full-repository scan, a mandatory numerical confidence score, or a question to the user for every substantive task.
- Code is evidence of current implemented behavior, not necessarily the intended product rule; surface the distinction when it affects the task.
- Read the detailed demand-driven context policy when a material gap or curation decision actually requires it, not automatically for all prompts.

## Canonical References

Read [docs/_index.md](../../../docs/_index.md) for the root global docs index.
Read [docs/DICTIONARY.md](../../../docs/DICTIONARY.md) when repository terminology matters to the task.
Read [docs/process/_index.md](../../../docs/process/_index.md) for process docs routing.
Read [docs/process/conceptual-simplicity.md](../../../docs/process/conceptual-simplicity.md) when the task depends on conceptual boundaries, module responsibilities, or anti-complecting rules.
Read [docs/process/docs-routing.md](../../../docs/process/docs-routing.md) when the repository follows the indexed global docs system.
Read [docs/process/transitional-docs.md](../../../docs/process/transitional-docs.md) when the global docs tree is only partially normalized.
Read [docs/process/demand-driven-context.md](../../../docs/process/demand-driven-context.md) when the task encounters a material context gap or needs knowledge curation rules.
