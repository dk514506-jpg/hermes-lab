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

Phase 3 of the source→matrix pipeline: (1) audit source links — `external-source-verification`; (2) chart rows from readable sources; (3) QC the charting pass with role reports (Methodologist, Ethics Auditor, ..., Locus batch check LAST — see the 'Locus batch check' section below). Run when a charting pass produced per-row drafts and the harness asks for a methodological QC report. Do NOT rewrite drafts — flag and recommend, with a reason and source basis for every flag.

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

## Locus batch check (10-field report)

Locus is the frame-keeper role that runs LAST on every batch: checks the reconciled charting against the disciplines and the interfaces (source -> claim -> matrix row -> design implication -> stake consequence -> artifact/pilot rule) WITHOUT re-reading sources. Report format — exactly these 10 fields:

1. `claims_stronger`: (row_id, what became stronger, why) — adopted re-charts, guards absorbed into dimpl/cimpl, provenance corrections, veto-first rewrites.
2. `claims_weaker`: (row_id, what became more conditional, why) — causal downgrades, ES demotions, cross-row-supported tags, originator-advocacy caveats.
3. `forbidden_implications`: (row_id, implication now forbidden, which discipline forbids it) — name the forbidding discipline (Purist veto, Ethics S-floor, Methodologist, Phenomenologist).
4. `stakes_moved`: (stake, direction, evidence) or 'none' — protected floors S1/S7/S10 hold/strengthen only; any trade is a breach.
5. `protected_floor_strain`: (stake, strain detail) or 'none' — strain = guarded in charting, enforcement deferred to artifact level (not a breach); unnamed cross-row interfaces get NAMED here (e.g., CORE-16<->CORE-19 junction).
6. `apparatus_burden`: one paragraph — proportionate or heavier; state the ACTUAL composition (Pri counts — verify, don't trust the pass brief's count; abstract-level count; quantitative payload), the yield, and the collapse recommendation.
7. `contrary_indicators`: (row_id, disconfirming signal) — source-side limits, contested claims, transfer risks.
8. `cosmotechnic_telos_check`: structural or decorative — one paragraph; three-level test: criterion-derived content, source-grounded micro-orders, artifact carriage.
9. `rows_to_downgrade`: (row_id, weight decision, reason) — tag convention appended to Discovery Notes: 'LOCUS <date>: supporting weight (not load-bearing)' or 'load-bearing'. Split evidence weight from design-role load: a row with zero evidence payload can still be ARCHITECTURALLY load-bearing (its design implication is the only source of a binding rule — batch-2 CORE-10 precedent, batch-3 CORE-14/19/20). Batch-level verdict: 'zero rows load-bearing on evidence weight — all payload in design-rule roles'.
10. `re_chart_required`: row_ids or 'none' — verify adopted re-charts satisfy the flag's REQUIRED additions item-by-item (not just 'it was re-charted'); list verification debts gated to the artifact pass, not the matrix write.

Conventions: verify claims against the canonical matrix / operational database (openpyxl read of Verif. column + Source Patch Log tail), never the memo's self-report; correct the parent's composition counts when wrong; name fault lines (opposing advocacy poles are never summed — shared corpus = double-counting risk). Copy `templates/locus_report.md` per batch.

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

## Digest method: chart as recallable thinking (Silvey preference)

The goal of charting is not to fill cells but to **digest the author so they remain callable across future rows and sessions**. A charted row that cannot be recalled when a later row needs it is a dead row. Five practices make a row recallable:

1. **Chart as thinking, not transcription.** The KFT, Limitations, and Disconfirming Implication cells should reflect your actual understanding of the argument, not a paraphrase of the abstract. A reader who hasn't read the source should grasp *why* the thesis matters and *where it could fail* from the Limitations and Disconfirming cells alone.

2. **Anchor in the author's own vocabulary.** Every author builds precise tools to do their work: Stiegler's *pharmakon*, *epiphylogenesis*, *grammatization*; Simondon's *concretization*, *margin of indeterminacy*, *element/individual/ensemble*; Heidegger's *Gestell*, *Bestand*, *poiesis*. Do not replace these with generic synonyms. Carry the terms and show how they hook into Monstare's concerns (telos, design veto, cosmotechnic audit).

3. **Cross-row recall.** When charting row N, say explicitly how it refines or tensions row M (already charted). The batch memo is where this becomes explicit. If A1-07 Stiegler is the pharmacological grounding for A1-08 Feenberg's democratic rationalization, name it. If A1-05 Simondon tensions A1-11 Winner, name the tension.

4. **Disconfirming implications as active guards.** The Disconfirming Implication cell is not academic hedging — it is the "when this author fails, what breaks" marker. If future work (artifact construction, pilot design) relies on a charted row, the disconfirming implication is the tripwire. Make it sharp enough to trigger when the row is being misused.

5. **Fault lines are named, not smoothed.** When two rows hold incompatible theses (e.g., Simondon's technical-object genesis vs. Winner's artifact-politics), the fault line is the continuity frame. Naming it tells future work the question is open, not resolved.

This is what "digest particular authors to be recallable in the future" means. It is a first-class charting discipline, not a style preference.

## Verification techniques

