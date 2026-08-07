#!/usr/bin/env python3
"""Phase 10 verification — FAOS × Ecology integration.

Run: python3 Phase10_Integration/verify_integration.py
Verifies the merged estate:
  1. Merged config loads under FaosConfig (schema faos-ecology-integration/1.0)
  2. Gate: all 5 modes select under their trigger sets; mode->result map
     matches the declared mapping (D2)
  3. Two-typed quarantine: axes independent; FAOS-clearing never licenses
     Ecology use; user-rejected final (D1)
  4. S0-S9 lifecycle enforced (prohibited edge blocked; halt states)
  5. Absence register fails closed; non-operational registry bars resonance
  6. Dojo close: 6-pass record, valid result states (D3)
  7. Both legacy suites still pass, checked NON-recursively (verify_all.py
     chains this verifier, so calling it here would infinitely recurse):
     FAOS canonical (scripts/run_tests.sh) + Ecology harness verifier
     (verify_harness.py) + Ecology phase9 verifier (verify_phase9.py).
     The full gate including this verifier is verify_all.py.
"""
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
DOCS = os.environ.get("ECOLOGY_FAOS_ROOT") or os.path.dirname(
    os.path.dirname(os.path.dirname(ROOT)))  # docs root or faos_canonical parent
sys.path.insert(0, ROOT)

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


from faos_engine_extension import FaosConfig, FaosConfigError  # noqa: E402
from faos_ecology_engine import (  # noqa: E402
    EcologyGate, GateContext, MODE_TO_RESULT,
    TwoTypedQuarantine, DojoClose, FaosEcologyEngine,
)

# 1. config loads
cfg = FaosConfig.load(os.path.join(ROOT, "faos_ecology_config.yaml"))
check("merged config loads", cfg.name == "faos-ecology-merged-pipeline",
      f"schema {cfg.schema_version}")
check("config: schema_version", cfg.schema_version == "faos-ecology-integration/1.0")

engine = FaosEcologyEngine(cfg)

# 2. gate: five modes
cases = [
    ("ACT", GateContext()),
    ("SCAFFOLD", GateContext(skill_atrophy_risk="medium")),
    ("ASK", GateContext(choice_branching_level="high", evidence_sufficiency="insufficient",
                        viable_paths=3, one_question_resolves=True)),
    ("ASK", GateContext(task_meaning_level="medium", choice_branching_level="medium",
                        evidence_sufficiency="insufficient", one_question_resolves=True)),
    ("DEFER", GateContext(protected_class="identity_claim")),
    ("STOP", GateContext(manipulative=True)),
]
for expected, ctx in cases:
    mode = engine.gate.select_mode(ctx)
    check(f"gate: {expected} selects", mode == expected, f"got {mode}")
# R9: pin the revision-round trigger sets (W9 mutation-drift guard)
check("gate: W2 ACT blocked when skill_load_trend falling",
      engine.gate.select_mode(GateContext(skill_load_trend="falling")) != "ACT",
      "never ACT during capability erosion")
check("gate: W3 high friction scaffolds",
      engine.gate.select_mode(GateContext(friction_value="high")) == "SCAFFOLD")
check("gate: W1 argument_against_resistance stops",
      engine.gate.select_mode(GateContext(argument_against_resistance=True)) == "STOP")
check("gate: W4 high-meaning unresolvable insufficiency defers",
      engine.gate.select_mode(GateContext(task_meaning_level="high",
                                          evidence_sufficiency="insufficient",
                                          one_question_resolves=False)) == "DEFER")
# mode->result mapping (D2)
for mode, result in MODE_TO_RESULT.items():
    check(f"gate: {mode} -> {result}", engine.gate.mode_map[mode] == result)
# gate decision record
d = engine.gate.gate_decision(GateContext(manipulative=True))
check("gate: STOP -> BLOCKED in decision", d["mode"] == "STOP" and d["result_state"] == "BLOCKED")

# 3. two-typed quarantine (D1)
q = engine.quarantine
# FAOS clears, Ecology bars (the load-bearing rule)
try:
    q.assert_use_licensed("Q0", "Q3", user_rejected=True)
    check("quarantine: Q0/Q3 user-rejected BLOCKED", False, "should have raised")
except FaosConfigError:
    check("quarantine: Q0/Q3 user-rejected BLOCKED", True, "FAOS clearing never licenses use")
