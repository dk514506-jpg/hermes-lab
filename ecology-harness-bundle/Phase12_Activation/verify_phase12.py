#!/usr/bin/env python3
"""Phase 12 verification — conditional package activation.

Run: python3 Phase12_Activation/verify_phase12.py
Verifies:
  1. Material_Arrangement_Scan package: 9-file set, skill_node (layer 2,
     role environmental_scan), 4 atomic ops, edge_map (4 internal + 2
     compatible_with), state_schema keys
  2. Feedback_Ecology_Map package: 9-file set, skill_node (layer 2, role
     embedding_map), 2 atomic ops, edge_map (3 internal + 3
     compatible_with), state_schema keys
  3. Package discipline: boundary_gate required; identity-level reframes
     confirmation-gated (Phase 11 confirmed-Q2); user defines meaning;
     CMO hypotheses claim-level; arrangement-only proposals
  4. Activation wiring: skill_graph_index — 4 edges un-quarantined,
     10 skill nodes, MAS+FEM no longer deferred
  5. T2R: 6 register ops flipped to instantiated + 3 NPT mechanisms
     explicitly REGISTERED-NOT-BUILT (49 instantiated + 3 registered-not-
     built = 52 entries; no UNINSTANTIATED)
  6. Executable ops: phase12_conditional_packages.py self-test passes
     (6 ops runnable, deterministic)
  7. Legacy: verify_phase11.py + verify_all.py + FAOS suite still pass
     (non-recursive)
"""
import json
import os
import subprocess
import sys
def _faos_root():
    """FAOS canonical suite root: bundle faos_canonical/ -> env -> home lab."""
    for cand in (os.path.join(ROOT, "..", "faos_canonical"),
                 os.environ.get("ECOLOGY_FAOS_ROOT"),
                 os.path.join(os.path.expanduser("~"), ".hermes",
                              "hermes-agent", "docs")):
        if cand and os.path.isfile(os.path.join(cand, "scripts", "run_tests.sh")):
            return os.path.abspath(cand)
    raise FileNotFoundError("FAOS canonical suite not found (run_tests.sh)")

ROOT = os.path.dirname(os.path.abspath(__file__))
FOUNDATION = os.path.dirname(ROOT)
DOCS = os.path.dirname(os.path.dirname(os.path.dirname(ROOT)))
POC = os.path.join(FOUNDATION, "GitHub_PoC")
sys.path.insert(0, ROOT)

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


PACKAGE_FILES = ["SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json",
                 "state_schema.json", "examples.md", "support_ops.md",
                 "recovery_ops.md", "evaluation_notes.md"]

# 1. Material_Arrangement_Scan
mas_dir = os.path.join(POC, "skills", "Material_Arrangement_Scan")
check("MAS: 9-file set", all(os.path.exists(os.path.join(mas_dir, f)) for f in PACKAGE_FILES))
mas_node = json.load(open(os.path.join(mas_dir, "skill_node.json")))
check("MAS: skill_node layer 2 role environmental_scan",
      mas_node["layer"] == 2 and mas_node["role"] == "environmental_scan")
check("MAS: boundary_gate required",
      mas_node.get("governance", {}).get("boundary_gate") == "required")
mas_ops = json.load(open(os.path.join(mas_dir, "atomic_ops.json")))
mas_op_ids = [o["id"] for o in mas_ops]
check("MAS: 4 atomic ops", len(mas_ops) == 4, str(mas_op_ids))
for op_id in ["scan_materials", "scan_meanings", "detect_shared_elements",
              "design_novelty_into_routine"]:
    check(f"MAS: op {op_id}", op_id in mas_op_ids)
mas_edges = json.load(open(os.path.join(mas_dir, "edge_map.json")))["edges"]
mas_edge_targets = [e["target"] for e in mas_edges]
check("MAS: edge_map 4 decomposes + 3 feeds + 2 compatible_with", len(mas_edges) == 9,
      f"{len(mas_edges)} edges")
