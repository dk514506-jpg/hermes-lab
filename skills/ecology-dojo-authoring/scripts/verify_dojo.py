#!/usr/bin/env python3
"""Generic per-dojo verifier for ConvoDojo-style practice packages.

Usage: python3 verify_dojo.py <dojo_dir> [<dojo_dir> ...]
Verifies the 7 canonical artifacts of an Ecology Phase6 dojo:
  dialogue_state_machine.json, persona_config.yaml, rubric.json,
  sparring_intensity_profile.json, in_session_coaching_rules.md,
  debrief_template.md, transfer_scenario_set.md
Prints [PASS]/[FAIL] per check; exits 1 if any check fails.
Matches the house register of council_notes/verify_phaseN.py (Phase 6 pattern).
Requires: python3 + PyYAML.
"""
import json
import os
import re
import sys

CANON = [
    "dialogue_state_machine.json", "persona_config.yaml", "rubric.json",
    "sparring_intensity_profile.json", "in_session_coaching_rules.md",
    "debrief_template.md", "transfer_scenario_set.md",
]

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def jload(path):
    with open(path) as f:
        return json.load(f)


def read(path):
    with open(path) as f:
        return f.read()


def verify_dojo(d):
    try:
        import yaml
    except ImportError:
        check("pyyaml available", False, "pip install pyyaml")
        return
    tag = os.path.basename(d)

    for canon in CANON:
        check(f"{tag}: exists {canon}", os.path.isfile(os.path.join(d, canon)))

    dsm = jload(os.path.join(d, "dialogue_state_machine.json"))
    check(f"{tag}: dsm stages with conditions",
          all(s.get("entry_conditions") and s.get("exit_conditions")
              for s in dsm.get("stages", [])) and len(dsm["stages"]) >= 5)
    check(f"{tag}: dsm adapted_from documents changes",
          "changed" in dsm.get("adapted_from", {}) and dsm["adapted_from"].get("kept"))
    check(f"{tag}: dsm transition_policy + custom_stages",
          dsm.get("transition_policy", {}).get("advance_requires")
          and dsm.get("custom_stages", {}).get("allowed") is True)
    check(f"{tag}: dsm coach_rules_ref anchors",
          all(s.get("coach_rules_ref", "").startswith("in_session_coaching_rules.md#")
              for s in dsm["stages"]))

    pcfg = yaml.safe_load(read(os.path.join(d, "persona_config.yaml")))
    personas = pcfg.get("personas", [])
    check(f"{tag}: persona count 2-3", 2 <= len(personas) <= 3)
    schema_keys = {"id", "name", "role", "context", "stance", "speech_profile",
                   "boundary_rules", "sanitization"}
    check(f"{tag}: persona full schema", all(schema_keys <= set(p.keys()) for p in personas))
    for req in ["lattice insights", "never coerces", "never shames"]:
        hits = sum(1 for p in personas for br in p.get("boundary_rules", []) if req in br)
        check(f"{tag}: boundary rule '{req}'", hits >= len(personas))
    check(f"{tag}: persona sanitization audited",
          all(p.get("sanitization", {}).get("audited") for p in personas))

    rub = jload(os.path.join(d, "rubric.json"))
    check(f"{tag}: rubrics >=2", len(rub.get("rubrics", [])) >= 2)
    check(f"{tag}: rubric dimensions evidence-anchored",
          all(dim.get("evidence") for r in rub["rubrics"] for dim in r.get("dimensions", [])))
    check(f"{tag}: rubric scoring lens + anchoring",
          all(r.get("scoring", {}).get("type") == "lens"
              and "anchoring" in r.get("scoring", {}) for r in rub["rubrics"]))
    check(f"{tag}: rubric_use_rules lens-not-verdict",
          any("lens" in u and "verdict" in u for u in rub.get("rubric_use_rules", [])))

    prof = jload(os.path.join(d, "sparring_intensity_profile.json"))
    check(f"{tag}: intensity 5 levels", len(prof.get("levels", [])) == 5)
    check(f"{tag}: intensity escalation policies", len(prof.get("escalation_policies", [])) >= 2)
    check(f"{tag}: intensity user_agreement_requirement",
          "user_agreement_requirement" in prof and "rule" in prof["user_agreement_requirement"])
    check(f"{tag}: intensity deescalation rules", len(prof.get("deescalation_rules", [])) >= 2)
    check(f"{tag}: intensity sycophancy_guard", "sycophancy_guard" in prof)

    rules = read(os.path.join(d, "in_session_coaching_rules.md"))
    for sec in ["Module Separation", "When to Interrupt", "Hint-Not-Answer", "On-Demand"]:
        check(f"{tag}: coaching rules '{sec}'", sec in rules)
    debrief = read(os.path.join(d, "debrief_template.md"))
    for sec in ["Rubric Lenses", "preserved_user_decision", "evidence"]:
        check(f"{tag}: debrief '{sec}'", sec.lower() in debrief.lower())
    transfer = read(os.path.join(d, "transfer_scenario_set.md"))
    n_base = len(re.findall(r"^\| scn_", transfer, re.M))
    n_tr = len(re.findall(r"^\| tr_", transfer, re.M))
    check(f"{tag}: transfer base >=3", n_base >= 3)
    check(f"{tag}: transfer scenarios >=2", n_tr >= 2)
    check(f"{tag}: transfer rules section", "Transfer Rules" in transfer)

    bank_ids = {p["id"] for p in personas}
    scn_personas = set(re.findall(r"p_[a-z_]+", transfer))
    missing = scn_personas - bank_ids
    check(f"{tag}: scenario persona refs resolve", not missing, f"missing={sorted(missing)}")

    for art in ["dialogue_state_machine.json", "rubric.json",
                "sparring_intensity_profile.json", "persona_config.yaml"]:
        txt = read(os.path.join(d, art))
        check(f"{tag}: evidence flags in {art}",
              "VERIFIED" in txt and "RECONSTRUCTED" in txt)


def main():
    if len(sys.argv) < 2:
        print("usage: verify_dojo.py <dojo_dir> [<dojo_dir> ...]")
        sys.exit(2)
    for d in sys.argv[1:]:
        if not os.path.isdir(d):
            print(f"[FAIL] not a directory: {d}")
            fails.append(d)
            continue
        verify_dojo(d)
        print()
    if fails:
        print(f"FAILED: {len(fails)} checks")
        sys.exit(1)
    print("ALL DOJO CHECKS PASSED")


if __name__ == "__main__":
    main()
