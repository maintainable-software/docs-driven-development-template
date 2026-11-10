---
type: Reference
title: Shared Skills
description: Synchronizes canonical repository skills into generated Claude Code copies using Bash.
tags:
  - skills
  - process
  - claude
  - codex
---

# Shared Skills

## Responsibility

Keep repository [skills](../DICTIONARY.md#skill) authored in `.agents/skills/`
available as generated copies in `.claude/skills/`. Edit the canonical source,
then commit the generated copies and their [synchronization manifest](../DICTIONARY.md#synchronization-manifest).
Relative documentation links retain the same directory depth.

Claude Code discovers project skills in `.claude/skills/`, as described in
[its skill documentation](https://code.claude.com/docs/en/skills).
Root [CLAUDE.md](../../CLAUDE.md) imports [AGENTS.md](../../AGENTS.md) using
[Claude's import syntax](https://code.claude.com/docs/en/memory), sharing the
repository instructions as well as the skill files.

## Not responsible for

The synchronizer does not translate agent-specific tool instructions, validate
YAML frontmatter, install global skills, or change host settings. A copied
skill still requires the tools its instructions use. It is a Bash adaptation
of the sibling design-system-starter synchronizer, with a separate text
manifest format; it does not read that script's JSON manifest.

## Inputs

Each immediate directory under `.agents/skills/` must have a `SKILL.md` file.
Names use lowercase ASCII letters, digits, and single internal hyphens, up to
64 characters; `synced` and `anthropic-skills` are reserved. Skill contents may
include nested files, binary resources, executable scripts, and empty folders.
Source trees and managed destination trees cannot contain symlinks or special
files. This script checks directory names and the presence of `SKILL.md`, not
whether the instructions satisfy the full Agent Skills specification.

## Outputs

[scripts/sync-skills.sh](../../scripts/sync-skills.sh) copies complete skill
directories and records their fingerprints in
`.claude/skills/.sync-skills-manifest`. Fingerprints cover paths, file bytes,
empty directories, and executable status. Unrelated Claude skills are preserved.
A removed canonical skill is removed from the generated destination only when
its existing copy matches the recorded fingerprint.

```bash
bash scripts/sync-skills.sh
bash scripts/sync-skills.sh --check
bash scripts/test-sync-skills.sh
```

Commands locate the repository relative to the script, so they also work when
invoked by absolute path from another working directory. Requirements are Bash
4.4+ and GNU coreutils/findutils, available on Linux and suitable WSL setups.
Native Windows and stock macOS utilities are not supported.

`--check` writes nothing and exits nonzero for drift or conflicts. Normal sync
also refuses manual edits, missing managed copies, malformed manifests, and
unmanaged destination collisions before writing generated files. Preserve any
manual work, restore the affected generated files from Git, then edit the
canonical source and rerun. Move an unrelated colliding skill aside before sync.
Do not delete the manifest to bypass conflict protection.

Sync stages a replacement beside the destination, then swaps directories.
Ordinary failures during the swap restore the previous directory. Run one sync
at a time and keep sources stable during it; concurrent runs and abrupt process
termination are not supported. A leftover `.claude/.sync-skills.*` directory
may contain an `old` recovery copy after an untrappable interruption.

## Adjacent parts

- [AGENTS.md](../../AGENTS.md) defines when agents synchronize shared skills.
- [Docs System](docs-system.md) governs documentation maintenance.
- [scripts/test-sync-skills.sh](../../scripts/test-sync-skills.sh) exercises
  synchronization and conflict protection in an isolated temporary repository.
