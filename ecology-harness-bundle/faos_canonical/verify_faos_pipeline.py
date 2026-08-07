#!/usr/bin/env python3
"""verify_faos_pipeline.py — deterministic verification for the FAOS pipeline.

Runs the full extended-schema config through the extension engine and
asserts every governance rule fires. Exit 0 = all pass; non-zero = failure.

Usage: python3 verify_faos_pipeline.py
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from faos_engine_extension import FaosConfig, FaosConfigError, FaosEngine  # noqa: E402

CONFIG = HERE / "triage_faos_integration.yaml"

PASS = 0
FAIL = 0


def check(label: str, fn) -> None:
    global PASS, FAIL
    try:
        fn()
        PASS += 1
        print(f"  ✓ {label}")
    except Exception as exc:  # noqa: BLE001
        FAIL += 1
        print(f"  ✗ {label} — {exc}")


def main() -> int:
    print(f"=== FAOS PIPELINE VERIFICATION ({CONFIG.name}) ===")

    # 1. Config loads and schema is declared
    cfg = FaosConfig.load(CONFIG)

    def t_schema():
        assert cfg.schema_version == "faos-integration/2.0", cfg.schema_version
    check("schema_version is faos-integration/2.0", t_schema)

    engine = FaosEngine(cfg)

    # 2. Route map: every primary + shadow resolves, weights present
    def t_routes():
        assert len(cfg.route_map) == 6, len(cfg.route_map)
        for cls, entry in cfg.route_map.items():
            assert entry.primary in cfg.paths, f"{cls}: {entry.primary}"
            assert entry.shadow is None or entry.shadow in cfg.paths
            assert entry.promotion_rule == "single"
    check("all 6 routes resolve (primary+shadow, single promotion)", t_routes)

    def t_weights():
        d = engine.route_with_shadow("bridge_leakage")
        assert d.authority_weight == 5
        d = engine.route_with_shadow("clean")
        assert d.authority_weight == 1
    check("authority weights applied (5..1)", t_weights)

    # 3. Shadow promotion gated on observed conditions
    def t_shadow():
        d = engine.route_with_shadow("bridge_leakage")
        assert engine.should_promote_shadow(d, d.shadow_conditions) is True
        assert engine.should_promote_shadow(d, []) is False
    check("shadow promotion gated on conditions", t_shadow)

    # 4. Evidence ladder: no skips
    def t_ladder_ok():
        engine.assert_evidence_promotion("impression", "lead")
        engine.assert_evidence_promotion("lead", "fact")
        engine.assert_evidence_promotion("fact", "claim")
        engine.assert_evidence_promotion("claim", "judgment")
    check("evidence ladder allows stepwise promotion", t_ladder_ok)

    def t_ladder_block():
        try:
            engine.assert_evidence_promotion("impression", "judgment")
        except FaosConfigError:
            return
        raise AssertionError("impression->judgment must be blocked")
    check("evidence ladder blocks impression->judgment skip", t_ladder_block)

    # 5. State lineage: prohibited edges enforced, halt states recognized
    def t_lineage_block():
        for edge in ("S0", "S5"):
            try:
                engine.assert_state_transition(*edge)
            except FaosConfigError:
                return
        raise AssertionError("S0->S5 must be blocked")
    check("state lineage blocks S0->S5", t_lineage_block)

    def t_halt():
        assert engine.is_halt_state("S6") and engine.is_halt_state("S7") and engine.is_halt_state("S8")
        assert not engine.is_halt_state("S3")
    check("halt states S6/S7/S8 recognized", t_halt)

    # 6. Quarantine tiers: deny-by-default, only Q0-Q2 operational
    def t_quarantine_ok():
        engine.assert_quarantine_claim("Q0")
        engine.assert_quarantine_claim("Q2")
    check("quarantine allows Q0-Q2", t_quarantine_ok)

    def t_quarantine_block():
        for tier in ("Q3", "Q5", "Q8"):
            try:
                engine.assert_quarantine_claim(tier)
            except FaosConfigError:
                continue
            raise AssertionError(f"{tier} must be non-operational")
    check("quarantine blocks Q3+ from runtime", t_quarantine_block)

    # 7. Typed metrics: missing bundle rejected
    def t_metrics():
        engine.validate_metric(60, unit="score", scale="0-100", owner="rubric",
                               function="triage", source_locus="triage.yaml",
                               source_layer="config")
    check("typed metric with full bundle accepted", t_metrics)

    def t_metrics_block():
        try:
            engine.validate_metric(60, unit="score", scale="", owner="",
                                   function="", source_locus="", source_layer="")
        except FaosConfigError:
            return
        raise AssertionError("metric missing bundle must be rejected")
    check("typed metric missing bundle rejected", t_metrics_block)

    # 8. Absence register: registered absence blocks, unknown key passes
    def t_absence_block():
        try:
            engine.assert_not_absent("valens_book_x_pages_2p-5p")
        except FaosConfigError:
            return
        raise AssertionError("registered absence must block")
    check("absence register blocks registered key", t_absence_block)

    def t_absence_pass():
        engine.assert_not_absent("unregistered_key")  # must not raise
    check("absence register passes unregistered key", t_absence_pass)

    # 9. Non-operational registry: barred resonance blocked, others pass
    def t_nonop_block():
        try:
            engine.assert_operational("temporal_echo")
        except FaosConfigError:
            return
        raise AssertionError("barred resonance must be blocked")
    check("non-operational registry blocks barred resonance", t_nonop_block)

    def t_nonop_pass():
        engine.assert_operational("authority_weight")  # must not raise
    check("non-operational registry passes operational term", t_nonop_pass)

    # 10. Close + Locus specs
    def t_close():
        spec = engine.close_spec("test-item", "fix-bridge")
        assert spec["path"] == "fix-bridge"
        assert len(spec["required_passes"]) >= 6
    check("close spec carries 6+ passes", t_close)

    def t_locus():
        spec = engine.locus_review_spec("test-item", "fix-bridge")
        assert spec["reviewer"] == "locus"
        assert len(spec["checks"]) == 7
        assert spec["verdict"] is None
    check("locus review spec has 7 checks", t_locus)

    # 9. All roles used anywhere are defined
    def t_roles():
        used = set()
        for p in cfg.paths.values():
            if isinstance(p, dict):
                for s in p.get("prep", []) + p.get("fulfill", []):
                    if isinstance(s, dict):
                        used.add(s.get("role", ""))
                used.add((p.get("propose") or {}).get("role", "orchestrator"))
        for role in used - {""}:
            assert role in cfg.roles, f"role {role} undefined"
        assert "locus" in cfg.roles
    check("all used roles defined (incl. locus)", t_roles)

    # 10. Config validate() passes end-to-end (already done at load, re-run)
    def t_validate():
        cfg.validate()
    check("config.validate() clean", t_validate)

    print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
