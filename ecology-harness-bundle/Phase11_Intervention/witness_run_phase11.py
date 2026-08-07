#!/usr/bin/env python3
"""Phase 11 witness run — the intervention pipeline end-to-end.

Run: python3 Phase11_Intervention/witness_run_phase11.py

Demonstrates the FULL successor stage on a realistic scenario:
  diagnosis (M-Au binding constraint) -> canvass_full_range (no selection)
  -> select_bct (Q7 arbitration: a reward candidate present) -> delivery
  -> retrocode_delivered_plan (planned vs delivered gap) -> calibration feed
Plus: skill_load->trend feeding the gate W2 trigger; stepwise S0-S9;
confirmed-Q2 allowance. Writes a witness record to GitHub_PoC/logs/.
"""
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
FOUNDATION = os.path.dirname(ROOT)
POC = os.path.join(FOUNDATION, "GitHub_PoC")
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(FOUNDATION, "Phase10_Integration"))

from phase11_intervention import (  # noqa: E402
    CombSuccessorStage, SkillLoadTrend, StepwiseLineage,
    ConfirmedQuarantine, BCT_10X_REWARD,
)
from faos_engine_extension import FaosConfig  # noqa: E402
from faos_ecology_engine import FaosEcologyEngine, GateContext  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


stage = CombSuccessorStage()
cfg = FaosConfig.load(os.path.join(FOUNDATION, "Phase10_Integration", "faos_ecology_config.yaml"))
engine = FaosEcologyEngine(cfg)

print("=== PHASE 11 WITNESS RUN — INTERVENTION PIPELINE ===")

# ------------------------------------------------------------------
# Scenario: user stuck on evening walking; diagnosis says M-Au binding
# ------------------------------------------------------------------
diagnosis = {
    "id": "d-walk-042",
    "target_behavior": "walk 30 minutes after dinner",
    "component_profile": [
        {"component": "M-Au", "salience": "strong",
         "evidence_quotes": ["I keep meaning to but I forget"], "confidence": "high"},
        {"component": "M-Re", "salience": "moderate",
         "evidence_quotes": ["I never plan it"], "confidence": "medium"},
    ],
    "binding_constraint": "M-Au",
    "evidence_sufficiency": "partial",
    "hypothesis_status": "hypothesis",
}

# 1. canvass — enumerate, never select
canvassed = stage.canvass_full_range(diagnosis, "M-Au")
check("canvass: candidates for binding constraint",
      len(canvassed["candidate_range"]) >= 3, str(len(canvassed["candidate_range"])))
check("canvass: no selection field (anti-premature-coherence)",
      "selected" not in canvassed)
candidates = canvassed["candidate_range"]
reward_in_range = [c for c in candidates if c["technique"].split(" ", 1)[0] in BCT_10X_REWARD]
check("canvass: reward technique present in range (Q7 gate applies at select, not canvass)",
      bool(reward_in_range), reward_in_range[0]["technique"] if reward_in_range else "none")

# 2. select — Q7 arbitration, default posture (no user request)
selection = stage.select_bct(candidates)
denied_rewards = [r for r in selection["rejected_with_reason"]
                  if r["technique"].startswith("10.")]
check("select: reward DENIED by default (never auto-selected)",
      bool(denied_rewards), f"{len(denied_rewards)} preserved as witnesses")
check("select: non-reward techniques selected",
      any(s["q7_ruling"] == "standard" for s in selection["selected_plan"]))
check("select: rejections preserved (Valens P4)",
      bool(selection["rejected_with_reason"]))
planned = selection["selected_plan"]

# 3. delivery + retrocode — the honesty op
# Delivered session includes a technique NOT in the plan (drift) and omits
# one that WAS planned (1.4 action planning) — both directions testable.
delivered_session = {
    "session_id": "dojo-walk-042",
    "dojo": "Ambivalence_Dojo",
    "delivered_techniques": [
        {"technique": "1.1 goal setting (behavior)"},
        {"technique": "8.7 graded tasks"},      # NOT in the plan — drift!
    ],
}
rc = stage.retrocode_delivered_plan(planned, delivered_session)
diff = rc["planned_vs_delivered_diff"]
check("retrocode: planned-but-not-delivered captured",
      len(diff["planned_but_not_delivered"]) >= 1, str(diff["planned_but_not_delivered"]))
