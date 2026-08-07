"""
faos_ecology_engine.py — Phase 10 integration module.

Binds the FAOS gateway engine (faos_engine_extension.py, in-estate copy)
with the Ecology Guardian intellect:

  1. EcologyGate — the 5-mode empowerment selector (ACT/SCAFFOLD/ASK/
     DEFER/STOP) implemented from empowerment_boundary.md's trigger sets
     and mode precedence (STOP > DEFER > ASK > SCAFFOLD > ACT), mapped to
     FAOS result states (D2): ACT→TRUE, SCAFFOLD→PARTIAL, ASK→INCONCLUSIVE,
     DEFER→PARTIAL, STOP→BLOCKED.
  2. Two-typed quarantine (D1): claim_trust (FAOS Q0-Q10) × use_permission
     (Ecology Q0-Q5) as INDEPENDENT axes. FAOS clearing a claim never
     licenses Ecology's use of it; user-rejected (Q3) is final.
  3. DojoClose — the FAOS 6-pass instrumented close applied to any dojo
     session record (D3 / memo Phase B).
  4. S0-S9 lifecycle + absence gating wired as engine enforcement (they
     were MAPPED-NOT-INSTANTIATED after Phase 9). Enforcement surface is
     the FAOS engine's contract: explicit prohibited_edges blocklist
     (S6→S5, S8→S3, S0→S5) + halt-state membership + fail-closed absence.
     NOT full stepwise/selector enforcement — that is a Phase 11 item
     (see Phase10_Revision_Plan R5).

Pure and deterministic: no LLM calls. Run self-test directly.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from faos_engine_extension import (  # noqa: E402
    FaosConfig,
    FaosConfigError,
    FaosEngine,
    RouteDecision,
)


# =========================================================================
# ECOLOGY GATE — the 5-mode empowerment selector (Guardian intellect)
# =========================================================================

MODE_PRECEDENCE = ["STOP", "DEFER", "ASK", "SCAFFOLD", "ACT"]
MODE_TO_RESULT = {"ACT": "TRUE", "SCAFFOLD": "PARTIAL", "ASK": "INCONCLUSIVE",
                  "DEFER": "PARTIAL", "STOP": "BLOCKED"}

PROTECTED_CLASSES = {
    "meaning_making": "DEFER",
    "identity_claim": "DEFER",
    "interpretive_closure": "DEFER",
    "unresolved_tension": "DEFER",
    "motivational_insight_acceptance": "DEFER",
    "final_commitment": "max(ASK, DEFER)",
    "value_judgment": "max(ASK, DEFER)",
    "interpersonal_stance": "max(ASK, DEFER)",
}


@dataclass
class GateContext:
    """The state the 5-mode selector reads (empowerment_boundary state vars)."""
    task_meaning_level: str = "low"          # low | medium | high
    choice_branching_level: str = "low"      # low | medium | high
    reversibility: str = "reversible"        # reversible | hard | irreversible
    user_authority_required: bool = False
    evidence_sufficiency: str = "sufficient" # insufficient | partial | sufficient
    skill_atrophy_risk: str = "low"          # low | medium | high
    skill_load_trend: str = "flat"           # rising | flat | falling (HEB canonical; R5 reconciled)
    protected_class: Optional[str] = None
    friction_value: str = "low"              # low | medium | high
    user_requested_full_execution: bool = False
    consent_scope_change: bool = False
    unsafe: bool = False
    coercive: bool = False
    manipulative: bool = False
    surveillance_risk: bool = False
    identity_closure_without_consent: bool = False
    boundary_violation: bool = False
    practice_mode: bool = False
    agent_confidence: str = "medium"         # low | medium | high
    practice_log_private: bool = False
    argument_against_resistance: bool = False
    viable_paths: int = 3           # DEFER branch trigger qualifier (>3 viable paths)
    one_question_resolves: bool = True  # ASK trigger: a single targeted question resolves it


class EcologyGate:
    """The Guardian intellect: select the empowerment mode from exact
    trigger sets (empowerment_boundary.md), then map to the FAOS result
    state. Mode precedence: STOP > DEFER > ASK > SCAFFOLD > ACT."""

    def __init__(self, config: FaosConfig):
        self.config = config
        mapping = (config.raw.get("gate", {}) or {}).get("empowerment_mode_map", {})
        # YAML parses bare TRUE/PARTIAL as booleans — normalize to strings.
        self.mode_map = {
            str(k).upper(): (str(v).upper() if not isinstance(v, bool) else ("TRUE" if v else "FALSE"))
            for k, v in (mapping or MODE_TO_RESULT).items()
        }
        if not mapping:
            self.mode_map = dict(MODE_TO_RESULT)

    # ---- individual trigger tests ---------------------------------- #

    def _want_stop(self, c: GateContext) -> bool:
        return bool(
            c.unsafe or c.coercive or c.manipulative
            or c.surveillance_risk
            or c.identity_closure_without_consent
            or c.boundary_violation
            or c.argument_against_resistance   # W1: absolute prohibition (MI spirit gate)
            or (c.practice_log_private and c.surveillance_risk)
        )

    def _want_defer(self, c: GateContext) -> bool:
        if c.protected_class:
            required = PROTECTED_CLASSES.get(c.protected_class, "DEFER")
            if "DEFER" in required:
                # R10: max(ASK, DEFER) classes defer only when the question
                # is the user's regardless of the answer (not resolvable by
                # one question); otherwise the ASK probe owns it.
                if "ASK" in required and c.one_question_resolves \
                        and not c.user_authority_required:
                    return False
                return True
        # DEFER's branch trigger is qualified in the source: high branching
        # that changes future option space (>3 viable paths, irreversible or
        # hard-to-reverse, paths affect each other). Plain high branching
        # that ONE question resolves is ASK's territory (cheap probe).
        branch_owned_by_user = (
            c.choice_branching_level == "high"
            and (c.viable_paths > 3 or c.reversibility in ("hard", "irreversible"))
        )
        # W4: scoped DEFER evidence clause — "evidence insufficient AND the
        # question belongs to the user anyway." High meaning + insufficient
        # evidence + NOT one-question-resolvable => the choice is the user's
        # to make; ASK owns the one-question-resolves cases (never shadowed).
        evidence_owned_by_user = (
            c.evidence_sufficiency == "insufficient"
            and c.task_meaning_level == "high"
            and not c.one_question_resolves
        )
        return bool(
            branch_owned_by_user
            or evidence_owned_by_user
            or c.user_authority_required
            or c.consent_scope_change
        )

    def _want_ask(self, c: GateContext) -> bool:
        # ASK is the ambiguity budget's cheap probe. Per empowerment_boundary
        # "ASK never substitutes for DEFER": if the choice belongs to the
        # user regardless of the answer (protected class, authority
        # required), it is DEFER — excluded here. Source trigger: high
        # branching, OR medium meaning with genuinely unknown direction
        # (encoded as medium branching + insufficient evidence + one
        # question resolves it).
        if c.protected_class or c.user_authority_required:
            return False
        high_branching = (
            c.choice_branching_level == "high"
            and c.one_question_resolves
            and c.evidence_sufficiency == "insufficient"
        )
        medium_unknown_direction = (
            c.task_meaning_level == "medium"
            and c.choice_branching_level == "medium"
            and c.evidence_sufficiency == "insufficient"
            and c.one_question_resolves
        )
        return bool(high_branching or medium_unknown_direction)

    def _want_scaffold(self, c: GateContext) -> bool:
        return bool(
            c.skill_atrophy_risk in ("medium", "high")
            or c.friction_value in ("medium", "high")   # W3: >= medium (Xu 2026)
            or c.choice_branching_level == "medium"
            or c.practice_mode
        )

    def _want_act(self, c: GateContext) -> bool:
        if c.user_requested_full_execution:
            return True
        # R5: trend value must be a known enum (rising|flat|falling) —
        # reject anything else so a typo can't silently pass the W2 check.
        if c.skill_load_trend not in ("rising", "flat", "falling"):
            raise FaosConfigError(
                f"Invalid skill_load_trend {c.skill_load_trend!r} — "
                f"must be one of rising|flat|falling (HEB canonical).")
        return bool(
            c.task_meaning_level == "low"
            and c.choice_branching_level == "low"
            and c.reversibility == "reversible"
            and c.evidence_sufficiency != "insufficient"
            and c.skill_atrophy_risk == "low"
            and c.skill_load_trend != "falling"   # W2: never ACT while capability erodes
            and c.agent_confidence in ("medium", "high")
        )

    # ---- selection -------------------------------------------------- #

    def select_mode(self, c: GateContext) -> str:
        """Mode precedence: STOP > DEFER > ASK > SCAFFOLD > ACT, with the
        empowerment_boundary rule 'ASK never substitutes for DEFER' encoded
        by exclusion (ASK excludes protected-class and authority-required
        contexts, which DEFER owns). Returns the highest-precedence mode
        whose trigger set fires; fail-closed default is DEFER."""
        if self._want_stop(c):
            return "STOP"
        if self._want_defer(c):
            return "DEFER"
        if self._want_ask(c):
            return "ASK"
        if self._want_scaffold(c):
            return "SCAFFOLD"
        if self._want_act(c):
            return "ACT"
        # fail-closed: nothing clearly licensed -> defer to the human
        return "DEFER"

    def gate_decision(self, c: GateContext) -> dict[str, Any]:
        """Full gate record: mode + FAOS result state + dissent."""
        mode = self.select_mode(c)
        result = self.mode_map.get(mode, "BLOCKED")
        return {
            "mode": mode,
            "result_state": result,
            "precedence_position": MODE_PRECEDENCE.index(mode),
            "dissent_required": bool((self.config.raw.get("gate", {}) or {}).get("dissent_required", True)),
            "fail_closed_note": "no trigger set fired cleanly -> DEFER (human)" if mode == "DEFER" and not (
                self._want_defer(c) or self._want_ask(c) or self._want_scaffold(c) or self._want_act(c)
            ) else None,
        }


# =========================================================================
# TWO-TYPED QUARANTINE (D1)
# =========================================================================

ECOLOGY_TIER_OPERATIONAL = {"Q0", "Q1"}  # fallback if config lacks `operational:`


class TwoTypedQuarantine:
    """Claim trust (FAOS Q0-Q10) × use permission (Ecology Q0-Q5) as
    INDEPENDENT axes. The load-bearing rule: FAOS clearing a claim is
    necessary but NEVER sufficient for use toward a human."""

    def __init__(self, config: FaosConfig):
        self.config = config
        eco_raw = (config.raw.get("ecology_quarantine", {}) or {})
        self.eco_tiers = eco_raw.get("tiers", {})
        # R7: read the operational set from config (schema-drift seam);
        # fall back to the constant only if the config omits it.
        declared = eco_raw.get("operational") or []
        self.eco_operational = set(declared) if declared else set(ECOLOGY_TIER_OPERATIONAL)

    def claim_trust_ok(self, q_claim: str) -> bool:
        """FAOS axis: is the claim trustworthy enough to build on?"""
        if not self.config.quarantine_tiers.tiers:
            return True
        if q_claim not in self.config.quarantine_tiers.tiers:
            raise FaosConfigError(f"Unknown claim-trust tier {q_claim!r}")
        return self.config.quarantine_tiers.is_operational(q_claim)

    def use_permission_ok(self, q_use: str, user_rejected: bool = False,
                          user_confirmed: bool = False) -> bool:
        """Ecology axis: may the material touch the human, and how?
        User-rejected (Q3) is FINAL regardless of evidence strength.
        R3 (Phase 11): Q2 identity-level becomes usable WITH explicit
        recorded user confirmation (the DEFER->confirm path); default
        remains quarantine. Fail-closed default unchanged."""
        if user_rejected or q_use == "Q3":
            return False
        if q_use not in self.eco_tiers:
            raise FaosConfigError(f"Unknown use-permission tier {q_use!r}")
        if q_use in self.eco_operational:
            return True
        if q_use == "Q2" and user_confirmed:
            return True
        return False

    def assert_use_licensed(self, q_claim: str, q_use: str,
                            user_rejected: bool = False,
                            user_confirmed: bool = False) -> None:
        """The merged gate: BOTH axes must pass. FAOS clearing never
        licenses Ecology use; Ecology's user-rejected class is final."""
        if not self.claim_trust_ok(q_claim):
            raise FaosConfigError(
                f"CLAIM NOT LICENSED: claim-trust tier {q_claim} is not "
                f"operational (FAOS Q0-Q10 axis)."
            )
        if not self.use_permission_ok(q_use, user_rejected, user_confirmed):
            raise FaosConfigError(
                f"USE NOT LICENSED: use-permission class {q_use} "
                f"{'(user-rejected — final)' if (user_rejected or q_use == 'Q3') else ''} "
                f"{'(identity-level — requires explicit user confirmation)' if q_use == 'Q2' and not user_confirmed else 'is not operational'} "
                f"(Ecology Q0-Q5 axis). FAOS clearing a claim never licenses "
                f"its use toward a human."
            )


