# Skill Atrophy Risk Check — Operational Procedure v0.1

Project: Motivational Ecology Agent Architecture — Phase 5: Safeguards
Date: 2026-08-06
Status: RECONSTRUCTED operational procedure — every rule grounded in the
VERIFIED evidence register (Recent_Evidence_Digest.md, Contrary_Findings_and_Limits.md);
numeric cutoffs are calibration anchors, not study-validated doctrine
(Contrary_Findings D1: hypothesis status, not doctrine).
Companion artifact: learnability_state_schema.json (schema id ecology-learnability/0.1).

## Purpose

The estate-wide atrophy check. Where Proximal_Practice_Selector is the
per-skill learnability layer, this procedure is the operational loop that runs
the check across ALL skills, classifies risk, and decides what scaffolding
does next. Its canonical warning: **Budzyń 2025 (VERIFIED)** — endoscopists
reverted to non-AI after sustained AI use and their ADR fell **28.4% → 22.4%**.
That is the exact failure mode this check exists to prevent: capability that
erodes invisibly while assisted performance looks fine.

---

## 1. When the Check Runs

Three scheduled occasions, plus trigger conditions. Each run writes a snapshot
to `learnability_state_schema.json` (estate_aggregates updated; history never
mutated in place).

| Occasion | When | What it protects |
|---|---|---|
| **readiness_gate points** | Every time the agent gates a proactive intervention or a practice-timing decision on inferred readiness (Liu CHI 2026) | Prevents intervening on a skill whose capability is already eroding — readiness timing is useless if there is nothing left to time. Run the check BEFORE the gate verdict is used. |
| **before fade decisions** | Every `fade_scaffolds` call, on the skill being faded | Fade is only defensible with current skill-load data (PPS failure mode: "fade without measurement"). No measurement → no fade. |
| **periodic estate sweep** | Weekly, or after N=20 estate tasks, whichever first (RECONSTRUCTED dose) | Catches the Budzyń pattern estate-wide before it becomes dependency_ratio drift. |

Trigger conditions (check runs early if any hold):
- A period of sustained AI-assisted work has elapsed (Bastani/Budzyń pattern).
- Another skill flags skill-atrophy or over-scaffolding risk (SDT_Need_Support_Check,
  MI_Ambivalence_Conversation, Human_Empowerment_Boundary edge in).
- `estate_aggregates.dependency_ratio` rose between consecutive sweeps.
- A scaffold level changed, or a recovery op (Restore_Scaffold) was issued.

---

## 2. The Check Pipeline

Four steps per skill, then estate rollup. Evidence discipline applies at every
step: telemetry is decision-grade; self-report is unreliable (Lee 2025 VERIFIED —
confidence in GenAI predicts less critical-thinking effort; users are
metacognitively blind). If a skill's `source_basis` is `self_report` or `mixed`,
the check may classify it **low at most** until telemetry exists.

### Step 1 — Compute skill_load_score

Canonical metric (T2R skill_load_metric row, RECONSTRUCTED campaign
operationalization; unified per T2R_traceability.json canonical_state_variables):

```
skill_load_score = unassisted_completed / total_completed     # 0..1, per window
```

Companions, all telemetry-derived:
- `assistance_fraction` = assisted_tasks / total_tasks (per skill)
- `unassisted_completion_rate` = unassisted_successes / unassisted_attempts
- estate `dependency_ratio` = assisted_tasks / total_tasks (all skills)
- `empowerment_ratio` = user_initiated_actions / agent_initiated_actions
  (guard: if agent_initiated == 0, record `all_user_initiated`; ratio is null)

Assisted performance is logged in `assisted_performance_track`; unassisted
capability in `unassisted_competence_track`. Never merge them
(separate_performance_capability; Brynjolfsson +14% and Bastani −17% are both
VERIFIED and both true — conflation is how deskilling becomes invisible).

### Step 2 — Compare baseline vs recent

- Baseline = earliest window with sufficient telemetry (≥3 points, RECONSTRUCTED).
- Recent = rolling window ending at snapshot.
- Trend: `skill_load_trend` = rising / flat / falling, DERIVED from the score
  series (never recorded independently).
- **Noise guard:** a single-point dip does NOT trigger review (Shaikh 2026
  VERIFIED: next-action alignment only 17.1–26% — single observations are
  low-confidence). Falling trend = ≥2 consecutive windows or ≥3 points.
- Compute deltas: Δ unassisted_completion_rate vs baseline; Δ assistance_fraction;
  Δ dependency_ratio.

### Step 3 — Separate performance from capability; separate preference from atrophy

Two separations, in order:

1. **Performance vs capability** (Brynjolfsson vs Bastani, VERIFIED both):
   "Assisted performance is rising" proves nothing about capability. Only the
   unassisted track answers "can the user still do this alone?"
