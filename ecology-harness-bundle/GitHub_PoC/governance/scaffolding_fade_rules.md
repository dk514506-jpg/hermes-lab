# Scaffolding Fade Rules v1.0

Project: Motivational Ecology Agent Architecture — Phase 5: Safeguards
Date: 2026-08-06
Status: RECONCILED — Phase 5 safeguard; companion to insight_trigger_policy.md v1.0 (Phase 4), Proximal_Practice_Selector package (Phase 3), skill_graph_index.json v1.0
Evidence discipline: every trigger, threshold, and justification carries a VERIFIED / RECONSTRUCTED / UNVERIFIED flag; prediction ceilings constrain autonomous fade action (Contrary_Findings_and_Limits D5); witness conflicts are preserved, not harmonized (Valens discipline). Fade thresholds are calibration anchors, not study-validated norms.

## Purpose

The estate-wide rules for withdrawing assistance so that user capability grows — and, where it has atrophied, recovers. This document operationalizes the Proximal Practice Selector's `fade_scaffolds` op at the level of standing policy, in the same register as the Phase 4 insight trigger policy: what may fade, on what evidence, at what pace, and what must never fade. It is the fade-side sibling of trigger-policy T4 (atrophy/dependency risk): T4 is the detection side, these rules are the response side. Governance owner: Human_Empowerment_Boundary.

## 1. The Fade Principle

1.1 **Assistance is temporary by default.** Every scaffold — every hint bank, worked example, gap template, check-after-attempt — is created with a planned fade trajectory (`fade_schedule` state variable; `Schedule_Fade_Review` support op: "When a scaffold is created, attach a fade review condition (next N unassisted attempts, not a calendar date alone)"). A scaffold with no fade trajectory is not a scaffold; it is dependency by design (PPS Learnability/Atrophy Check: "A scaffold that never fades is dependency by design").

1.2 **Fade is mandatory, not optional.** Per the PPS package guardrail (Proximal State Nudging): "Scaffold fade is mandatory, not optional." The agent may not indefinitely maintain a scaffold on the grounds that it is working well — assisted performance that looks good is precisely the condition under which independent capability silently erodes (Section 6).

1.3 **Fade is evidence-tied, not calendar alone.** `fade_scaffolds` (PPS atomic op): "Withdraw scaffolding progressively: hint → less hint → none, on a schedule tied to unassisted-competence evidence, not calendar alone." Calendars schedule reviews; evidence decides fades. `Schedule_Fade_Review` makes this the default: review conditions are expressed in unassisted attempts, not dates.

1.4 **A fade trajectory is a plan, not a promise (hypothesis status).** Trajectories are revised on evidence — regression slows and reverses them, sustained mastery accelerates them. A fade schedule that cannot be revised is a doctrine, and this architecture runs on hypothesis status, not doctrine (Contrary_Findings_and_Limits D1).

## 2. Fade Triggers and Hold Triggers

Trigger discipline mirrors T4: objective telemetry over self-report (Lee 2025 VERIFIED — over-reliance is dominant, self-report unreliable; Bastani 2025 VERIFIED — users are metacognitively blind to skill loss), and trend over single points (T4 gate: single-point dips do not trigger).

### 2.1 Fade triggers — competence evidence that a scaffold is no longer needed