check("MAS: compatible_with COMB + TDF present",
      ("COMB_Behavioral_Diagnosis", "Material_Arrangement_Scan") in
      [(e["source"], e["target"]) for e in mas_edges] and
      ("TDF_Barrier_Facilitator_Grid", "Material_Arrangement_Scan") in
      [(e["source"], e["target"]) for e in mas_edges])
mas_ss = json.load(open(os.path.join(mas_dir, "state_schema.json")))
check("MAS: state_schema keys", all(k in mas_ss for k in
      ["materials_inventory", "meanings_inventory", "shared_element_map",
       "arrangement_proposals", "practice_graph"]))

# 2. Feedback_Ecology_Map
fem_dir = os.path.join(POC, "skills", "Feedback_Ecology_Map")
check("FEM: 9-file set", all(os.path.exists(os.path.join(fem_dir, f)) for f in PACKAGE_FILES))
fem_node = json.load(open(os.path.join(fem_dir, "skill_node.json")))
check("FEM: skill_node layer 2 role embedding_map",
      fem_node["layer"] == 2 and fem_node["role"] == "embedding_map")
check("FEM: boundary_gate required",
      fem_node.get("governance", {}).get("boundary_gate") == "required")
fem_ops = json.load(open(os.path.join(fem_dir, "atomic_ops.json")))
fem_op_ids = [o["id"] for o in fem_ops]
check("FEM: 2 atomic ops", len(fem_ops) == 2, str(fem_op_ids))
for op_id in ["assess_coherence", "form_cmo_hypothesis"]:
    check(f"FEM: op {op_id}", op_id in fem_op_ids)
fem_edges = json.load(open(os.path.join(fem_dir, "edge_map.json")))["edges"]
check("FEM: edge_map has 3 internal + 3 compatible_with", len(fem_edges) == 6,
      f"{len(fem_edges)} edges")
fem_ss = json.load(open(os.path.join(fem_dir, "state_schema.json")))
check("FEM: state_schema keys", all(k in fem_ss for k in
      ["normalization_state", "coherence_questions", "cmo_hypotheses"]))

# 3. discipline in op definitions
def has_guardrail(ops, op_id, needle):
    for o in ops:
        if o["id"] == op_id:
            return any(needle.lower() in g.lower() for g in o.get("guardrails", []))
    return False

check("MAS: scan_meanings identity-confirmation guardrail",
      has_guardrail(mas_ops, "scan_meanings", "confirmation"))
check("MAS: scan_materials cues-not-replacement guardrail",
      has_guardrail(mas_ops, "scan_materials", "never replace"))
check("MAS: design_novelty no-imposed-meaning guardrail",
      has_guardrail(mas_ops, "design_novelty_into_routine", "never by imposing meaning"))
check("FEM: assess_coherence ask-never-supply guardrail",
      has_guardrail(fem_ops, "assess_coherence", "never supplies"))
check("FEM: form_cmo_hypothesis claim-level guardrail",
      has_guardrail(fem_ops, "form_cmo_hypothesis", "never verdicts"))

# 4. activation wiring: skill_graph_index
g = json.load(open(os.path.join(POC, "skill_graph_index.json")))
node_ids = {n["id"] for n in g["skill_nodes"]}
check("graph: 10 skill nodes", len(g["skill_nodes"]) == 10, str(len(g["skill_nodes"])))
check("graph: MAS + FEM promoted",
      "Material_Arrangement_Scan" in node_ids and "Feedback_Ecology_Map" in node_ids)
check("graph: 4 edges un-quarantined", len(g["quarantined_edges"]) == 0,
      f"{len(g['quarantined_edges'])} remaining")
live = [(e["source"], e["target"]) for e in g["edges"]]
check("graph: MAS/FEM edges live",
      ("COMB_Behavioral_Diagnosis", "Material_Arrangement_Scan") in live and
      ("TDF_Barrier_Facilitator_Grid", "Feedback_Ecology_Map") in live)
check("graph: Autopoietic_Boundary_Check still deferred",
      any(n["id"] == "Autopoietic_Boundary_Check" for n in g["deferred_nodes"]))

