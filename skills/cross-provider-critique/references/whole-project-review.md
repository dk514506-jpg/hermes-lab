# Whole-Project Review Shape (phases 1-N, worked 2026-08-06)

When the user asks to "review the whole project / assess quality of output
phases 1-N, enlist <judge> as judge, give it a detailed rubric," use this
shape. Proven on the Ecology campaign (Phases 1-8; judge verdict 4.7/5 DEPLOY;
user-directed DeepSeek after Anthropic credit died mid-campaign).

## The four artifacts

1. **review_rubric.md** (council_notes/) — the judging instrument. Dimensions
   A-G scored 0-5 with a one-line artifact citation per score:
   - A Evidence discipline (flags consistent, witness conflicts preserved,
     integrity handling, anti-fabrication)
   - B Coherence & truthfulness (cross-phase consistency, single-source-of-
     truth honesty, self-description accuracy, correction history)
   - C Architectural quality (5-layer interconnect, conventions honored,
     boundary encoded not prose, learnability machinery operational)
   - D Governance & continuity (registered in own ecology, resumable from
     disk, self-application gap honest, deferred items documented)
   - E Verification depth (verifiers run + enforce real classes, catch the
     error classes the review rounds found, reproducible, judge feedback
     integrated)
   - F Valens discipline transposition (hypothesis-status, quarantine law,
     no premature closure, user sovereignty)
   - G Practical usability (fresh reader can install, practitioner can run a
     session, deferred/roadmap state explicit)
   Plus: scoring convention (0-5, artifact-cited), judge output format
   (per-dimension scores, 3 strongest, 3 weakest, 5 recommendations,
   overall verdict deploy/revise/rebuild), and the artifact map the judge
   should read per phase.

2. **judge_brief_whole.txt** — brief pointing at the rubric + the artifact
   tree; "read broadly, sample the packages, run the verifiers; name real
   files; do NOT invent content you did not read; say what you did not read."

3. **self_assessment.md** — YOUR OWN honest pre-judge scoring of the same
   dimensions (write it BEFORE the judge lands). Include "what I want the
   judge to check hardest" — 4-6 pointed questions (is the discipline real or
   pattern-matching? is the architecture decorative? did judge integration
   improve truthfulness or just document it? is the correction log complete
   or flattering?). Comparing your self-score to the judge's score IS
   calibration data; record the delta.

4. **whole_project_decision_memos.md** — judge recommendations that require
   USER judgment (ethics, scope, environment) become decision memos: finding,
   options, recommended default, what happens if deferred. NEVER decide
   user-sovereignty items unilaterally — "Pip proposes, Dallas disposes."
   Separately list what you DID integrate (no judgment needed) so the
   boundary is explicit.

## Judge invocation

- Write brief-to-file, background hermes chat with notify_on_complete (see
  SKILL.md mechanism).
- Run the full verifier gate yourself first — the judge should re-run it as
  independent evidence, but you need the baseline.
- Whole-project reads take 10-20 min (not 3-8) — the judge reads 8 phases.
- Retry loop: `for a in 1 2 3; do hermes chat -q "..."; [ -s <outfile> ] && break; sleep 5; done` — but a 2-3s exit across ALL attempts = API failure (pitfall 7), stop and switch providers.

## Integration order (after verdict)

1. Fix the judge's mechanical findings FIRST (they're proven by its evidence).
2. Log every accepted finding in Calibration_Log.md rows (finding | fix |
   guard) — the review itself becomes a calibration row.
3. Build the guard the judge proposed if it's the "no automated guard" class
   (e.g. flag-semantics grep guard — verify_phase8.py check 6).
4. Update continuity: handoff_notes.md status block, journal entry.
5. Re-run the full gate; report the delta between self-assessment and judge
   scores explicitly.

## After the verdict: decision round + acceptance test (the full loop)

A DEPLOY verdict is not the end — it hands back to the user. Worked shape
(2026-08-06 Ecology campaign, after the 4.7/5 verdict):

1. **Decision memos → user decides.** Present the judge's HIGH/MEDIUM
   recommendations as memos with lettered options + recommended default.
   The user replies with COMPACT CODES ("1a 2a 3C 4b") + "proceed with
   assumptions" — no long-form needed. Record each decision in the
   Calibration_Log standing-items table (Q7/Q8/Q11 → RESOLVED/DECISIONED with
   date + full rule text) and the layer decision (BCW/BCT → extend COMB) in
   its own subsection. Decisions must land in the log, never stay chat-only.
2. **Acceptance test (the deploy act).** The verdict says the architecture is
   specified-but-never-run; the acceptance test runs ONE real session per the
   artifacts and produces the first runtime log. Proven invocation + log-schema
   validation + the outcome_arbitration-pending rule live in the
   `ecology-dojo-authoring` skill (references/acceptance_testing.md) — load
   that skill when running it.
3. **Loose-ends inventory.** After the test, give the user a concrete list of
   what is theirs-to-do (kanban script, arbitrating the debrief — the Q10
   unassisted act) vs what is already scheduled agent-side (Q7 rule
   propagation, Phase 9 leads). The acceptance test's outcome_arbitration
   field stays "pending — user arbitrates every pass" until the user reviews
   the debrief; that review IS the campaign's own self-application check.

## Worked example (Ecology Phases 1-8, 2026-08-06)

- Self-assessment: 4.3/5 (weaknesses: graph-index divergence, runtime void,
  Q10 lag). Judge: 4.7/5 DEPLOY (scores A5 B5 C4 D5 E5 F5 G4).
- Judge's verified evidence: re-ran the 9-verifier gate, spot-checked 4 DOIs
  against publishers live (incl. confirming a retraction), confirmed the
  Phase-8 fix rows landed in the tree.
- Judge's 3 weakest: Q11 (HEB gate declared, no execution layer), the whole
  unexercised runtime layer, the uninstantiated BCW/BCT intervention layer.
- Integrated: stale QA-checklist rows closed (row 21), flag-semantics guard
  built (row 22), 4 decision memos written for Dallas, handoff + journal
  updated, full gate green.