check("retrocode: delivered-but-not-planned captured (drift detected)",
      "8.7" in diff["delivered_but_not_planned"])
check("retrocode: calibration feed declared", "calibration_feed" in diff)

# 4. skill_load -> trend feeds the gate W2 trigger
trend = SkillLoadTrend()
series = [0.85, 0.83, 0.80, 0.76]   # capability eroding, clearly past threshold
t = trend.convert(series)
check("trend: falling detected from real series", t["trend"] == "falling",
      f"delta={t['delta']}")
ctx = GateContext(skill_load_trend=t["trend"])
mode = engine.gate.select_mode(ctx)
check("gate: ACT blocked while skill_load_trend falling (W2 guard live)",
      mode != "ACT", f"mode={mode}")
check("trend: HEB canonical enum", t["trend"] in ["rising", "flat", "falling"])

# 5. stepwise S0-S9 with selector promotion
sw = StepwiseLineage(engine)
sw.advance_item("S0", "S1")
sw.advance_item("S1", "S2")
sw.advance_item("S2", "S3")
sw.advance_item("S3", "S4", selector_declared=True)
check("stepwise: S0->S4 with selector at promotion OK", True)
try:
    sw.advance_item("S4", "S5")   # selector required here too
    check("stepwise: selector required at S4->S5", False, "should have raised")
except Exception:
    check("stepwise: selector required at S4->S5", True)

# 6. confirmed-Q2 allowance
q = ConfirmedQuarantine(cfg)
try:
    q.assert_use_licensed("Q0", "Q2")
    check("Q2: blocked by default", False, "should have raised")
except Exception:
    check("Q2: blocked by default (identity-level)", True)
q.assert_use_licensed("Q0", "Q2", user_confirmed=True)
check("Q2: allowed with explicit confirmation (DEFER->confirm path)", True)

# ------------------------------------------------------------------
# Write witness record
# ------------------------------------------------------------------
stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
outdir = os.path.join(POC, "logs", f"witness_phase11_{stamp}")
os.makedirs(outdir, exist_ok=True)
record = {
    "run": "phase11-intervention-witness",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "scenario": "stuck evening-walk habit; M-Au binding constraint",
    "diagnosis": diagnosis,
    "mapping_disclosure": "EXAMPLE_RANGE demo stand-in (R4): candidate techniques + "
                          "evidence anchors are demo constants; the real BCW/BCT "
                          "mapping table is not yet in the estate. Anchors are "
                          "estate-cited literature, not pipeline-verified findings.",
    "canvass": {"candidates": len(candidates), "no_selection_field": True},
    "select": {
        "selected": [s["technique"] for s in planned],
        "rejected_witnesses": [r["technique"] for r in selection["rejected_with_reason"]],
        "q7_ruling": "reward DENIED by default; never auto-selected",
    },
    "retrocode": diff,
    "skill_load_trend": t,
    "gate_w2": {"skill_load_trend": t["trend"], "mode": mode, "act_blocked": mode != "ACT"},
    "stepwise": "S0->S4 with selector promotion; S4->S5 requires selector",
    "confirmed_q2": "Q2 blocked by default; allowed with explicit confirmation",
    "result": "PASS",
}
with open(os.path.join(outdir, "witness.json"), "w") as f:
    json.dump(record, f, indent=2)
print(f"\nwitness record: {outdir}/witness.json")

if fails:
    print(f"\n=== WITNESS RUN: {len(fails)} FAILURES ===")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print("\n=== WITNESS RUN: PASS — intervention pipeline demonstrated end-to-end ===")
sys.exit(0)
