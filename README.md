# Docs-Driven Agentic Engineering (DEA) Template

Template version: 1.0.0

- [What This Template Is For](#what-this-template-is-for)
- [How To Set Up](#how-to-set-up)
- [How To Use This Workflow](#how-to-use-this-workflow)
- [Technical Documentation](#technical-documentation)

## What This Template Is For

This template gives you an **easy starting point** for docs-driven agentic engineering (DEA).
You'll get a reusable documentation workflow that you can copy into your own repository and adapt from there.

- **Agents discover relevant docs**
- **Agents maintain docs system**
- **Engineers remain in control over what to add and when**

## How To Set Up

For any agent:

- add the contents of `AGENTS.md` to your repository's `AGENTS.md`, or copy the file if you do not already have one
- copy the `docs/` directory into the target repository

This shared setup gives the destination repository the canonical DEA documentation model and the repository-level workflow rules.

Continue with:

- [Set Up With Codex](#set-up-with-codex)
- [Set Up With Claude](#set-up-with-claude)

### Set Up With Codex

For the Codex-specific setup:

- copy `.agents/skills/` into the target repository
- copy the contents of `.codex/config.toml`
- copy `.codex/profiles/repo-analyst.md` into your `.codex/profiles`

Recommended target layout in the destination repository:

```text
<repo>/
  AGENTS.md
  docs/
  .agents/skills/
  .codex/config.toml
  .codex/profiles/repo-analyst.md
```

What each copied part does:

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Contains the always-on repository rules. |
| `docs/` | Contains the canonical shared DEA workflow documentation. |
| `.agents/skills/` | Contains the operational skills that implement the workflow. |
| `.codex/config.toml` | Registers the reusable `repo-analyst` profile. |
| `.codex/profiles/repo-analyst.md` | Defines the analytical reading behavior for deep repository understanding and contradiction-finding. |

## How To Use This Workflow

### tl;dr

- You decide which docs to add, when to add docs and how (manually, automated workflows, etc)
- The workflow then helps the agent consistently
  - route through the relevant docs
  - maintain the docs system
  - keep documentation aligned with repository truth.

---

This workflow is not fully automatic by itself. It gives the agent a structured documentation system and clear maintenance rules, but users still need to define the repository's actual documentation content and boundaries.

What users need to do:

- define which global docs areas should exist under `docs/`
- define which topic docs should be added as the repository grows
- decide what belongs in global docs versus co-located `*.docs.md` files
- define the repository's actual business-domain terminology in `docs/DICTIONARY.md` once stable terms exist
- make explicit when new workflow conventions or product concepts should become canonical documentation
- explicitly request creation of new co-located docs when they are warranted, because co-located doc creation is intentionally conservative

What the workflow automates for Codex once those structures exist:

- routing through global docs for every substantive prompt
- reading only the minimum sufficient set of global docs by default
- checking for adjacent co-located docs when concrete files are read
- updating existing co-located docs when the documented file changes in a relevant way
- maintaining `_index.md` routing integrity when global docs change
- maintaining `README.md` as the human mental-model entrypoint in each docs folder
- maintaining `_status.md` and `_decisions.md` when current-state or rationale information changes
- maintaining `docs/DICTIONARY.md` when important repository terminology is introduced, changed, or removed
- proactively surfacing meaningful contradictions noticed while routing or reading docs

In practice, the workflow works best when users treat documentation structure as part of repository design. The automation keeps the system coherent, but it does not decide the repository's product model or documentation scope on its own.

## Technical Documentation

This section describes the full structure of the current repository and how the workflow is wired.

Rules for this root `README.md`:

- there should be a Table of Contents directly under the `h1`, without its own headline
- the top Table of Contents should include only this document's top-level `h2` sections
- the Table of Contents should not list any subheadings from within Technical Documentation
- the Technical Documentation section should describe the structure in depth and be exhaustive enough to cover:
  - the intention of every file
  - which files are shared across all agents
  - which files are agent-specific and, when relevant, which agents they belong to
  - the wiring of how the different agents implement the DEA workflow

### High-Level Structure

The repository has three layers:

1. Shared workflow rules in `docs/`
2. Agent activation rules in `AGENTS.md`
3. Codex-specific implementation files in `.agents/` and `.codex/`

The intended split is:

- `docs/` defines the canonical workflow model
- `AGENTS.md` makes the workflow mandatory for this repository
- Codex-specific files implement Codex-native behavior on top of the shared model

### File Inventory And Intent

#### Shared Across Agents

These files are intended to be reusable regardless of agent vendor.

`docs/_index.md`

- Root navigation file for the global docs tree.
- First routing entrypoint when global docs are needed.
- Defines the top-level docs areas and when each should be read.

`docs/README.md`

- Human mental-model entrypoint for the `docs/` tree.
- Explains what the documentation system is for.

`docs/_status.md`

- Present-state doc for the root docs area.
- Captures what is true now, what is still unsettled, and current gaps.

`docs/_decisions.md`

- Rationale doc for the root docs area.
- Explains why the docs system is shaped the way it is when that is not obvious from the file tree alone.

`docs/DICTIONARY.md`

- Canonical business-domain dictionary for terminology used by this repository's own docs.
- Keeps domain language consistent, linkable, and centrally maintained.

`docs/process/_index.md`

- Navigation file for the process docs area.
- Routes readers to the specific process documents that define the DEA workflow.

`docs/process/README.md`

- Human mental-model entrypoint for the process docs area.
- Explains what the process area covers and how the documents in it fit together.

`docs/process/_status.md`

- Present-state context for the process area.
- Records what parts of the process are active and which parts are still only lightly exercised.

`docs/process/_decisions.md`

- Rationale for the process docs area.
- Explains why routing, status, and rationale are separated.

`docs/process/docs-routing.md`

- Defines the routing model for global docs.
- Establishes `_index.md` as navigation, `README.md` as the human entrypoint, `_status.md` as current-state context, `_decisions.md` as rationale, and topic docs as focused mechanisms or rules.

`docs/process/docs-system.md`

- Defines the overall documentation system.
- Explains the split between global docs under `docs/` and optional co-located docs in `*.docs.md`.
- Defines maintenance expectations for routing, dictionary updates, and doc ownership.

`docs/process/colocated-docs.md`

- Defines the naming, purpose, and constraints for co-located `*.docs.md` files.
- Establishes that co-located docs are optional and discovered by adjacency rather than global routing.

`docs/process/transitional-docs.md`

- Defines how to work safely when a repository has not fully adopted the indexed docs model.
- Exists so the workflow can be applied incrementally in less normalized repositories.

These files are shared because they define the DEA model itself rather than any Codex-specific mechanism.

#### Shared In Spirit, But Currently Codex-Wired

`AGENTS.md`

- Declares the always-on repository rules for how the workflow must be applied.
- Tells the agent to route through global docs for every substantive prompt.
- Tells the agent to check co-located docs when reading or editing concrete files.
- Tells the agent to maintain global docs, the dictionary, and co-located docs when relevant.

This file is conceptually cross-agent, but the current contents are explicitly wired to Codex skills by name:

- `global-docs-router`
- `global-docs-maintainer`
- `business-dictionary-maintainer`
- `colocated-docs-reader`
- `colocated-docs-maintainer`
- `colocated-docs-creator`

That means the policy is reusable, but the mechanism currently assumes an agent runtime that understands this skill system.

#### Codex-Specific

`.agents/skills/global-docs-router/SKILL.md`

- Codex operational skill for deciding whether global docs are needed and, if they are, reading the minimum sufficient set.
- Implements proactive contradiction surfacing during routing.

`.agents/skills/global-docs-maintainer/SKILL.md`

- Codex operational skill for maintaining canonical docs and `_index.md` routing integrity when repository truth changes.

`.agents/skills/business-dictionary-maintainer/SKILL.md`

- Codex operational skill for maintaining `docs/DICTIONARY.md` as the canonical terminology file.

`.agents/skills/colocated-docs-reader/SKILL.md`

- Codex operational skill for checking whether a concrete file has an adjacent `*.docs.md` file and reading it when relevant.

`.agents/skills/colocated-docs-maintainer/SKILL.md`

- Codex operational skill for updating an existing adjacent `*.docs.md` file when the documented file changes.

`.agents/skills/colocated-docs-creator/SKILL.md`

- Codex operational skill for creating a new co-located doc only when the user explicitly requested one and the file meets narrow warrant criteria.

`.codex/config.toml`

- Codex configuration file.
- Registers the reusable `repo-analyst` profile.
- Currently pins that profile to `gpt-5.4`.

`.codex/profiles/repo-analyst.md`

- Codex profile instructions for analytical work.
- Expands the default reading behavior to lower omission risk.
- Optimizes for repository understanding, contradiction-finding, and broad context gathering instead of minimal implementation-oriented routing.

### Current Agent Support Matrix

Shared across all agents in principle:

- `docs/`

Shared across some agents but not all in current form:

- `AGENTS.md`
  - directly useful for Codex
  - potentially reusable for Cursor and other tools that recognize `AGENTS.md`
  - not a complete native integration for Claude or Gemini as currently implemented

Codex-specific:

- `.agents/skills/`
- `.codex/config.toml`
- `.codex/profiles/repo-analyst.md`

Not yet implemented:

- Claude-native files such as `CLAUDE.md` or `.claude/...`
- Gemini-native files such as `GEMINI.md` or Gemini-specific project configuration
- Cursor-native rule files beyond the partial reuse possible through `AGENTS.md`

### DEA Workflow Wiring

The current DEA wiring for Codex works like this:

1. The repository-level trigger lives in `AGENTS.md`.
2. `AGENTS.md` requires global docs routing for every substantive prompt.
3. `AGENTS.md` requires co-located doc checks when concrete files are read or modified.
4. `AGENTS.md` requires docs maintenance behavior when files under `docs/` or term definitions change.
5. The actual operational behavior is implemented by the Codex skills in `.agents/skills/`.
6. Those skills read the canonical rules from `docs/` and apply them to the current task.
7. For deep analysis tasks, `.codex/config.toml` exposes the `repo-analyst` profile, which uses `.codex/profiles/repo-analyst.md` to widen the reading strategy beyond the default conservative router behavior.

That means the wiring is intentionally layered:

- `docs/` defines the workflow
- `AGENTS.md` enforces the workflow
- `.agents/skills/` executes the workflow in Codex
- `.codex/profiles/repo-analyst.md` provides an alternate Codex reading mode for analytical tasks

### Relationship Between Global Docs And Co-Located Docs

The repository uses two documentation scopes:

- global docs under `docs/`
- optional file-specific docs in `*.docs.md`

Global docs are for:

- cross-cutting workflow rules
- canonical process definitions
- shared terminology
- repository-wide discoverability

Co-located docs are for:

- one concrete source or configuration file
- non-obvious local intent
- important invariants or boundary expectations
- file-specific guidance that would be too narrow for global docs

The two systems are intentionally separate:

- global docs participate in `_index.md` routing
- co-located docs are discovered only by adjacency

### What Would Need To Change For Multi-Agent Support

To support more than Codex cleanly, keep `docs/` as the canonical workflow layer and add thin native integration files per agent.

Examples:

- Claude support would add `CLAUDE.md` and likely `.claude/` configuration while continuing to reuse `docs/`.
- Gemini support would add Gemini-native repository instructions while continuing to reuse `docs/`.
- Cursor support would likely reuse `AGENTS.md` and may add Cursor-native rule configuration if needed.

The intended future pattern is:

- one shared DEA model in `docs/`
- one thin activation layer per agent runtime
- minimal duplication of workflow logic outside `docs/`
