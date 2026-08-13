---
name: evidence-matrix-charting-qc
description: "Charting QC: evidence-matrix drafts, causal status, ES."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, evidence-matrix, methodological-qc, charting, anti-fabrication, role-reports]
    category: research
    related_skills: [external-source-verification, grounded-citations]
---

# Evidence-Matrix Charting QC (Methodologist role)

Phase 3 of the source→matrix pipeline: (1) audit source links — `external-source-verification`; (2) chart rows from readable sources; (3) QC the charting pass with role reports (Methodologist, Ethics Auditor, ...). Run when a charting pass produced per-row drafts and the harness asks for a methodological QC report. Do NOT rewrite drafts — flag and recommend, with a reason and source basis for every flag.

## Inputs

- Drafts file: one section per row (Key Finding / Thesis, Effect Size / Strength, Limitations, Disconfirming Implication, H1/H2, Design Implication, Cosmotechnic Implication, Causal Status).
- Rows file (JSON) carrying SEEDED Causal Status, Evidence Type, Key Finding, Design Implication, plus per-row source URLs.
- Source extracts: `sources/` dir + web cache (`cache/web/*.md`). Read abstracts/conclusions only; never re-read full PDFs.

## Report format — exactly these 7 fields

1. `causal_status_changes`: (row_id, current_status, recommended_status, reason)
2. `evidence_type_misclassifications`: (row_id, current_type, recommended_type, reason)
3. `effect_size_checks`: (row_id, claimed_strength, supported_strength, note) — use `not_quantifiable` where the source supports no number
4. `generalization_risks`: (row_id, risk, why_it_matters)
5. `sced_pilot_flags`: (row_id, flag) for rows feeding pilot/model logic
6. `limitations_missed`: (row_id, limitation_Pip_missed, source_basis)
7. `rows_where_claim_exceeds_source`: list of row_ids

Save the report to the role-reports dir AND return the full report text in the final message (the parent consumes it directly).

## Per-row checklist

**(a) Causal status must match what the source IS, not what the theory asserts.**
- theory/framework article → conceptual; philosophical essay → conceptual; narrative review → correlational at best; meta-analysis of experiments → causal (lab-bounded).
- A source that merely CITES experiments does not become causal (citation-is-not-evidence).
- The 'causal' seed on a theoretical synthesis is the most common error. If every theory row qualifies as causal, the taxonomy collapses — say so explicitly.
- Methods papers (MRT, MOST, reporting guidelines, SCED texts, statistical-design papers) chart as 'conceptual (methods)': the source IS a method and reports no results. An executed version of the design may license causal claims — keep that design-licenses note SCOPED (e.g., MRT licenses proximal-effect attribution only, assumptions checked; only a MOST confirming-phase RCT licenses package-level claims) — it never upgrades the source's own status. (Batch-3: CORE-19 Klasnja MRT and CORE-20 Collins MOST were both seeded 'causal' and both downgraded.)
- Abstract-level charting of a primary empirical source keeps its evidentiary class ONLY with a catalog-attribution qualifier: 'causal (lab-bounded, animal; catalog-attributed — unverified against text, Tier-P)' names the source's nature (it IS a primary experimental monograph) without licensing any specific finding; evidence-type analog 'empirical (animal, 1957; catalog-attributed)'. (Batch-3: CORE-12 Ferster & Skinner 1957, archive-lending-only.)
- A draft line like "causal as asserted within the theory — Methodologist to adjudicate" is an invitation; adjudicate, don't punt.

**(b) Evidence type taxonomy:** theoretical / narrative review / systematic review / meta-analysis / philosophical. 'review' alone is too coarse — check the paper's OWN title and abstract ('A Meta-Analytic Review of Experiments...' → meta-analysis; 'This study demonstrates...' with no protocol → narrative review, and qualify it as non-systematic / advocacy-adjacent when the author is the theory's proponent).

**(c) ES proportionality:** verify every quoted d/r/ES VERBATIM against the abstract in the cached extract before trusting it. Flag anachronistic citations — a 1994/1997 source cannot marshal a 1998 meta-analysis; external meta-analyses leaking into a draft's Strength line are citation-is-not-evidence. Narrative reviews, theory articles, and philosophy get `not_quantifiable` even when the draft gives them 'high strength' (that's a construct-role claim, not an ES — label it as such).

**(d) Generalization:** lab free-choice persistence ≠ field/digital engagement; name the contested estimates (e.g., Cameron & Pierce 1994 / Eisenberger & Cameron 1996 vs Deci et al. 1999 — the divergence is partly coding-driven, documented in DKR 1999's own appendix); theory-originator-authored reviews carry advocacy bias and are NOT independent confirmation (literature overlap = double-counting risk). Advocacy runs BOTH directions: a critic-authored position review over the same corpus is the OPPOSING pole of the originator's advocacy, not independent confirmation either — weight proponent and critic rows (e.g., CORE-10 Locke & Latham vs CORE-11 Ordonez et al. 'Goals Gone Wild') as a held tension, never summed.

**(e) SCED/pilot logic:** coefficients imported from literature = DIRECTION + BOUNDED BAND, never a point estimate lifted from the strongest cell. Parameters with no quantitative basis in the source (e.g., an authorship parameter from a conceptual paper) = structural/presence-based (0/1 or ordinal), not calibrated scalars. Pilots need a baseline/no-reward contrast to speak to a meta-analysis's evidence class (studies without controls were excluded from it). N-of-1/small-N cannot yield causal claims; selection effects block causal inference from self-selected users.

## Verification techniques

- Grep the source extracts for the exact quoted numbers/phrases before trusting any draft claim.
- Garbled/binary PDF text layer (font-obfuscated): try utf-16 decode; if still garbled, grep the web cache for the article's clean OCR'd text — author-site publication lists often cache the full text (worked case: clean abstract found under `cache/web/www.bsfrey.ch-160a063f4f.md` while the local reading file was garbage). Report what is unverifiable; never fabricate.
- Page-precise quotes: confirm they exist in the local extract. A reading file covering only front matter/preface/index means body-page claims are UNVERIFIED — flag the quote AND the reading base as narrower than claimed. Edition variance (archive scan vs print) changes page numbers.
- Provenance: confirm the charted text is actually the row's named source (e.g., 1994 companion chapter vs 1997 book — 10 pp vs 604 pp). Provenance-tag or rename rows where they diverge; keep claims at charted-text level.
- Check the draft's own 'Sources read' header against what the extracts actually contain.

## Disciplines

Citation-is-not-evidence; Tier-P stays visible (plausible, not proven); H2 is a vector not a scalar; prevent false generalization from weak/correlational papers; SCED rows must not imply causal certainty. Distinguish 'confirmation' (never available from a narrative review) from 'corroboration'. Use the word 'durable'/'proven' only where the source demonstrates it.

## Files

- `templates/methodologist_report.md` — 7-field report skeleton to copy per batch.
- `references/monstare-batch1-methodologist.md` — worked case: batch-1 findings, source-file map, the anachronism catch, d-value verification, unverifiable quote.

Companion phases: source-audit = `external-source-verification`; producing grounded prose = `grounded-citations`.
