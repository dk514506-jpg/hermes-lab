# Building an Architecture That Refuses to Steal Agency
### What happened when I spent a day running an agent campaign on a 2nd-century astrologer's rules

*August 6, 2026 · Home lab · Companion package: GitHub_PoC/*

---

## The one-sentence version

I spent today building a governed agent architecture on Hermes whose central
rule is: the agent proposes and the human disposes — enforced in verifiers and
logs, structurally, not promised in prose. Eight phases, one day, judged by
other agents; the strongest artifact is a log of the campaign's own errors.

## Where it runs

A home lab. A personal, self-hosted Hermes setup on my own machine, built for
my own use: my learning, my motivation, my agency. It is not a workplace
system and it was never meant to be one. No deployment story, no org
integration, no enterprise anything. Just me and my machines and a set of
rules about who gets to decide what.

## Why I'm telling you

You're AI researchers, so the interesting part isn't the artifacts — it's the
process discipline that produced them, because I believe it's reusable: a way
of building agent systems that can't quietly take over their user's judgment,
and a way of proving they don't. That last part is the hard one. Anyone can
write "we value human autonomy" into a system prompt. Making it
machine-checkable is another thing entirely.

## The method: reconstruction discipline, from a 2nd-century astrologer

Vettius Valens wrote a 10-book astrological anthology that survives in
partly-corrupted manuscripts. Reconstructing it demands a brutal discipline:
preserve conflicting witnesses instead of harmonizing them, label every claim
source-vs-inference, quarantine untrustworthy claims, refuse premature
coherence, treat worked examples as test vectors. I've spent months in that
corpus, and at some point it clicked for me the way Hegel clicked for me on
that bus — the discipline stopped being about astrology and became a way of
seeing. Because stripped of the astrology, it is exactly the discipline you
want in an agent that must support a human's agency rather than erode it. So
I ran the campaign on it: ten recovered Valens principles, transposed into
machine-checkable form.

## What got built (broad strokes)

Eight phases, one day, each phase gated by its own verifier:

1. **Foundation** — 8 behavioral-change frameworks (COM-B,
   self-determination theory, motivational interviewing, and the rest)
   distilled into a theory matrix with every link evidence-flagged.
2. **Evidence base** — 70+ sources fetched and checked against live journal
   APIs (existence + retraction status — not full-text review); retracted
   papers exiled to a register; opinion pieces and preprints honestly flagged.
3. **Skill library** — 8 skill packages (90 files), each with atomic
   operations and recovery paths.
4. **Graph + lattice** — a reconciled skill graph and a motivational
   "lattice," an insight engine that treats every insight as a *hypothesis*,
   user-correctable, with a quarantine law: user-rejected insights are
   removed regardless of evidence strength.
5. **Safeguards** — the estate's rulebook: five action modes
   (ACT/SCAFFOLD/ASK/DEFER/STOP), a preserved-user-decision set, absolute
   prohibitions, and skill-atrophy controls so the agent never deskills its
   user.
6. **Practice dojos** — five conversational practice environments
   (ambivalence, conflict, coaching, workplace, everyday conversation), each
   with state machines, personas, rubrics, and a spirit gate that refuses to
   grade technique without the motivational-interviewing spirit (partnership,
   empathy, evocation).
7. **Harness** — the whole thing packaged as a self-contained, installable
   estate with its own in-tree verifier.
8. **Evaluation** — a real evaluation instrument: rubric, applied QA
   checklists, and a calibration log that records every error the campaign
   caught about itself.

## The calibration log

The artifact that does the most work is a log of the campaign's *own* errors —
22 corrections, each recorded as finding → fix → verifier guard. Examples: a
README that overclaimed "all VERIFIED" (caught, corrected, now guarded by a
regex that fails the build); a "single source of truth" graph that diverged
from its packages (caught by an outside judge, reconciled, guarded); a
verification gate that claimed to run nine verifiers but ran three (caught,
rewritten, guarded by itself).

Fun fact: the first draft of this report said "all machine-verified." Row 1
of the calibration log is about a README that did exactly that. I fixed the
report. The discipline is hard even when you're the one enforcing it — which
is the whole point of making it structural. My google drive is full of
unfinished drafts because I know exactly how easy it is to let an exhausted
line of thinking turn into a permanent stasis. This campaign was my way of
getting the rocks rolling.

## Three rounds of independent judging

Each phase was reviewed by outside judges — Claude and DeepSeek via API,
fresh contexts, detailed rubrics — and each round found real defects: missing
documents, stale paths, an overclaiming gate. Every finding was verified
against the tree and integrated with a guard. The final whole-project verdict:
**4.7/5, DEPLOY**, with the judge independently verifying four citations
against publishers live (including confirming the Wang & Fan 2025 retraction
the digest had correctly exiled).

Honest framing: the judges are LLMs — the same model family that built the
estate. Their value is as *adversarial reviewers whose every finding was
machine-held*, not as independent human auditors. The proof is in the loop:
judges find defects, the campaign fixes them, the fixes are mechanically
guarded.

## The runtime proof

The architecture lived as documentation and verifiers all day; I ran it once,
at the end, as the acceptance test: a live dojo session (an ambivalent
persona about starting exercise) through the real model pipeline. The spirit
gate fired exactly once, at the single technique-without-spirit turn, and
never graded it; the session logged per a strict append-only schema; the
log's outcome field said, by design, "pending — user arbitrates every pass."
Then I approved it — and that approval is in the record, verbatim. The system
refused to arbitrate for the human even in its own acceptance test.

Honest caveat: the runtime evidence is one session, one approval. The gates
are mechanical and the log is append-only, but the runtime sample is n=1 —
read the log and judge whether that matters.

## The loop I'd rather you attack

The architecture was designed by an agent, audited by other agents, and its
integrity proof is mechanical: a regex that fails the build, an append-only
log, a gate that refuses to grade. Can agent-supervised agents be made
non-circular? I think partly — by externalizing the guards — and the
calibration log is the evidence either way. I'd rather you find the 23rd
error than praise the 22 fixes.

## What I didn't do (yet)

- The acceptance test is n=1 — one session, one approval.
- The boundary gate is not yet enforced at the execution layer — a declared
  firewall isn't a working firewall. That's Phase 9, which exists precisely
  because of this gap.
- The intervention-design layer (diagnosis → intervention) is specified but
  not built; the runtime layer beyond the acceptance session is unexercised.

## What's next

Phase 9: wiring the boundary gate at the execution layer (a plugin that
refuses to run an operation without a boundary pass), extending the
diagnostic layer into an intervention stage, and transposing the remaining
Valens principles into verifier rules and guards — 31 design questions for
that work are already written.

---

*Questions welcome. The calibration log, judge verdicts, and acceptance-test
runtime log are in the package — the log is the fastest way in.*
