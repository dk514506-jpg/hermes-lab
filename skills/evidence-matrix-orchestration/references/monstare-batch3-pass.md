# Monstare batch 3 — CORE completion pass (2026-08-13)

Session detail for the orchestration skill: source-pass catches, abstract-level decisions,
causal-status adjudications, and the CORE-16 Phenomenologist re-chart.

## Source pass: wrong-article catches (content-identity gate)
- **CORE-19 (Klasnja et al. 2015 MRT)**: seeded readable PMC5820391 = Aasdahl et al. 2018
  (J Occup Rehabil, return-to-work scale) — a DIFFERENT study; seeded landing
  10.1016/j.cct.2015.07.003 = Broglio et al. (Contemp Clin Trials, dose escalation) — a
  THIRD article. Both had only BAD_STUB audit verdicts (content never read). Replacement:
  author-hosted PDF (co-author A. Tewari's site, ambujtewari.com, text-layer verified) +
  landing doi.org/10.1037/hea0000305 (CrossRef-verified). Lesson: content-verify identity
  (eutils/CrossRef) for stub/bot-challenged verdicts before charting.
- **CORE-14**: old landing DOI 10.1093/019823682X.003.0002 dead (404) → replaced with
  10.1093/analys/58.1.7 (Analysis 58(1):7-19, CrossRef-verified; OUP curl 403 = bot-block,
  not dead).
- **CORE-20**: audit CSV "BAD_DEAD 404" applied to a SUPERSEDED URL (PSU 2018 MOST overview
  PDF); the current PMC2062525 (Collins, Murphy & Strecher 2007) is live and correct —
  match audit verdicts by URL equality, not RowID.

## Abstract-level charting decisions (documented, handoff-permitted)
- **CORE-12 (Ferster & Skinner 1957)**: archive lending only; charted from archive.org
  catalog metadata (741 pp, Appleton-Century-Crofts, ONR/Harvard 1949-1955). Textbook claim
  "VR most extinction-resistant" = unverified Tier-P reading; the CF-3 dependency linkage
  is labeled Tier-P hypothesis, not charted finding.
- **CORE-17 (Kazdin 1982)**: archive lending only; Kazdin 2021 JEAB paywalled (abstract
  corroborates). Google Books landing is a LATER edition — claims stay at 1982-edition level.

## Causal-status / evidence-type adjudications (batch-3)
- CORE-13: causal → correlational (narrative review; Annual Review chapter; CORE-06 precedent).
- CORE-19/20: causal → conceptual (methods); design-licenses scoped (proximal only /
  confirming RCT only).
- CORE-12: causal (lab-bounded, animal; catalog-attributed — unverified, Tier-P).
- CORE-03: review → theoretical (integration proposal; journal itself tags "METHODOLOGY").
- CORE-11: review → narrative review (advocacy-adjacent, critical); CORE-13: review →
  narrative review (non-systematic).
- CORE-11 vs CORE-10 = opposing advocacy poles over the SAME corpus — never mutually
  confirming, never summed.

## CORE-16 Phenomenologist re-chart (flattening by OMISSION)
- KF initially preserved 2 of 5 felt invariants; the re-chart added: time distortion
  (book's element 8), loss of self-consciousness with its paradox (self disappears from
  awareness yet emerges stronger; can reach self-transcendence, element 7), absorption /
  merging of action and awareness, and relief-from-everyday-worries (element 5 clause).
  Ordering (felt-first, challenge-skill as one element among several) was kept.
- Anchors: "Control over consciousness cannot be institutionalized" (p. 21) — a reliably
  reproduced condition-set is, by the book's own logic, no longer flow (conditions-in /
  flow-out machinery forbidden); freedom-to-return (p. 61: captive self loses "the freedom
  to determine the content of consciousness"); "golden ratio" is QUALITATIVE METAPHOR — no
  numeric challenge-skill ratio exists in the source; flow conditions are structural
  (presence-based 0/1), never calibrated scalars.

## Pilot flags carried to the Tier-C pilot
- SCED baseline required (no-reward baseline phase; batch-1/2 rule).
- Reporting ≠ design quality (SCRIBE 2016 verbatim scope disclaimer).
- MRT: proximal ≠ distal; SUTVA/no-carryover assumptions pre-registered; decision-point
  density (power) feasibility unexamined.
- MOST: optimization ≠ validation — the pilot is screening/refining-stage logic, not a
  confirming-phase trial; component-level ≠ ecology-level.

## Files
- Rows/drafts/final: `Monstare_batch_3_rows.json`, `Monstare_batch_3_charting_drafts.md`,
  `Monstare_batch_3_charting_final.json`
- Sources: `Monstare_batch3_sources/` (fulltexts + `batch3_reading_extracts.md`)
- Updates: `Monstare_batch_3_{evtype,access,url,caveat}_updates.json`
- Patch script: `scripts/monstare_patch_charting_b3.py`
- Role reports: `Monstare_role_reports/B3_*.md`
