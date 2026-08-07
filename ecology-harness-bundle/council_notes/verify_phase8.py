#!/usr/bin/env python3
"""Phase 8 verification: evaluation artifacts.

Run: python3 council_notes/verify_phase8.py
Verifies the Phase 8 changed paths:
  1. All 5 evaluation outputs exist and are non-trivial
  2. Evaluation_Rubric.md operationalizes the 10 plan criteria
  3. Calibration_Log.md records the campaign's correction history
  4. The 3 QA checklists are applied (name real packages/dojos, cite verifiers)
  5. Evaluation protocol references the outside-judge round
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
EVAL = os.path.join(ROOT, "..", "Phase8_Evaluation")

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


# 1. All 5 outputs exist, non-trivial
OUTPUTS = ["Evaluation_Rubric.md", "Skill_Package_QA_Checklist.md",
           "Motivational_Lattice_QA_Checklist.md", "Practice_Dojo_QA_Checklist.md",
           "Calibration_Log.md"]
for f in OUTPUTS:
    p = os.path.join(EVAL, f)
    sz = os.path.getsize(p) if os.path.exists(p) else 0
    check(f"output exists + non-trivial: {f}", sz > 3000, f"{sz} bytes")

# 2. Rubric: 10 criteria operationalized (criteria sections present)
rub = open(os.path.join(EVAL, "Evaluation_Rubric.md")).read()
for c in ["AtomicOp", "trigger", "completion", "empowerment", "atrophy",
          "unassisted capability", "evidence", "user correction", "calibrated",
          "sycophancy", "implication", "selection"]:
    check(f"rubric criterion mentions: {c}", c.lower() in rub.lower())
check("rubric: scoring ladder 0/1/2", "0 — ABSENT" in rub or "0 —" in rub)
check("rubric: protocol references outside judges", "outside-judge" in rub or "outside judge" in rub)
check("rubric: findings feed Calibration_Log", "Calibration_Log" in rub)

# 3. Calibration log: correction history present
cal = open(os.path.join(EVAL, "Calibration_Log.md")).read()
for item in ["Jose 2025", "CALM-IT", "Strack", "TDF", "COMB", "stale", "quarantine",
             "governance", "Phase 3", "Phase 4", "Phase 5", "Phase 6", "Phase 7"]:
    check(f"calibration log records: {item}", item in cal)

# 4. QA checklists applied (name real packages/dojos, cite verifiers)
sk = open(os.path.join(EVAL, "Skill_Package_QA_Checklist.md")).read()
for pkg in ["Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis",
            "TDF_Barrier_Facilitator_Grid", "SDT_Need_Support_Check",
            "MI_Ambivalence_Conversation", "Proximal_Practice_Selector",
            "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"]:
    check(f"skill QA covers: {pkg}", pkg in sk)
check("skill QA cites verifiers", "verify_" in sk)

lat = open(os.path.join(EVAL, "Motivational_Lattice_QA_Checklist.md")).read()
for item in ["quarantine", "user_verdict", "hypothesis", "evidence_edge", "T1", "T6"]:
    check(f"lattice QA covers: {item}", item in lat)

dojo = open(os.path.join(EVAL, "Practice_Dojo_QA_Checklist.md")).read()
for d in ["Conversation_Dojo", "Coaching_Dojo", "Ambivalence_Dojo",
          "Conflict_Dojo", "Workplace_Dojo"]:
    check(f"dojo QA covers: {d}", d in dojo)
for item in ["sycophancy", "intensity", "fade", "spirit gate", "de-escalation"]:
    check(f"dojo QA covers: {item}", item in dojo)

# 5. Meta-evaluation (post-judge revision, Claude 5.1): do the checklists cover the rubric?
# The rubric's §1.1 sibling-instrument mapping divides criteria by layer: skill QA = 1-5,
# lattice QA = 6/7/10, dojo QA = 8/9. The correct meta-check is UNION coverage across all
# three checklists, plus per-instrument coverage of its assigned criteria.
RUBRIC_CRITERIA = ["AtomicOp", "trigger", "completion", "empowerment", "atrophy",
                   "unassisted", "evidence", "correction", "calibrated", "sycophancy"]
texts = {f: open(os.path.join(EVAL, f)).read() for f in
         ["Skill_Package_QA_Checklist.md", "Motivational_Lattice_QA_Checklist.md",
          "Practice_Dojo_QA_Checklist.md"]}
union_missing = [c for c in RUBRIC_CRITERIA
                 if not any(c.lower() in t.lower() for t in texts.values())]
check("meta: union of 3 checklists covers all 10 criteria", not union_missing,
      f"missing={union_missing or 'none'}")
# Assigned divisions (per Evaluation_Rubric.md §1.1): skill QA → 1-5, lattice QA → 6/7/10, dojo QA → 8/9
skill_assigned = ["AtomicOp", "trigger", "completion", "empowerment", "atrophy", "unassisted"]
lat_assigned = ["evidence", "correction", "unassisted"]  # 6=evidence, 7=correction, 10=implication/selection
dojo_assigned = ["calibrated", "sycophancy"]
check("meta: skill QA covers assigned 1-5",
      all(c.lower() in texts["Skill_Package_QA_Checklist.md"].lower() for c in skill_assigned))
check("meta: lattice QA covers assigned 6/7/10",
      all(c.lower() in texts["Motivational_Lattice_QA_Checklist.md"].lower() for c in lat_assigned))
check("meta: dojo QA covers assigned 8/9",
      all(c.lower() in texts["Practice_Dojo_QA_Checklist.md"].lower() for c in dojo_assigned))
# GAP discipline: every checklist marks GAPs honestly (they must exist somewhere)
for f in ["Skill_Package_QA_Checklist.md", "Motivational_Lattice_QA_Checklist.md",
          "Practice_Dojo_QA_Checklist.md"]:
    txt = texts[f]
    check(f"meta: {f} marks GAPs honestly", "GAP" in txt or "PARTIAL" in txt)
# Calibration log has 20 rows (16 campaign + 4 phase-8 judge findings)
cal = open(os.path.join(EVAL, "Calibration_Log.md")).read()
check("calibration log: 20 correction rows", "| 20 |" in cal)

# 6. Flag-semantics guard (whole-project judge rec 5b — closes Calibration_Log row 1's
#    open proposal): fail on bare "all VERIFIED" / "everything VERIFIED" style overclaims
#    in the campaign's summary READMEs. Excludes lines that DESCRIBE a past correction
#    (e.g. 'README "all VERIFIED" claim corrected') — those are historical records, not
#    current overclaims.
FLAG_OVERCLAIM = re.compile(
    r"(all|every|everything|entirely|fully)\s+VERIFIED",
    re.IGNORECASE,
)
CORRECTION_CONTEXT = re.compile(
    r"(claim\s+corrected|corrected|fixed|downgraded|was\s+wrong|now\s+correct)",
    re.IGNORECASE,
)
flag_files = [
    os.path.join(ROOT, "..", "README.md"),
    os.path.join(ROOT, "..", "Hermes_Agent_Harness", "README.md"),
    os.path.join(ROOT, "..", "Hermes_Agent_Harness", "handoff_notes.md"),
]
flag_hits = []
for fp in flag_files:
    if os.path.exists(fp):
        for i, line in enumerate(open(fp), 1):
            if FLAG_OVERCLAIM.search(line) and not CORRECTION_CONTEXT.search(line):
                flag_hits.append(f"{os.path.relpath(fp, ROOT)}:{i}")
check("flag-semantics: no bare 'all VERIFIED' overclaims in summary READMEs",
      not flag_hits, f"hits={flag_hits or 'none'}")

print()
if fails:
    print(f"{len(fails)} FAILURE(S): {fails}")
    sys.exit(1)
print("ALL PHASE 8 CHECKS PASSED — exit 0")