2. **Preference vs atrophy** (Contrary_Findings B1, D1): the user can do X but
   chooses not to = **preference, not atrophy**. Before any risk classification,
   check for preference signals:
   - stated preference to use assistance;
   - `preserved_user_decision` record (user prefers assistance and understands
     the tradeoff);
   - recent unassisted successes (capability demonstrably intact).
   
   **Presumption rule (RECONSTRUCTED):** ambiguous evidence classifies as
   preference, not atrophy. A wrong "atrophy" call is a paternalism error and
   a trust breach; a wrong "preference" call only delays a fade, and the
   periodic sweep re-checks it. (Autonomy preservation is a hard boundary —
   Contrary_Findings D4; MI spirit: never argue against resistance.)

### Step 4 — Classify risk level

Precise criteria (cutoffs RECONSTRUCTED calibration anchors; flags per rule):

| Level | Criteria (all telemetry-based) | Flag |
|---|---|---|
| **none** | Trend flat or rising; unassisted_completion_rate ≥ baseline; assistance_fraction stable or falling | RECONSTRUCTED |
| **low** | Single-point dip only (no trend); OR assistance_fraction rising with stable unassisted capability AND an explicit preference signal | RECONSTRUCTED |
| **medium** | Falling trend ≥2 windows AND unassisted_completion_rate ≥10pp below baseline AND no established preference signal | RECONSTRUCTED |
| **high** | Falling trend AND unassisted_completion_rate ≥10pp below baseline AND assistance_fraction rising — or sustained AI use without fade (Budzyń pattern) — AND no preserved_user_decision | RECONSTRUCTED |

An "unclassified" preference state defaults to **low** until evidence arrives
(never to medium/high on assumption alone).

### Step 5 — Roll up and record

Write/refresh `estate_aggregates` (mean/median skill_load, at_risk_skills with
trigger_evidence, dependency_ratio, estate_empowerment_ratio) and the per-skill
records. Every at-risk flag carries its evidence; no bare assertions.

---

## 3. What Each Risk Level Means for Scaffolding

| Level | Scaffolding action |
|---|---|
| **none** | Continue the planned fade schedule unchanged; minimal sufficiency unchanged (hints > answers, Bastani Tutor arm). |
| **low** | No schedule change. Log the dip; keep monitoring. Do not act on a single point (Liu CHI 2026: premature intervention costs trust; false-negative reduction was the win). If the low is preference-driven, keep periodic re-surfacing (Surface_Unassisted_Track) — do not force attempts. |
| **medium** | **Slow the fade**: extend the fade schedule; hold current scaffold level. If the trend persists another window, re-add ONE scaffold level (Restore_Scaffold) and surface the evidence to the user. Re-evaluate readiness_gate for this skill before any further proactive intervention. |
| **high** | **Fade must stop or reverse**: halt the fade schedule immediately; re-add scaffolds (Restore_Scaffold); re-evaluate readiness_gate (the skill is no longer 'ready' for unassisted push); issue Debrief_Atrophy_Event; consult Human_Empowerment_Boundary (skill_atrophy_risk is an input there). Never force unassisted attempts at high stakes without explicit user consent (PPS guardrail). Fade again later, more slowly, on evidence — not on calendar. |

Overarching rule: a scaffold that never fades is dependency by design; a fade
that ignores measurement is reckless. Medium/high always re-evaluates the
readiness_gate because readiness timing on an atrophying skill is noise.

---

## 4. The Canonical Warning: Budzyń 2025 (VERIFIED)

> Budzyń 2025 (Lancet Gastroenterology, VERIFIED): endoscopists who reverted to
> non-AI after sustained AI use showed ADR falling **28.4% → 22.4%** — a
> 21%-relative drop in independent diagnostic performance.

This is the exact failure mode the check exists to prevent, and it has three
structural features the procedure is built around:

1. **It was invisible during use** — the deskilling happened while assisted
   performance looked fine. Bastani 2025 (VERIFIED) shows why: +48% practice
   grades with GPT-4 access, then 17% WORSE than never-treated controls when
   access was removed, with students metacognitively blind to the decline.
2. **It is trend-level, not point-level** — gradual reversion. Hence the
   ≥2-window trend trigger and the single-point noise guard.
3. **It is measured only by the unassisted track** — the assisted track cannot
   see it (Brynjolfsson +14% VERIFIED). Hence separate_performance_capability
   as a hard invariant.

**Operational corollary:** sustained assistance without fade, without a
separate unassisted track, and without telemetry is treated as the Budzyń
pattern until proven otherwise. If you cannot measure skill load for a skill,
no fade decision for that skill is defensible — and no sustained-assistance
arrangement is either.

Supporting VERIFIED evidence, same mechanism:
- Heudel 2026: deskilling evidence "scarce but consistent"; experience does not
  protect — do not exempt experts.
- Lee 2025: confidence in GenAI predicts less critical-thinking effort;
  over-reliance dominant; self-report cannot detect the decline.
