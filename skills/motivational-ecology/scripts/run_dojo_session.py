#!/usr/bin/env python3
"""run_dojo_session.py — platform wiring demonstration driver.

DEMONSTRATED PATH (deterministic, no LLM): walks a real dojo
dialogue_state_machine.json through the merged engine (gate + two-typed
quarantine + 6-pass close), catalogues the stage guards, and — where a
guard's retreat semantics can be exercised — demonstrates the HOLD and
retreat to the guard's retreat_target. Writes a session record to
GitHub_PoC/logs/live_session_<stamp>/.

HONEST BOUNDARY: this driver generates NO coach turns and involves NO
LLM and NO human. The genuine human-facing live LLM session through the
motivational-ecology skill is the remaining runtime act (absence
register: post_meld_live_llm_session = human-session-pending). Records
written by this driver are labeled "platform wiring demonstration" and
must never be presented as live human sessions.

Usage:
  python3 run_dojo_session.py --dojo Ambivalence_Dojo [--scenario person]
  python3 run_dojo_session.py --list                 # list available dojos

Exit 0 = session completed with valid close record.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
FOUNDATION = os.path.join(
    os.path.expanduser("~"), ".hermes", "hermes-agent", "docs",
    "Ecology", "Foundation")
P10 = os.path.join(FOUNDATION, "Phase10_Integration")
POC = os.path.join(FOUNDATION, "GitHub_PoC")
sys.path.insert(0, P10)

from faos_engine_extension import FaosConfig  # noqa: E402
from faos_ecology_engine import FaosEcologyEngine, GateContext  # noqa: E402

DOJOS = {
    "Ambivalence_Dojo": os.path.join(POC, "routines", "Ambivalence_Dojo", "dialogue_state_machine.json"),
    "Conflict_Dojo": os.path.join(POC, "routines", "Conflict_Dojo", "dialogue_state_machine.json"),
    "Coaching_Dojo": os.path.join(POC, "routines", "Coaching_Dojo", "dialogue_state_machine.json"),
    "Conversation_Dojo": os.path.join(POC, "routines", "Conversation_Dojo", "dialogue_state_machine.json"),
    "Workplace_Dojo": os.path.join(POC, "routines", "Workplace_Dojo", "dialogue_state_machine.json"),
}

# Scenario: the coaching context that drives the gate at each stage.
# medium meaning + medium branching + medium atrophy → SCAFFOLD (structure,
# don't complete for the user) — the canonical coaching posture.
SCENARIO_CONTEXT = GateContext(
    task_meaning_level="medium",
    choice_branching_level="medium",
    reversibility="reversible",
    skill_atrophy_risk="medium",
    skill_load_trend="flat",
    friction_value="medium",
    agent_confidence="medium",
)


def load_dojo(dojo_name: str) -> dict:
    path = DOJOS.get(dojo_name)
    if not path or not os.path.exists(path):
        raise SystemExit(f"dojo {dojo_name!r} not found. Available: {sorted(DOJOS)}")
    return json.load(open(path))


def main() -> int:
    ap = argparse.ArgumentParser(description="Live dojo session through the merged gateway")
    ap.add_argument("--dojo", default="Ambivalence_Dojo", help="dojo name")
    ap.add_argument("--list", action="store_true", help="list dojos and exit")
    ap.add_argument("--scenario", default="person",
                    help="scenario label for the session record")
    ap.add_argument("--q-claim", default="Q0")
    ap.add_argument("--q-use", default="Q0")
    args = ap.parse_args()

    if args.list:
        for name in sorted(DOJOS):
            print(name)
        return 0

    cfg = FaosConfig.load(os.path.join(P10, "faos_ecology_config.yaml"))
    engine = FaosEcologyEngine(cfg)
    sm = load_dojo(args.dojo)
    stages = sm.get("stages", [])

    print(f"=== LIVE SESSION: {args.dojo} (scenario: {args.scenario}) ===")
    print(f"(gate context: meaning={SCENARIO_CONTEXT.task_meaning_level}, "
          f"branching={SCENARIO_CONTEXT.choice_branching_level}, "
          f"atrophy={SCENARIO_CONTEXT.skill_atrophy_risk})\n")

    # Gate ruling at session entry (the gateway decides what the agent may do)
    gate = engine.gate.gate_decision(SCENARIO_CONTEXT)
    engine.quarantine.assert_use_licensed(args.q_claim, args.q_use)
    print(f"[GATE] mode={gate['mode']} result={gate['result_state']} "
          f"dissent_required={gate['dissent_required']}")
    print(f"[QUARANTINE] claim_trust={args.q_claim} use_permission={args.q_use} — licensed\n")

    stages_walked = []
    guards_catalogued = []
    guard_events = []   # R2: actual HOLD/retreat events, when exercised
    for i, stage in enumerate(stages):
        sid = stage.get("id", f"stage-{i}")
        stages_walked.append(sid)
        print(f"  [{i+1}/{len(stages)}] {sid}")
        guard = stage.get("guard")
        if guard:
            gid = guard.get("id", "unknown")
            guards_catalogued.append({"guard": gid,
                                      "rule": guard.get("rule", "")[:80],
                                      "retreat_target": guard.get("retreat_target")})
            print(f"       guard armed: {gid} — "
                  f"retreat_target={guard.get('retreat_target')}")
            # R2: exercise the guard's retreat semantics for the FIRST
            # guard in the walk — demonstrate the HOLD + retreat per the
            # state machine's transition_policy. Subsequent guards are
            # catalogued only (honest: not evaluated in this walk).
            if not guard_events and guard.get("retreat_target"):
                retreat_target = guard["retreat_target"]
                if any(s.get("id") == retreat_target for s in stages):
                    print(f"       >>> GUARD FIRES: HOLD at {sid}; retreat to "
                          f"{retreat_target} (transition_policy: "
                          f"exit_conditions_met AND stage_guards_passed)")
                    guard_events.append({
                        "event": "HOLD_AND_RETREAT",
                        "guard": gid,
                        "held_stage": sid,
                        "retreat_target": retreat_target,
                        "note": "demonstration of guard semantics — the "
                                "retreat_target stage is re-entered",
                    })
                    stages_walked.append(retreat_target)
                    print(f"  [{i+1}/{len(stages)} RETREAT] {retreat_target} "
                          f"(re-entered after guard HOLD)")
                else:
                    guard_events.append({
                        "event": "GUARD_CATALOGUED_ONLY",
                        "guard": gid,
                        "held_stage": sid,
                        "note": f"retreat_target {retreat_target!r} not in "
                                f"stage list — guard catalogued, not evaluated",
                    })

    # 6-pass instrumented close (D3 / memo Phase B) — R3: NO fabricated
    # observed findings. The driver passes NO user_agreement/boundary/
    # no_shaming fields, so DojoClose emits its labeled template/unknown
    # evidence ("NOT asserted (unknown)") per engine R6.
    close_record = engine.dojo_close.close_dojo_session({
        "session_id": f"live-{args.dojo}-{args.scenario}",
        "dojo": args.dojo,
        "stages_walked": stages_walked,
        "gates_fired": guard_events,   # actual HOLD/retreat events only
        "close_verdict": "PASS",
        "simulated": True,             # R3: marks the whole record simulated
    })
    engine.dojo_close.validate_close_record(close_record)

    print(f"\n=== CLOSE ({close_record['result_state']}) ===")
    for pass_name, entry in close_record["completed_passes"].items():
        print(f"  {pass_name}: {entry['state']} — {entry['evidence'][:70]}")

    # Write session record
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    outdir = os.path.join(POC, "logs", f"live_session_{stamp}")
    os.makedirs(outdir, exist_ok=True)
    record = {
        "run": "phase13-platform-wiring-demonstration",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dojo": args.dojo,
        "scenario": args.scenario,
        "gate": gate,
        "quarantine": {"claim_trust": args.q_claim, "use_permission": args.q_use,
                       "licensed": True},
        "stages_walked": stages_walked,
        "guards_catalogued": guards_catalogued,
        "guard_events": guard_events,
        "close": close_record,
        "note": ("platform wiring demonstration (Phase 13): deterministic machinery walk "
                 "through the merged gateway — gate + two-typed quarantine + 6-pass close. "
                 "The genuine human-facing live LLM session through the motivational-ecology "
                 "skill is the remaining runtime act (absence register: human-session-pending). "
                 "Do not treat this record as a live human session."),
        "result": "PASS",
    }
    with open(os.path.join(outdir, "session.json"), "w") as f:
        json.dump(record, f, indent=2)
    print(f"\nsession record: {outdir}/session.json")
    print("\n=== SESSION COMPLETE — 6-pass close recorded ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
