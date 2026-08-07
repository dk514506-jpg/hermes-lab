#!/usr/bin/env python3
"""Phase 6 verification: the five practice dojos (Phase6_Dojo).

Run: python3 council_notes/verify_phase6.py
Verifies the Phase 6 dojo layer per the cross-dojo conventions in the Phase 6
index README (§2.1-2.5, §5) and the estate Phase 5 safeguards:

Generic checks (ALL five dojos):
  1. Exactly the seven canonical artifacts exist (no missing, no extra)
  2. Every JSON parses; every YAML parses
  3. Every stage carries entry_conditions / exit_conditions / coach_rules_ref
  4. Persona banks: >= 2 personas, full schema, boundary_rules encoding
     no-coercion / no-shaming / no-lattice-reference, provenance evidence flags
  5. Rubric banks: >= 2 rubrics, all lens-type scoring, rubric_use_rules present
  6. Intensity profiles: levels 1-5, escalation + de-escalation policies +
     sycophancy guard (schema invariants from ecology-dojo/sparring_intensity/0.1)
  7. Coach rules: hint-not-answer scaffolding invariant (Bastani 2025,
     scaffolding_fade_rules.md §3.5); module separation declared
  8. Debrief template carries the preserved_user_decision section
     (empowerment_boundary.md §3.2; agent_deference_rules.md §2.1 — the debrief
     is where deferred decisions are recorded)
  9. Transfer sets: >= 3 base + >= 2 transfer scenarios
 10. Evidence discipline: VERIFIED + RECONSTRUCTED flags at DATA level
     (YAML comments do not survive parsing; the campaign discipline is that
     artifacts carry their flags in data, per README Evidence Discipline)

Owned-specific checks (Ambivalence_Dojo, Conflict_Dojo — authored by this
subagent; sibling dojos are checked on the generic invariants only, with
ownership attributed so the index agent can route any gaps):
  - exact required stage family; required hard gates; rubric extends bases
    (mi_fidelity_v1 / conflict_deescalation_v1); required domain dimensions;
    persona stance dynamics; user_agreement required in intensity profile
"""
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("[FAIL] pyyaml not installed — pip install pyyaml")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(ROOT, "..", "Phase6_Dojo"))
ARTIFACTS = [
    "dialogue_state_machine.json",
    "persona_config.yaml",
    "rubric.json",
    "sparring_intensity_profile.json",
    "in_session_coaching_rules.md",
    "debrief_template.md",
    "transfer_scenario_set.md",
]

DOJO_SPECS = {
    "Ambivalence_Dojo": {
        "owner": "owned",
        "stages": ["engage", "discern-ambivalence", "explore-both-sides",
                   "evoke-change-talk", "consolidate", "close"],
        "gates": ["spirit_gate", "no_premature_closure", "no_argument_against_resistance"],
        "extends": {"amb_mi_fidelity_v1": "mi_fidelity_v1"},
        "dims": ["darn_cat_evocation", "reflection_to_question_ratio",
                 "no_premature_closure"],
        "stance": ["change_talk_affinity"],
        "scn": "scn_amb_", "tr": "tr_amb_",
    },
    "Conflict_Dojo": {
        "owner": "owned",
        "stages": ["engage", "de-escalate", "separate-positions-from-interests",
                   "reframe", "generate-options", "close"],
        "gates": ["no_shaming", "no_forced_agreement", "deescalation_first"],
        "extends": {"conf_deescalation_v2": "conflict_deescalation_v1"},
        "dims": ["positions_vs_interests", "reframing_quality", "option_generation"],
        "stance": ["position", "interests"],
        "scn": "scn_conf_", "tr": "tr_conf_",
    },
    "Workplace_Dojo": {
        "owner": "owned",
        "stages": ["engage", "clarify-objective", "give-feedback", "request",
                   "delegate", "disagree-professionally", "explore-options",
                   "negotiate-align", "commit-close"],
        "gates": ["no_personal_attack", "power_gradient_guard", "no_forced_commitment"],
        "extends": {},
        "dims": ["ask_explicitness", "behavioral_specificity", "interest_discovery"],
        "stance": ["change_talk_affinity"],
        "scn": "scn_wk_", "tr": "tr_wk_",
    },
    "Conversation_Dojo": {"owner": "sibling", "scn": "scn_convo_", "tr": "tr_convo_"},
    "Coaching_Dojo": {"owner": "sibling", "scn": "scn_coach_", "tr": "tr_coach_"},
}

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def load_json(p):
    with open(p) as f:
        return json.load(f)