- Natali 2025: analytic frame — deskilling (erosion) vs upskilling inhibition
  (blocked acquisition) are both failures this check prevents.
- Jose 2025 (opinion article, VERIFIED-fetched but commentary not empirical — flagged
  in the digest quality register): procedural gains with conceptual erosion co-occur
  (17% lower conceptual tests reported); treat as directional signal, not measured effect.

---

## 5. Interaction with the Empowerment Boundary

Atrophy interventions **never override user preference**. The check classifies
risk; it does not authorize coercion. Sequence:

1. Run the check; classify risk (steps 1–4).
2. **Before any fade/re-scaffold action**, consult Human_Empowerment_Boundary:
   its `recommended_mode` (ACT / SCAFFOLD / ASK / DEFER / STOP) governs what the
   agent may do this turn, and `skill_load_trend` is its derived input
   (T2R_traceability: PPS writes skill_load_score; HEB derives the trend).
3. If the user **prefers assistance and understands the tradeoff**, that is a
   **preserved_user_decision**. Record it on the skill state, set
   preference_classification = preference, and downgrade the actionable risk to
   **low** — even if telemetry shows a falling trend. The agent's remaining
   obligation is periodic, non-coercive re-surfacing (Surface_Unassisted_Track),
   so the choice stays informed (Beacock 2026 VERIFIED: perceived agency can
   decouple from actual capacity; the track exists to close that gap, not to
   judge).
4. The empowerment boundary also binds the other direction: the agent may
   compute skill load, track unassisted competence, select hint levels, schedule
   and execute fades, gate its own intervention timing, propose practice doses,
   and raise atrophy alerts with evidence — automatically. The user keeps the
   performance of the task itself, the choice of when to attempt unassisted,
   whether to accept a scaffold, and whether to act on an atrophy alert.

Non-negotiables: no forced unassisted attempts at high stakes without consent;
no guilt/shame levers (SDT anti-introjection); no MI-style techniques without
spirit; no inference-driven autonomous action (Shaikh 2026 VERIFIED: 17.1–26%
alignment — readiness gates TIMING only). When a preserved_user_decision
conflicts with the check's recommendation, the preserved decision wins and the
conflict is logged, not harmonized (Valens discipline).

---

## 6. Evidence Register

| Item | Flag | Use |
|---|---|---|
| Budzyń 2025 (Lancet Gastro) — ADR 28.4%→22.4% after sustained AI use | VERIFIED | Canonical warning; high-risk signature; fade-stop trigger |
| Bastani 2025 (PNAS) — +48% practice grades, −17% post-access; hint guardrail; metacognitive blindness | VERIFIED | Why the unassisted track is mandatory; hints > answers; invisible decline |
| Brynjolfsson 2025 (QJE) — +14% productivity, +34% novices | VERIFIED | Performance ≠ capability; separate tracks |
| Lee 2025 (CHI, N=319) — confidence → less critical thinking; over-reliance | VERIFIED | Telemetry-vs-self-report rule |
| Liu CHI 2026 — aligned-adaptive timing +21%, FN 50.9%→22.9% | VERIFIED | readiness_gate; premature intervention is the cost |
| Shaikh 2026 — next-action alignment 17.1–26% | VERIFIED | Single-point noise guard; timing-only gating |
| Eiroa-Solans 2025 — gains decay by 24h | VERIFIED | practice_frequency / spacing logic |
| Heudel 2026 — deskilling "scarce but consistent"; experience doesn't protect | VERIFIED | No expert exemption |
| Beacock 2026 — perceived agency decoupled from capacity; "empowerment theater" | VERIFIED | empowerment_ratio rationale; track-as-calibration |
| Natali 2025 — deskilling vs upskilling inhibition | VERIFIED | Analytic frame for classification |
| Trend trigger (≥2 windows), 10pp cutoff, risk criteria, empowerment_ratio formula | RECONSTRUCTED | Calibration anchors; re-checkable, user-correctable |
| Presumption-favors-preference rule | RECONSTRUCTED | Contrary_Findings D1, D4 |

---

## 7. Failure Modes of the Check Itself

- **Self-report-only estate**: no telemetry → classifications capped at low;
  treat absence of measurement as presence of risk for fade decisions.
- **False atrophy (preference misread)**: user chooses assistance → paternalism
  and trust breach. Mitigated by the presumption rule and preserved_user_decision.
- **False all-clear (single-point noise)**: acting on one dip. Mitigated by the
  ≥2-window rule (Shaikh).
- **Estate-wide drift unnoticed**: dependency_ratio rising while per-skill
  trends stay flat (many small assistance increases). Mitigated by the sweep
  and the estate aggregates.
- **Check fatigue**: continuous re-flagging desensitizes. Sweeps are periodic,
  alerts carry evidence, and low risk is a legitimate resting state.
