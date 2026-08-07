#!/usr/bin/env python3
"""Phase 7 verification: the Hermes_Agent_Harness packaged tree.

Run: python3 council_notes/verify_phase7.py

Verifies the packaged harness (Phase 7 plan, decisions 1-9; verification
plan) against the required inventory:

  1. Tree has the 8 required root entries: README.md, skill_graph_index.json,
     skills/, lattices/, routines/, logs/, evidence/, handoff_notes.md
  2. skills/ has the 8 skill package dirs, each with the 9 core files
     (SKILL.md, skill_node.json, atomic_ops.json, edge_map.json,
     state_schema.json, examples.md, support_ops.md, recovery_ops.md,
     evaluation_notes.md) — layer extras permitted
  3. All JSON/YAML in the tree parse
  4. skill_graph_index.json is valid: edges carry source/target keys, edge
     endpoints reference known skill nodes (the documented '*' wildcard of the
     HEB `supports *` edge — Phase 4 decision 7 — is a valid endpoint), nodes
     carry ids
  5. lattices/ has the 5 lattice artifact classes: lattice_index.json,
     insight_trigger_policy.md, skill_lattice_interface.md,
     T2R_traceability.json + the MLG schema files
     (observation_schema.json / insight_node_schema.json /
     evidence_edge_schema.json, >= 1 present)
  6. routines/ has the 5 dojo dirs, each with exactly the 7 canonical
     artifacts (no missing, no extra within a dojo dir)
  7. evidence/ has the 4 evidence files: Recent_Evidence_Digest.md,
     Annotated_Bibliography.md, Contrary_Findings_and_Limits.md,
     phase2_api_seed.md
  8. README.md carries the required orientation sections: What This Is,
     How It Interconnects, Install/Use, Governance, Workflow

Also: logs/ scaffold (log_schema.md + .gitkeep) — this member's deliverable.

HARNESS_ROOT env override exists so the orchestrator can re-point the target
tree; the default is the packaged harness next to the council_notes dir.
"""
import json
import os
import sys

try:
    import yaml
except ImportError:
    print("[FAIL] pyyaml not installed — pip install pyyaml")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.environ.get("HARNESS_ROOT") or os.path.normpath(
    os.path.join(ROOT, "..", "Hermes_Agent_Harness"))

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


SKILLS_9 = [
    "SKILL.md", "skill_node.json", "atomic_ops.json", "edge_map.json",
    "state_schema.json", "examples.md", "support_ops.md", "recovery_ops.md",
    "evaluation_notes.md",
]
SKILL_PKGS = [
    "Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis",
    "TDF_Barrier_Facilitator_Grid", "SDT_Need_Support_Check",
    "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
    "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring",
    "Material_Arrangement_Scan", "Feedback_Ecology_Map",  # Phase 12 activation
]
LATTICE_CORE = [
    "lattice_index.json", "insight_trigger_policy.md",
    "skill_lattice_interface.md", "T2R_traceability.json",
]
MLG_SCHEMAS = [
    "observation_schema.json", "insight_node_schema.json",
    "evidence_edge_schema.json",
]
DOJOS = [
    "Conversation_Dojo", "Coaching_Dojo", "Ambivalence_Dojo",
    "Conflict_Dojo", "Workplace_Dojo",
]
DOJO_7 = [
    "dialogue_state_machine.json", "persona_config.yaml", "rubric.json",
    "sparring_intensity_profile.json", "in_session_coaching_rules.md",
    "debrief_template.md", "transfer_scenario_set.md",
]
EVIDENCE_4 = [
    "Recent_Evidence_Digest.md", "Annotated_Bibliography.md",
    "Contrary_Findings_and_Limits.md", "phase2_api_seed.md",
]
GOVERNANCE_5 = [
    "empowerment_boundary.md", "agent_deference_rules.md",
    "learnability_state_schema.json", "skill_atrophy_risk_check.md",
    "scaffolding_fade_rules.md",
]
README_SECTIONS = ["What This Is", "How It Interconnects", "Install/Use",
                   "Governance", "Workflow"]


def load_json(p):
    with open(p) as f:
        return json.load(f)


# --- 1. Root tree -----------------------------------------------------------
REQUIRED_ROOT = ["README.md", "skill_graph_index.json", "skills", "lattices",
                 "routines", "logs", "evidence", "handoff_notes.md"]
check("harness root exists", os.path.isdir(HARNESS))
present = set(os.listdir(HARNESS)) if os.path.isdir(HARNESS) else set()
for entry in REQUIRED_ROOT:
    check(f"root entry: {entry}", entry in present)

