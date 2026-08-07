#!/usr/bin/env python3
"""run_gate.py — the empowerment gate, callable from the
motivational-ecology skill.

Usage:
  python3 run_gate.py --meaning high --branching high --reversibility hard
  python3 run_gate.py --atrophy medium --trend falling
  python3 run_gate.py --manipulative

Prints the gate decision (mode + FAOS result state + dissent flag) and the
two-typed quarantine ruling for the claimed tiers. Exit 0 = ruling issued;
exit 1 = gate error (e.g. invalid enum).

Loads the REAL merged engine (Phase10_Integration/faos_ecology_engine.py)
with the REAL merged config. No LLM — deterministic.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _estate_root() -> str:
    """Portable estate resolution: $ECOLOGY_ESTATE_ROOT -> walk-up -> home lab."""
    env = os.environ.get("ECOLOGY_ESTATE_ROOT")
    if env and os.path.isdir(os.path.join(env, "GitHub_PoC")):
        return env
    probe = HERE
    while True:
        if os.path.isdir(os.path.join(probe, "GitHub_PoC")):
            return probe
        parent = os.path.dirname(probe)
        if parent == probe:
            break
        probe = parent
    lab = os.path.join(os.path.expanduser("~"), ".hermes", "hermes-agent",
                       "docs", "Ecology", "Foundation")
    if os.path.isdir(os.path.join(lab, "GitHub_PoC")):
        return lab
    raise FileNotFoundError(
        "Estate not found: set ECOLOGY_ESTATE_ROOT to a directory containing "
        "GitHub_PoC/ (bundle layout), or run from the home-lab path.")


FOUNDATION = _estate_root()
P10 = os.path.join(FOUNDATION, "Phase10_Integration")
sys.path.insert(0, P10)

from faos_engine_extension import FaosConfig  # noqa: E402
from faos_ecology_engine import FaosEcologyEngine, GateContext  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Empowerment gate + quarantine ruling")
    ap.add_argument("--meaning", default="low", choices=["low", "medium", "high"])
    ap.add_argument("--branching", default="low", choices=["low", "medium", "high"])
    ap.add_argument("--reversibility", default="reversible",
                    choices=["reversible", "hard", "irreversible"])
    ap.add_argument("--atrophy", default="low", choices=["low", "medium", "high"])
    ap.add_argument("--trend", default="flat", choices=["rising", "flat", "falling"])
    ap.add_argument("--friction", default="low", choices=["low", "medium", "high"])
    ap.add_argument("--confidence", default="medium", choices=["low", "medium", "high"])
    ap.add_argument("--authority", action="store_true",
                    help="user_authority_required")
    ap.add_argument("--insufficient", action="store_true",
                    help="evidence_sufficiency = insufficient")
    ap.add_argument("--protected", default=None,
                    help="protected class (identity_claim, meaning_making, ...)")
    ap.add_argument("--manipulative", action="store_true")
    ap.add_argument("--surveillance", action="store_true")
    ap.add_argument("--unsafe", action="store_true")
    ap.add_argument("--coercive", action="store_true")
    ap.add_argument("--boundary", action="store_true",
                    help="boundary_violation")
    ap.add_argument("--arg-resistance", action="store_true",
                    dest="arg_resistance", help="argument_against_resistance")
    ap.add_argument("--requested", action="store_true",
                    help="user_requested_full_execution")
    ap.add_argument("--practice", action="store_true", help="practice_mode")
    ap.add_argument("--q-claim", default="Q0", help="FAOS claim-trust tier")
    ap.add_argument("--q-use", default="Q0", help="Ecology use-permission class")
    ap.add_argument("--user-rejected", action="store_true", dest="user_rejected")
    ap.add_argument("--user-confirmed", action="store_true", dest="user_confirmed")
    args = ap.parse_args()

    cfg = FaosConfig.load(os.path.join(P10, "faos_ecology_config.yaml"))
    engine = FaosEcologyEngine(cfg)

    ctx = GateContext(
        task_meaning_level=args.meaning,
        choice_branching_level=args.branching,
        reversibility=args.reversibility,
        skill_atrophy_risk=args.atrophy,
        skill_load_trend=args.trend,
        friction_value=args.friction,
        agent_confidence=args.confidence,
        user_authority_required=args.authority,
        evidence_sufficiency="insufficient" if args.insufficient else "sufficient",
        protected_class=args.protected,
        manipulative=args.manipulative,
        surveillance_risk=args.surveillance,
        unsafe=args.unsafe,
        coercive=args.coercive,
        boundary_violation=args.boundary,
        argument_against_resistance=args.arg_resistance,
        user_requested_full_execution=args.requested,
        practice_mode=args.practice,
    )

    try:
        decision = engine.gate.gate_decision(ctx)
        engine.quarantine.assert_use_licensed(
            args.q_claim, args.q_use, args.user_rejected, args.user_confirmed)
    except Exception as e:
        print(f"GATE ERROR: {e}")
        return 1

    print("=== EMPOWERMENT GATE DECISION ===")
    print(f"mode:          {decision['mode']}")
    print(f"result_state:  {decision['result_state']}")
    print(f"precedence:    {decision['precedence_position']} "
          f"(STOP > DEFER > ASK > SCAFFOLD > ACT)")
    print(f"dissent_required: {decision['dissent_required']}")
    if decision.get("fail_closed_note"):
        print(f"note:          {decision['fail_closed_note']}")
    print()
    print("=== TWO-TYPED QUARANTINE ===")
    print(f"claim_trust (FAOS Q0-Q10):  {args.q_claim} — licensed")
    print(f"use_permission (Ecology Q0-Q5): {args.q_use}"
          f"{' (user-confirmed)' if args.user_confirmed else ''}"
          f"{' (user-REJECTED — final)' if args.user_rejected else ''} — licensed")
    print()
    print("=== INTERPRETATION FOR THE CONVERSATION ===")
    print(interpret(decision["mode"]))
    return 0


def interpret(mode: str) -> str:
    return {
        "STOP": "Do not proceed. Record why. The action is outside what the "
                "gate permits (safety/prohibition trigger).",
        "DEFER": "The choice belongs to the user. Support, ask, hold — do not "
                 "act for them or push a direction.",
        "ASK": "One targeted question resolves the ambiguity. Ask it. Never "
               "substitute ASK for DEFER when the choice is the user's by right.",
        "SCAFFOLD": "Structure the work, present options, keep capability "
                    "preservation first. Do not complete the task for the user.",
        "ACT": "Proceed within the explicit request or prior authorization. "
               "Record the mode selection.",
    }[mode]


if __name__ == "__main__":
    sys.exit(main())
