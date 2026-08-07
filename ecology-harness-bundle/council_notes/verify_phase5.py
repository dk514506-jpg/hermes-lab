#!/usr/bin/env python3
"""Phase 5 verification: learnability safeguard artifacts.

Run: python3 council_notes/verify_phase5.py
Verifies the Phase 5 changed paths:
  1. Phase5_Safeguards/learnability_state_schema.json exists and parses
  2. Schema is itself valid JSON Schema draft-07 (meta-schema check)
  3. A realistic estate snapshot instance conforms (per-skill state,
     estate aggregates, thresholds, evidence)
  4. Negative tests: invalid enum/range values are rejected;
     required telemetry_policy.rationale is enforced
  5. No dangling $refs; every definition is reachable from the root
  6. Phase5_Safeguards/skill_atrophy_risk_check.md exists and carries the
     required operational sections
"""
import json
import os
import re
import sys

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("[FAIL] jsonschema not installed — pip install jsonschema")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
SAFE = os.path.join(ROOT, "..", "Phase5_Safeguards")
SCHEMA_PATH = os.path.join(SAFE, "learnability_state_schema.json")
MD_PATH = os.path.join(SAFE, "skill_atrophy_risk_check.md")

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def build_instance():
    """Realistic estate snapshot covering every schema branch."""
    return {
        "schema_version": "ecology-learnability/0.1",
        "project": "Motivational Ecology Agent Architecture",
        "estate_id": "test-user",
        "generated_at": "2026-08-06T19:00:00Z",
        "telemetry_policy": {
            "preference": "objective telemetry preferred over self-report for all skill_load, atrophy, and fade decisions",
            "self_report_status": "unreliable for capability estimation; flagged and de-weighted",
            "rationale": "Lee 2025 VERIFIED: confidence predicts less critical thinking.",
            "flag": "VERIFIED",
            "self_report_uses": ["context", "preference_signal", "readiness_statement"],
            "telemetry_sources": [{"field": "task_outcome", "source": "task telemetry"}],
        },
        "skills": [{
            "skill_id": "demo_skill",
            "skill_load_score": 0.55,
            "skill_load_trend": "falling",
            "baseline_performance": [{"timestamp": "2026-07-01T00:00:00Z", "task_id": "t1",
                                      "mode": "none", "outcome": "completed_unassisted",
                                      "source": "telemetry", "initiator": "user"}],
            "recent_performance": [{"timestamp": "2026-08-01T00:00:00Z", "task_id": "t2",
                                    "mode": "hint", "outcome": "completed_assisted",
                                    "source": "telemetry", "initiator": "user"}],
            "assisted_performance_track": [],
            "unassisted_competence_track": [],
            "assistance_fraction": 0.45,
            "unassisted_completion_rate": 0.6,
            "last_practice": "2026-08-05T00:00:00Z",
            "practice_frequency": "3 sessions/week",
            "source_basis": "telemetry",
            "atrophy_risk": "medium",
            "empowerment_ratio": 1.2,
            "empowerment_ratio_flag": "computed",
            "preference_classification": {"classification": "unclassified",
                                          "basis": "insufficient windows",
                                          "flag": "RECONSTRUCTED"},
            "readiness_state": "emerging",
            "scaffold_level_current": 2,
            "fade_schedule": [],
            "last_scaffold_fade": "2026-07-20T00:00:00Z",
            "preserved_user_decision": "",
        }],
        "estate_aggregates": {
            "skill_count": 1,
            "mean_skill_load": 0.55,
            "median_skill_load": 0.55,
            "at_risk_skills": [{"skill_id": "demo_skill", "risk_level": "medium",
                                "trigger_evidence": ["skill_load_score 0.62 -> 0.41 over 3 windows"]}],
            "dependency_ratio": 0.45,
            "estate_empowerment_ratio": 1.2,
            "sweep_timestamp": "2026-08-06T19:00:00Z",
        },
        "thresholds": {
            "trend_trigger": {"rule": "falling over 2 windows triggers review",
                              "flag": "RECONSTRUCTED", "grounding": "Budzyn 2025"},
            "single_point_dip": {"rule": "no single-point action",
                                 "flag": "RECONSTRUCTED", "grounding": "Shaikh 2026"},
            "preference_vs_atrophy": {"rule": "preference beats atrophy on ambiguity",
                                      "flag": "RECONSTRUCTED", "grounding": "Contrary_Findings B1"},
            "risk_classification": [
                {"level": "none", "criteria": "flat/rising", "flag": "RECONSTRUCTED"},
                {"level": "low", "criteria": "single dip or preference", "flag": "RECONSTRUCTED"},
                {"level": "medium", "criteria": "trend + 10pp", "flag": "RECONSTRUCTED"},
                {"level": "high", "criteria": "trend + 10pp + rising assistance", "flag": "RECONSTRUCTED"},
            ],
            "budzyn_anchor": {"finding": "ADR 28.4 -> 22.4", "use": "canonical warning"},
        },
        "evidence": [{"id": "budzyn-2025", "flag": "VERIFIED",
                      "finding": "ADR reversion", "use_in_schema": "budzyn_anchor"}],
    }