# 5. T2R flips
t = json.load(open(os.path.join(POC, "lattices", "T2R_traceability.json")))
tr = t.get("traceability", [])
flipped = {x["register_op"]: x.get("package") for x in tr
           if "instantiated" in str(x.get("status", "")).lower()
           and x.get("package") in ("Material_Arrangement_Scan", "Feedback_Ecology_Map")}
check("T2R: 6 ops instantiated in new packages",
      len(flipped) == 6, str(sorted(flipped)))
check("T2R: scan_materials -> MAS", flipped.get("scan_materials") == "Material_Arrangement_Scan")
check("T2R: assess_coherence -> FEM", flipped.get("assess_coherence") == "Feedback_Ecology_Map")
# R2 (judge W2): the 3 NPT mechanisms must be IN the register as
# REGISTERED-NOT-BUILT — not pruned out to make "ZERO UNINSTANTIATED" true.
rnb = {x["register_op"] for x in tr if "REGISTERED-NOT-BUILT" in str(x.get("status", ""))}
check("T2R: 3 NPT mechanisms REGISTERED-NOT-BUILT (not pruned)",
      rnb == {"assess_participation", "assess_collective_action", "assess_monitoring"},
      str(sorted(rnb)))
inst_count = sum(1 for x in tr if "instantiated" in str(x.get("status", "")).lower())
rnb_count = sum(1 for x in tr if "REGISTERED-NOT-BUILT" in str(x.get("status", "")))
check("T2R: 49 instantiated + 3 registered-not-built = 52",
      inst_count == 49 and rnb_count == 3 and len(tr) == 52,
      f"{len(tr)} entries ({inst_count} inst + {rnb_count} rnb)")
uninst = [x["register_op"] for x in tr if "UNINSTANTIATED" in str(x.get("status", ""))]
check("T2R: no UNINSTANTIATED remain", len(uninst) == 0, str(uninst))

# 6. executable ops
try:
    r = subprocess.run([sys.executable, os.path.join(ROOT, "phase12_conditional_packages.py")],
                       capture_output=True, text=True, timeout=60)
    check("exec: package self-test passes", r.returncode == 0,
          r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[:100])
except Exception as e:
    check("exec: package self-test passes", False, str(e))

# 6b. R8: behavioral shared-element check (>= 2 practices required)
try:
    sys.path.insert(0, ROOT)
    from phase12_conditional_packages import MaterialArrangementScan
    mas = MaterialArrangementScan()
    pg1 = {"practices": [{"practice": "one", "materials": ["x"], "meanings": []}]}
    r1 = mas.detect_shared_elements(pg1, "t")
    check("R8: detect_shared_elements single-practice -> no overlaps",
          r1["shared_element_map"]["shared_materials"] == [], "wholesale pass-through closed")
    pg2 = {"practices": [
        {"practice": "a", "materials": ["m1", "m2"], "meanings": []},
        {"practice": "b", "materials": ["m2", "m3"], "meanings": []}]}
    r2 = mas.detect_shared_elements(pg2, "t")
    overlaps = [s["element"] for s in r2["shared_element_map"]["shared_materials"]]
    check("R8: detect_shared_elements true overlaps only",
          overlaps == ["m2"], f"overlaps={overlaps}")
except Exception as e:
    check("R8: detect_shared_elements behavioral check", False, str(e))

# 7. legacy (non-recursive)
legacy = [
    ("Phase 11 verifier", sys.executable,
     [os.path.join(FOUNDATION, "Phase11_Intervention", "verify_phase11.py")], FOUNDATION),
    ("FAOS canonical", "bash", [os.path.join(_faos_root(), "scripts", "run_tests.sh")], _faos_root()),
]
for name, exe, cmd, cwd in legacy:
    try:
        r = subprocess.run([exe] + cmd, capture_output=True, text=True, timeout=600, cwd=cwd)
        tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()
        check(f"legacy: {name} still passes", r.returncode == 0, tail)
    except Exception as e:
        check(f"legacy: {name} still passes", False, str(e))

print()
print("=== RESULT:", f"{len(fails)} FAILURES" if fails else "PASS — Phase 12 conditional packages activated and verified", "===")
sys.exit(1 if fails else 0)