# Phase 6 — Practice Dojo Routines: Index and Integration Layer

Project: Motivational Ecology Agent Architecture
Phase: 6 of 8 — the ConvoDojo practice layer
Date: 2026-08-06
Status: COMPLETE — all five dojos built, verified, reviewed, and revised
(revision round 2026-08-06). Conversation, Coaching, Ambivalence, Conflict,
Workplace dojos + integration index. Structural verification 41/41; durable
verifier at council_notes/verify_phase6.py.
Evidence discipline: Valens-style. VERIFIED = grounded in fetched evidence or built
artifacts inspected; RECONSTRUCTED = design application or inference, flagged as such;
declared-but-unverified inventory entries are marked DECLARED. User retains interpretive
sovereignty; insights are hypotheses, never facts.

---

## 1. The Five Dojos and Their Inventories

All five dojos live under `routines/<Dojo>_Dojo/` in this harness (source:
Ecology/Foundation/Phase6_Dojo/). Each is a
**seven-artifact content package** (see §2.1) consumed by the shared operating skill
`ConvoDojo_Practice_Sparring` (Phase 3, layer 5, skill_graph node `ConvoDojo_Practice_Sparring`).

| Dojo | Directory | Personas | Rubrics | Stage families |
|---|---|---|---|---|
| Workplace Communication | `Workplace_Dojo/` | 3: p_maya_crossfunctional (peer, conflicting priorities), p_daniel_manager_feedback (manager, feedback), p_elinor_stakeholder (sponsor, terse) | 3: professional_clarity_v1, feedback_effectiveness_v1, workplace_negotiation_align_v1 | Spine: engage → clarify-objective → explore-options → negotiate-align → commit-close; speech acts: give-feedback, request, delegate, disagree-professionally |
| Conversation | `Conversation_Dojo/` | 3: p_maya_chatty_colleague, p_dev_terse_flatmate, p_liam_topic_hopper | 3: listening_and_followup_v1, small_talk_flow_v1, clarity_and_repair_v1 | engage → explore → repair → challenge → consolidate → close |
| Coaching | `Coaching_Dojo/` | 3: p_aria_stuck_lead, p_ronan_advice_seeker, p_soham_high_achiever | 3: powerful_questions_v1, grow_structure_v1, listening_ownership_v1 | engage → explore → challenge → consolidate → close |
| Ambivalence | `Ambivalence_Dojo/` | 3: p_maia_career, p_devon_exercise, p_robin_caregiving | 3: amb_mi_fidelity_v1, amb_spirit_gate_v1, amb_sustain_talk_navigation_v1 | engage → discern-ambivalence → explore-both-sides → evoke-change-talk → consolidate → close |
| Conflict | `Conflict_Dojo/` | 3: p_marcus_arch, p_elena_vendor, p_ines_sibling | 3: conf_deescalation_v2, conf_interest_based_v1, conf_emotional_safety_v1 | engage → de-escalate → separate-positions-from-interests → reframe → generate-options → close |

Status: ALL FIVE VERIFIED (artifacts built and inspected; structural checks 41/41
passed; revised 2026-08-06). Persona/stage/rubric names above are the built inventories.

---

## 2. Cross-Dojo Conventions