def load_yaml(p):
    with open(p) as f:
        return yaml.safe_load(f)


parsed = {}
for d, spec in DOJO_SPECS.items():
    tag = "owned" if spec["owner"] == "owned" else "sibling"
    dpath = os.path.join(BASE, d)
    present = set(os.listdir(dpath)) if os.path.isdir(dpath) else set()
    missing = set(ARTIFACTS) - present
    extra = present - set(ARTIFACTS)
    check(f"[{tag}] {d}: inventory", not missing and not extra,
          f"missing={missing or 'none'}, extra={extra or 'none'}")
    for a in ARTIFACTS:
        p = os.path.join(dpath, a)
        try:
            if a.endswith(".json"):
                parsed[(d, a)] = load_json(p)
            elif a.endswith(".yaml"):
                parsed[(d, a)] = load_yaml(p)
            else:
                with open(p) as f:
                    parsed[(d, a)] = f.read()
            check(f"[{tag}] {d}/{a}: parses", True)
        except Exception as e:
            check(f"[{tag}] {d}/{a}: parses", False, str(e))

STAGE_KEYS = ("entry_conditions", "exit_conditions", "coach_rules_ref")
PERSONA_KEYS = ("id", "name", "role", "context", "stance", "speech_profile",
                "boundary_rules", "sanitization", "provenance")

