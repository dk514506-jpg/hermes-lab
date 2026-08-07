# Validator Rounds + Public PoC Packaging

Session-specific detail from the Ecology campaign (2026-08-06): after the
judge/whole-project rounds, the user asked for (a) a semi-technical Discord
report and (b) a GitHub proof-of-concept package, both "with multiple rounds
of review, revision, and resynthesis." This reference captures the two
reusable patterns that emerged.

## Pattern 1 — The validator round (Locus pattern), incl. round 2

A VALIDATOR is a reviewer who checks TRUTHFULNESS against primary sources
(not taste). Useful when the deliverable makes factual claims a public
audience could check.

- Brief the validator with a numbered claim list: "VERIFY at least these N
  claims against the actual files; report each as VERIFIED (file+line
  evidence) or DISCREPANCY (with the truth); then list unsupported/overstated
  claims with the caveat to add. Do NOT edit files."
- Validator round 1 output shape: a claim-verification table + a caveat list.
  In the worked example: 9/10 claims verified exactly; 9 caveats, the
  sharpest being that the draft report's "78 sources fetched and verified"
  regressed to the EXACT overclaim class the campaign's own calibration-log
  row 1 had corrected ("all VERIFIED" in a README). The summary layer
  regresses to the sins the source layer already fixed — always re-check
  summary phrasing against the calibration history.
