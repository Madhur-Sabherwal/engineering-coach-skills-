#!/usr/bin/env bash
# Copies every skill in ./skills into your Claude Code skills folder.
# Usage: bash scripts/install.sh [coach-data-engineering coach-robotics ...]
set -euo pipefail
src="$(cd "$(dirname "$0")/.." && pwd)/skills"
dst="$HOME/.claude/skills"
mkdir -p "$dst"
if [ "$#" -gt 0 ]; then names=("$@"); else names=($(ls "$src")); fi
for n in "${names[@]}"; do
  cp -R "$src/$n" "$dst/"
  echo "Installed $n"
done
