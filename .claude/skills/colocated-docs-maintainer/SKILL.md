---
name: colocated-docs-maintainer
description: Update an existing adjacent *.docs.md file when source/config changes or validated reusable context affect it during an authorized editing task, including when the source file is unchanged.
---

# Colocated Docs Maintainer

Use this skill whenever you modify a concrete source or configuration file, **or** when validated, reusable context supplied during an authorized editing task may change an existing relevant adjacent `*.docs.md` file even without a source/config edit.

## Workflow

1. Derive the co-located docs path by replacing the file extension with `.docs.md`.
2. Check whether that co-located docs file exists.
3. If it exists and the source change or validated reusable context affects documented behavior, interface, intent, invariants, or constraints, update it in the same authorized task.
4. If it does not exist, stop and do not create a new co-located docs file unless the user explicitly requests one.
5. If the co-located docs and code disagree about current behavior, correct stale descriptions to match confirmed implementation. Keep explicit intended or planned requirements distinct; do not discard them merely because they are not implemented yet. Resolve unclear intent before making a dependent change.
6. When a material context gap is resolved by validated user input, check the existing relevant adjacent `*.docs.md` for newly incorrect or missing local behavior, intent, invariants, interfaces, or constraints, even if the concrete source file was not modified.
7. If the existing adjacent doc is affected, update it in the same authorized task, keeping actual-versus-planned behavior explicit and avoiding duplication of a cross-cutting global rule.
8. If the adjacent doc does not exist, do not create one without explicit user instruction. If the information is cross-cutting, use the relevant existing global doc instead.

## Boundaries

- Do not create new co-located docs files unless explicitly requested.
- Do not update unrelated `*.docs.md` files.
- Do not use this skill for global docs under `docs/`.
- Do not treat any user statement as automatically validated canonical truth; follow `docs/process/demand-driven-context.md`.
- Do not scan unrelated files or discover co-located docs through the global index.

## Canonical References

Read [docs/process/colocated-docs.md](../../../docs/process/colocated-docs.md) for the co-located docs convention.
Read [docs/process/demand-driven-context.md](../../../docs/process/demand-driven-context.md) for context-gap resolution and knowledge curation rules.
