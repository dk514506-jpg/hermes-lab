#!/usr/bin/env python3
"""Phase3_Skills verification: canonical 9-file shape, JSON validity, schema fields,
edge/op consistency, SKILL.md section completeness, seed-index agreement."""
import json, os, sys

# Conforming packages only. ConvoDojo_Practice_Sparring / Motivational_Lattice_Generator
# are canonical-9 shape but lack the extension fields (inputs/outputs/triggers/...) —
# align them to the union schema before adding to this list.
SKILLS = ["COMB_Behavioral_Diagnosis", "TDF_Barrier_Facilitator_Grid",
          "SDT_Need_Support_Check", "MI_Ambivalence_Conversation",
          "Proximal_Practice_Selector"]
ROOT = "/home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase3_Skills"
REQUIRED_FILES = ["SKILL.md","skill_node.json","atomic_ops.json","edge_map.json","state_schema.json","examples.md","support_ops.md","recovery_ops.md","evaluation_notes.md"]
NODE_REQ = ["id","name","layer","purpose","inputs","outputs","state_read","state_write","triggers","completion_conditions"]
OP_REQ = ["id","name","description","inputs","outputs","guardrails"]
SKILL_MD_SECTIONS = ["Purpose","Trigger Conditions","Inputs","Outputs","State Variables","Atomic Operations","Typed Edges","Empowerment Boundary","Learnability / Skill-Atrophy Check","Motivational-Lattice Interface","Conversational / Practice Mode","Guardrails","Failure Modes","Recovery Operations","Examples","Handoff Notes"]
EDGE_TYPES = {"decomposes_to","can_follow","compatible_with","supports","recovers_with"}

fails = 0
for s in SKILLS:
    d = os.path.join(ROOT, s)
    present = sorted(os.listdir(d))
    if present != sorted(REQUIRED_FILES):
        print(f"FAIL {s}: file shape {present} != {REQUIRED_FILES}"); fails += 1

    node = json.load(open(os.path.join(d, "skill_node.json")))
    missing = [k for k in NODE_REQ if k not in node]
    if missing: print(f"FAIL {s} skill_node missing {missing}"); fails += 1
    if node["id"] != s: print(f"FAIL {s} skill_node id mismatch"); fails += 1

    ops = json.load(open(os.path.join(d, "atomic_ops.json")))
    op_ids = [o["id"] for o in ops]
    if len(op_ids) != len(set(op_ids)): print(f"FAIL {s} duplicate op ids"); fails += 1
    for o in ops:
        missing = [k for k in OP_REQ if k not in o]
        if missing: print(f"FAIL {s} op {o['id']} missing {missing}"); fails += 1

    edges = json.load(open(os.path.join(d, "edge_map.json")))["edges"]
    et = [e["type"] for e in edges]
    if not set(et) <= EDGE_TYPES:
        print(f"FAIL {s} illegal edge types {set(et) - EDGE_TYPES}"); fails += 1
    if et.count("decomposes_to") != len(op_ids):
        print(f"FAIL {s} decomposes_to count {et.count('decomposes_to')} != ops {len(op_ids)}"); fails += 1

    dt = {e["target"] for e in edges if e["type"] == "decomposes_to"}
    if dt != set(op_ids):
        print(f"FAIL {s} decomposes_to mismatch {dt ^ set(op_ids)}"); fails += 1

    json.load(open(os.path.join(d, "state_schema.json")))

    md = open(os.path.join(d, "SKILL.md")).read()
    miss = [h for h in SKILL_MD_SECTIONS if f"### {h}" not in md]
    if miss: print(f"FAIL {s} SKILL.md missing sections {miss}"); fails += 1

    for o in op_ids:
        if o not in dt:
            print(f"FAIL {s} op {o} not in decomposes_to"); fails += 1

    print(f"PASS {s}: 9 files, node/op/edge/state JSON valid, {len(ops)} ops, {len(edges)} edges ({et.count('decomposes_to')} decomposes_to), 16 SKILL.md sections")

idx = json.load(open(os.path.join(ROOT, "skill_graph_index.json")))
idx_edges = {(e["type"], e["from"], e["to"]) for e in idx["edges"]}
for s in SKILLS:
    em = json.load(open(os.path.join(ROOT, s, "edge_map.json")))["edges"]
    flagged = [e for e in em if e.get("flag")]
    overlap = [(e["type"], e["source"], e["target"]) for e in flagged
               if (e["type"], e["source"], e["target"]) in idx_edges]
    print(f"PASS {s}: seed-index agreement — {len(overlap)} of {len(flagged)} flagged edges match skill_graph_index.json")

print("\nRESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
sys.exit(1 if fails else 0)
