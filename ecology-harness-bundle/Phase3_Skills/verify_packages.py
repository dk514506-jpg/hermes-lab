#!/usr/bin/env python3
"""Verify Phase3_Skills HiSkill packages: structure, syntax, and consistency.

Checks per package: canonical 9 core files, 16-section SKILL.md standard (plan v2 s8),
JSON/YAML parse, AtomicOps consistency (SKILL.md <-> atomic_ops.json <-> edge_map.json
decomposes_to), edge-endpoint resolution, and agreement with the seed
skill_graph_index.json (edges touching built skills). Exit 1 on any failure.
"""
import json, os, re, sys
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
PACKAGES = ["Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis", "TDF_Barrier_Facilitator_Grid",
            "SDT_Need_Support_Check", "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
            "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"]
CORE9 = ["SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json", "state_schema.json",
         "examples.md", "support_ops.md", "recovery_ops.md", "evaluation_notes.md"]
SECTIONS16 = ["## Purpose", "## Trigger Conditions", "## Inputs", "## Outputs", "## State Variables",
              "## Atomic Operations", "## Typed Edges", "## Empowerment Boundary",
              "## Learnability / Skill-Atrophy Check", "## Motivational-Lattice Interface",
              "## Conversational / Practice Mode", "## Guardrails", "## Failure Modes",
              "## Recovery Operations", "## Examples", "## Handoff Notes"]
PASCAL2SNAKE = {}  # legacy map removed — all skill ids normalized to PascalCase (Phase 4 decision 3)
BUILT = {"Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis", "TDF_Barrier_Facilitator_Grid",
         "SDT_Need_Support_Check", "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
         "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"}
KNOWN_SKILLS = BUILT | {"Material_Arrangement_Scan",
                        "Feedback_Ecology_Map", "Autopoietic_Boundary_Check", "Behavior_Definition_Cell",
                        "Post_Close_Calibration_Debrief"}
norm = lambda v: v


def ops_of(pkg):
    """atomic_ops.json may be a list or a dict with an 'ops' key (Phase 4 schema 0.2)."""
    d = json.load(open(os.path.join(BASE, pkg, "atomic_ops.json")))
    if isinstance(d, dict):
        return d.get("ops", d.get("atomic_ops", []))
    return d

failures = []
def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        failures.append(f"{name}: {detail}")

def edges_of(pkg):
    return json.load(open(os.path.join(BASE, pkg, "edge_map.json")))["edges"]

print("=== 1. JSON PARSE ===")
for p in PACKAGES:
    for f in sorted(os.listdir(os.path.join(BASE, p))):
        if f.endswith(".json"):
            try:
                json.load(open(os.path.join(BASE, p, f)))
                check(f"json {p}/{f}", True)
            except Exception as e:
                check(f"json {p}/{f}", False, str(e))

print("=== 2. YAML PARSE ===")
try:
    yaml.safe_load(open(os.path.join(BASE, "ConvoDojo_Practice_Sparring", "persona_config.yaml")))
    check("yaml persona_config.yaml", True)
except Exception as e:
    check("yaml persona_config.yaml", False, str(e))

print("=== 3. CANONICAL 9-FILE STRUCTURE ===")
for p in PACKAGES:
    missing = [f for f in CORE9 if f not in set(os.listdir(os.path.join(BASE, p)))]
    check(f"core9 {p}", not missing, f"missing {missing}")

print("=== 4. SKILL.md 16-SECTION STANDARD ===")
for p in PACKAGES:
    text = open(os.path.join(BASE, p, "SKILL.md")).read()
    missing = [s for s in SECTIONS16 if s not in text]
    check(f"sections {p}", not missing, f"missing {missing}")

print("=== 5. AtomicOps: SKILL.md <-> atomic_ops.json <-> edge_map.json ===")
for p in PACKAGES:
    ops = [o["id"] for o in ops_of(p)]
    st = open(os.path.join(BASE, p, "SKILL.md")).read()
    check(f"ops-in-skill {p}", all(f"- {o}" in st for o in ops))
    # decomposes_to edges split: op-targeted (must match atomic_ops) vs skill-targeted
    # (valid skill-level refinement edges, e.g. decomposes_to COMB->TDF — Phase 4)
    dt_all = [e for e in edges_of(p) if e["type"] == "decomposes_to"]
    dt_op = [e["target"] for e in dt_all if e["target"] in ops]
    dt_skill = [e["target"] for e in dt_all if e["target"] not in ops]
    check(f"decomp-matches-ops {p}", set(dt_op) == set(ops))
    check(f"decomp-ordered {p}", [e["order"] for e in dt_all if e["target"] in ops] == list(range(1, len(ops) + 1)))
    if dt_skill:
        print(f"  NOTE {p}: skill-level decomposes_to targets (Phase 4): {dt_skill}")

print("=== 6. EDGE ENDPOINT RESOLUTION ===")
for p in PACKAGES:
    self_id = p  # PascalCase == dirname (Phase 4 decision 3)
    ops = {o["id"] for o in ops_of(p)}
    op_names = set()
    for r in ("recovery_ops.md", "support_ops.md"):
        op_names |= set(re.findall(r"^### (.+)$", open(os.path.join(BASE, p, r)).read(), re.M))
    bad = []
    for e in edges_of(p):
        for v in (e["source"], e["target"]):
            if v == "*" or norm(v) == self_id or v in ops or v in op_names or norm(v) in KNOWN_SKILLS:
                continue
            bad.append(v)
    check(f"endpoints {p}", not bad, f"unresolved {set(bad)}")

print("=== 7. SEED INDEX AGREEMENT (edges touching built skills) ===")
seed = json.load(open(os.path.join(BASE, "skill_graph_index.json")))
for e in seed["edges"]:
    f, t, ty = e["source"], e["target"], e["type"]  # Phase 4 decision 1: source/target keys
    if norm(f) not in BUILT and norm(t) not in BUILT:
        print(f"  SKIP  {ty} {f}->{t} (both endpoints unbuilt)")
        continue
    # Phase 4 revision: direction-sensitive for directed edge types (recovers_with,
    # can_follow, decomposes_to); set-equality only for undirected (compatible_with).
    directed = ty in ("recovers_with", "can_follow", "decomposes_to", "supports")
    found = any(
        x["type"] == ty and (
            (norm(x["source"]), norm(x["target"])) == (norm(f), norm(t)) if directed
            else {norm(x["source"]), norm(x["target"])} == {norm(f), norm(t)}
        )
        for p in PACKAGES for x in edges_of(p))
    check(f"seed {ty} {f}->{t}", found, "direction-sensitive" if directed else "direction-blind")

print(f"\n=== RESULT: {len(failures)} failures ===")
for fl in failures:
    print("  FAIL:", fl)
sys.exit(1 if failures else 0)