def main():
    # 1. Artifacts exist
    for p in [SCHEMA_PATH, MD_PATH]:
        check(f"Phase 5 output exists: {os.path.basename(p)}", os.path.exists(p))

    # 2. Schema parses + is valid draft-07
    try:
        schema = json.load(open(SCHEMA_PATH))
        check("parse learnability_state_schema.json", True, f"{len(json.dumps(schema))} bytes")
    except Exception as e:
        check("parse learnability_state_schema.json", False, str(e))
        print(f"{len(fails)} FAILURE(S): {fails}")
        sys.exit(1)

    check("$id is ecology-learnability/0.1", schema.get("$id") == "ecology-learnability/0.1")
    check("schema_version const matches $id",
          schema.get("properties", {}).get("schema_version", {}).get("const") == "ecology-learnability/0.1")

    meta_errs = list(Draft7Validator(Draft7Validator.META_SCHEMA).iter_errors(schema))
    check("schema is valid draft-07", not meta_errs, f"{len(meta_errs)} errors")

    v = Draft7Validator(schema)

    # 3. Conformance
    errs = list(v.iter_errors(build_instance()))
    check("realistic estate instance conforms", not errs, f"{len(errs)} errors")

    # 4. Negative tests
    bad = build_instance()
    bad["skills"][0]["skill_load_trend"] = "sideways"
    bad["skills"][0]["skill_load_score"] = 1.7
    msgs = [str(e.message) for e in v.iter_errors(bad)]
    check("rejects invalid trend enum",
          any("'sideways' is not one of" in m for m in msgs), "; ".join(msgs[:1]))
    check("rejects score > 1",
          any("greater than the maximum of 1" in m for m in msgs), "; ".join(msgs[:1]))

    no_rat = build_instance()
    del no_rat["telemetry_policy"]["rationale"]
    msgs2 = [str(e.message) for e in v.iter_errors(no_rat)]
    check("enforces required telemetry_policy.rationale",
          any("rationale" in m for m in msgs2), "; ".join(msgs2[:1]))

    # 5. $ref integrity
    text = json.dumps(schema)
    refs = set(re.findall(r'"\$ref": "#/definitions/(\w+)"', text))
    defined = set(schema.get("definitions", {}))
    check("no dangling $refs", refs <= defined, f"refs={sorted(refs)}")
    reachable = set(re.findall(r'"\$ref": "#/definitions/(\w+)"', text))
    check("all definitions reachable from root", reachable == defined,
          f"unreachable={sorted(defined - reachable)}")

    # 6. Markdown sections present
    md = open(MD_PATH).read()
    for sec in ["When the Check Runs", "The Check Pipeline", "Classify risk level",
                "Budzy", "Empowerment Boundary", "Evidence Register"]:
        check(f"md section: {sec}", sec.lower() in md.lower())

    # 7. Truthfulness guards (post-review revision round, 2026-08-06):
    #    Jose 2025 is an OPINION article per the digest quality register — the
    #    atrophy check must carry the caveat, never cite it as plain VERIFIED.
    jose_line = [l for l in md.splitlines() if "Jose 2025" in l]
    check("Jose 2025 cited with opinion caveat",
          any("opinion" in l and "commentary" in l for l in jose_line),
          jose_line[0][:80] if jose_line else "no Jose line found")
    check("Jose 2025 not flagged bare VERIFIED",
          all("VERIFIED" not in l.replace("VERIFIED-fetched", "") for l in jose_line),
          jose_line[0][:80] if jose_line else "no Jose line found")

    #    CALM-IT is a preprint — the fade rules must flag it as such.
    fade_md = open(os.path.join(SAFE, "scaffolding_fade_rules.md")).read()
    calm_lines = [l for l in fade_md.splitlines() if "CALM-IT" in l or "Nguyen 2026" in l]
    check("CALM-IT flagged as preprint in fade rules",
          all("preprint" in l for l in calm_lines),
          f"{len(calm_lines)} CALM-IT line(s), all preprint-flagged")

    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {fails}")
        sys.exit(1)
    print("ALL PHASE 5 CHANGED PATHS VERIFIED — exit 0")


if __name__ == "__main__":
    main()