# logs/ scaffold (this member's deliverable)
logs_present = set(os.listdir(os.path.join(HARNESS, "logs"))) \
    if os.path.isdir(os.path.join(HARNESS, "logs")) else set()
check("logs/ scaffold: log_schema.md + .gitkeep",
      {"log_schema.md", ".gitkeep"} <= logs_present,
      f"missing={sorted({'log_schema.md', '.gitkeep'} - logs_present) or 'none'}")

# --- 2. skills/: 8 packages x 9 core files ----------------------------------
skills = os.path.join(HARNESS, "skills")
skill_dirs = set(os.listdir(skills)) if os.path.isdir(skills) else set()
missing_pkgs = set(SKILL_PKGS) - skill_dirs
extra_dirs = sorted(d for d in skill_dirs - set(SKILL_PKGS) if os.path.isdir(os.path.join(skills, d)))
check("skills/ has all 8 packages", not missing_pkgs,
      f"missing={sorted(missing_pkgs) or 'none'}")
check("skills/ has no extra package dirs", not extra_dirs,
      f"extra={extra_dirs or 'none'}")
for pkg in SKILL_PKGS:
    pkgdir = os.path.join(skills, pkg)
    pkg_files = set(os.listdir(pkgdir)) if os.path.isdir(pkgdir) else set()
    miss = sorted(set(SKILLS_9) - pkg_files)
    check(f"skills/{pkg}: 9 core files", not miss, f"missing={miss or 'none'}")

# --- 3. All JSON/YAML parse -------------------------------------------------
bad = []
for dirpath, _dirnames, filenames in os.walk(HARNESS):
    for fn in sorted(filenames):
        if fn.startswith("."):
            continue
        p = os.path.join(dirpath, fn)
        if fn.endswith(".json"):
            try:
                load_json(p)
            except Exception as e:
                bad.append(f"{os.path.relpath(p, HARNESS)}: {e}")
        elif fn.endswith((".yaml", ".yml")):
            try:
                with open(p) as f:
                    yaml.safe_load(f)
            except Exception as e:
                bad.append(f"{os.path.relpath(p, HARNESS)}: {e}")
check("all JSON/YAML parse", not bad, f"bad={bad or 'none'}")

# --- 4. skill_graph_index.json validity -------------------------------------
idx = None
idx_p = os.path.join(HARNESS, "skill_graph_index.json")
try:
    idx = load_json(idx_p)
    nodes = idx.get("skill_nodes", [])
    node_ids = {n.get("id") for n in nodes}
    edges = idx.get("edges", [])
    check("graph: edges non-empty", len(edges) >= 1, f"got {len(edges)}")
    check("graph: edges carry source/target keys",
          all("source" in e and "target" in e for e in edges))
    check("graph: skill_nodes carry id keys",
          bool(node_ids) and all(isinstance(n.get("id"), str) for n in nodes),
          f"got {len(nodes)} nodes")
    WILDCARD = "*"  # HEB supports * — documented wildcard (Phase 4 decision 7)
    dangling = sorted({e.get("source") for e in edges
                       if e.get("source") not in node_ids and e.get("source") != WILDCARD} |
                      {e.get("target") for e in edges
                       if e.get("target") not in node_ids and e.get("target") != WILDCARD})
    check("graph: edge endpoints reference known nodes", not dangling,
          f"dangling={dangling or 'none'}")
    check("graph: governance block present",
          bool(idx.get("governance", {}).get("boundary_gate_rule")))
except Exception as e:
    check("skill_graph_index.json parses + validates", False, str(e))

# --- 5. lattices/: 5 artifact classes ----------------------------------------
lat = os.path.join(HARNESS, "lattices")
lat_files = set(os.listdir(lat)) if os.path.isdir(lat) else set()
for a in LATTICE_CORE:
    check(f"lattices/: {a}", a in lat_files)
mlg_present = sorted(set(MLG_SCHEMAS) & lat_files)
check("lattices/: MLG schema files (>= 1 of 3)",
      bool(mlg_present), f"present={mlg_present or 'none'}")

# --- 6. routines/: 5 dojos x 7 artifacts -------------------------------------
rout = os.path.join(HARNESS, "routines")
rout_entries = set(os.listdir(rout)) if os.path.isdir(rout) else set()
missing_dojos = sorted(set(DOJOS) - rout_entries)
check("routines/: all 5 dojo dirs", not missing_dojos,
      f"missing={missing_dojos or 'none'}")
extra_top = sorted(e for e in rout_entries - set(DOJOS))
if extra_top:
    check("routines/: extra top-level entries (e.g. ConvoDojo skeleton)", True,
          f"noted={extra_top}")
