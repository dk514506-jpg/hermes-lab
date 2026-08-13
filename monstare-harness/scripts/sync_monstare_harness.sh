#!/usr/bin/env bash
# Sync the Monstare agentic harness from the live workspace into this repo.
#
# Copies (one-way: workspace -> repo):
#   $WORKSPACE/Monstare_role_prompts/                      -> monstare-harness/role_prompts/
#   curated $WORKSPACE/scripts/monstare_*.py               -> monstare-harness/scripts/
#   $WORKSPACE/skills/.../evidence-matrix-orchestration/   -> skills/evidence-matrix-orchestration/
#   $WORKSPACE/skills/.../evidence-matrix-charting-qc/     -> skills/evidence-matrix-charting-qc/
#
# Usage:
#   scripts/sync_monstare_harness.sh            # copy + commit (no push)
#   scripts/sync_monstare_harness.sh --push     # copy + commit + push origin main
#
# The live workspace defaults to /opt/data; override with MONSTARE_WORKSPACE.
# Only the curated script list below is synced — add new canonical pipeline
# scripts to SCRIPTS when they graduate from batch-specific staging.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORKSPACE="${MONSTARE_WORKSPACE:-/opt/data}"
PUSH=0
[[ "${1:-}" == "--push" ]] && PUSH=1

# Curated pipeline scripts (the reusable harness machinery; batch-specific
# staging scripts like monstare_batch3_stage*.py stay in the workspace).
SCRIPTS=(
  monstare_link_audit.py
  monstare_consolidate.py
  monstare_patch_matrix.py
  monstare_patch_charting.py
  monstare_extract_reading.py
  monstare_batch2_rows.py
  monstare_patch_charting_b3.py
)

SRC_DIRS=(
  "$WORKSPACE/Monstare_role_prompts"
  "$WORKSPACE/skills/autonomous-ai-agents/evidence-matrix-orchestration"
  "$WORKSPACE/skills/research/evidence-matrix-charting-qc"
)

cd "$REPO_ROOT"

# --- sanity ---
[ -d .git ] || { echo "ERROR: not a git repo: $REPO_ROOT" >&2; exit 1; }
for p in "${SRC_DIRS[@]}"; do
  [ -d "$p" ] || { echo "ERROR: missing source dir: $p (set MONSTARE_WORKSPACE if /opt/data is not it)" >&2; exit 1; }
done

copy_dir() { # copy_dir <src> <dst> — rsync if available, else rm+cp fallback
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$1/" "$2/"
  else
    rm -rf "$2" && cp -r "$1" "$2"
  fi
}

# 1. role prompts
copy_dir "$WORKSPACE/Monstare_role_prompts" "monstare-harness/role_prompts"

# 2. curated scripts
mkdir -p monstare-harness/scripts
for s in "${SCRIPTS[@]}"; do
  if [ -f "$WORKSPACE/scripts/$s" ]; then
    cp "$WORKSPACE/scripts/$s" monstare-harness/scripts/
  else
    echo "WARN: missing $WORKSPACE/scripts/$s — skipping" >&2
  fi
done

# 3. skills
copy_dir "$WORKSPACE/skills/autonomous-ai-agents/evidence-matrix-orchestration" "skills/evidence-matrix-orchestration"
copy_dir "$WORKSPACE/skills/research/evidence-matrix-charting-qc" "skills/evidence-matrix-charting-qc"

# 4. commit only if the harness paths actually changed
if git status --porcelain -- monstare-harness skills/evidence-matrix-orchestration skills/evidence-matrix-charting-qc | grep -q .; then
  git add monstare-harness skills/evidence-matrix-orchestration skills/evidence-matrix-charting-qc
  git commit -m "sync Monstare harness from live workspace ($(date +%F))"
  echo "Synced and committed."
else
  echo "No harness changes — already in sync."
fi

if [ "$PUSH" -eq 1 ]; then
  git push origin main
  echo "Pushed."
else
  echo "Run 'git push origin main' to publish (or re-run with --push)."
fi
