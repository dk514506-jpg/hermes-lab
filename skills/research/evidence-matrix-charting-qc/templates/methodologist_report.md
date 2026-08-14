# METHODOLOGIST QC REPORT — <batch name> (<date>)

Scope: <row list>. Method: <one-liner: what was verified against which extracts>. Disciplines: citation-is-not-evidence; Tier-P stays visible (plausible, not proven); H2 is a vector not a scalar; SCED rows must not imply causal certainty.

## 1. causal_status_changes
- (row_id, current_status, recommended_status, "reason — source genre vs seeded status; adjudicate 'Methodologist to adjudicate' lines")

## 2. evidence_type_misclassifications
- (row_id, current_type, recommended_type, "reason — check the paper's OWN title/abstract; 'review' is too coarse: theoretical / narrative review / systematic review / meta-analysis / philosophical")

## 3. effect_size_checks
- (row_id, claimed_strength, supported_strength, "note — verify every d/r/ES verbatim against the abstract; use not_quantifiable where the source supports no number; flag anachronistic external citations")

## 4. generalization_risks
- (row_id, risk, "why it matters — lab→field external validity, contested estimates, advocacy bias, provenance gaps")

## 5. sced_pilot_flags
- (row_id, "flag — direction + bounded band, not point estimates; structural/presence-based parameters where no quantitative basis; baseline/no-reward contrast required; N-of-1 cannot yield causal claims")

## 6. limitations_missed
- (row_id, "limitation the drafter missed", "source basis — quote/paraphrase location in the extract")

## 7. rows_where_claim_exceeds_source
- row_id — "what exceeds the source and why"

---
Cross-cutting notes for the matrix owner:
- <evidence-type taxonomy gaps, external-citation leak sweep, Tier-P language audit, verifiability of page-precise quotes>