- Grep the source extracts for the exact quoted numbers/phrases before trusting any draft claim.
- Garbled/binary PDF text layer (font-obfuscated): try utf-16 decode; if still garbled, grep the web cache for the article's clean OCR'd text — author-site publication lists often cache the full text (worked case: clean abstract found under `cache/web/www.bsfrey.ch-160a063f4f.md` while the local reading file was garbage). Report what is unverifiable; never fabricate.
- Page-precise quotes: confirm they exist in the local extract. A reading file covering only front matter/preface/index means body-page claims are UNVERIFIED — flag the quote AND the reading base as narrower than claimed. Edition variance (archive scan vs print) changes page numbers.
- Provenance: confirm the charted text is actually the row's named source (e.g., 1994 companion chapter vs 1997 book — 10 pp vs 604 pp). Provenance-tag or rename rows where they diverge; keep claims at charted-text level.
- Check the draft's own 'Sources read' header against what the extracts actually contain.
- Staleness: audit CSVs / verification reports can PREDATE the current matrix cells (batch-3 CORE-20 lesson: the CSV called an old URL dead/wrong after the cell had already been replaced). For every row, verify the CURRENT cell live (curl HTTP status + size / text-layer sniff), not the CSV verdict.
- Completion checks: when a pass claims 'all rows charted', verify in the workbook itself (Verif. column, Discovery Notes tags, Source Patch Log tail) rather than trusting the memo — the memo is a self-report.
- Verify draft LIMITATION lines against the extract before keeping them: a limitation that is NOT
  in the source must be corrected or softened, not charted (batch-3 CORE-13: the draft claimed the
  review was 'restricted to work with animals'; the verified text covers human subjects briefly —
  'results are broadly similar', with weaker reinforcers — so the limitation became
  'animal-primary with brief human coverage').
- Attribute contested within-field claims as the authors' position, not settled fact (batch-3
  CORE-13: 'no integrated theory of conditioned reinforcement exists' is a contested stance, and
  the senior author's own theories are foregrounded — mark advocacy-adjacent within-field).

## Disciplines

Citation-is-not-evidence; Tier-P stays visible (plausible, not proven); H2 is a vector not a scalar; prevent false generalization from weak/correlational papers; SCED rows must not imply causal certainty. Distinguish 'confirmation' (never available from a narrative review) from 'corroboration'. Use the word 'durable'/'proven' only where the source demonstrates it.

## Image-only and partial-text source conventions

When a source is image-only (no extractable text layer), lending-only, or gated behind login, charting is still acceptable **supplemented by secondary synthesis** (Philpapers abstract, independent summaries, publisher pages) — but you MUST:
- Flag the row as "abstract-level" or "image-only" in Discovery Notes
- Record verification debt: "Full text needed for page-precise verification"
- Never make schedule/mechanism/quote claims beyond the documented reading base
- Distinguish "full text read" from "synthesized from summary" — a draft that doesn't distinguish these is a coverage violation

Examples: batch-4a A1-07 Stiegler (image-only PDF, supplemented by Philpapers abstract + independent summary); batch-4b A1-11 Winner (image-only PDF, supplemented by Chicago UP page + Boundary 2 review + ESTS article); batch-4b A1-14 Mitcham, A1-16 Mumford (DLI/archive.org image-only scans).

## Epithet register (living document)

The Epithet Register (`/opt/data/Monstare_epithet_register.md`) preserves each author's voice — not just their claims, but their tonal signature and the felt sense of what they are pointing at. Downstream artifacts (Design Veto Catalogue, Cosmotechnic Audit Card, pilot rules) draw from this register so rules grounded in an author *sound* like that author.

Per author: **Epithet** (1-3 word signature), **Quotations** (range from subtle to robust — tonal register is exemplified, never described), **Reverie** (evocative vignette, 100-200 words, conveying the full spectrum of feelings and thoughts on the concept). See the register file for worked examples (Heidegger, Borgmann, Haraway).

Grow the register with each batch. The epithet is the seed; the quotations are the body; the reverie is the felt sense.

## Synthesis memos as deliverables

After charting a spine (area or sub-batch), produce a **synthesis memo** that traces the cross-row tissue — the living organism of ideas in relation, not just a list of theses. Anatomy: organs (which authors serve which function), interconnecting nexuses (fault lines that are also connections), cross-cutting themes (through-lines that run across the whole spine), remaining specializations needed. The synthesis is where recallability becomes explicit: "when this author is needed, what whole body of thought does it call up?"

## Files

- `templates/methodologist_report.md` — 7-field report skeleton to copy per batch.
- `templates/locus_report.md` — 10-field Locus batch-check skeleton (run last, copy per batch).
- `references/monstare-batch1-methodologist.md` — worked case: batch-1 findings, source-file map, the anachronism catch, d-value verification, unverifiable quote.
- `references/monstare-locus-batch3.md` — Locus worked case: weight-tag adjudication (evidence weight vs design-role load), re-chart verification, apparatus-burden judgment, completion verification.
- `references/monstare-batch-handoff-hunt.md` — batch handoff prompt structure, per-source readability triage, sub-agent source-hunt protocol with halting buckets.
- `references/monstare-batch4a-digest.md` — batch-4a digest pass: image-only PDFs, partial-text caveats, cross-row recall convention.
- `references/monstare-batch5-epithet-register.md` — epithet register structure, reverie examples, forward-looking template.

Companion phases: source-audit = `external-source-verification`; producing grounded prose = `grounded-citations`.
