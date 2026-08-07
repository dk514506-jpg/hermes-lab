#!/usr/bin/env bash
# Ecology Campaign — Hermes Kanban setup
# Run this in YOUR terminal (parent context). The agent session runs as a
# delegated-child context and is (correctly) refused board mutations.
set -euo pipefail

echo "== 1. Create the campaign board =="
hermes kanban boards create ecology \
  --name "Motivational Ecology Campaign" \
  --description "Valens-style reconstruction campaign, Phases 1-8" \
  --switch

echo "== 2. Phase 5 tasks (the active workstream) =="
# Council A deliverables — agency controls
T1=$(hermes kanban create \
  "Phase 5: empowerment_boundary.md (agency rulebook)" \
  --body "Estate-wide rulebook for NOT stealing human agency. Five modes ACT/SCAFFOLD/ASK/DEFER/STOP, preserved_user_decision set, absolute prohibitions, escalation ladder, quarantine interaction. Council A deliverable — file lands at docs/Ecology/Foundation/Phase5_Safeguards/empowerment_boundary.md" \
  --priority high \
  --json | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))")
T2=$(hermes kanban create \
  "Phase 5: agent_deference_rules.md (defer/stop mechanics)" \
  --body "Operational rules for WHEN the agent defers: defer triggers, DEFER/STOP mechanics, silence-as-action, propose-vs-dispose asymmetry, re-opening deferred decisions. Council A deliverable — docs/Ecology/Foundation/Phase5_Safeguards/agent_deference_rules.md" \
  --priority high \
  --json | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))")

# Council B deliverables — atrophy controls
T3=$(hermes kanban create \
  "Phase 5: learnability_state_schema.json (estate schema)" \
  --body "Estate-wide JSON schema for skill load + atrophy across ALL skills: skill_load_score 0..1 canonical, trend, baseline vs recent arrays, assistance_fraction, dependency_ratio, empowerment ratio (inverse metric). Council B deliverable — docs/Ecology/Foundation/Phase5_Safeguards/learnability_state_schema.json" \
  --priority high \
  --json | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))")
T4=$(hermes kanban create \
  "Phase 5: skill_atrophy_risk_check.md (check procedure)" \
  --body "Operational check pipeline: compute skill_load_score, baseline-vs-recent, separate performance from capability, classify risk (none/low/medium/high), scaffolding response per level. Budzyn 2025 VERIFIED canonical warning. Council B deliverable" \
  --priority high \
  --json | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))")

# Council C deliverable — fade rules
T5=$(hermes kanban create \
  "Phase 5: scaffolding_fade_rules.md (fade trajectories)" \
  --body "Estate-wide fade rules: fade is mandatory, triggers vs hold triggers, hints>answers gradient, stepwise pacing, readiness-gate integration (Liu 2026), unassisted-metrics signal (Bastani/Brynjolfsson), what never fades. Council C deliverable — docs/Ecology/Foundation/Phase5_Safeguards/scaffolding_fade_rules.md" \
  --priority high \
  --json | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))")

echo "== 3. Chain: scaffolding_fade_rules is the parent of the other four =="
for t in "$T1" "$T2" "$T3" "$T4"; do
  hermes kanban link "$T5" "$t" || true
done

echo "== 4. Board state =="
hermes kanban list

echo
echo "DONE. Visual board: hermes dashboard -> Kanban tab (drag-drop cards)."
echo "Or CLI: hermes kanban list / show / comment / complete"