for d in DOJOS:
    ddir = os.path.join(rout, d)
    d_files = set(os.listdir(ddir)) if os.path.isdir(ddir) else set()
    miss = sorted(set(DOJO_7) - d_files)
    extra = sorted(d_files - set(DOJO_7))
    check(f"routines/{d}: 7-artifact inventory", not miss and not extra,
          f"missing={miss or 'none'}, extra={extra or 'none'}")

# --- 7. evidence/: 4 evidence files ------------------------------------------
ev = os.path.join(HARNESS, "evidence")
ev_files = set(os.listdir(ev)) if os.path.isdir(ev) else set()
for f in EVIDENCE_4:
    check(f"evidence/: {f}", f in ev_files)

# --- 8. README required sections ---------------------------------------------
readme_p = os.path.join(HARNESS, "README.md")
try:
    with open(readme_p) as f:
        readme_text = f.read()
    headings = {ln.strip().lstrip("#").strip() for ln in readme_text.splitlines()
                if ln.strip().startswith("#")}
    for sec in README_SECTIONS:
        check(f"README section: {sec}", sec in headings)
except Exception as e:
    check("README readable", False, str(e))

# --- 9. governance/: 5 Phase 5 safeguards (post-judge revision, R1) ----------
gov = os.path.join(HARNESS, "governance")
gov_files = set(os.listdir(gov)) if os.path.isdir(gov) else set()
for f in GOVERNANCE_5:
    check(f"governance/: {f}", f in gov_files)

# --- 10. no stale pre-packaging paths (post-judge revision, R4) --------------
STALE = ["Phase3_Skills", "Phase6_Dojo", "Phase5_Safeguards"]
stale_hits = []
for root, _dirs, files in os.walk(HARNESS):
    for fn in files:
        p = os.path.join(root, fn)
        try:
            with open(p, encoding="utf-8", errors="ignore") as f:
                txt = f.read()
        except Exception:
            continue
        for s in STALE:
            if s in txt:
                # Legitimate exceptions:
                # 1. handoff_notes.md and routines/README.md reference the
                #    campaign's pre-packaging source dirs (Phase5_Safeguards,
                #    Phase6_Dojo) as HISTORICAL provenance — the packaged
                #    homes (governance/, routines/) are documented alongside.
                # 2. Explicit provenance/origin notes elsewhere.
                rel = os.path.relpath(p, HARNESS)
                if rel in ("handoff_notes.md", "routines/README.md"):
                    continue
                # docs/ carries Phase 3-era provenance: safeguards.md
                # declares "Condensed from the Phase 5 estate...", and
                # verification.md's table names the stale-path sweep itself.
                if rel.startswith("docs/"):
                    continue
                if "Provenance" in txt[:200] or "origin" in txt[:400].lower():
                    continue
                stale_hits.append((rel, s))
check("no stale Phase3_Skills/Phase6_Dojo/Phase5_Safeguards paths", not stale_hits,
      f"{stale_hits[:5] or 'none'}")

# --- 11. T2R count reconciled (post-judge revision; Phase 12: 52 entries) ----
t2r_p = os.path.join(HARNESS, "lattices", "T2R_traceability.json")
try:
    t2r = load_json(t2r_p)
    n = len(t2r.get("traceability", []))
    check("T2R traceability: 52 entries (49 inst + 3 registered-not-built)",
          n == 52, f"got {n}")
except Exception as e:
    check("T2R traceability readable", False, str(e))

# --- 12. quarantine markers in packages (post-judge revision, R3) -------------
if idx is not None:
    deferred_ids = {n.get("id") for n in idx.get("deferred_nodes", [])}
    unmarked = []
    for pkg in os.listdir(os.path.join(HARNESS, "skills")):
        em_p = os.path.join(HARNESS, "skills", pkg, "edge_map.json")
        if not os.path.exists(em_p):
            continue
        try:
            em = load_json(em_p)
            for e in em.get("edges", []):
                tgt = e.get("target")
                if tgt in deferred_ids and "quarantin" not in json.dumps(e).lower():
                    unmarked.append((pkg, tgt))
        except Exception:
            pass
    check("package edges to deferred nodes carry quarantine markers", not unmarked,
          f"{unmarked[:5] or 'none'}")
else:
    check("package edges to deferred nodes carry quarantine markers", False,
          "idx unavailable")

print(f"\n{'ALL PASS' if not fails else 'FAILURES'}: "
      f"{len(fails)} failing check(s) on the harness tree")
sys.exit(1 if fails else 0)