for d, spec in DOJO_SPECS.items():
    tag = "owned" if spec["owner"] == "owned" else "sibling"
    dsm = parsed[(d, "dialogue_state_machine.json")]
    check(f"[{tag}] {d}: stage structure",
          all(all(k in s for k in STAGE_KEYS) for s in dsm["stages"]))
    check(f"[{tag}] {d}: transition_policy complete",
          all(k in dsm["transition_policy"] for k in
              ("advance_requires", "retreat_requires", "loop_guard", "interrupt_handling")))

    pc = parsed[(d, "persona_config.yaml")]
    personas = pc["personas"]
    check(f"[{tag}] {d}: persona count", len(personas) >= 2, f"got {len(personas)}")
    for p in personas:
        pid = p.get("id")
        check(f"[{tag}] {d}/{pid}: full schema", all(k in p for k in PERSONA_KEYS))
        br = " ".join(p["boundary_rules"]).lower()
        for kw in ("coerc", "sham", "lattice"):
            check(f"[{tag}] {d}/{pid}: boundary '{kw}'", kw in br)
        check(f"[{tag}] {d}/{pid}: provenance evidence flag",
              p["provenance"].get("verified") in ("VERIFIED", "RECONSTRUCTED"))

    rub = parsed[(d, "rubric.json")]
    check(f"[{tag}] {d}: rubric count", len(rub["rubrics"]) >= 2,
          f"got {len(rub['rubrics'])}")
    check(f"[{tag}] {d}: rubrics all lens-type",
          all(r["scoring"]["type"] == "lens" for r in rub["rubrics"]))
    check(f"[{tag}] {d}: rubric_use_rules present", bool(rub.get("rubric_use_rules")))

    inty = parsed[(d, "sparring_intensity_profile.json")]
    check(f"[{tag}] {d}: intensity levels 1-5",
          [l["level"] for l in inty["levels"]] == [1, 2, 3, 4, 5])
    check(f"[{tag}] {d}: intensity policy set",
          all(k in inty for k in ("escalation_policies", "deescalation_rules",
                                  "sycophancy_guard")))

    coach = parsed[(d, "in_session_coaching_rules.md")]
    check(f"[{tag}] {d}: hint-not-answer invariant",
          "hint" in coach.lower() and "answer" in coach.lower())
    check(f"[{tag}] {d}: module separation declared",
          "persona module" in coach and "coach module" in coach)

    debrief = parsed[(d, "debrief_template.md")]
    check(f"[{tag}] {d}: debrief preserved_user_decision section",
          "Preserved User Decision" in debrief)

    tr = parsed[(d, "transfer_scenario_set.md")]
    base_n = len(re.findall(rf"^\| {re.escape(spec['scn'])}", tr, re.M))
    tr_n = len(re.findall(rf"^\| {re.escape(spec['tr'])}", tr, re.M))
    check(f"[{tag}] {d}: base scenarios >= 3", base_n >= 3, f"got {base_n}")
    check(f"[{tag}] {d}: transfer scenarios >= 2", tr_n >= 2, f"got {tr_n}")

    # Owned-specific checks
    if spec["owner"] == "owned":
        check(f"[owned] {d}: stage family exact",
              [s["id"] for s in dsm["stages"]] == spec["stages"])
        gates = [g["id"] for g in dsm["transition_policy"].get("hard_gates", [])]
        for g in spec["gates"]:
            check(f"[owned] {d}: hard gate '{g}'", g in gates)
        check(f"[owned] {d}: no drafting artifacts", "wait," not in json.dumps(dsm))
        for rid, base in spec["extends"].items():
            r = next((x for x in rub["rubrics"] if x["id"] == rid), None)
            check(f"[owned] {d}: {rid} extends {base}",
                  r is not None and r.get("extends", {}).get("base") == base)
        all_dims = [x["id"] for r in rub["rubrics"] for x in r["dimensions"]]
        for dim in spec["dims"]:
            check(f"[owned] {d}: rubric dimension '{dim}'", dim in all_dims)
        for need in spec["stance"]:
            check(f"[owned] {d}: persona stance '{need}'", need in personas[0]["stance"])
        check(f"[owned] {d}: intensity user_agreement required",
              inty.get("user_agreement", {}).get("required") is True)
        if d == "Ambivalence_Dojo":
            check("[owned] Amb: MI spirit gate in coach rules",
                  "spirit gate" in coach.lower())
            check("[owned] Amb: no-premature-closure protocol",
                  "no-premature-closure" in coach.lower())
        if d == "Conflict_Dojo":
            check("[owned] Con: de-escalation-first",
                  "de-escalation-first" in coach.lower()
                  or "deescalation_first" in coach.lower())
            check("[owned] Con: no-shaming gate", "no-shaming gate" in coach.lower())
        if d == "Workplace_Dojo":
            check("[owned] Wk: SBI scaffolding", "sbi" in coach.lower())
            check("[owned] Wk: power-gradient rule", "power-gradient" in coach.lower())
            check("[owned] Wk: fade policy", "scaffolding_fade_rules" in coach)
            check("[owned] Wk: real-conversation boundary",
                  "real-conversation boundary" in coach.lower())
            check("[owned] Wk: intensity mirror guard",
                  "mirror_monitor" in inty.get("sycophancy_guard", {}))

    # Evidence discipline at data level (comments do not count)
    for a in ARTIFACTS:
        content = parsed[(d, a)]
        if isinstance(content, (dict, list)):
            content = json.dumps(content)
        check(f"[{tag}] {d}/{a}: VERIFIED+RECONSTRUCTED data flags",
              "VERIFIED" in content and "RECONSTRUCTED" in content)

print(f"\n{'ALL PASS' if not fails else 'FAILURES'}: "
      f"{len(fails)} failing check(s) across the five dojos "
      f"(owned: Ambivalence + Conflict + Workplace; sibling: Conversation, Coaching)")
sys.exit(1 if fails else 0)
