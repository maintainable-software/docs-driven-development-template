#!/usr/bin/env bash
# Requires Bash 4.4+ and GNU coreutils/findutils. See docs/process/skills.md.
set -euo pipefail
export LC_ALL=C
fail() { printf 'Skill sync: %s\n' "$*" >&2; exit 1; }
check=false
case "${1-}" in
    --check) check=true ;;
    --help|-h) printf 'Usage: %s [--check]\n' "$0"; exit 0 ;;
    '') ;;
    *) fail "Unknown argument: $1" ;;
esac
(( $# <= 1 )) || fail 'Too many arguments'
root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
source_dir=$root/.agents/skills
destination=$root/.claude/skills
manifest=.sync-skills-manifest
for path in "$root/.agents" "$source_dir" "$root/.claude" "$destination"; do
    [[ ! -L $path ]] || fail "Symlink directory: $path"
    [[ ! -e $path || -d $path ]] || fail "Expected directory: $path"
done
[[ -d $source_dir ]] || fail "Missing source: $source_dir"
valid_name() { [[ $1 =~ ^[a-z0-9]+(-[a-z0-9]+)*$ && ${#1} -le 64 && $1 != synced && $1 != anthropic-skills ]]; }
# Include names, bytes, empty directories, and executable permissions.
fingerprint() (
    set -euo pipefail
    cd -- "$1"
    find . -mindepth 1 -print0 | sort -z | while IFS= read -r -d '' path; do
        [[ ! -L $path ]] || fail "Symlink: $1/$path"
        if [[ -d $path ]]; then
            printf 'd\0%s\0' "$path"
        elif [[ -f $path ]]; then
            printf 'f\0%s\0' "$path"
            if [[ -x $path ]]; then printf 'x\0'; else printf -- '-\0'; fi
            sha256sum < "$path"
        else
            fail "Unsupported file: $1/$path"
        fi
    done | sha256sum | cut -d ' ' -f 1
)
declare -A desired=() previous=()
shopt -s nullglob dotglob
for path in "$source_dir"/*; do
    name=${path##*/}
    valid_name "$name" || fail "Invalid skill name: $name"
    [[ -d $path && ! -L $path && -f $path/SKILL.md ]] || fail "Missing skill directory/SKILL.md: $path"
    desired[$name]=$(fingerprint "$path")
done
if [[ -e $destination/$manifest || -L $destination/$manifest ]]; then
    [[ -f $destination/$manifest && ! -L $destination/$manifest ]] || fail 'Invalid manifest file'
    {
        IFS= read -r header || fail 'Empty manifest'
        [[ $header == 'skill-sync-v1' ]] || fail 'Unsupported manifest version'
        while IFS= read -r line || [[ -n $line ]]; do
            [[ $line =~ ^([a-z0-9-]+)$'\t'([a-f0-9]{64})$ ]] || fail 'Malformed manifest record'
            name=${BASH_REMATCH[1]} digest=${BASH_REMATCH[2]}
            valid_name "$name" || fail 'Invalid manifest name'
            [[ ! ${previous[$name]+exists} ]] || fail 'Duplicate manifest name'
            previous[$name]=$digest
        done
    } < "$destination/$manifest"
fi
# Validate every conflict before changing anything.
for name in "${!previous[@]}"; do
    path=$destination/$name
    [[ -d $path && ! -L $path ]] || fail "Managed skill missing/replaced: $name; restore its generated copy"
    actual=$(fingerprint "$path")
    [[ $actual == "${previous[$name]}" ]] || fail "Manual changes in $name; preserve them and restore the generated copy"
done
for name in "${!desired[@]}"; do
    if [[ ! ${previous[$name]+exists} && ( -e $destination/$name || -L $destination/$name ) ]]; then
        fail "Unmanaged destination exists: $name; move it aside first"
    fi
done
emit_manifest() {
    printf 'skill-sync-v1\n'
    for name in "${!desired[@]}"; do printf '%s\t%s\n' "$name" "${desired[$name]}"; done | sort
}
if [[ -f $destination/$manifest ]] && cmp -s "$destination/$manifest" <(emit_manifest); then
    printf 'Skills already synchronized (%s skills).\n' "${#desired[@]}"
    exit 0
fi
$check && fail 'Skills are out of date. Run bash scripts/sync-skills.sh'
# Stage a complete replacement, preserving unrelated Claude skills.
mkdir -p -- "$root/.claude"
stage=$(mktemp -d "$root/.claude/.sync-skills.XXXXXXXX")
cleanup() {
    status=$?
    if [[ -d $stage/old && ! -e $destination ]]; then
        mv -- "$stage/old" "$destination" || { printf 'Recovery copy: %s/old\n' "$stage" >&2; exit 1; }
    fi
    rm -rf -- "$stage"
    exit "$status"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
mkdir -- "$stage/new"
if [[ -d $destination ]]; then cp -a -- "$destination/." "$stage/new/"; fi
for name in "${!previous[@]}"; do rm -rf -- "$stage/new/$name"; done
for name in "${!desired[@]}"; do
    cp -a -- "$source_dir/$name" "$stage/new/$name"
    actual=$(fingerprint "$stage/new/$name")
    [[ $actual == "${desired[$name]}" ]] || fail "Source changed while copying: $name"
done
emit_manifest > "$stage/new/$manifest"
if [[ -d $destination ]]; then mv -- "$destination" "$stage/old"; fi
mv -- "$stage/new" "$destination"
printf 'Synchronized %s skills.\n' "${#desired[@]}"
