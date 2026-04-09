## Repo Rules

### Docs Workflow

* For every substantive prompt, first use the `global-docs-router` skill.
* Follow the repository documentation model and maintenance rules defined under `docs/process/`.
* When reading a concrete source or configuration file, use the `colocated-docs-reader` skill to check for an adjacent `*.docs.md` file.
* When modifying a file under `docs/`, use the `global-docs-maintainer` skill.
* When docs or repository instructions change important repository terminology, use the `business-dictionary-maintainer` skill.
* When modifying a concrete source or configuration file, use the `colocated-docs-maintainer` skill to update an existing adjacent `*.docs.md` file if it exists and is affected.
* Do not create new co-located `*.docs.md` files as part of normal maintenance. Those files are created manually and only when explicitly requested.
