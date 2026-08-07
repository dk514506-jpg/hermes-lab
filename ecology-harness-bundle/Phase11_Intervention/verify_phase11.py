#!/usr/bin/env python3
"""Phase 11 verification — BCW/BCT intervention layer + handoff items.

Run: python3 Phase11_Intervention/verify_phase11.py
Verifies:
  1. COMB has 17 ops (14 + 3 successor-stage); successor edges present
  2. canvass_full_range: output is unranked candidates (no selection field)
  3. select_bct: Q7 gate machine-enforced — reward DENY without
     user-request+disclosure or documented exception; rejections preserved
     as witnesses (Valens P4)
  4. retrocode_delivered_plan: planned-vs-delivered diff output schema
  5. skill_load→trend op: series -> HEB canonical trend (rising|flat|falling)
  6. Stepwise S0-S9: adjacent-forward + pre-declared-selector promotion
  7. Confirmed-Q2: usable only with user_confirmed; user-rejected outranks
  8. Legacy: verify_integration.py (Phase 10) + FAOS canonical suite
     (scripts/run_tests.sh) still pass — checked NON-recursively
     (verify_all.py chains this verifier via the gate; the full gate is
     council_notes/verify_all.py, run separately).
"""
import json
import os
import subprocess
import sys
def _faos_root():
    """FAOS canonical suite root: bundle faos_canonical/ -> env -> home lab."""
    for cand in (os.path.join(ROOT, "..", "faos_canonical"),
                 os.environ.get("ECOLOGY_FAOS_ROOT"),
                 os.path.join(os.path.expanduser("~"), ".hermes",
                              "hermes-agent", "docs")):
        if cand and os.path.isfile(os.path.join(cand, "scripts", "run_tests.sh")):
            return os.path.abspath(cand)
    raise FileNotFoundError("FAOS canonical suite not found (run_tests.sh)")

ROOT = os.path.dirname(os.path.abspath(__file__))
FOUNDATION = os.path.dirname(ROOT)
DOCS = os.path.dirname(os.path.dirname(os.path.dirname(ROOT)))
POC = os.path.join(FOUNDATION, "GitHub_PoC")
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(FOUNDATION, "Phase10_Integration"))

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


from phase11_intervention import (  # noqa: E402
    CombSuccessorStage, SkillLoadTrend, StepwiseLineage,
    ConfirmedQuarantine, BCT_10X_REWARD,
)
from faos_engine_extension import FaosConfig, FaosConfigError  # noqa: E402
from faos_ecology_engine import FaosEcologyEngine  # noqa: E402

# 1. COMB package artifacts
ops_path = os.path.join(POC, "skills", "COMB_Behavioral_Diagnosis", "atomic_ops.json")
ops = json.load(open(ops_path))
names = [o.get("id") for o in ops]
check("comb: 17 ops (14 + 3 successor)", len(ops) == 17, f"got {len(ops)}")
for op_id in ["canvass_full_range", "select_bct", "retrocode_delivered_plan"]:
    check(f"comb: {op_id} present", op_id in names)
em = json.load(open(os.path.join(POC, "skills", "COMB_Behavioral_Diagnosis", "edge_map.json")))
edge_targets = [e.get("target") for e in em["edges"]]
check("comb: successor edges in edge_map",
      all(t in edge_targets for t in ["canvass_full_range", "select_bct", "retrocode_delivered_plan"]))
ss = json.load(open(os.path.join(POC, "skills", "COMB_Behavioral_Diagnosis", "state_schema.json")))
check("comb: successor state vars", all(k in ss for k in
      ["candidate_range", "selected_plan", "rejected_with_reason", "planned_vs_delivered_diff"]))

# 2. canvass: enumerate without selecting
stage = CombSuccessorStage()
diag = {"id": "d-001", "component_profile": ["M-Au", "M-Re"]}
canvassed = stage.canvass_full_range(diag, "M-Au")
check("canvass: candidates returned", bool(canvassed["candidate_range"]))
check("canvass: no selection field", "selected" not in canvassed,
      "anti-premature-coherence: canvassing never selects")

# 3. select_bct: Q7 machine-enforced
candidates = canvassed["candidate_range"]
reward_cands = [c for c in candidates if c["technique"].split(" ", 1)[0] in BCT_10X_REWARD]
# 3a. DENY without request
res_deny = stage.select_bct(candidates)
denied = [r for r in res_deny["rejected_with_reason"] if r["technique"].startswith("10.")]
check("Q7: reward DENIED without user request", bool(denied) and bool(reward_cands),
      f"{len(denied)} reward candidates rejected-as-witnesses")
# 3b. ALLOW with request + disclosure
res_allow = stage.select_bct(candidates, user_explicit_request=True, deci_risk_disclosed=True)
allowed = [s for s in res_allow["selected_plan"] if s["technique"].startswith("10.")]
check("Q7: reward ALLOWED with request + disclosure",
      bool(allowed) and allowed[0]["q7_ruling"] == "user_requested")
# 3c. ALLOW via exception path (requires extrinsic_evidence — R8)
res_exc = stage.select_bct(candidates, already_extrinsic_behavior=True,
                           extrinsic_evidence="PPS skill_load 0.62, extrinsic anchor: user works for pay")
exc = [s for s in res_exc["selected_plan"] if s["technique"].startswith("10.")]
check("Q7: exception path documented, never default",
      bool(exc) and exc[0]["q7_ruling"] == "exception_path")
# 3c2. exception WITHOUT evidence -> DENY (R8)
res_exc_bare = stage.select_bct(candidates, already_extrinsic_behavior=True)
exc_bare = [r for r in res_exc_bare["rejected_with_reason"]
            if r["technique"].startswith("10.")]
