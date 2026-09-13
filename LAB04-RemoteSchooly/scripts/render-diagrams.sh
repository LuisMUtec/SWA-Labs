#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for source in "$repo_root"/architecture/diagrams/*.dot; do
  output_base="${source%.dot}"
  dot -Tsvg "$source" -o "${output_base}.svg"
  dot -Tpng -Gdpi=150 "$source" -o "${output_base}.png"
done

echo "Rendered architecture diagrams."