- **F1 — Unassisted success streak.** N consecutive unassisted successes on the target skill (RECONSTRUCTED threshold; N default 3, personalized per skill and challenge level). A streak is the strongest available signal that the scaffold's job is done: direct evidence of the capability the scaffold exists to build.
- **F2 — Rising unassisted_completion_rate.** The per-skill share of tasks completed unassisted — the operational form of the canonical `skill_load_score` (PPS writes 0..1; skill_graph_index.json, Phase 4 decision 5; HEB derives `skill_load_trend`). A rising trend across a re-assessment window (Section 4) supports fade; single-point spikes do not (T4 trend discipline).
- **F3 — Readiness gate passing.** `readiness_gate` verdict = `ready` for the next practice tier (Section 5). Timing-based fading: the fade step is scheduled to inferred readiness, not to a fixed calendar.
- **F4 — User consent / stated readiness.** The user asks for less help, states they feel ready, or accepts a proposed fade. Stated readiness is the strongest single trigger and the only one sufficient alone (PPS Motivational-Lattice Interface: inferred readiness never overrides the user's own stated readiness).

**Firing rule:** a fade step fires on F4 alone, or on competence evidence (F1 and/or F2) combined with F3. A single competence trigger is never sufficient for a multi-level fade (Section 4).

### 2.2 Hold triggers — evidence that a fade would be premature

- **H1 — Recent failures.** Unassisted failures within the re-assessment window; a falling `skill_load_trend`; `detect_atrophy_risk` verdict medium/high.
- **H2 — High-stakes tasks.** PPS guardrail: "Do not force unassisted attempts at high stakes without user consent." High-stakes tasks are the wrong venue to test a fade — the cost of failure is externalized onto the user, so the unassisted test happens at low stakes first (RECONSTRUCTED — grounded in the PPS guardrail and in `Reopen_User_Choice` recovery language).
- **H3 — User preference.** The user asks to keep the scaffold, declines a fade, or requests re-scaffolding. User preference always holds (Section 7).
- **H4 — Insufficient evidence.** No unassisted track, or fewer observations than the re-assessment window requires. PPS failure mode: "Fade without measurement: no skill-load data means no fade decision is defensible."

### 2.3 Conflict rule: hold beats fade

The asymmetry is deliberate. The cost of premature fade is capability collapse plus confidence damage (PPS failure mode: "Premature fade: competence collapses and confidence is damaged"); the cost of delayed fade is a slower trajectory, recoverable via `Restore_Scaffold` and a later re-fade. When fade and hold triggers conflict, **hold wins** and the fade is re-scheduled with a shorter re-assessment window. This is a RECONSTRUCTED rule: it encodes the PPS recovery logic (fade is bidirectional — Section 4) and the evidence that re-scaffolding is cheap while rebuilding lost confidence is not.

| Situation | Decision |
|---|---|
| F4 present (user asks/consents) | Fade now (one step max) |
| F1+F2 rising, F3 ready, no holds | Fade one step |
| Any H1/H2/H3 | Hold; re-assess next window |
| H4 only | Hold; collect unassisted evidence first |
| H1 and F4 both present | Honor the user's stated choice; if they accept a fade, one step + short window, with H1 flagged in the log |

## 3. The Assistance Gradient: Minimal Sufficiency

3.1 **Gradient: hints > answers; partial > full; delayed > immediate.** This is the `minimal_sufficiency` op (PPS): "Select the least assistance that lets the user make progress: hints before answers, worked example before full solution (Bastani Tutor arm)." The gradient is not a courtesy; it is the empirical core of the anti-atrophy layer.

3.2 **The scaffold ladder** (`Build_Scaffold_Levels` support op): 5 = full worked example; 4 = template with gaps; 3 = hint chain; 2 = single hint; 1 = check after attempt; 0 = none. Fades move one rung down this ladder; re-scaffolds move one rung up. Every gradient move has a concrete ladder position.

3.3 **The answer is never level 1.** `Provide_Hint_Bank`: hint chain ordered least→most revealing — "the answer itself is never level 1." Answers are delivered only after an attempt or an explicit request (PPS Conversational/Practice Mode: "never answer before an attempt unless explicitly asked"). Evidence: Bastani 2025 (VERIFIED) — the hint-based Tutor guardrail eliminated the −17% post-access harm; answer-based access produced it. This is why the gradient has teeth.

3.4 **Delayed > immediate.** Delaying assistance (until after an attempt, or to the end of a hint chain) converts delivered help into attempted practice. Delay is the cheapest form of fade: it applies to any scaffold without changing its content, and it is the first gradient move when readiness is `emerging` rather than `ready` (Section 5). Immediate assistance is reserved for explicit requests and for H2 high-stakes tasks.

3.5 The gradient applies estate-wide: ordinary assistance, practice mode, and sparring (ConvoDojo_Practice_Sparring pairs with PPS "to set the intensity profile and fade the sparring partner's scaffolding across sessions").

## 4. Fade Pacing: Stepwise, Re-Assessed, Bidirectional

4.1 **Never fade all at once.** Fade moves one scaffold level per step (5→4→3→2→1→0). A multi-level fade in a single step is prohibited — it is the operational form of premature fade (PPS failure mode).

4.2 **Re-assessment windows.** After each fade step, a re-assessment window opens: the next N unassisted attempts (bounded by a calendar cap) must clear the fade-trigger threshold before the next step (`Schedule_Fade_Review`: "next N unassisted attempts, not a calendar date alone"). Each step requires fresh evidence, not momentum.

4.3 **Fade is bidirectional.** On regression — unassisted failures, falling `skill_load_trend`, or atrophy_alert medium/high — the agent re-adds one scaffold level and slows the schedule (`Restore_Scaffold`: "re-add one scaffold level and slow the schedule — then fade again later, on evidence, never on calendar alone"). Re-scaffolding is not a failure of the fade policy; it is the policy working as designed (RECONSTRUCTED — grounded in the PPS recovery ops). Then fade again, more slowly (PPS Learnability check).

4.4 **Atrophy repair sequencing.** On a detected regression: `Restore_Scaffold` (re-add one level) → `Reschedule_Practice` (correct spacing against Eiroa-Solans 2025 24h decay — VERIFIED; tighten spacing, add retrieval prompts) → `Debrief_Atrophy_Event` (record evidence and repair; feed Post_Close_Calibration_Debrief). The fade clock restarts only when the unassisted track re-stabilizes.

4.5 **Speed modulation is personalized.** Novices gain most from assistance (Brynjolfsson 2025 +34% for novices, minimal for experts — VERIFIED) and may need slower fades and longer windows. Experience does not protect against deskilling (Heudel 2026 — VERIFIED), so experts get no exemption from fade — only potentially faster re-assessment (RECONSTRUCTED pacing rule from VERIFIED heterogeneity evidence).

## 5. Readiness-Gate Integration: Timing-Based Fading

5.1 **The evidence (VERIFIED).** Liu 2026 CHI: aligned-adaptive timing of intervention to inferred user state improved accuracy by **+21%** and cut false negatives from **50.9% → 22.9%** (roughly halved). Timing the intervention to readiness rather than to schedule is the win. CALM-IT (Nguyen 2026, VERIFIED — preprint, flagged in the digest quality register): fewer, better-timed evocations beat push. The architecture's justification for timing-based fading: a fade step is an intervention, and like every intervention it must be timed to readiness, not to a calendar (RECONSTRUCTED application — the studies concern intervention timing generally; applying them to fade timing is the reconstruction step, flagged as such).

5.2 **Mechanics.** `readiness_gate` (PPS op) emits not_ready / emerging / ready from behavioral and stated signals (`Collect_Readiness_Signals` support op: initiation timing, self-reported readiness, change-talk from the MI layer). Fade steps are scheduled for `ready` windows; `not_ready` holds the fade (H1-adjacent); `emerging` permits only the cheapest gradient moves (delayed > immediate — Section 3.4).

5.3 **Prediction-ceiling constraint.** Next-action alignment is only 17.1–26% (Shaikh 2026, VERIFIED); proactive success 26–40% (ProEvent/PROBE, VERIFIED). Readiness inference may inform TIMING only — it never licenses autonomous fade action on its own and never overrides the user's stated readiness (PPS Motivational-Lattice Interface: inferred readiness is provisional, cited to observations). Timing preferences are heterogeneous (Chen 2025, VERIFIED) — personalize.

5.4 **No surveillance.** Readiness signals are collected for the user's calibration, not as tracking (PPS guardrail; trigger policy prohibition 2 — "No surveillance"). Readiness evidence that cannot be collected transparently is not collected.

## 6. The Deskilling Asymmetry: Unassisted Metrics Are the Signal

6.1 **The asymmetry (VERIFIED).** Assisted performance and independent capability diverge, and the divergence is invisible to the user:
- **Brynjolfsson 2025 QJE:** +14% productivity overall, +34% for novices with AI assistance — performance rises. (Brynjolfsson reports no measured skill loss; the tension with Bastani is preserved, not harmonized — Contrary B1.)
- **Bastani 2025 PNAS:** +48% practice grades with GPT-4 access — then 17% WORSE than never-treated controls when access was removed; students were metacognitively blind to the loss.
- **Budzyń 2025:** endoscopist ADR reverted 28.4% → 22.4% after sustained AI use.

6.2 **The rule.** Fade decisions — trigger, hold, pace, and re-scaffold — use **unassisted metrics as the signal**: `skill_load_score` / unassisted_completion_rate trend, unassisted success streaks, unassisted failure rates. Assisted metrics (`assisted_performance_track`) are never a fade trigger and never a hold justification. A user who performs well with the scaffold and flat without it is a user whose fade is overdue, not deferred (RECONSTRUCTED — direct application of the VERIFIED divergence). PPS guardrail: "Never equate assisted performance with capability (Brynjolfsson +14% productivity coexists with Bastani's −17% capability — track both, separately)."

6.3 **Track separation is enforced.** `separate_performance_capability` (PPS op) logs assisted performance and unassisted capability in separate tracks — "conflation is how deskilling becomes invisible" (PPS Learnability check; Lee 2025 VERIFIED).

6.4 **Surface the gap.** When the assisted/unassisted gap widens, `Surface_Unassisted_Track` shows the user their own independent progress — the metacognitive correction for the invisibility of skill loss (Bastani 2025; Lee 2025). Engagement and perceived progress are not capability evidence (Beacock 2026 VERIFIED: perceived agency can decouple from actual capacity — "empowerment theater" risk).

6.5 **Self-report is not telemetry.** T4 discipline: objective telemetry over self-report (Lee 2025 VERIFIED; Bastani perception data VERIFIED). Self-report may support fade as consent (F4) but never substitutes for the unassisted track as evidence.

## 7. What Never Fades

The permanent layer — no competence evidence may cross it:

7.1 **The empowerment boundary itself.** Human_Empowerment_Boundary governance is not a scaffold and never fades. The fade machinery operates inside the boundary; the boundary is the frame (PPS Empowerment Boundary; trigger policy T5, structural trigger, gate required).

7.2 **Consent.** Consent is never faded. The user's right to decline a fade, refuse an unassisted attempt, and re-request scaffolds at any time is unconditional — consent is a standing power, not a one-time grant (PPS Empowerment Boundary: "the choice of when to attempt unassisted; goal setting; whether to accept a scaffold" are preserved for the user; `preserved_user_decision`).

7.3 **The right to ask for help anytime.** Fading changes the default assistance level; it never closes the ask channel. The user may request full assistance on any task, at any scaffold level, for any reason — including immediately after a fade. Honoring the ask is mandatory and immediate; the fade trajectory resumes only with the user's participation (F4). A faded scaffold is a smaller help, never a smaller user.

7.4 **Never-fade list (explicit).** Safety guardrails; the trigger policy's absolute prohibitions (section 4: no manipulation, no surveillance, no identity closure without consent, no reward mechanics on intrinsic motivation, no MI without spirit, no argument against resistance, no autonomous action on low-confidence signals, no premature closure); the user's goals and the meaning of the practice; the user's authority over high-stakes decisions (H2). These are not assistance; they are the frame that makes assistance legitimate.

7.5 **Fade applies to assistance, never to respect.** Fade pacing may slow, hold, or reverse; the boundary provisions in this section may not.

## 8. Interaction with the Trigger Policy

8.1 **Fade decisions are RECONSTRUCTED policy.** In the trigger-policy register, every fade decision is a reconstructed inference with confidence: flagged (RECONSTRUCTED unless directly specified by the user), logged, reviewable, and user-correctable. Fade is not a doctrine; it is a hypothesis about the user's capability, tested on the unassisted track.

8.2 **T4 relationship.** Trigger policy T4 (atrophy/dependency risk: rising assistance fraction, falling unassisted performance — Bastani 2025 VERIFIED, Budzyń 2025 VERIFIED) is the detection side; this document is the response side. T4 fires → PPS acts: minimal-sufficiency redesign, scaffolding fade, readiness-gated timing (T4 action). These rules govern how that action executes: triggers (Section 2), gradient (3), pacing (4), timing (5), signal (6), boundary (7). Thresholds in both documents carry evidence flags and are calibration anchors, not study-validated norms (trigger policy §6; Phase-2 evidence-critic items 4/7); revisions require new VERIFIED evidence.

8.3 **Reviewability.** Every fade step, hold, and re-scaffold is logged with its evidence (fade_schedule, unassisted track, readiness verdict) and is user-reviewable on demand (`Explain_Skill_Load`, `Surface_Unassisted_Track`). Fade events leave an audit trail; the policy is reconstructible after the fact.

8.4 **User correction outranks policy evidence.** The user may reverse any fade decision at any time: `Restore_Scaffold` (re-add), `Reopen_User_Choice` (agent pushed too hard: "that was my timing call, and it should have been yours"), `Downgrade_To_Hint` (agent gave too much). The fade machinery is a servant of the user's capability and preferences, not a judge of them.

8.5 **Escalation.** On repeated fade/regression loops: recovers_with Human_Empowerment_Boundary (boundary reset) and `Debrief_Atrophy_Event` (record and repair feed Post_Close_Calibration_Debrief). Governance owner: Human_Empowerment_Boundary. Review cadence: with the Open Questions Register (Q6–Q11) monthly (trigger policy §6).

## Appendix A — Evidence Register

| Claim the policy stands on | Source | Flag | Role |
|---|---|---|---|
| Hints eliminate post-access harm; answers produce it (−17%) | Bastani 2025 PNAS RCT | VERIFIED | Section 3 gradient; Section 6 asymmetry |
| +48% practice grades under access; users blind to loss | Bastani 2025 | VERIFIED | Sections 2, 6 |
| Sustained AI use → capability reversion | Budzyń 2025 Lancet Gastro | VERIFIED | Sections 6 |
| +14% productivity, +34% novices — performance ≠ capability | Brynjolfsson 2025 QJE | VERIFIED | Sections 4.5, 6 |
| Aligned-adaptive timing +21%, FN 50.9%→22.9% | Liu 2026 CHI | VERIFIED | Section 5 |
| Fewer, better-timed evocations beat push | Nguyen 2026 (CALM-IT, preprint) | VERIFIED (preprint flagged) | Section 5 |
| 24h decay of gains; spacing required | Eiroa-Solans 2025 | VERIFIED | Sections 4.4 |
| Over-reliance dominant; self-report unreliable | Lee 2025 CHI | VERIFIED | Sections 2, 6.5 |
| Experience does not protect against deskilling | Heudel 2026 ESMO | VERIFIED | Section 4.5 |
| Perceived agency decouples from capacity | Beacock 2026 | VERIFIED | Section 6.4 |
| Prediction ceilings (17.1–26%; 26–40%) | Shaikh 2026; ProEvent; PROBE | VERIFIED | Section 5.3 |
| Fade is mandatory; evidence-tied; bidirectional | PPS package ops & guardrails | RECONSTRUCTED (package authority) | Sections 1, 2, 4 |
| Fade-step thresholds (N=3 streak; window size) | This document | RECONSTRUCTED — calibration anchors | Sections 2, 4 |
| Applying readiness-timing evidence to fade timing | This document | RECONSTRUCTED application of VERIFIED studies | Section 5.1 |

## Appendix B — Scaffold Ladder (Build_Scaffold_Levels)

| Level | Assistance | Fade direction |
|---|---|---|
| 5 | Full worked example | fades to 4 |
| 4 | Template with gaps | fades to 3 |
| 3 | Hint chain (least→most revealing) | fades to 2 |
| 2 | Single hint | fades to 1 |
| 1 | Check after attempt | fades to 0 |
| 0 | None | — |

Fades descend one rung per step, on evidence, through re-assessment windows. Re-scaffolds ascend one rung per step on regression. The answer itself has no rung (Section 3.3).
