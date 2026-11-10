---
type: Reference
title: Transitional Docs
description: Explains how to work safely in repositories whose documentation structure is only partially normalized toward the indexed global docs model.
tags:
  - docs
  - transitional
  - legacy
  - migration
  - normalization
---

# Transitional Docs

Some repositories will be in a mixed state:

- area docs exist, but `docs/index.md` does not
- legacy `_index.md` files still use standalone `Path` and `Summary` fields
- technical docs live outside the intended long-term docs tree
- instruction fragments exist in legacy folders

Use those repositories as follows:

1. Read the smallest useful legacy material for the current task.
2. Make the gap explicit.
3. Prefer normalizing toward:
   - root `docs/index.md`
   - area `index.md` files
   - linked-list entries with descriptions, `Read when`, and `Tags`
   - canonical topic docs in `docs/`

Do not assume transitional locations are the intended long-term system.

## Migrating Existing Template Repositories

The filename and entry-shape changes are a breaking convention change. Migrate
index filenames, their entries, and consuming instructions together. Do not
leave two competing canonical indexes in one directory.

1. Inventory the actual docs tree, including additional areas. Search the whole
   repository, including hidden agent/config folders and examples, for
   `_index.md`, `Path`, and `Summary` dependencies.
2. Rename each `_index.md` to `index.md`. Convert entries to file-relative
   Markdown links and descriptions with labelled `Read when` and `Tags`
   inside the same list item. Preserve the useful routing specificity.
3. Declare `okf_version: "0.2"` only in `docs/index.md`; leave nested indexes
   without frontmatter. Add concept metadata under the
   [bundle and metadata rules](docs-system.md#okf-bundle-and-concept-metadata),
   preserving existing valid metadata and unrelated extension fields.
4. Make concept frontmatter authoritative for titles, descriptions, and tags;
   align index projections and keep reading conditions independently curated.
   Maintain child-area metadata in the parent index. Keep Dictionary discovery
   in the root index and direct links to definitions where useful.
5. Update skills, instructions, links, examples, and any consumers of the old
   entry schema in the same change. Preserve historical decisions, marking
   superseded filename guidance explicitly.
6. Run the structural validator and review representative routing paths before
   treating the migrated bundle as complete.

Large repositories may migrate in coherent area-sized changes. During that
transition, follow the smallest relevant legacy index when necessary, identify
the partial state in the relevant status doc, and update all consumers of each
migrated area together. Do not declare the whole bundle migrated while other
concepts or indexes still violate its contract. Preserve adjacency-based
co-located discovery; moving those files into `docs/` is not part of migration.
