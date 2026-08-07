"""
phase11_intervention.py — Phase 11 intervention layer module.

Implements the COMB successor stage (decision 3C) as executable logic:

  1. canvass_full_range  — enumerate the full BCTv1 range for a diagnosed
     binding constraint WITHOUT selecting (anti-premature-coherence).
  2. select_bct          — Q7 arbitration (Dallas 2a): BCT 10.x reward
     techniques NEVER auto-selected; require explicit user request + Deci
     risk disclosure, or the documented already-extrinsic exception path
     (never the default). Rejections preserved as witnesses (Valens P4).
  3. retrocode_delivered_plan — retrocode what was ACTUALLY delivered vs
     planned; produce the diff for the calibration log (the honesty op).
  4. skill_load_to_trend — D3 (T2R #9): convert PPS skill_load_score series
     to HEB skill_load_trend (rising/flat/falling — HEB canonical enum).
     Feeds the Phase 10 gate W2 trigger (ACT requires != falling).
  5. Stepwise S0-S9 + selector promotion — D4 (Phase 10 R5 handoff):
     advance_item enforces stepwise-only transitions + pre-declared
     selector at S3/S4->S5, per Valens Book IX.
  6. Confirmed-Q2 allowance — D4 (Phase 10 self-review #3 handoff):
     identity-level use class usable WITH explicit recorded user
     confirmation; default-quarantined otherwise.

Pure and deterministic: no LLM calls. Run self-test directly.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# ---- Phase 10 engine import (in-estate) -------------------------------- #
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "Phase10_Integration"))

from faos_engine_extension import FaosConfig, FaosConfigError, FaosEngine  # noqa: E402
from faos_ecology_engine import (  # noqa: E402
    FaosEcologyEngine, GateContext, TwoTypedQuarantine,
)

# =========================================================================
# BCTv1 REWARD TECHNIQUE REGISTER (Q7 scope: BCT 10.x)
# =========================================================================

BCT_10X_REWARD = {
    "10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "10.7", "10.8", "10.9", "10.10", "10.11",
}

# A minimal BCTv1 candidate model used by the module's own tests. Real
# deployments populate from the estate's TDF/BCW mapping tables.
EXAMPLE_RANGE = [
    {"technique": "1.1 goal setting (behavior)", "component_target": "M-Au",
     "evidence_anchor": "Locke & Latham 2002 (goal-setting verified)", "fit_score": 0.8},
    {"technique": "10.4 social reward", "component_target": "M-Au",
     "evidence_anchor": "Deci 1999 undermining (reward-verified)", "fit_score": 0.6},
    {"technique": "8.7 graded tasks", "component_target": "C-Ps",
     "evidence_anchor": "bandura 1997 self-efficacy", "fit_score": 0.7},
    {"technique": "1.4 action planning", "component_target": "M-Re",
     "evidence_anchor": "Gollwitzer 1999 implementation intentions", "fit_score": 0.85},
]


# =========================================================================
# D1: COMB successor stage — executable ops
# =========================================================================

class CombSuccessorStage:
    """The three successor ops from decision 3C, executable."""

    # ---- 1. canvass_full_range ------------------------------------- #

    def canvass_full_range(self, diagnosis: dict[str, Any],
                           binding_constraint: str) -> dict[str, Any]:
        """Enumerate the full applicable BCTv1 range WITHOUT selecting.
        Output carries NO selection field (anti-premature-coherence)."""
        # component_profile in the estate's schema is a LIST OF DICTS
        # ({"component": ..., "salience": ...}); accept plain string lists
        # too for robustness.
        profile = diagnosis.get("component_profile", [])
        profile_components = {
            (p.get("component") if isinstance(p, dict) else p) for p in profile
        }
        # In production this draws from the BCW/BCT mapping table for the
        # diagnosed component; the module's EXAMPLE_RANGE stands in for the
        # mapping in deterministic tests.
        range_out = [dict(c, component_target=c["component_target"])
                     for c in EXAMPLE_RANGE
                     if c["component_target"] == binding_constraint
                     or c["component_target"] in profile_components]
        return {
            "op": "canvass_full_range",
            "diagnosis_id": diagnosis.get("id", "unknown"),
            "binding_constraint": binding_constraint,
            "candidate_range": range_out,
            "note": "scored but UNRANKED — selection is a separate op",
        }

    # ---- 2. select_bct ---------------------------------------------- #

    SELECT_FIT_THRESHOLD = 0.5   # R2: component-fit × anchor passes this

    def select_bct(self, candidate_range: list[dict[str, Any]],
                   user_explicit_request: bool = False,
                   deci_risk_disclosed: bool = False,
                   already_extrinsic_behavior: bool = False,
                   extrinsic_evidence: Optional[str] = None) -> dict[str, Any]:
        """Q7 arbitration (Dallas 2a). BCT 10.x reward techniques are NEVER
        auto-selected. Rejections preserved as witnesses (Valens P4).
        R2 (judge W2): non-reward selection is by component-fit ×
        evidence-anchor strength (fit_score >= SELECT_FIT_THRESHOLD AND
        anchored) — the op no longer wholesale-passes everything."""
        selected: list[dict[str, Any]] = []
        rejected: list[dict[str, Any]] = []
        for cand in candidate_range:
            tech = cand.get("technique", "")
            tech_id = tech.split(" ", 1)[0] if tech else ""
            if tech_id in BCT_10X_REWARD:
                if user_explicit_request and deci_risk_disclosed:
                    ruling = "user_requested"
                    cand = dict(cand, q7_ruling=ruling, deci_risk_disclosed=True)
                    selected.append(cand)
                elif already_extrinsic_behavior:
                    # R8 (judge W8): exception path requires evidence anchor
                    if not extrinsic_evidence:
                        cand = dict(cand, q7_ruling="DENIED_never_auto_selected",
                                    reason="exception path requires extrinsic_evidence "
                                           "(bare flag insufficient)")
                        rejected.append(cand)
                        continue
                    ruling = "exception_path"
                    cand = dict(cand, q7_ruling=ruling,
                                deci_risk_disclosed=False,
                                extrinsic_evidence=extrinsic_evidence,
                                exception_note="already-extrinsic (Eisenberger & Cameron 1996) — documented, never default")
                    selected.append(cand)
                else:
                    cand = dict(cand, q7_ruling="DENIED_never_auto_selected",
                                reason="BCT 10.x reward technique requires explicit user request + Deci risk disclosure")
                    rejected.append(cand)
            else:
                # R2: evidence-strength selection — fit × anchor
                fit = float(cand.get("fit_score", 0.0))
                anchored = bool(cand.get("evidence_anchor"))
                if fit >= self.SELECT_FIT_THRESHOLD and anchored:
                    cand = dict(cand, q7_ruling="standard")
                    selected.append(cand)
                else:
                    cand = dict(cand, q7_ruling="REJECTED_below_fit_threshold",
                                reason=f"fit_score {fit} < {self.SELECT_FIT_THRESHOLD} or missing evidence anchor")
                    rejected.append(cand)
        return {
            "op": "select_bct",
            "selected_plan": selected,
            "rejected_with_reason": rejected,   # witnesses (Valens P4)
            "note": "rejected candidates preserved, never dropped",
        }

    # ---- 3. retrocode_delivered_plan -------------------------------- #

    def retrocode_delivered_plan(self, planned: list[dict[str, Any]],
                                 delivered_session: dict[str, Any]) -> dict[str, Any]:
        """Retrocode what was ACTUALLY delivered into BCTv1 labels; compare
        planned vs delivered; produce the diff for the calibration log."""
        delivered = delivered_session.get("delivered_techniques", [])
        planned_ids = {p.get("technique", "").split(" ", 1)[0] for p in planned}
        delivered_ids = {d.get("technique", "").split(" ", 1)[0] for d in delivered}
        delivered_but_not_planned = sorted(delivered_ids - planned_ids)
        planned_but_not_delivered = sorted(planned_ids - delivered_ids)
        return {
            "op": "retrocode_delivered_plan",
            "delivered_plan": delivered,
            "planned_vs_delivered_diff": {
                "delivered_but_not_planned": delivered_but_not_planned,
                "planned_but_not_delivered": planned_but_not_delivered,
                # R10: count BOTH directions (was planned-only)
                "gap_count": len(planned_but_not_delivered) + len(delivered_but_not_planned),
                "gap_planned_not_delivered": len(planned_but_not_delivered),
                "gap_delivered_not_planned": len(delivered_but_not_planned),
                "calibration_feed": "diff recorded for defect pass + pattern_thresholds risk_repeat=3",
            },
        }


# =========================================================================
# D3: skill_load -> trend conversion (T2R #9; HEB canonical enum)
# =========================================================================

@dataclass
class TrendSpec:
    window: int = 3            # number of recent scores considered
    min_change: float = 0.05   # |delta| threshold for rising/falling


class SkillLoadTrend:
    """Convert a PPS skill_load_score series to HEB skill_load_trend.
    HEB canonical enum: rising | flat | falling. Note: the Phase 10
    GateContext used 'steady' — this op emits HEB's canonical 'flat'
    (schema-drift fix recorded in Phase 11)."""

    def __init__(self, spec: Optional[TrendSpec] = None):
        self.spec = spec or TrendSpec()

    def convert(self, score_series: list[float]) -> dict[str, Any]:
        if not score_series:
            return {"trend": "flat", "window": self.spec.window,
                    "note": "empty series -> flat (no evidence of change)"}
        recent = score_series[-self.spec.window:]
        if len(recent) < 2:
            return {"trend": "flat", "window": self.spec.window,
                    "note": "insufficient points for trend"}
        first, last = recent[0], recent[-1]
        delta = last - first
        # R1 (judge W1): snap deltas within epsilon of ±min_change to
        # ±min_change. Float subtraction can land just inside the band for
        # a TRUE threshold move (e.g. 0.65->0.7 computes 0.0499999...);
        # snapping NEAR ZERO (previous guard) missed exactly this case.
        if abs(abs(delta) - self.spec.min_change) < 1e-9:
            import math
            delta = math.copysign(self.spec.min_change, delta)
        if delta >= self.spec.min_change:
            trend = "rising"
        elif delta <= -self.spec.min_change:
            trend = "falling"
        else:
            trend = "flat"
        return {"trend": trend, "window": self.spec.window,
                "min_change": self.spec.min_change,
                "delta": round(delta, 4),
                "series_used": recent,
                "note": "HEB canonical enum (rising|flat|falling)"}


# =========================================================================
# D4: stepwise S0-S9 + selector promotion (Phase 10 R5 handoff)
# =========================================================================

# Valens Book IX: promotion requires a pre-declared prospective selector.
# The config's rule is "Promotion (S3/S4→S5) requires a pre-declared
# prospective selector" — under stepwise enforcement the ONLY reachable
# promotion edge is S4->S5 (S3->S4 is qualification completion, not
# promotion; S3->S5 is a prohibited skip). Selector required there only.
STEPWISE_ORDER = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]
PROMOTION_EDGES = {"S4": "S5"}  # the promotion edge (selector pre-declared required)


class StepwiseLineage:
    """Extends the FAOS engine's blocklist enforcement with stepwise-only
    transitions + pre-declared-selector promotion (Valens Book IX)."""

    def __init__(self, engine: FaosEcologyEngine):
        self.engine = engine

    def advance_item(self, from_state: str, to_state: str,
                     selector_declared: bool = False) -> None:
        # First: the engine's own blocklist enforcement (3-edge blocklist)
        self.engine.assert_state_transition(from_state, to_state)
        # Halt states are terminal: a halted item may not proceed forward
        # (S6 result-conditioned, S7 blocked, S8 quarantined — Book IX).
        if self.engine.is_item_halted(from_state):
            raise FaosConfigError(
                f"Halt-state violation: {from_state} is a halt state "
                f"(S6 result-conditioned / S7 blocked / S8 quarantined) — "
                f"an item may not proceed past it (Valens Book IX). "
                f"Triggered at {from_state} -> {to_state}.")
        # Stepwise: only adjacent forward edges, unless the config's
        # prohibited_edges list already covers the jump (it does: S0->S5).
        fi = STEPWISE_ORDER.index(from_state)
        ti = STEPWISE_ORDER.index(to_state)
        if ti != fi + 1:
            raise FaosConfigError(
                f"Stepwise violation: {from_state} -> {to_state} is not an "
                f"adjacent forward transition (Valens Book IX).")
        # Selector requirement at promotion edges
        if from_state in PROMOTION_EDGES and PROMOTION_EDGES[from_state] == to_state:
            if not selector_declared:
                raise FaosConfigError(
                    f"Promotion {from_state}->{to_state} requires a "
                    f"pre-declared prospective selector (Valens Book IX).")


# =========================================================================
# D4: confirmed-Q2 allowance (Phase 10 self-review #3 handoff)
# =========================================================================

class ConfirmedQuarantine(TwoTypedQuarantine):
    """Named alias for the confirmed-Q2 allowance (R3): the Q2
    identity-level allowance now lives in the base TwoTypedQuarantine
    (faos_ecology_engine.py), so the merged engine's process_work_item is
    self-sufficient. This subclass exists for callers who want the
    allowance's name explicit; behavior is inherited (user-rejected
    outranks confirmation; fail-closed default unchanged)."""

    # inherited: use_permission_ok(q_use, user_rejected, user_confirmed)
    # inherited: assert_use_licensed(q_claim, q_use, user_rejected, user_confirmed)


# =========================================================================
# SELF-TEST
# =========================================================================

def _self_test() -> None:
    stage = CombSuccessorStage()

    # 1. canvass: enumerate without selecting
    diag = {"id": "d-001", "component_profile": ["M-Au", "M-Re"]}
    canvassed = stage.canvass_full_range(diag, "M-Au")
    assert canvassed["candidate_range"], "empty canvass"
    assert "selected" not in canvassed, "canvass must not select"
    print(f"  canvass: {len(canvassed['candidate_range'])} candidates, no selection field OK")

    # 2. select: Q7 gate
    # 2a. reward technique WITHOUT user request -> DENIED
    res = stage.select_bct(canvassed["candidate_range"])
    reward_rejected = [r for r in res["rejected_with_reason"]
                       if r["technique"].startswith("10.")]
    assert reward_rejected, "reward technique should be rejected without user request"
    print(f"  select: reward DENIED without user request OK ({len(res['selected_plan'])} selected, {len(res['rejected_with_reason'])} rejected-as-witnesses)")

    # 2b. reward WITH user request + disclosure -> allowed
    res2 = stage.select_bct(canvassed["candidate_range"],
                            user_explicit_request=True, deci_risk_disclosed=True)
    reward_selected = [s for s in res2["selected_plan"]
                       if s["technique"].startswith("10.")]
    assert reward_selected, "reward should be allowed with request + disclosure"
    assert reward_selected[0]["q7_ruling"] == "user_requested"
    print(f"  select: reward ALLOWED with user request + disclosure OK ({reward_selected[0]['technique']})")

    # 2b2. R7: request-only and disclosure-only -> DENY (AND-semantics)
    for partial in (dict(user_explicit_request=True, deci_risk_disclosed=False),
                    dict(user_explicit_request=False, deci_risk_disclosed=True)):
        rp = stage.select_bct(canvassed["candidate_range"], **partial)
        denied = [r for r in rp["rejected_with_reason"] if r["technique"].startswith("10.")]
        assert denied, f"partial trigger should DENY: {partial}"
    print("  select: partial request/disclosure combos DENY OK (AND-semantics)")

    # 2c. reward via exception path (requires extrinsic_evidence — R8)
    res3 = stage.select_bct(canvassed["candidate_range"], already_extrinsic_behavior=True,
                            extrinsic_evidence="PPS skill_load 0.62, extrinsic anchor")
    reward_exc = [s for s in res3["selected_plan"] if s["technique"].startswith("10.")]
    assert reward_exc and reward_exc[0]["q7_ruling"] == "exception_path"
    print("  select: reward ALLOWED via documented exception path (with evidence) OK")
    res3b = stage.select_bct(canvassed["candidate_range"], already_extrinsic_behavior=True)
    exc_denied = [r for r in res3b["rejected_with_reason"] if r["technique"].startswith("10.")]
    assert exc_denied, "exception without evidence should DENY"
    print("  select: exception WITHOUT extrinsic_evidence DENIED OK (R8)")

    # 2d. R2: evidence-strength selection — below-fit candidate rejected
    weak = [{"technique": "1.7 reduce cues", "component_target": "O-Ph",
             "evidence_anchor": "anchor", "fit_score": 0.10}]
    res_weak = stage.select_bct(weak)
    weak_rejected = [r for r in res_weak["rejected_with_reason"]
                     if r["q7_ruling"] == "REJECTED_below_fit_threshold"]
    assert weak_rejected, "below-threshold fit should be rejected (R2)"
    print("  select: below-fit-threshold candidate REJECTED OK (R2 evidence-strength)")

    # 3. retrocode: honesty op
    planned = [{"technique": "1.1 goal setting (behavior)"},
               {"technique": "10.4 social reward"}]
    delivered = {"delivered_techniques": [{"technique": "1.1 goal setting (behavior)"},
                                          {"technique": "1.4 action planning"}]}
    rc = stage.retrocode_delivered_plan(planned, delivered)
    assert "10.4" in rc["planned_vs_delivered_diff"]["planned_but_not_delivered"]
    assert "1.4" in rc["planned_vs_delivered_diff"]["delivered_but_not_planned"]
    print(f"  retrocode: gap captured ({rc['planned_vs_delivered_diff']['gap_count']} planned-not-delivered) OK")

    # 4. skill_load -> trend (HEB canonical); window=3 uses the LAST 3
    t = SkillLoadTrend()
    assert t.convert([0.8, 0.85, 0.82, 0.78])["trend"] == "falling", t.convert([0.8, 0.85, 0.82, 0.78])
    assert t.convert([0.7, 0.75, 0.8, 0.85])["trend"] == "rising"
    assert t.convert([0.8, 0.81, 0.8, 0.79])["trend"] == "flat", t.convert([0.8, 0.81, 0.8, 0.79])
    assert t.convert([0.9])["trend"] == "flat"
    # R1 (judge W1): exact-threshold boundary pairs must classify correctly
    assert t.convert([0.65, 0.7])["trend"] == "rising", t.convert([0.65, 0.7])
    assert t.convert([0.7, 0.65])["trend"] == "falling", t.convert([0.7, 0.65])
    assert t.convert([0.1, 0.15])["trend"] == "rising", t.convert([0.1, 0.15])
    assert t.convert([0.15, 0.1])["trend"] == "falling", t.convert([0.15, 0.1])
    print("  skill_load->trend: rising/flat/falling + short-series + R1 boundary pairs OK")

    # 5. stepwise S0-S9
    here = Path(__file__).resolve().parent
    cfg = FaosConfig.load(here / ".." / "Phase10_Integration" / "faos_ecology_config.yaml")
    engine = FaosEcologyEngine(cfg)
    sw = StepwiseLineage(engine)
    sw.advance_item("S0", "S1")
    sw.advance_item("S3", "S4")  # qualification completion — no selector needed
    try:
        sw.advance_item("S4", "S5")  # promotion — selector required
        raise AssertionError("S4->S5 without selector should be blocked")
    except FaosConfigError:
        print("  stepwise: S4->S5 requires pre-declared selector OK")
    sw.advance_item("S4", "S5", selector_declared=True)
    print("  stepwise: S4->S5 with selector OK")
    try:
        sw.advance_item("S1", "S3")  # skip
        raise AssertionError("S1->S3 skip should be blocked")
    except FaosConfigError:
        print("  stepwise: S1->S3 skip BLOCKED OK")
    sw.advance_item("S5", "S6")
    try:
        sw.advance_item("S6", "S7")  # halt-state exit
        raise AssertionError("S6->S7 halt exit should be blocked")
    except FaosConfigError:
        print("  stepwise: S6->S7 halt-state exit BLOCKED OK")
    print("  stepwise: adjacent forward + selector promotion + halt exit OK")

    # 6. confirmed-Q2
    q = ConfirmedQuarantine(cfg)
    try:
        q.assert_use_licensed("Q0", "Q2")  # no confirmation
        raise AssertionError("Q2 without confirmation should be blocked")
    except FaosConfigError:
        print("  quarantine: Q2 without confirmation BLOCKED (default) OK")
    q.assert_use_licensed("Q0", "Q2", user_confirmed=True)
    print("  quarantine: Q2 WITH explicit user confirmation ALLOWED OK")
    try:
        q.assert_use_licensed("Q0", "Q2", user_confirmed=True, user_rejected=True)
        raise AssertionError("user-rejected must outrank confirmation")
    except FaosConfigError:
        print("  quarantine: user-rejected outranks confirmation OK")

    print("\nPHASE 11 INTERVENTION MODULE SELF-TEST PASSED")


if __name__ == "__main__":
    _self_test()