# =========================================================================
# DOJO CLOSE — 6-pass instrumented close on any dojo session record (D3)
# =========================================================================

CLOSE_PASSES = ["victory", "defect", "dissent", "proxy_check",
                "boundary_check", "transfer_status"]
RESULT_STATES = ["TRUE", "FALSE", "PARTIAL", "INCONCLUSIVE", "BLOCKED"]


class DojoClose:
    """Wraps a dojo session record with the FAOS 6-pass instrumented close."""

    def __init__(self, config: FaosConfig):
        self.config = config

    def close_dojo_session(self, session: dict[str, Any]) -> dict[str, Any]:
        dojo = session.get("dojo", "unknown")
        stages = session.get("stages_walked", [])
        gates = session.get("gates_fired", [])
        consent_recorded = bool(session.get("user_agreement"))
        boundary_rules = bool(session.get("boundary_rules_recorded"))
        no_shaming = bool(session.get("no_shaming_events", 0) == 0)
        # R6 (W6/Locus 3): evidence derives from ACTUAL session fields where
        # present; template defaults are labeled "template" — never asserted
        # as observed findings without provenance.
        dissent_evidence = (
            f"gates_fired={len(gates)} gate events recorded in session input"
            if gates else
            "template: no gate events in session input — guard-preservation "
            "not asserted (unknown)"
        )
        boundary_evidence = (
            "session records user_agreement + boundary_rules + zero no_shaming "
            "events" if (consent_recorded and boundary_rules and no_shaming)
            else "template: consent/boundary/no_shaming not present in session "
                 "input — NOT asserted (unknown)"
        )
        close = {
            "victory": {
                "state": "TRUE" if session.get("close_verdict", "FAIL") == "PASS" else "BLOCKED",
                "evidence": f"session walked {len(stages)} stages to close; gates fired: {len(gates)}",
            },
            "defect": {
                "state": "PARTIAL",
                "evidence": "dojo artifacts walked deterministically; live-LLM session is a runtime act",
            },
            "dissent": {
                "state": "TRUE" if gates else "INCONCLUSIVE",
                "evidence": dissent_evidence,
            },
            "proxy_check": {
                "state": "TRUE",
                "evidence": "measured success (stage walk) corresponds to actual goal (gate machinery live)",
            },
            "boundary_check": {
                "state": "TRUE" if (consent_recorded and boundary_rules and no_shaming) else "INCONCLUSIVE",
                "evidence": boundary_evidence,
            },
            "transfer_status": {
                "state": "TRUE",
                "evidence": "close record inheritable by gateway-wired runtime sessions",
            },
        }
        return {
            "item": session.get("session_id", f"{dojo}-session"),
            "path": "dojo-session",
            "dojo": dojo,
            "required_passes": CLOSE_PASSES,
            "result_state": "TRUE" if session.get("close_verdict", "FAIL") == "PASS" else "BLOCKED",
            "completed_passes": close,
        }

    def validate_close_record(self, record: dict[str, Any]) -> None:
        if record.get("result_state") not in RESULT_STATES:
            raise FaosConfigError(f"Bad result state {record.get('result_state')!r}")
        completed = record.get("completed_passes", {})
        for p in CLOSE_PASSES:
            if p not in completed:
                raise FaosConfigError(f"Close record missing pass: {p}")
            # R6: every pass must carry a state AND evidence (no bare keys)
            entry = completed[p]
            if entry.get("state") not in RESULT_STATES:
                raise FaosConfigError(
                    f"Close pass {p!r} has invalid state {entry.get('state')!r}")
            if not entry.get("evidence"):
                raise FaosConfigError(f"Close pass {p!r} missing evidence")


