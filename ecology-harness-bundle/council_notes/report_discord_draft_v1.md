# Building an Architecture That Refuses to Steal Agency
### One day, eight phases, and a 2000-year-old method — a campaign report

*Report date: 2026-08-06 · Campaign: Motivational Ecology Agent Architecture
· Companion GitHub proof-of-concept: see the package accompanying this report*

---

## The one-sentence version

We spent today building a complete, governed "motivational ecology" agent
architecture on Hermes — a skill library, practice environment, and safety
estate whose central commitment is that the agent proposes and the human
disposes, enforced structurally rather than promised in prose.

## Why we're telling you

You're AI researchers. So the interesting part isn't the artifacts — it's the
*process discipline* that produced them, because we believe it's reusable:
a method for building agent systems that can't quietly take over their user's
judgment, and a way of *proving* they don't.

## The method: reconstruction discipline, borrowed from a 2nd-century astrologer

Vettius Valens wrote a 10-book astrological anthology that survives today in
partly-corrupted manuscripts. Reconstructing it requires a brutal epistemic
discipline: preserve conflicting witnesses instead of harmonizing them, label
every claim source-vs-inference, quarantine claims (not sources) that can't be
trusted, refuse premature coherence, and treat worked examples as test vectors
rather than decorations.

That discipline — stripped of the astrology — turns out to be exactly what you
want when building an agent that must *support* a human's agency rather than
erode it. So we ran the campaign on it. The whole architecture is a
transposition of ten recovered Valens principles into machine-checkable form.

## What got built (broad strokes)

**Eight phases, one day, all machine-verified:**

1. **Foundation** — 8 behavioral-change frameworks (COM-B, SDT, MI, TDF...)
   distilled into a theory matrix with every link evidence-flagged.
2. **Evidence base** — 78 sources fetched and verified against live journal
   APIs; retracted papers exiled to a register; opinion articles and preprints
   honestly flagged.
3. **Skill library** — 8 skill packages (90 files), each with atomic
   operations, state schemas, edge maps, recovery operations.
4. **Graph + lattice** — a reconciled skill graph and a motivational "lattice"
   (an insight engine that treats every insight as a *hypothesis*, user-
   correctable, with a quarantine law: user-rejected insights are removed
   regardless of evidence strength).
5. **Safeguards** — the estate's rulebook: five action modes
   (ACT/SCAFFOLD/ASK/DEFER/STOP), a preserved-user-decision set, absolute
   prohibitions, and skill-atrophy controls so the agent never deskills its
   user.
6. **Practice dojos** — five conversational practice environments
   (ambivalence, conflict, coaching, workplace, everyday conversation), each
   with state machines, personas, rubrics, and a spirit gate that refuses to
   grade technique without motivational spirit.
7. **Harness** — the whole thing packaged as a self-contained, installable
   estate with its own in-tree verifier.
8. **Evaluation** — a real evaluation instrument: rubric, applied QA
   checklists, and a calibration log that records every error the campaign
   caught about itself.

## The part that might interest you most: the calibration log

The single most impressive artifact is a log of the campaign's *own* errors —
22 corrections, each recorded as finding → fix → verifier guard. Examples:
a README that overclaimed "all VERIFIED" (caught, corrected, now guarded by a
regex that fails the build); a "single source of truth" graph that diverged
from its packages (caught by an outside judge, reconciled, guarded); a
verification gate that claimed to run nine verifiers but ran three (caught,
rewritten, guarded by itself). The campaign policed its own truthfulness the
way it polices its agents' — because a system that can't admit its own errors
can't be trusted to protect yours.

## Outside judges, not self-congratulation

Three rounds of independent judging by other models (Claude and DeepSeek via
API), each with a detailed rubric, each finding real defects — missing
documents, stale paths, an overclaiming gate — and each round's findings
integrated and guarded. The final whole-project verdict: **4.7/5, DEPLOY**,
with the judge independently verifying four citations against publishers
live (including confirming a retraction the digest had correctly exiled).

## The runtime proof

The architecture was *specified* all day — until the end, when we ran the
acceptance test: a live dojo session (an ambivalent persona about starting
exercise) through the real model pipeline. The spirit gate fired exactly once
at the single technique-without-spirit turn, never graded it; the session
logged per a strict schema; the log's outcome field said, by design, "pending
— user arbitrates every pass." Then the user approved it, and that approval
is in the record. The firewall demonstrably held, and the system refused to
arbitrate for the human even in its own acceptance test.

## The philosophy, stated plainly

- **Skill preservation is a measured objective.** The architecture tracks its
  user's skill load and fades scaffolding; the campaign applied that to
  itself.
- **Hypothesis-status over doctrine.** Every insight, profile, and diagnosis
  is a hypothesis the user can correct — and rejection is absolute.
- **Questions outrank conclusions.** Ambivalence is a designed halt state,
  not a defect.
- **The agent proposes; the user disposes.** Structurally, not stylistically.

## What's next

Phase 9: wiring the boundary gate at the execution layer (a plugin that
refuses to run an operation without a boundary pass), extending the
diagnostic spine into an intervention layer, and — the part we're most
excited about — formally melding the Valens corpus (the method's source) with
the Ecology estate. The 31 design questions for that meld are already written.

---

*Questions welcome. The full proof-of-concept package (calibration log, judge
verdicts, acceptance-test runtime log, architecture docs) accompanies this
report.*
