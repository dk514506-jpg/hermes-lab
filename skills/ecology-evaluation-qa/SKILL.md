---
name: ecology-evaluation-qa
description: "Use when authoring applied QA checklists for Ecology phases."
---

# Ecology Evaluation QA (Phase-8 style applied checklists)

## Purpose
Author applied evaluation/QA artifacts for the Motivational Ecology Agent Architecture
campaign (`~/.hermes/hermes-agent/docs/Ecology/Foundation/`): master
rubrics, per-package QA checklists, lattice QA checklists, calibration logs. "Applied"
means every check names the exact artifact file(s) that answer it, states the pass
condition, and cites the verifier check that enforces it — or flags **GAP**. Output
must survive an outside-judge review round (cross-provider critique), so it must be
answerable from the artifacts, not a generic template.

## Trigger Conditions
- User asks for an evaluation/QA checklist, rubric, or calibration artifact for an
  Ecology phase (Phase 8 pattern: one artifact per layer — skill packages, lattice,
  dojos — plus master rubric and calibration log).
- User asks to "apply" the plan criteria to the real artifacts ("against the plan
  criteria", "per-package rows", "where a verifier already enforces it say 'verified
  by …'").
- A review round needs to know which criteria are machine-enforced vs review-only.

Not this skill: dojo *building* → ecology-dojo-authoring; evidence digest work →
recent-evidence-distillation.

## Read FIRST (in this order)
1. The phase plan (`PhaseN_Plan.md`) — the criteria to operationalize; the council
   split (which sibling owns which outputs; keep your format consistent with theirs).
2. The verifier SOURCES (`council_notes/verify_phaseN.py`,
   `Phase3_Skills/verify_packages.py`) — never cite "verified" from memory; cite exact
   check numbers read from the code.
3. The audited layer: per-package `SKILL.md` files, JSON schemas, index files
   (`skill_graph_index.json`, `lattice_index.json`), policy files
   (`insight_trigger_policy.md`, `skill_lattice_interface.md`), `T2R_traceability.json`.
4. Sibling outputs already in the phase dir (rubric, dojo checklist) — match their
   check/evidence/pass-condition shape.

## Method — the applied-checklist loop
For each plan criterion × audited unit (package / layer):
1. **Name the evidence file(s)** that answer the check (e.g.
   `COMB_Behavioral_Diagnosis/atomic_ops.json` + `edge_map.json` decomposes_to).
2. **State the pass condition** concretely (e.g. "every SKILL.md op present in
   atomic_ops.json; decomposes_to targets match ops in order 1..N").
3. **Cite enforcement**: "verified by verify_packages.py check 5" — only if the
   verifier really tests that condition (read the source). Otherwise **GAP**.
4. **State-var parity**: diff SKILL.md "## State Variables" against the package's
   `state_schema.json`. No verifier does this — drift found live (TDF SKILL.md kept
   `binding_constraint` after state_schema renamed to `binding_constraint_comb`).
5. Collect **reconciliation notes** (known pending items: uninstantiated register ops,
   unbuilt conversion ops) and **cross-cutting gaps** with proposed verifier closures.

## Core insight — verifiers enforce structure, not substance
Build verifiers pass while most evaluation criteria remain content-level gaps. Section
presence ≠ content; JSON validity ≠ schema↔SKILL.md parity; no verifier scans evidence
citations, hypothesis wording, or verdict propagation. When a criterion is unenforced,
say so explicitly as **GAP** with a proposed closure (e.g. "extend verify_packages.py
with checks 8–10"). The GAP column is what makes the checklist judge-usable.

## Pitfalls
- Never write "verified by verify_phaseN.py" without reading that verifier's source;
  check numbers are exact and drift between versions.
- Don't assume verifier-pass means criterion-met; the checklist's value is the gaps.
- Output-shape constraints ("output ONLY these N files + K-line summary") are strict —
  deliver exactly that in the final response, nothing else.
- The 16-section SKILL.md standard has no "Completion Conditions" section; completion
  lives in terminal `record_*` ops, and no verifier checks one exists — flag it.
- Session detail goes in `references/`, not the SKILL.md body.

## References
- `references/phase8_evaluation_notes.md` — verifier coverage map with exact check
  numbers (verify_packages.py 1–7, verify_phase4.py 1–10, verify_critique_revisions.py
  1–6), per-package op counts, lattice QA facts (tiers Q0–Q5, triggers T1–T6, schema
  required fields, validation gates, prediction ceilings), reconciliation notes
  (T2R 48/39/9, skill_load_score→trend pending, TDF rename drift), cross-cutting gaps
  + proposed closures, and the produced checklist locations.
- Related: ecology-dojo-authoring (house `council_notes/verify_phaseN.py` register,
  parallel-build coordination), recent-evidence-distillation (evidence discipline).
