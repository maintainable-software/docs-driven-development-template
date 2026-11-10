#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
mkdir -p "$work/repo/scripts" "$work/repo/.agents/skills/example/assets/empty"
cp "$root/scripts/sync-skills.sh" "$work/repo/scripts/"
cd "$work/repo"
printf 'Example skill\n' > .agents/skills/example/SKILL.md
printf '\0\1\2' > '.agents/skills/example/assets/binary file'
printf '#!/bin/sh\nexit 0\n' > .agents/skills/example/run.sh
chmod +x .agents/skills/example/run.sh
sync_skills() { bash scripts/sync-skills.sh "$@"; }
reject() { if sync_skills "$@" > "$work/error" 2>&1; then printf 'Expected rejection\n' >&2; exit 1; fi; }
reject --check
[[ ! -e .claude ]]
sync_skills
sync_skills --check
diff -r .agents/skills/example .claude/skills/example
[[ -x .claude/skills/example/run.sh && -d .claude/skills/example/assets/empty ]]
mkdir .claude/skills/personal
printf 'Keep me\n' > .claude/skills/personal/SKILL.md
printf 'Updated\n' >> .agents/skills/example/SKILL.md
reject --check
sync_skills
sync_skills --check
printf 'Manual edit\n' >> .claude/skills/example/SKILL.md
reject
reject --check
cp .agents/skills/example/SKILL.md .claude/skills/example/SKILL.md
ln -s /tmp .agents/skills/example/link
reject
rm .agents/skills/example/link
mkdir .agents/skills/personal
printf 'Collision\n' > .agents/skills/personal/SKILL.md
reject
rm -r .agents/skills/personal
cp .claude/skills/.sync-skills-manifest "$work/manifest"
printf '../escape\tinvalid\n' >> .claude/skills/.sync-skills-manifest
reject
cp "$work/manifest" .claude/skills/.sync-skills-manifest
rm -r .agents/skills/example
reject --check
sync_skills
sync_skills --check
[[ ! -e .claude/skills/example && -f .claude/skills/personal/SKILL.md ]]
# Source ancestors must not redirect writes or reads.
mv .agents .agents-real
ln -s .agents-real .agents
reject
printf 'All skill synchronization tests passed.\n'