### 2.1 The seven-artifact shape
Every dojo is exactly seven artifacts, in ConvoDojo style and schema (ecology-dojo/*/0.1):

1. `dialogue_state_machine.json` — staged dialogue control; entry/exit conditions per stage; coach controls transitions.
2. `persona_config.yaml` — sanitized persona bank; persona module only generates turns.
3. `rubric.json` — rubric bank; lenses, not verdicts.
4. `sparring_intensity_profile.json` — calibrated pushback levels 1–5 + escalation/de-escalation policy + sycophancy guard.
5. `in_session_coaching_rules.md` — the coach module (control plane): stage rules, intensity, feedback, safety.
6. `debrief_template.md` — evidence-grounded debrief; provisional until the user reviews.
7. `transfer_scenario_set.md` — base + transfer scenarios; generalization tests.

The Phase 3 `ConvoDojo_Practice_Sparring` SKILL.md is the shared executor: its AtomicOps
(select_scenario, configure_persona, set_intensity_profile, open_stage, advance_stage,
generate_interlocutor_turn, coach_interrupt, apply_rubric_lens, calibrate_pushback,
run_adversarial_stress_test, debrief_session, run_transfer_scenario,
check_psychological_safety) consume any dojo's artifacts. A dojo is not a new skill
node; it is content for the existing ConvoDojo node (RECONSTRUCTED — Phase 5 handoff:
"Phase 6 builds the ConvoDojo layer", and the skill graph already carries
ConvoDojo_Practice_Sparring as the practice node).

Internal conventions across the seven artifacts (enforced by verify_phase6.py):
- State machines declare `hard_gates` in `transition_policy` — dojo-specific safety
  invariants (e.g., Workplace: no_personal_attack, power_gradient_guard,
  no_forced_commitment) that no intensity level may cross.
- Intensity profiles declare `user_agreement.required: true` — intensity is set with
  the user, never assumed.
- Every artifact carries VERIFIED + RECONSTRUCTED evidence flags at DATA level
  (YAML comments do not count; grounding blocks in JSON/YAML, flag lines in markdown).

### 2.2 Coach/persona separation (invariant)
- Persona module generates turns; coach module controls staging, intensity, feedback.
- The persona never evaluates the user and never knows the user's lattice insights
  (Ma 2025 VERIFIED — persona priming degrades performance and embeds bias; also a
  manipulation guard).
- The coach recommends; the user decides. Coaching is on_demand by default.
- Ground: EasyMED 2025 (VERIFIED — persona/case module separated from response
  generation) and Voigt 2025 (VERIFIED — trainee roles separated from feedback/tutor roles).

### 2.3 Rubric-as-lens rule
- Rubrics are lenses, not verdicts: every score anchors to ≥1 utterance-level quote.
- No rubric score becomes a verdict about the user as a person.
- Automated scoring (Han 2026 VERIFIED — ~52.6% auto-coding accuracy) is an input
  requiring evidence anchoring, never final.
- Debriefs consume rubric output with evidence sections; the user corrects the record.

### 2.4 Fade policy (Phase 5 governs sparring scaffolding)
- Per `governance/scaffolding_fade_rules.md` §3.5 (harness governance layer), ConvoDojo pairs with
  Proximal_Practice_Selector: the sparring partner's scaffolding **fades across
  sessions** — coach hints and stage scaffolding descend the ladder (5 → 0) on
  unassisted-competence evidence, one rung per step, through re-assessment windows.
- Escalation is proficiency-gated (default) or user-requested; transfer scenarios
  run only after sustained proficiency ≥ 2.
- **What never fades** (scaffolding_fade_rules.md §7): the empowerment boundary,
  consent, and the right to ask for help anytime. A faded scaffold is a smaller help,
  never a smaller user.
- Fade decisions are RECONSTRUCTED policy: hypotheses about capability, tested on the
  unassisted track, user-reversible at any time (Restore_Scaffold, Reopen_User_Choice).

---

## 3. Theory-Core Map (with evidence flags)

Each dojo is anchored to a theory core. Flag convention: the theory field itself is
marked VERIFIED when Phase 1–2 evidence directly supports it; the dojo *application*
is separately flagged (almost always RECONSTRUCTED — the design step is ours).

| Dojo | Theory core | Flag |
|---|---|---|
| Conversation | Communication theory: dialogue acts, pragmatics, conversational coherence (Gricean implicature, turn-taking) | RECONSTRUCTED application (field canonical; not directly verified in Phase 1–2 digest) |
| Coaching | Coaching psychology / positive psychology (inquiry-based coaching, GROW-style structure); SDT need support | RECONSTRUCTED application; SDT component VERIFIED (digest Area 3: Li 2025, Wang 2025, Ma & Chen 2025) |
| Ambivalence | Motivational Interviewing (spirit: partnership/acceptance/compassion/evocation; DARN-CAT change talk) | VERIFIED (digest Area 1: Aimi/Shenoi 2026 MISC-2 fidelity; Lim 2025 HMM change-talk dynamics; Mahmood 2025 MIBot; Kuchipudi 1990 spirit gate) |
| Conflict | Conflict resolution / interest-based negotiation (positions vs interests; getting-to-yes tradition; de-escalation) | RECONSTRUCTED application (canonical field; not directly verified in digest) |
| Workplace | Organizational communication (coordination, feedback, power gradients, genre/channel register) | RECONSTRUCTED application; role-play mechanism VERIFIED (digest Area 6: EasyMED 2025 comparable outcomes + psychological safety; AgentForge 2026 coordination demands drive learning; Rudolph 2025 authenticity gap; Ma 2025 persona-bias caution) |

The through-line for all five: LLM role-play partners are viable practice tools when
structural separation is respected (EasyMED, Voigt — VERIFIED), and the practice layer
serves user long-run capability, never task completion (digest Cross-Area Convergence 1,
RECONSTRUCTED synthesis of VERIFIED sources).

---

## 4. Lattice and Skill-Graph Links

### 4.1 Practice logs → lattice (observations)
- Dojo practice logs and debriefs are **observations** for the motivational lattice
  (skill_lattice_interface.md §1.1 flow: skill outputs become new observations — the
  lattice refreshes). Capture is consent-scoped (capture_observation, MLG op) and
  **never surveillance**: practice data stays in practice
  (empowerment_boundary.md §4.2; lattice Q5_SURVEILLANCE_RISK).
- Change-talk signals from dojo logs (esp. Ambivalence_Dojo) may trigger insight
  formation per insight_trigger_policy T3 — change-talk enters conversation only via
  evocation, never as accusation (VERIFIED — Lim 2025 HMM dynamics; MI spirit).
- Lattice insights may inform scenario selection and intensity calibration ONLY with
  user consent and provisional marking; the persona is never scripted from lattice
  insights about the user (skill_lattice_interface.md §2; Ma 2025).
- Insight instances populate at runtime (lattice_index.json status: SEED).

### 4.2 Dojos → skill graph (ConvoDojo edges)
- All five dojos execute through `ConvoDojo_Practice_Sparring` (skill_graph_index.json,
  layer 5, built). Existing edges apply unchanged:
  - `recovers_with: ConvoDojo_Practice_Sparring → Human_Empowerment_Boundary`
    (sparring overreach → boundary reset; RECONSTRUCTED, kind=cross-skill)
  - `can_follow`/`supports`: MLG can_follow_into ConvoDojo; HEB supports * via
    boundary_gate (Phase 4 decision 7)
- Dojo practice logs feed the lattice refresh loop (4.1); lattice insights feed back
  into scenario/intensity selection (consent-gated). Closed loop, never closed circle:
  the user's verdict arbitrates every pass (skill_lattice_interface.md §1.1).
- No new graph nodes are added by Phase 6 (RECONSTRUCTED — dojos are content packages
  for the existing node, per §2.1).

---

## 5. Governance

- **Phase 5 safeguards govern all dojos.** The five Phase 5 documents
  (empowerment_boundary.md, agent_deference_rules.md, learnability_state_schema.json,
  skill_atrophy_risk_check.md, scaffolding_fade_rules.md) apply estate-wide; the dojo
  layer is explicitly named in their scope (scaffolding_fade_rules.md §3.5; Phase 5
  README handoff).
- **HEB gate required.** Every AtomicOp in a dojo session runs under the boundary gate
  (skill_graph_index.json governance; skill_lattice_interface.md §6): no AtomicOp
  executes on high-meaning tasks (identity, values, commitments, interpretive closure)
  without a Human_Empowerment_Boundary check first. Dojo practice is a SCAFFOLD-mode
  activity under HEB mode selection; escalation ladder L1–L5 applies (sparring
  overreach → boundary reset).
- **Intensity is user-owned.** Pushback level is set with the user, escalated by agreed
  policy, de-escalated on any overwhelm signal. Psychological safety outranks challenge
  at every level (EasyMED 2025 VERIFIED).
- **Real-conversation boundary.** Dojos rehearse skills; they never script, authorize,
  or commit the user's real-world words or decisions (in_session_coaching_rules.md §7;
  HEB preserved_user_decision set).
- **Evidence register for this index:** EasyMED 2025, AgentForge 2026, Voigt 2025,
  Rudolph 2025, Ma 2025, Han 2026, Lim 2025, Aimi/Shenoi 2026, Mahmood 2025,
  Kuchipudi 1990 — all VERIFIED (digest Areas 1, 3, 6). Cross-dojo conventions and
  theory-core applications — RECONSTRUCTED (this document). Thresholds are calibration
  anchors, not study-validated norms.

## 6. Open Items
- ~~Verify Conversation/Coaching/Ambivalence/Conflict dojo inventories on build
  completion and update §1.~~ DONE in the 2026-08-06 revision round — all five
  dojos verified (41/41 structural checks), inventories confirmed, §1 updated.
- Runtime enforcement of the HEB gate beyond declarations (Phase 5+ wiring; policy fully
  specified in skill_lattice_interface.md §6 and empowerment_boundary.md §7).
- skill_load_score → skill_load_trend conversion op (PPS writes, HEB derives) —
  documented in T2R_traceability.json; dojo logs are a first-class input to it.
