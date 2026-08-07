#!/usr/bin/env python3
"""Post-critique revision verification for Ecology Phase 3.

Covers the files changed in the 2026-08-06 critique round:
  ConvoDojo_Practice_Sparring/atomic_ops.json
  Human_Empowerment_Boundary/state_schema.json
  T2R_traceability.json
  skill_graph_index.json
  COMB_Behavioral_Diagnosis/edge_map.json
  TDF_Barrier_Facilitator_Grid/edge_map.json
  MI_Ambivalence_Conversation/atomic_ops.json

Run: python3 council_notes/verify_critique_revisions.py
Also invokes the structural verifier (verify_phase3.py) at the end.
"""
import json
import os
import subprocess
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "Phase3_Skills")
fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def load(rel):
    with open(os.path.join(BASE, rel)) as f:
        return json.load(f)


# 1. ConvoDojo atomic_ops.json — guardrails on every op + safety op
d = load("ConvoDojo_Practice_Sparring/atomic_ops.json")
ops = d["ops"]
check("ConvoDojo: 13 ops", len(ops) == 13, f"got {len(ops)}")
check("ConvoDojo: every op has inputs/outputs/guardrails",
      all(o.get("inputs") and o.get("outputs") and o.get("guardrails") for o in ops))
safety = [o for o in ops if o["id"] == "check_psychological_safety"]
check("ConvoDojo: check_psychological_safety present", len(safety) == 1)
check("ConvoDojo: safety op reads sycophancy_risk",
      safety and "sycophancy_risk" in json.dumps(safety[0].get("inputs", {})))

# 2. HEB state_schema.json — skill_load_trend documented as derived
d = load("Human_Empowerment_Boundary/state_schema.json")
check("HEB: skill_load_trend exists", "skill_load_trend" in d)
check("HEB: trend note references skill_load_score",
      "skill_load_score" in d["skill_load_trend"].get("note", ""))

# 3. T2R_traceability.json — 48 entries reconcile, canonical vars, conventions
d = load("T2R_traceability.json")
tr = d["traceability"]
inst = sum(1 for t in tr if t["status"].startswith("instantiated"))
uninst = sum(1 for t in tr if t["status"].startswith("UNINSTANTIATED"))
partial = len(tr) - inst - uninst
check("T2R: 48 entries", len(tr) == 48, f"got {len(tr)}")
check("T2R: counts reconcile (39+9+0)", (inst, uninst, partial) == (39, 9, 0),
      f"inst={inst} uninst={uninst} partial={partial}")
check("T2R: all entries well-formed",
      all(all(k in t for k in ("register_op", "package_op", "package", "status")) for t in tr))
check("T2R: canonical_state_variables",
      "skill_load" in d["canonical_state_variables"] and "binding_constraint" in d["canonical_state_variables"])
check("T2R: edge_conventions.recovers_with", "recovers_with" in d["edge_conventions"])

# 4. skill_graph_index.json — reconciled flagship edge + resolved conventions (Phase 4)
d = load("skill_graph_index.json")
comb_tdf = [e for e in d["edges"]
            if e.get("source") == "COMB_Behavioral_Diagnosis" and e.get("target") == "TDF_Barrier_Facilitator_Grid"]
check("Index: decomposes_to COMB->TDF present (source/target keys, Phase 4)",
      len(comb_tdf) == 1 and comb_tdf[0]["type"] == "decomposes_to")
check("Index: RECONCILED note on flagship edge",
      comb_tdf and "RECONCILED" in comb_tdf[0].get("note", ""))
rw_edges = [e for e in d["edges"] if e.get("type") == "recovers_with"]
check("Index: recovers_with convention RESOLVED (0 pending notes, Phase 4 decision 2)",
      all("DIRECTION CONVENTION PENDING" not in e.get("note", "") for e in rw_edges),
      f"{len(rw_edges)} recovers_with edges, all direction-normalized")
check("Index: recovers_with edges carry kind=cross-skill (Phase 4)",
      all(e.get("kind") == "cross-skill" for e in rw_edges))

# 5. COMB/TDF edge maps — direction reconciled
comb = load("COMB_Behavioral_Diagnosis/edge_map.json")
comb_edges = comb["edges"] if isinstance(comb, dict) else comb
check("COMB map: decomposes_to COMB->TDF",
      any(e.get("type") == "decomposes_to" and e.get("target") == "TDF_Barrier_Facilitator_Grid" for e in comb_edges))
tdf = load("TDF_Barrier_Facilitator_Grid/edge_map.json")
tdf_edges = tdf["edges"] if isinstance(tdf, dict) else tdf
check("TDF map: supports TDF->COMB removed",
      not any(e.get("type") == "supports" and e.get("target") == "COMB_Behavioral_Diagnosis" for e in tdf_edges))
check("TDF map: can_follow TDF->COMB reverse pass kept",
      any(e.get("type") == "can_follow" and e.get("target") == "COMB_Behavioral_Diagnosis" for e in tdf_edges))

# 6. MI atomic_ops.json — Focusing ops added
mi = load("MI_Ambivalence_Conversation/atomic_ops.json")
mi_ops = mi["ops"] if isinstance(mi, dict) and "ops" in mi else mi
mi_ids = [o["id"] for o in mi_ops]
check("MI: agree_direction + prioritize present",
      "agree_direction" in mi_ids and "prioritize" in mi_ids)
check("MI: focusing ops carry guardrails",
      all(o.get("guardrails") for o in mi_ops if o["id"] in ("agree_direction", "prioritize")))

print()
if fails:
    print(f"{len(fails)} failure(s)")
    sys.exit(1)

print("ALL CRITIQUE-REVISION CHECKS PASSED")
print()
print("=== structural verifier (verify_phase3.py) ===")
r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "verify_phase3.py")],
                   capture_output=True, text=True)
print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip())
sys.exit(r.returncode)