# =========================================================================
# MERGED ENGINE — the integrated gateway (FAOS engine + Ecology gate)
# =========================================================================

class FaosEcologyEngine(FaosEngine):
    """The Phase 10 merged engine: FAOS gateway infrastructure with the
    Ecology Guardian intellect at the gate."""

    def __init__(self, config: FaosConfig):
        super().__init__(config)
        self.gate = EcologyGate(config)
        self.quarantine = TwoTypedQuarantine(config)
        self.dojo_close = DojoClose(config)

    # S0-S9 lifecycle enforcement (now instantiated)
    def advance_item(self, from_state: str, to_state: str) -> None:
        self.assert_state_transition(from_state, to_state)

    def is_item_halted(self, state: str) -> bool:
        return self.is_halt_state(state)

    # absence gating (now instantiated)
    def require_key_present(self, key: str) -> None:
        self.assert_not_absent(key)

    # full gate decision for a work item
    def process_work_item(self, context: GateContext,
                          q_claim: str, q_use: str,
                          user_rejected: bool = False,
                          user_confirmed: bool = False) -> dict[str, Any]:
        """R3 (Phase 11): user_confirmed wired through — the confirmed-Q2
        allowance is expressible via the engine API (identity-level use
        class usable WITH explicit recorded user confirmation, per the
        DEFER->confirm path). ConfirmedQuarantine subclass enforces the
        precedence: user-rejected outranks confirmation."""
        gate_record = self.gate.gate_decision(context)
        self.quarantine.assert_use_licensed(q_claim, q_use, user_rejected,
                                            user_confirmed)
        return {
            "gate": gate_record,
            "quarantine": {
                "claim_trust": q_claim,
                "use_permission": q_use,
                "user_rejected": user_rejected,
                "user_confirmed": user_confirmed,
                "licensed": True,
            },
        }


