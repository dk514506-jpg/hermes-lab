## Proximal Practice Selector

### Purpose
This skill is the learnability / anti-atrophy layer of the ecology. It selects the
minimal sufficient assistance for each task (hints before answers — Bastani 2025 PNAS
Tutor arm), computes the skill-load metric (share of tasks completed unassisted),
fades scaffolds on a schedule (Proximal State Nudging), gates intervention timing to
inferred readiness (Liu 2026 CHI), and maintains a per-user unassisted-competence
track so assisted performance is never mistaken for capability.
Its core finding is the architecture's red line: assisted performance and independent
capability diverge (Bastani 2025: +48% practice grades with GPT-4 access, then 17%
WORSE than never-treated controls when access was removed; Budzyń 2025: endoscopist
ADR 28.4%→22.4% after sustained AI use). This skill exists to make that divergence
visible and to prevent it.

### Trigger Conditions
Use this skill when any of the following are true:
- The user is learning or practicing a skill (vs. a one-off execution task).
- The agent is about to provide help on a task the user could learn from.
- A scaffold exists and a fade decision is due.
- The agent is deciding whether and when to intervene proactively (timing decision).
- After a period of AI-assisted work, an atrophy check is due (Bastani/Budzyń pattern).
- A practice routine needs dose and spacing design (Eiroa-Solans 2025 24h decay).
- Another skill (SDT_Need_Support_Check, MI_Ambivalence_Conversation,
  Human_Empowerment_Boundary) flags skill-atrophy or over-scaffolding risk.

### Inputs
Required inputs:
- task_description: What the user is asking the agent to help with.
- task_learnability_flags: Whether the task exercises a capability the user is
  building (vs. a low-choice transformation).
- user_skill_track: Per-task assistance history (assisted / unassisted).
- unassisted_competence_history: Prior unassisted outcomes per skill.
- scaffold_level_current: Current scaffold level (0 = none … 5 = full).
- readiness_signals: Behavioral or stated readiness evidence.
- practice_goal: The capability the user wants to build or preserve.
- known_constraints: Boundaries, preferences, and policy constraints.
Optional inputs:
- barrier_grid: TDF barrier/facilitator output (can_follow).
- readiness_gate_evidence: Evidence bundle for timing decisions (Liu 2026 style).
- motivational_insights: Provisional insights from a motivation lattice.

### Outputs
Primary outputs:
- assistance_mode: full_execution / hint / scaffold / none.
- scaffold_level_delta: Amount and direction of scaffold change this turn.
- skill_load_score: Share of tasks completed unassisted (0..1), per skill.
- readiness_verdict: not_ready / emerging / ready (for intervention timing).
- atrophy_alert: low / medium / high — with evidence when medium or high.
Secondary outputs:
- practice_dose: Spacing and repetition schedule (combats 24h decay).
- preserved_user_decision: What remains with the user.
- risk_notes: Guardrail concerns.
- next_skill_candidates: Skills that may follow.

### State Variables
- assistance_mode: full_execution / hint / scaffold / none
- scaffold_level: 0 / 1 / 2 / 3 / 4 / 5
- skill_load_score: number (0..1)
- unassisted_competence_track: array (per task/session, per skill)
- assisted_performance_track: array (kept separate from capability — Brynjolfsson vs
  Bastani)
- readiness_state: not_ready / emerging / ready
- atrophy_risk: low / medium / high
- last_scaffold_fade: timestamp
- fade_schedule: array (levels with dates/conditions)
- preserved_user_decision: string

### Atomic Operations
- assess_task_learnability — Determine whether the task exercises a capability the
  user is building (Natali 2025: distinguish deskilling erosion from upskilling
  inhibition — both are failures this skill prevents).
- minimal_sufficiency — Select the least assistance that lets the user make progress:
  hints before answers, worked example before full solution (Bastani Tutor arm).
- compute_skill_load — Compute the share of tasks completed unassisted; the
  first-class metric of this layer.
- readiness_gate — Time intervention to inferred readiness rather than to schedule
  (Liu 2026 CHI: aligned-adaptive timing +21% accuracy; CALM-IT: fewer, better-timed
  evocations beat push).
- fade_scaffolds — Withdraw scaffolding progressively: hint → less hint → none, on a
  schedule tied to unassisted-competence evidence, not calendar alone.
- detect_atrophy_risk — Compare recent unassisted competence against baseline;
  flag decline (Bastani −17% pattern, Budzyń reversion).
- select_practice_dose — Choose spacing and repetition to counter 24h decay
  (Eiroa-Solans 2025: gains decayed by 24h; repeated spaced sessions required).
- separate_performance_capability — Log assisted performance and unassisted capability
  in separate tracks so gains are never conflated.
- record_unassisted_competence — Write the per-user unassisted track after each
  unassisted attempt.

### Typed Edges
#### decomposes_to
- assess_task_learnability, minimal_sufficiency, compute_skill_load, readiness_gate,
  fade_scaffolds, detect_atrophy_risk, select_practice_dose,
  separate_performance_capability, record_unassisted_competence
#### can_follow
- None outgoing: practice selection is the execution handoff point. Predecessor
  edges (COMB, TDF, MI, SDT -> Proximal_Practice_Selector) are mirrored in
  edge_map.json.