- **Validator round 2 (the key addition): verify the FIXES, not the
  document.** After the revision round, dispatch the validator again with the
  claimed-fix list (a/b/c/...) and ask: each fix VERIFIED / PARTIAL / NOT
  DONE with file evidence, PLUS any NEW unsupported claims introduced by the
  revisions. In the worked example: 7/10 verified, 3 PARTIAL (count still
  overstated vs the shipped bibliography's own header; timezone note applied
  to one of two byte-identical copies; one stale pointer + 6 stale install
  paths survived), plus 4 newly-exposed residuals (a bare-VERIFIED line in a
  newly-shipped evidence file, bare-COMPLETE status phrasing, "run it
  yourself" overstatement). Every residual was the same fixable class the
  campaign already policed.
- Round 2 catches what round 1 cannot: whether the revision introduced NEW
  claims that need the same discipline. Two rounds minimum for anything that
  will be publicly posted.

## Pattern 2 — Public PoC package tripwires (skeptic-proofing)

When packaging a governed campaign for GitHub/public posting, a rigor critic
plus the validator surfaced these P0-level traps (all real, all fixed):

1. **The quick start must run against what ships.** A README whose `cp -r
   skills/*` and `python3 verify/verify_harness.py` reference directories not
   in the package = dead commands = "the package fails its own standards."
   Fix either way: ship the full estate (skills/, verify/, root files) so the
   shipped verifier passes in-package (`HARNESS VERIFIED — exit 0`), or
   delete the quick start. Shipping the whole estate made it a stronger PoC
   AND made the "SHIPPED in-tree" claim true.
2. **Ship the flagship evidence RAW, not as a curated extract.** A "22-row
   calibration log" that ships only 11 rows (with the rest "in the working
   archive" — a pointer with no address) is the integrity artifact made
   invisible. Ship the full log, the raw judge verdicts (byte-identical to
   originals), the runtime log. The curated-extract framing is honest in
   prose and dishonest in behavior.
3. **Date/timezone inconsistencies get flagged by the first skeptic.** Log
   timestamp 2026-08-07T03:14Z + approval dated 2026-08-06 looks like
   approving a session before it ran. One `_timezone_note` line resolving
   UTC vs local fixes it. Apply to ALL copies (the note landed in only one of
   two byte-identical copies in the worked example — round 2 caught it).
4. **"Proven" overstates n=1.** One simulated acceptance session
   demonstrates; it does not prove. "proven in a live acceptance test" →
   "demonstrated / exercised." Add the n=1 caveat explicitly ("read the log
   and judge whether that matters") — owning it converts a vulnerability into
   a trust signal.
5. **Anchor every checkable claim.** "Judge independently verified 4
   citations" ships with zero DOIs = uncheckable = the strongest claim
   becomes the strongest doubt. Add the DOI table (works, venue, DOI, and
   explicit RETRACTED marking for register-only entries). Ship the
   bibliography. An AI-research audience checks citations first; fabrication
   is the epidemic they're primed to suspect.
6. **Audience framing block up front:** "What this is / What this is NOT /
   Why Valens (or the odd source) / What you can check right now." The
   astrology hook was a coin flip until given an explicit early
   non-astrology framing. Lead with the problem, treat the unusual method as
   a case study.
7. **Stale install paths survive the archive's own stale-path sweep.**
   verify_phase7's sweep covered Phase3_Skills/Phase6_Dojo/Phase5_Safeguards
   but not "Hermes_Agent_Harness/..." placement lines in SKILL.mds — the
   packaged copies carried paths that only make sense in the archive. When
   packaging, sweep for ARCHIVE ROOT names in shipped files, not just the
   phase dirs.
8. **Ask for the 23rd error, not praise for the 22nd.** The closing
   invitation ("we'd rather you find the 23rd error than praise the 22
   fixes" + "the calibration log is the fastest way in") is the specific,
   self-deprecating move this audience rewards.

## Report-level (Discord) fixes that generalized

- "all machine-verified" is the row-1 overclaim class — and the draft
  committed it. Fix the phrase AND optionally surface the irony ("the first
  draft of this report said 'all machine-verified.' Row 1 of the calibration
  log is about a README that did exactly that.") — converts a near-mistake
  into the best authenticity signal.
- "the user approved it" → "the author, in this case — stated plainly"
  (an independent reader discounts self-approval; stating it disarms the
  inference).
- Cut redundant philosophy sections; compress the exotic-method section so
  the payoff arrives fast; thread format beats one long post.
- Judge framing for public audiences: LLM judges grading an LLM-built estate
  must be framed as "adversarial reviewers whose every finding was
  machine-held," with the score hedged — never "independent human auditors."

## Pattern 3 — Match the USER's voice for shareable outputs (merged-voice directive)

When the user asks for a report/package for an external audience AND provides
their own writing as the tone reference ("match the tone of my own writing"),
the finished piece must sound like THEM, not like a polished campaign
document. Worked 2026-08-06: user pointed at Google Drive writing + their
Substack blog (perfectpolitics.substack.com → archiecarter.substack.com,
"Perfect Politics"), then refined: "have it be a merged voice which
predominantly sounds like me and then punch it up and make it sound more
mature and wise and insightful."

Process that worked:
1. **Fetch/read the voice samples BEFORE drafting.** web_extract the blog
   posts; find local writing (journal, notes, drafts). Read at least 2
   samples fully. Extract the register: sentence rhythm, word-choice level,
   paragraph openings, punctuation habits, recurring tics, how they handle
   transitions, first-person habits, self-disclosure level.
2. **Characterize the register in one paragraph** so the rewrite has a spec.
   From the worked example: first person throughout; plain Anglo-Saxon verbs
   next to philosophical vocabulary; honest self-disclosure without
   apology; concrete specifics over abstractions; earnest sincerity, not
   irony; theory as a lived lens ("made something click into place in my
   head"); zero corporate polish; humility about own position ("this is
   conjecture... but it's the best explanation I can guess").
3. **Draft in that voice, then PUNCH IT UP.** The refinement is deliberate:
   predominantly the user's voice, elevated — composed, weighted, more
   reflective. Add the wise/insightful lines that do the reflective work
   ("the difference between a system that says it respects your judgment and
   one that provably does," "move the honesty out of the persona and into
   the machinery," "a stated rule is a promise; a verifier-guarded rule is a
   fact"). The user's voice is the base register; the punch-up is the
   insight layer. Do NOT flatten it back to neutral-professional.
4. **Voice applies to narrative documents; docs/ stay neutral.** The Discord
   report and README get the merged voice; technical reference docs
   (architecture.md, verification.md) read fine in a neutral register — keep
   them neutral.
5. **Keep the honesty markers from the validator rounds** (n=1 caveat,
   stated-plainly authorship, "find the 23rd error") — they're already the
   right register for this user; they're part of why the voice matches.
6. **Scope check is part of the voice.** This user's architecture is
   home-lab only, explicitly NOT a workplace/enterprise system, and work-
   based machinery (OneDrive/SharePoint sync) was called "not necessary."
   Public deliverables must carry that framing ("Where it runs: a home
   lab... It was never meant to be a workplace system") — it's a statement
   of who the project is for, not a detail.
