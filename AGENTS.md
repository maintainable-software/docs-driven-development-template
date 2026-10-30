## Repo Rules

### Docs Workflow

* For every substantive prompt, first use the `global-docs-router` skill.
* Follow the repository documentation model and maintenance rules defined under `docs/process/`.
* When reading a concrete source or configuration file, use the `colocated-docs-reader` skill to check for an adjacent `*.docs.md` file.
* When modifying a file under `docs/`, use the `global-docs-maintainer` skill.
* When docs or repository instructions change important repository terminology, use the `business-dictionary-maintainer` skill.
* When modifying a concrete source or configuration file, or when validated reusable context affects its existing adjacent `*.docs.md` without a source edit, use the `colocated-docs-maintainer` skill to update that doc during an authorized editing task.
* Do not create new co-located `*.docs.md` files as part of normal maintenance. Those files are created manually and only when explicitly requested.
* After discovering task-relevant documentation and code context, assess whether any material knowledge or unresolved decision is needed before dependent work. Follow `docs/process/demand-driven-context.md` when a meaningful gap is found; do not interrupt for informational gaps.
* When a blocking context gap prevents a correct decision, stop and ask the user for the missing information or an explicit safe way to limit the task. Wait for their answer before making an ambiguous high-impact decision or starting dependent work. When non-blocking, continue useful work and surface material unresolved questions at the appropriate point.
* When user-supplied information resolves a context gap, automatically assess whether existing docs need a validated, reusable update as part of an authorized editing task. Do not promote provisional assumptions into canonical truth or create new `*.docs.md` files automatically.