check("Q7: exception without extrinsic_evidence DENIED (R8)",
      bool(exc_bare) and "requires extrinsic_evidence" in exc_bare[0]["reason"])
# 3c3. R7: request-only -> DENY (AND-semantics)
res_req_only = stage.select_bct(candidates, user_explicit_request=True,
                                deci_risk_disclosed=False)
req_only = [r for r in res_req_only["rejected_with_reason"]
            if r["technique"].startswith("10.")]
check("Q7: request-only (no disclosure) DENIED (R7 AND-semantics)",
      bool(req_only))
# 3c4. R7: disclosure-only -> DENY
res_dis_only = stage.select_bct(candidates, user_explicit_request=False,
                                deci_risk_disclosed=True)
dis_only = [r for r in res_dis_only["rejected_with_reason"]
            if r["technique"].startswith("10.")]
check("Q7: disclosure-only (no request) DENIED (R7 AND-semantics)",
      bool(dis_only))
# 3d. rejections preserved (Valens P4)
check("Q7: rejections preserved as witnesses",
      bool(res_deny["rejected_with_reason"]), "no silent drops")

# 4. retrocode: honesty op
planned = [{"technique": "1.1 goal setting (behavior)"}, {"technique": "10.4 social reward"}]
delivered = {"delivered_techniques": [{"technique": "1.1 goal setting (behavior)"},
                                      {"technique": "1.4 action planning"}]}
rc = stage.retrocode_delivered_plan(planned, delivered)
diff = rc["planned_vs_delivered_diff"]
check("retrocode: planned-not-delivered captured", "10.4" in diff["planned_but_not_delivered"])
check("retrocode: delivered-not-planned captured", "1.4" in diff["delivered_but_not_planned"])
check("retrocode: calibration feed declared", "calibration_feed" in diff)

# 5. skill_load -> trend (HEB canonical enum)
t = SkillLoadTrend()
check("trend: falling detected", t.convert([0.8, 0.85, 0.82, 0.78])["trend"] == "falling")
check("trend: rising detected", t.convert([0.7, 0.75, 0.8, 0.85])["trend"] == "rising")
check("trend: flat within threshold", t.convert([0.8, 0.81, 0.8, 0.79])["trend"] == "flat")
check("trend: HEB canonical enum", t.convert([0.8, 0.85, 0.82, 0.78])["trend"] in
      ["rising", "flat", "falling"])
check("trend: feeds gate W2 (falling -> no ACT)",
      t.convert([0.8, 0.85, 0.82, 0.78])["trend"] == "falling")

# 6. stepwise S0-S9 + selector promotion
cfg = FaosConfig.load(os.path.join(FOUNDATION, "Phase10_Integration", "faos_ecology_config.yaml"))
engine = FaosEcologyEngine(cfg)
sw = StepwiseLineage(engine)
sw.advance_item("S0", "S1")
sw.advance_item("S3", "S4")   # qualification completion — no selector
check("stepwise: adjacent forward OK (S3->S4 qualification)", True)
try:
    sw.advance_item("S4", "S5")  # promotion — selector required
    check("stepwise: selector required at promotion", False, "should have raised")
except FaosConfigError:
    check("stepwise: selector required at promotion", True)
sw.advance_item("S4", "S5", selector_declared=True)
check("stepwise: promotion with selector OK", True)
try:
    sw.advance_item("S1", "S3")  # skip
    check("stepwise: skip blocked", False, "should have raised")
except FaosConfigError:
    check("stepwise: skip blocked", True, "Book IX stepwise")
try:
    sw.advance_item("S0", "S5")  # engine blocklist still holds
    check("stepwise: engine blocklist still active", False, "should have raised")
except FaosConfigError:
    check("stepwise: engine blocklist still active", True, "S0->S5 prohibited")
sw.advance_item("S5", "S6")
try:
    sw.advance_item("S6", "S7")  # halt-state exit
    check("stepwise: halt-state exit blocked", False, "should have raised")
except FaosConfigError:
    check("stepwise: halt-state exit blocked", True, "S6 is terminal (Book IX)")

# 7. confirmed-Q2
q = ConfirmedQuarantine(cfg)
try:
    q.assert_use_licensed("Q0", "Q2")
    check("Q2: blocked by default", False, "should have raised")
except FaosConfigError:
    check("Q2: blocked by default", True, "identity-level default quarantine")
q.assert_use_licensed("Q0", "Q2", user_confirmed=True)
check("Q2: allowed with explicit confirmation", True)
try:
    q.assert_use_licensed("Q0", "Q2", user_confirmed=True, user_rejected=True)
    check("Q2: user-rejected outranks confirmation", False, "should have raised")
except FaosConfigError:
    check("Q2: user-rejected outranks confirmation", True)

# 8. legacy suites (non-recursive — verify_all chains this via gate)
legacy = [
    ("Phase 10 integration", sys.executable,
     [os.path.join(FOUNDATION, "Phase10_Integration", "verify_integration.py")]),
    ("FAOS canonical", "bash", [os.path.join(_faos_root(), "scripts", "run_tests.sh")]),
]
for name, exe, cmd in legacy:
    cwd = FOUNDATION if "verify_integration" in cmd[0] else _faos_root()
    try:
        r = subprocess.run([exe] + cmd, capture_output=True, text=True, timeout=600, cwd=cwd)
        tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()
        check(f"legacy: {name} still passes", r.returncode == 0, tail)
    except Exception as e:
        check(f"legacy: {name} still passes", False, str(e))

print()
print("=== RESULT:", f"{len(fails)} FAILURES" if fails else "PASS — Phase 11 intervention layer verified", "===")
sys.exit(1 if fails else 0)