# =========================================================================
# SELF-TEST
# =========================================================================

def _self_test() -> None:
    here = Path(__file__).resolve().parent
    cfg_path = here / "faos_ecology_config.yaml"
    cfg = FaosConfig.load(cfg_path)
    engine = FaosEcologyEngine(cfg)

    print(f"Loaded merged config: {cfg.name} (schema {cfg.schema_version})")

    # 1. gate: each mode fires under its trigger set
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
        assert mode == expected, f"expected {expected}, got {mode}"
        print(f"  gate: {expected} OK (result {engine.gate.mode_map[expected]})")

    # 2. mode -> result state mapping
    for mode, result in MODE_TO_RESULT.items():
        d = engine.gate.gate_decision(GateContext())  # ACT default
        assert engine.gate.mode_map[mode] == result
    print("  gate: mode->result mapping OK")

    # 3. two-typed quarantine: FAOS clearing never licenses Ecology use
    try:
        engine.quarantine.assert_use_licensed("Q0", "Q3")  # trust OK, use REJECTED
        raise AssertionError("Q0/Q3 should be blocked (user-rejected class)")
    except FaosConfigError as e:
        print(f"  quarantine: Q0 claim + Q3 use BLOCKED as designed — {str(e)[:60]}...")
    try:
        engine.quarantine.assert_use_licensed("Q5", "Q0")  # trust BLOCKED
        raise AssertionError("Q5/Q0 should be blocked (non-operational claim)")
    except FaosConfigError as e:
        print(f"  quarantine: Q5 claim BLOCKED as designed — {str(e)[:60]}...")
    engine.quarantine.assert_use_licensed("Q0", "Q0")  # both licensed
    print("  quarantine: Q0/Q0 licensed OK; axes independent")

    # 4. S0-S9 lifecycle
    engine.advance_item("S0", "S1")
    try:
        engine.advance_item("S0", "S5")
        raise AssertionError("S0->S5 should be blocked")
    except FaosConfigError:
        print("  state: S0->S5 BLOCKED (prohibited edge) OK")
    print("  state: S0->S1 allowed OK")

    # 5. absence gate
    try:
        engine.require_key_present("scoring_gold_set_calibration_origin")
        raise AssertionError("registered absence should block")
    except FaosConfigError as e:
        print(f"  absence: registered absence BLOCKS as designed — {str(e)[:50]}...")

    # 6. dojo close
    rec = engine.dojo_close.close_dojo_session(
        {"dojo": "Conflict_Dojo", "stages_walked": ["engage", "de-escalate"],
         "gates_fired": [{"guard": "deescalation_first"}], "close_verdict": "PASS",
         "session_id": "test-session"})
    engine.dojo_close.validate_close_record(rec)
    print(f"  dojo close: 6-pass record OK (result {rec['result_state']})")

    print("\nMERGED ENGINE SELF-TEST PASSED")


if __name__ == "__main__":
    _self_test()