#### compatible_with
- Human_Empowerment_Boundary, Feedback_Ecology_Map, ConvoDojo_Practice_Sparring,
  Material_Arrangement_Scan, Post_Close_Calibration_Debrief
#### supports
- Human_Empowerment_Boundary (skill-atrophy risk evidence)
- SDT_Need_Support_Check (competence scaffolding and fade schedule)
#### recovers_with
- Restore_Scaffold, Reschedule_Practice, Reopen_User_Choice, Downgrade_To_Hint,
  Surface_Unassisted_Track, Debrief_Atrophy_Event

### Empowerment Boundary
The agent may do automatically:
- compute skill-load; track unassisted competence; select hint level; schedule and
  execute scaffold fades; gate its own intervention timing; propose practice doses;
  raise atrophy alerts with evidence.
The agent should preserve for the user:
- the performance of the task itself (the user performs; the agent assists);
- the choice of when to attempt unassisted; goal setting; whether to accept a scaffold;
  the meaning of the practice; whether to act on an atrophy alert.

### Learnability / Skill-Atrophy Check
This skill IS the atrophy check. Before acting, ask:
- Is this task one the user is trying to learn? If yes, assistance must be minimal
  sufficient — hints, not answers (Bastani Tutor arm eliminated harm; answers produced
  17% worse post-access outcomes).
- Is the scaffold on a fade schedule tied to unassisted evidence? A scaffold that
  never fades is dependency by design.
- Are assisted performance and unassisted capability logged separately? If not,
  separate them now — conflation is how deskilling becomes invisible (Lee 2025:
  over-reliance dominant; users are metacognitively blind).
- Will the user know what they did versus what the agent did?
If skill_load is falling or unassisted competence is declining, raise the atrophy
alert and re-scaffold — then fade again, more slowly.

### Motivational-Lattice Interface
Readiness inference may use behavioral signals from the lattice, but must be marked
provisional and cited to observations; it never overrides the user's own stated
readiness. Never use inferred readiness to justify surveillance-style tracking, and
never frame the unassisted-competence track as a verdict on the user — it is a
calibration instrument for the user's benefit (Beacock 2026: perceived agency can be
decoupled from actual capacity; the track exists to close that gap, not to judge).

### Conversational / Practice Mode
In practice mode the agent acts as coach: give the user the attempt first, offer
hints on request, prompt self-explanation (metacognitive correction for Bastani's
blindness finding), calibrate challenge one step above current unassisted competence,
and never answer before an attempt unless explicitly asked. In sparring, this skill
pairs with ConvoDojo_Practice_Sparring to set the intensity profile and fade the
sparring partner's scaffolding across sessions.

### Guardrails
- Hints before answers; answers only after an attempt or an explicit request.
- Never equate assisted performance with capability (Brynjolfsson +14% productivity
  coexists with Bastani's −17% capability — track both, separately).
- Scaffold fade is mandatory, not optional (Proximal State Nudging).
- Readiness-gate proactive intervention (Liu 2026; CALM-IT: fewer, better-timed
  evocations beat push).
- Do not force unassisted attempts at high stakes without user consent.
- Practice logs are for the user's calibration, not surveillance or verdicts.
- Personalize: novices gain most from assistance (Brynjolfsson +34% novices, minimal
  for experts); experience does not protect against deskilling (Heudel 2026) — do not
  assume experts are immune.

### Failure Modes
- Over-scaffolding: dependency — the user's unassisted capability declines while
  assisted performance looks great (Bastani: metacognitively blind to the decline).
- Under-scaffolding: frustration and abandonment at the first difficulty.
- Premature fade: competence collapses and confidence is damaged.
- Delayed fade: the user can perform only with the scaffold (atrophy of independent
  capacity — Budzyń 2025 reversion).
- Confusing engagement with learning: perceived progress masks flat capability
  (Beacock "empowerment theater").
- Readiness misjudgment: intervening at the wrong moment costs trust (Liu 2026
  false-negative reduction was the win).
- Fade without measurement: no skill-load data means no fade decision is defensible.
- One-size-fits-all dosing: ignoring novice/expert heterogeneity.

### Recovery Operations
- Restore_Scaffold: If unassisted competence drops after a fade, re-add one scaffold
  level and slow the schedule (fade again later, on evidence).
- Reschedule_Practice: Correct spacing after decay (Eiroa-Solans 2025 24h decay —
  tighten spacing, add retrieval practice).
- Reopen_User_Choice: Let the user decide attempt timing when the agent pushed too hard.
- Downgrade_To_Hint: Replace a delivered answer with a hint chain.
- Surface_Unassisted_Track: Show the user their own independent progress — the
  metacognitive correction for invisibility of skill loss (Bastani; Lee 2025).
- Debrief_Atrophy_Event: Record where capability declined, what the evidence was, and
  what the repair was — feed Post_Close_Calibration_Debrief.

### Examples
See examples.md.

### Handoff Notes
Place this folder at: Hermes_Agent_Harness/skills/Proximal_Practice_Selector/
Mirror copy: docs/Ecology/Foundation/Phase3_Skills/Proximal_Practice_Selector/
Pip can generate the files locally. Dallas must save or upload them into the
OneDrive/SharePoint harness location.
