#!/usr/bin/env python3
"""Lightweight harness verifier — ships INSIDE the harness tree.

Run: python3 verify/verify_harness.py   (from the harness root, or anywhere —
it self-locates HARNESS_ROOT as the parent of the verify/ dir)

This is the consumer-facing re-verification tool. The full build-time
verifier (council_notes/verify_phase7.py in the Foundation tree) runs the
deep checks (edge-set consistency, quarantine markers, stale-path sweep);
this lightweight version checks what a consumer who edited local files most
needs: inventory integrity, JSON/YAML parse, and graph/README coherence.
Exit 1 on any failure.
"""
import json
import os
import sys

try:
    import yaml
except ImportError:
    yaml = None

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = ["Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis",
          "TDF_Barrier_Facilitator_Grid", "SDT_Need_Support_Check",
          "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
          "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"]
CORE9 = ["SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json",
         "state_schema.json", "examples.md", "support_ops.md",
         "recovery_ops.md", "evaluation_notes.md"]
DOJOS = ["Conversation_Dojo", "Coaching_Dojo", "Ambivalence_Dojo",
         "Conflict_Dojo", "Workplace_Dojo"]
DOJO_7 = ["dialogue_state_machine.json", "persona_config.yaml", "rubric.json",
          "sparring_intensity_profile.json", "in_session_coaching_rules.md",
          "debrief_template.md", "transfer_scenario_set.md"]
GOVERNANCE_5 = ["empowerment_boundary.md", "agent_deference_rules.md",
                "learnability_state_schema.json", "skill_atrophy_risk_check.md",
                "scaffolding_fade_rules.md"]

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def load_json(p):
    with open(p) as f:
        return json.load(f)


# 1. Required root entries
for entry in ["README.md", "skill_graph_index.json", "DEFERRED_PACKAGES.md",
              "skills", "lattices", "routines", "governance", "logs",
              "evidence", "handoff_notes.md", "verify"]:
    check(f"root entry: {entry}", os.path.exists(os.path.join(HARNESS, entry)))

# 2. skills/: 8 packages × 9 core files
for s in SKILLS:
    d = os.path.join(HARNESS, "skills", s)
    present = set(os.listdir(d)) if os.path.isdir(d) else set()
    missing = [f for f in CORE9 if f not in present]
    check(f"skills/{s}: 9 core files", not missing, f"missing={missing or 'none'}")

# 3. JSON/YAML parse across the tree
bad = []
for root, _dirs, files in os.walk(HARNESS):
    if "verify" in root and "verify_harness.py" not in files:
        continue
    for fn in files:
        p = os.path.join(root, fn)
        if fn.endswith(".json"):
            try:
                load_json(p)
            except Exception as e:
                bad.append(f"{os.path.relpath(p, HARNESS)}: {e}")
        elif fn.endswith(".yaml") and yaml is not None:
            try:
                yaml.safe_load(open(p))
            except Exception as e:
                bad.append(f"{os.path.relpath(p, HARNESS)}: {e}")
check("all JSON/YAML parse", not bad, f"bad={bad[:3] or 'none'}")

# 4. Graph index coherence
idx = load_json(os.path.join(HARNESS, "skill_graph_index.json"))
node_ids = {n.get("id") for n in idx.get("skill_nodes", [])}
edges = idx.get("edges", [])
check("graph: edges use source/target", all("source" in e and "target" in e for e in edges))
check("graph: edge endpoints known", all(
    (e.get("source") in node_ids or e.get("source") == "*") and
    (e.get("target") in node_ids or e.get("target") == "*") for e in edges))

# 5. routines/: 5 dojos × 7 artifacts
for d in DOJOS:
    ddir = os.path.join(HARNESS, "routines", d)
    present = set(os.listdir(ddir)) if os.path.isdir(ddir) else set()
    missing = [f for f in DOJO_7 if f not in present]
    check(f"routines/{d}: 7 artifacts", not missing, f"missing={missing or 'none'}")

# 6. governance/: 5 Phase 5 safeguards
gov = set(os.listdir(os.path.join(HARNESS, "governance"))) if os.path.isdir(os.path.join(HARNESS, "governance")) else set()
for f in GOVERNANCE_5:
    check(f"governance/: {f}", f in gov)

# 7. evidence/: 4 files
ev = set(os.listdir(os.path.join(HARNESS, "evidence"))) if os.path.isdir(os.path.join(HARNESS, "evidence")) else set()
for f in ["Recent_Evidence_Digest.md", "Annotated_Bibliography.md",
          "Contrary_Findings_and_Limits.md", "phase2_api_seed.md"]:
    check(f"evidence/: {f}", f in ev)

print()
if fails:
    print(f"{len(fails)} FAILURE(S): {fails}")
    sys.exit(1)
print("HARNESS VERIFIED — exit 0")