# FAOS bars, Ecology would allow
try:
    q.assert_use_licensed("Q5", "Q0")
    check("quarantine: Q5/Q0 BLOCKED", False, "should have raised")
except FaosConfigError:
    check("quarantine: Q5/Q0 BLOCKED", True, "claim not trustworthy")
# both licensed
q.assert_use_licensed("Q0", "Q0")
check("quarantine: Q0/Q0 licensed", True, "independent axes both green")
# user-rejected final even with good claim AND good use class
try:
    q.assert_use_licensed("Q0", "Q1", user_rejected=True)
    check("quarantine: user-rejected final", False, "should have raised")
except FaosConfigError:
    check("quarantine: user-rejected final", True, "user verdict outranks evidence")

# 4. S0-S9 lifecycle
engine.advance_item("S0", "S1")
check("state: S0->S1 allowed", True)
try:
    engine.advance_item("S0", "S5")
    check("state: S0->S5 blocked", False, "should have raised")
except FaosConfigError:
    check("state: S0->S5 blocked", True, "prohibited edge")
check("state: S6 halt", engine.is_item_halted("S6"))
check("state: S7 halt", engine.is_item_halted("S7"))
check("state: S8 halt", engine.is_item_halted("S8"))

# 5. absence + non-operational
try:
    engine.require_key_present("scoring_gold_set_calibration_origin")
    check("absence: registered blocks", False, "should have raised")
except FaosConfigError:
    check("absence: registered blocks", True, "fail-closed")
try:
    engine.assert_operational("temporal_echo")
    check("non-op: temporal_echo barred", False, "should have raised")
except FaosConfigError:
    check("non-op: temporal_echo barred", True, "context only, never evidence")

# 6. dojo close (D3)
rec = engine.dojo_close.close_dojo_session(
    {"dojo": "Ambivalence_Dojo", "stages_walked": ["engage", "discern-ambivalence"],
     "gates_fired": [{"guard": "no_premature_closure"}], "close_verdict": "PASS",
     "session_id": "witness-integration"})
engine.dojo_close.validate_close_record(rec)
check("dojo close: 6 passes", all(p in rec["completed_passes"] for p in
      ["victory", "defect", "dissent", "proxy_check", "boundary_check", "transfer_status"]))
check("dojo close: valid result", rec["result_state"] in
      ["TRUE", "FALSE", "PARTIAL", "INCONCLUSIVE", "BLOCKED"], rec["result_state"])
# R6: template-honest close — boundary_check INCONCLUSIVE when the session
# carries no consent/boundary data (never asserted as observed)
check("dojo close: R6 template honesty",
      rec["completed_passes"]["boundary_check"]["state"] == "INCONCLUSIVE",
      "no consent fields in input -> not asserted")

# 6b. process_work_item seam test (W9: the seam was never exercised)
seam = engine.process_work_item(
    GateContext(skill_atrophy_risk="medium", choice_branching_level="medium"),
    q_claim="Q0", q_use="Q0")
check("seam: process_work_item returns gate + quarantine",
      seam["gate"]["mode"] == "SCAFFOLD" and seam["quarantine"]["licensed"] is True,
      f"mode={seam['gate']['mode']} licensed={seam['quarantine']['licensed']}")

# 7. legacy suites still pass (NON-recursive: verify_all.py now chains THIS
# verifier, so calling verify_all from here would infinitely recurse).
legacy = [
    ("FAOS canonical", "bash", ["scripts/run_tests.sh"], _faos_root()),
    ("Ecology harness verifier", sys.executable,
     ["GitHub_PoC/verify/verify_harness.py"], FOUNDATION),
    ("Ecology phase9 verifier", sys.executable,
     ["council_notes/verify_phase9.py"], FOUNDATION),
]
for name, exe, args, cwd in legacy:
    try:
        r = subprocess.run([exe] + args, capture_output=True, text=True, timeout=600, cwd=cwd)
        tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()
        check(f"legacy: {name} still passes", r.returncode == 0, tail)
    except Exception as e:
        check(f"legacy: {name} still passes", False, str(e))

print()
print("=== RESULT:", f"{len(fails)} FAILURES" if fails else "PASS — Phase 10 integration verified", "===")
sys.exit(1 if fails else 0)