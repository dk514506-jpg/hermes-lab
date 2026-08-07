#!/usr/bin/env python3
"""Verify Phase 3 skill packages: file counts, JSON validity, SKILL.md section coverage."""
import json
import os
import sys

ROOT = "/home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase3_Skills"
SKILLS = [
    "Human_Empowerment_Boundary",
    "COMB_Behavioral_Diagnosis",
    "TDF_Barrier_Facilitator_Grid",
    "SDT_Need_Support_Check",
    "MI_Ambivalence_Conversation",
    "Proximal_Practice_Selector",
    "Motivational_Lattice_Generator",
    "ConvoDojo_Practice_Sparring",
]
REQUIRED_FILES = [
    "SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json",
    "state_schema.json", "examples.md", "support_ops.md", "recovery_ops.md",
    "evaluation_notes.md",
]
REQUIRED_SECTIONS = [
    "Purpose", "Trigger Conditions", "Inputs", "Outputs", "State Variables",
    "Atomic Operations", "Typed Edges", "Empowerment Boundary",
    "Learnability / Skill-Atrophy Check", "Motivational-Lattice Interface",
    "Conversational / Practice Mode", "Guardrails", "Failure Modes",
    "Recovery Operations", "Examples", "Handoff Notes",
]

failures = []
total_files = 0

for skill in SKILLS:
    d = os.path.join(ROOT, skill)
    if not os.path.isdir(d):
        failures.append(f"[{skill}] directory missing")
        continue
    files = os.listdir(d)
    total_files += len(files)
    missing = [f for f in REQUIRED_FILES if f not in files]
    if missing:
        failures.append(f"[{skill}] missing files: {missing}")
    extras = [f for f in files if f not in REQUIRED_FILES and f != "skill_graph_index.json"]
    if extras:
        print(f"[{skill}] extra files: {extras}")

    # JSON validity
    for jf in ["skill_node.json", "atomic_ops.json", "edge_map.json", "state_schema.json"]:
        p = os.path.join(d, jf)
        if os.path.exists(p):
            try:
                data = json.load(open(p))
                if isinstance(data, dict):
                    print(f"[{skill}] {jf}: OK ({len(data)} top-level keys)")
                elif isinstance(data, list):
                    print(f"[{skill}] {jf}: OK (list of {len(data)})")
            except Exception as e:
                failures.append(f"[{skill}] {jf} INVALID JSON: {e}")

    # SKILL.md section coverage
    sp = os.path.join(d, "SKILL.md")
    if os.path.exists(sp):
        text = open(sp).read()
        miss_sec = [s for s in REQUIRED_SECTIONS if s.lower() not in text.lower()]
        if miss_sec:
            failures.append(f"[{skill}] SKILL.md missing sections: {miss_sec}")
        else:
            print(f"[{skill}] SKILL.md: all {len(REQUIRED_SECTIONS)} sections present")

    # edge_map sanity: does it reference real edge types?
    ep = os.path.join(d, "edge_map.json")
    if os.path.exists(ep):
        try:
            em = json.load(open(ep))
            items = em if isinstance(em, list) else em.get("edges", [])
            types = {e.get("type") for e in items} if isinstance(items, list) else set()
            allowed = {"decomposes_to", "can_follow", "compatible_with", "supports", "recovers_with"}
            bad = types - allowed
            if bad:
                failures.append(f"[{skill}] edge_map unknown types: {bad}")
            else:
                print(f"[{skill}] edge_map: {len(items)} edges, types {sorted(types) or 'EMPTY'}")
        except Exception as e:
            failures.append(f"[{skill}] edge_map parse error: {e}")

print(f"\nTotal files on disk: {total_files}")
if failures:
    print("\nFAILURES:")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("\nALL PHASE 3 CHECKS PASSED")
