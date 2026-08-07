# Phase 13 Self-Review — findings (pre-external-verdict)

Date: 2026-08-07
Status: SELF-REVIEW FINDINGS — Pip's own critical pass over the Phase 13
live-wire build, recorded BEFORE the external judge/Locus verdicts arrive.

## Findings

1. **[FIXED] SKILL.md lacked the demonstrated-vs-pending boundary.** The
   skill instructed "run via run_dojo_session.py" without stating that the
   demonstrated path is deterministic machinery and a genuine human-facing
   live LLM session is PENDING (absence register: human-session-pending).
   A fresh agent loading the skill could be misled into claiming a live
   session happened. Fix: added a "Demonstrated vs pending" section
   stating what is verified (gate wrapper, session driver, platform-wiring
   record) vs pending (genuine human session), with the explicit
   instruction "Do not claim a live human session occurred when only the
   driver demonstration exists."

2. **[CLEAN] All five gate modes work through the CLI wrapper.**
   Probes: --meaning low → ACT; --atrophy medium → SCAFFOLD;
   --branching high --insufficient → ASK; --protected identity_claim →
   DEFER; --manipulative → STOP. The wrapper preserves the engine's
   precedence.

3. **[CLEAN] Two-typed quarantine load-bearing rule in the wrapper.**
   Probes: Q2 without confirmation → BLOCKED; Q2 WITH --user-confirmed →
   licensed; Q2 with BOTH --user-confirmed AND --user-rejected →
   BLOCKED (user-rejected outranks confirmation). The FAOS-clearing-
   never-licenses-use rule holds through the CLI.

4. **[FIXED EARLIER] Absence register honesty.** The first edit flipped
   post_meld_live_llm_session to class=recorded — overclaiming: the
   driver session is deterministic, NOT a genuine live LLM session with a
   human. Corrected to class=human-session-pending with the blocks text
   naming the platform-wired boundary and the driver demonstration as
   evidence. The session record note was also corrected to
   "platform wiring demonstration."

5. **[NOTED] verify_phase7 needed Phase 13-era updates.** The mirror sync
   (new packages, docs/, witnesses, graph, T2R) tripped verify_phase7's
   Phase 7-era expectations (8 packages, 48 T2R entries, docs/ absent).
   All three failures were verifier staleness, not estate defects:
   SKILL_PKGS extended to 10, T2R count 52, docs/ added to the
   historical-provenance exceptions. The mirror's graph index + T2R were
   ALSO stale (my initial sync missed them) — synced from canonical.

## Verification before external verdicts

- run_gate.py: all 5 modes + quarantine rulings (exit 0 per call)
- run_dojo_session.py: lists 5 dojos; Ambivalence session walked 6
  stages, 3 guards armed, 6-pass close TRUE, record written
- verify_phase13.py: PASS (28 checks)
- verify_all.py full gate: PASS (14 verifiers, exit 0)
- FAOS canonical suite: PASS

## Expected external input

- judge_deepseek_phase13.txt (adversarial)
- locus_validation_phase13.txt (7-check discipline)
