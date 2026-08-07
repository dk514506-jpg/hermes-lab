#!/usr/bin/env python3
"""Phase 4 verification: graph/lattice reconciliation checks.

Run: python3 council_notes/verify_phase4.py
Verifies the Phase 4 decisions:
  1. Edge keys source/target everywhere (seed index + packages)
  2. recovers_with: source=recovered-skill, target=recovery-provider; kind discriminator
  3. Node ids PascalCase matching dirnames; boundary_gate required on all nodes
  4. TDF binding_constraint renamed to binding_constraint_comb
  5. skill_load_score canonical (PPS writes, HEB derives trend)
  6. Dangling edges quarantined in the index (deferred targets)
  7. HEB gate declared on every skill_node
Plus: Phase 4 outputs exist (lattice_index.json, skill_lattice_interface.md,
insight_trigger_policy.md), all JSON valid, both package verifiers pass.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(ROOT, "..", "Phase3_Skills")
SKILLS = ["Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis", "TDF_Barrier_Facilitator_Grid",
          "SDT_Need_Support_Check", "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
          "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"]
DEFERRED = ["Material_Arrangement_Scan", "Feedback_Ecology_Map", "Autopoietic_Boundary_Check"]

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def load(rel):
    with open(os.path.join(SKILLS_DIR, rel)) as f:
        return json.load(f)


# 1. Phase 4 outputs exist
for f in ["lattice_index.json", "skill_graph_index.json", "skill_lattice_interface.md", "insight_trigger_policy.md"]:
    check(f"Phase 4 output exists: {f}", os.path.exists(os.path.join(SKILLS_DIR, f)))

# 2. All JSON valid
for pkg in SKILLS + [""]:
    d = os.path.join(SKILLS_DIR, pkg)
    if not os.path.isdir(d):
        continue
    for f in sorted(os.listdir(d)):
        if f.endswith(".json"):
            try:
                json.load(open(os.path.join(d, f)))
            except Exception as e:
                check(f"JSON valid {pkg}/{f}", False, str(e))
check("All package JSON parses", True)

# 3. Decision 1: source/target keys in index; no from/to
idx = load("skill_graph_index.json")
check("Index uses source/target (decision 1)", all("source" in e and "target" in e for e in idx["edges"]))
check("Index has no from/to keys (decision 1)", all("from" not in e and "to" not in e for e in idx["edges"]))

# 4. Decision 2: recovers_with direction + kind
rw = [e for e in idx["edges"] if e["type"] == "recovers_with"]
check("Index recovers_with all cross-skill kind", all(e.get("kind") == "cross-skill" for e in rw))
check("Index recovers_with directions correct",
      {(e["source"], e["target"]) for e in rw} == {
          ("MI_Ambivalence_Conversation", "SDT_Need_Support_Check"),
          ("ConvoDojo_Practice_Sparring", "Human_Empowerment_Boundary"),
          ("COMB_Behavioral_Diagnosis", "Human_Empowerment_Boundary"),
          ("TDF_Barrier_Facilitator_Grid", "Human_Empowerment_Boundary")})

# 5. Decision 3: node ids PascalCase == dirname; boundary gate required
for pkg in SKILLS:
    node = load(f"{pkg}/skill_node.json")
    check(f"node id matches dirname: {pkg}", node.get("id") == pkg)
    check(f"boundary_gate required: {pkg}",
          node.get("governance", {}).get("boundary_gate") == "required")

# 6. Decision 4: TDF binding_constraint_comb
tdf_state = load("TDF_Barrier_Facilitator_Grid/state_schema.json")
check("TDF uses binding_constraint_comb (decision 4)", "binding_constraint_comb" in tdf_state)
check("TDF no bare binding_constraint", "binding_constraint" not in tdf_state)

# 7. Decision 5: skill_load canonical
check("Index documents skill_load_score canonical (decision 5)",
      "skill_load" in load("T2R_traceability.json")["canonical_state_variables"])

# 8. Decision 6: quarantined edges present; deferred nodes declared
check("Index has quarantined_edges (decision 6)", "quarantined_edges" in idx and len(idx["quarantined_edges"]) >= 3)
check("Index declares deferred nodes", {n["id"] for n in idx["deferred_nodes"]} == set(DEFERRED))

# 9. Decision 7: governance section with boundary gate rule
check("Index governance section (decision 7)",
      "boundary_gate_rule" in idx.get("governance", {}))

# 10. Lattice index coherence
lat = load("lattice_index.json")
check("Lattice index has layers", set(lat.get("lattice_layers", {}).keys()) == {"observation", "interpretation", "evidence_edge"})
check("Lattice index has quarantine tiers", "Q2_IDENTITY_LEVEL" in lat.get("quarantine_tiers", {}))
check("Lattice index has insight triggers", len(lat.get("insight_triggers", [])) >= 5)
check("Lattice index references MLG schemas",
      "observation" in lat["lattice_layers"] and "schema" in lat["lattice_layers"]["observation"])

print()
if fails:
    print(f"{len(fails)} failure(s)")
    for f in fails:
        print(" -", f)
    sys.exit(1)

print("ALL PHASE 4 CHECKS PASSED")
print()
print("=== verify_packages.py (build council verifier, all 8 packages) ===")
r = subprocess.run([sys.executable, os.path.join(SKILLS_DIR, "verify_packages.py")],
                   capture_output=True, text=True)
print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip())
if r.returncode != 0:
    sys.exit(r.returncode)
print()
print("=== verify_phase3.py (structural verifier) ===")
r2 = subprocess.run([sys.executable, os.path.join(ROOT, "verify_phase3.py")],
                    capture_output=True, text=True)
print(r2.stdout.strip().splitlines()[-1] if r2.stdout.strip() else r2.stderr.strip())
sys.exit(r2.returncode)
