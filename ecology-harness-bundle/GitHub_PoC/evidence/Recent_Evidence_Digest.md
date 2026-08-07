# Recent Evidence Digest v1.0

Project: Motivational Ecology Agent Architecture — Phase 2: Recent Evidence Review
Date: 2026-08-06
Status: VERIFIED — assembled from council distillations (3 subagents, 70+ sources fetched)
Window convention (declared): primary 2025-01-01..2026-08-06 (strict "post-2024");
2024 papers marked "2024 (pre-window)" only when foundational or high-impact.
Evidence discipline: VERIFIED = fetched; RECONSTRUCTED = inference for
agent-applicability; UNVERIFIED = search-only, not fetched.

## Purpose

Post-2024 evidence across the plan's search areas, organized for synthesis.
Full citation details in Annotated_Bibliography.md; counter-evidence in
Contrary_Findings_and_Limits.md.

## Search Area 1: MI in coaching, health, education, justice, workplace, digital

- **AI-delivered MI is feasible and achieves human-level fidelity** — Aimi structured-workflow LLM coach matched a novice MI-trained human on MISC-2 fidelity (reflection-to-question ratio 0.84 vs 0.62; complex reflections 66.7% vs 50%; client change talk 90.8% vs 73.2%) (Shenoi 2026, VERIFIED). MIBot: 98% MI-adherent utterances, higher than typical human counselors, but perceived empathy lower (Mahmood 2025, VERIFIED). CALM-IT: fewer, better-timed evocations beat push (Nguyen 2026, VERIFIED).
- **But the ceiling is readiness, not behavior** — Karve 2025 scoping review: only 3/15 AI-MI studies showed substantial behavior change; 3 RCTs. Li 2025 RCT (N=177): readiness d=0.52, confidence d=0.54 — but vaccine hesitancy unchanged. Eiroa-Solans 2025 RCT (N=237): gains at 15 min, decayed by 24h, no behavior change. Implication (RECONSTRUCTED): repeated spaced sessions, not one-shots.
- **MI transfers to coercive settings** — Pinto e Silva 2025 meta (22 studies, justice-involved): attendance, dropout reduction, recidivism reduction in official records (VERIFIED). Peer-delivered MI feasible in military culture (Livingston 2026, feasibility only, VERIFIED).
- **Fidelity measurement is maturing** — automatic MI coding now ~52.6% accuracy (Han 2026, VERIFIED); LLM+HMM transition dynamics predict session quality at 0.80 LOOCV (Lim 2025, VERIFIED).
- **Training modality gates transfer** — VR MI training: usable, confidence up, but only 40% empathy with virtual patients, speech-recognition broke flow (Verhoeven 2025, VERIFIED).
- **2024 (pre-window):** Cohen 2024 established LLM-based MITI/CLEAR automated coding; Steenstra 2024 proved fully-generative MI delivery feasible (both RECONSTRUCTED via Mahmood 2025 citations).

## Search Area 2: COM-B/TDF in implementation and qualitative diagnosis

- **TDF→COM-B→BCW is now standardised practice** — Wong 2025 (JMIR Aging, VERIFIED): flagship TDF×AI study; 27 older adults; 9 of 14 domains mapped to 6 COM-B components; acceptance hinges on "AI as supportive tool, not replacement." Derksen 2025 (Implementation Science, preregistered, VERIFIED): 99 studies, 2,563 barriers/facilitators synthesised via TDF, solutions via BCW; self-critical finding: most primary CDSS studies had "very limited stakeholder involvement or theoretical underpinning." Liu 2025 (BMC Public Health, VERIFIED): 34 HCP interviews; 7 TDF domains; privacy/stigma/time/role conflict dominate. Carey & Hogan 2025 (invited review, VERIFIED): canonical 3-step pipeline restated; cites ~20% research-to-practice translation rate.
- **The frameworks are moving from behaviour-change to AI-adoption diagnosis** — the notable 2025 shift (RECONSTRUCTED synthesis of verified items).
- **2024 (pre-window):** Brown 2024 (university students' physical activity, seed anchor); Yang 2024 (exercise adherence, IJNS) — both VERIFIED abstracts.
- **Gap (VERIFIED):** no validated automated/LLM-assisted TDF coding workflow (Bijker 2024 UNVERIFIED registry record only); few trials test whether TDF-diagnosis→BCW-selection outperforms atheoretical intervention.

## Search Area 3: SDT in health, work, digital environments, learning

- **Competence-first mediation in GenAI learning** — Li 2025 (npj Science of Learning, N=1465, VERIFIED): introjected regulation most central node, intrinsic peripheral; competence satisfaction outweighed autonomy and relatedness. Wang 2025 (N=1056, VERIFIED): needs drive AI literacy via SRL strategies.
- **Human scaffolding multiplies GenAI benefit** — Ma & Chen 2025 (16-week, N=150, VERIFIED): AI + teacher scaffolding beat AI-only and gamified; needs satisfaction mediated. Li & Chiu 2025 (N=364, VERIFIED): needs partially/fully mediate teacher-support→engagement.
- **Perceived agency drives adoption more than accuracy** — Beacock 2026 (ethnography n=51, VERIFIED preprint): sustained use driven by perceived agency gains; perceived agency ≠ structural empowerment.
- **Dark side is real** — Goh 2025 (GenAI dependency scale, VERIFIED record-level); Jose 2025 (opinion, VERIFIED): procedural gains with conceptual erosion; ChatGPT-using students 17% lower on conceptual tests; AI can erode autonomy and relatedness.
- **Health effects modest** — Ntoumanis & Moller 2025 (VERIFIED): SDT-informed interventions work, small-to-moderate, mediated by autonomous motivation.
- **2024 (pre-window):** Chiu 2024 classification tool (Delphi, 36 teachers, 20 activities × SDT×SRL — de facto design taxonomy); Evans 2024 (CLT×SDT, N=1287); Wang & Wang 2024 (EFL LLM engagement) — all VERIFIED.

## Search Area 4: Skill atrophy from AI assistance

- **The core finding: assisted performance rises, independent capability falls** — Bastani 2025 (PNAS RCT, ~1000 students, VERIFIED): GPT-4 access +48% practice grades; when removed, students scored 17% WORSE than never-treated controls; hint-based Tutor guardrail eliminated harm; students metacognitively blind. Budzyń 2025 (Lancet Gastro, VERIFIED): endoscopists reverted to non-AI after sustained AI use: ADR 28.4%→22.4%. Heudel 2026 (ESMO scoping review, VERIFIED): "scarce but consistent" deskilling evidence; automation bias; 12% false-positive recall rise; >30% pathologists reversed correct diagnoses under time pressure; 80-85% case-volume collapse in cytology.
- **Skill loss is invisible to the user** — Lee 2025 (CHI, N=319, VERIFIED): confidence in GenAI predicts less critical-thinking effort; over-reliance dominant. Bastani's perception data confirms.
- **Natali 2025 (VERIFIED):** distinguishes deskilling (erosion) from upskilling inhibition (blocked acquisition) — the analytic frame. Berzin & Topol 2025 (Lancet commentary, VERIFIED): demands skill-preservation mandates.
- **Guardrail/friction design is the decisive moderator** — hints vs answers (Bastani); oversight roles (Choudhury 2024 pre-window, VERIFIED); cognitive co-regulation, "System 0" (Gutoreva 2026, VERIFIED preprint).
- **2024 (pre-window):** Choudhury & Chaudhry 2024 (JMIR): self-referential learning loop + clinician deskilling.

## Search Area 5: Empowerment-based assistive agents

- **Assistance ≠ empowerment** — Brynjolfsson 2025 (QJE RCT, 5179 agents, VERIFIED): +14% productivity, +34% for novices, minimal for experts; assistance compresses the skill gradient. Contrast with Area 4: performance gain and capability erosion coexist.
- **Perceived agency is decoupled from actual capacity** — Beacock 2026 (VERIFIED): "empowerment theater" risk; sustained use driven by perceived gains. Wang 2026 (CHI EA scoping, 80 articles, VERIFIED): user autonomy = sustained capacity to author one's goals while the system co-participates; five autonomy-support mechanism categories.
- **Heterogeneity is the rule** — Yu 2024 (Nature Medicine, 140 radiologists, VERIFIED pre-window): experience/AI-familiarity don't predict benefit; AI error incidence dominates.
- **Friction can be protective** — Xu 2026 (arXiv, 1223-paper bibliometric, VERIFIED): epistemic-sovereignty research declining (19.1%→13.1%) while autonomous-agent optimization surges (19.6%); proposes scaffolded cognitive friction (devil's advocate).
- **Technical sense of empowerment exists** — Yu 2025 (IJCAI survey, VERIFIED): information-theoretic empowerment (Klyubin); formalizable objective for assistive agents.
- **Normative split unresolved** — Astobiza 2025 (VERIFIED): "obsolescence regime" thesis vs augmentation camp.

## Search Area 6: LLM role-play and conversational training

- **LLM role-play partners are viable training tools** — EasyMED 2025 (4-week controlled study, VERIFIED): learning outcomes comparable to human standardized patients, stronger early gains for novices, better psychological safety. AgentForge 2026 (N=37, VERIFIED): role with visible coordination demands = most effective learning.
- **Structural separation is best practice** — persona/case-grounded module separated from response generation (EasyMED); trainee roles separated from feedback/tutor roles (Voigt 2025); visible intermediate artifacts and coordination demands drive learning (AgentForge 2026 — Fang et al.).
- **Adversarial robustness testing is mature** — 2026 multi-agent stress testing (VERIFIED): cumulative degradation under pressure; judge aligns with humans r=0.82.
- **Authenticity gaps persist** — Rudolph 2025 (EDM, VERIFIED): LLM clients elicit measurably different counselling patterns than humans (64 vs 74 sessions, sentence-level GeCCo coding). Ma 2025 (VERIFIED): persona priming can degrade performance below chance and embed demographic bias — critical caution for persona banks.
- **2024 (pre-window):** Louie 2024 (Roleplay-doh, CHI, RECONSTRUCTED via citation).

## Search Area 7: Proactive / personalized agents

- **Proactivity is the ceiling capability** — benchmarks converge on 26-40% success regardless of model: ProEvent 2026 (VERIFIED, GPT-5.1 reacts correctly 26.7%); PROBE 2025 (VERIFIED, best 40%); UniClawBench 2026 (VERIFIED, 400 real-world tasks, 5 decomposed capabilities).
- **Timing and restraint matter as much as content** — ProACT 2026 (VERIFIED): explicitly decides silence vs speech; improves appropriateness/non-interruptiveness. Liu 2026 (CHI, VERIFIED): physiological+behavioral user-state classifiers; aligned-adaptive timing +21% accuracy, false negatives 50.9%→22.9%. Chen 2025 (CHI, VERIFIED): users want control over proactivity; timing preferences heterogeneous.
- **Over-action is as prevalent as under-action** — ProEvent: agents overact and miss cancellations.
- **Personalization and proactivity are coupled** — Xu 2026 survey (VERIFIED): 4 capabilities (profile modeling, memory, planning, action execution); timing personalization is a design axis (Liu).
- **Communication policy is a design dimension** — CPE 2026 (VERIFIED): text vs UI channels have complementary strengths.
- **Gap (VERIFIED):** no work integrates skill-preservation/empowerment constraints into proactive behavior; "when NOT to act" not yet benchmarked.

## Search Area 8: User modeling, behavior latticing, motivation inference

- **Motivational state is learnable and predictive** — Lim 2025 (BMC Psychiatry, VERIFIED): LLM-scored change-talk valence → HMM transition dynamics predict session quality at 0.80 LOOCV; the psychological core of "behavior latticing."
- **Behavior lattices can be extracted automatically** — SERUM 2026 (VERIFIED): finite-state action/intent models from egocentric screen video via hierarchical VLM annotation; "schematic equilibrium" convergence; Markov models beat frequency baselines.
- **Next-action prediction is viable but low-confidence** — Shaikh 2026 (LongNAP, VERIFIED): 360K actions / 1800 hours / 20 users; beats baselines 79%/39% but only 17.1% of trajectories align (26% at high confidence). Treat as timing priors, not autonomous-action triggers.
- **State-timed support beats content-only** — Liu 2026 (CHI, VERIFIED): see Area 7.
- **Withdrawal flag:** SRSUPM 2026 (psychological-motivation recommender) WITHDRAWN for experimental errors — do not build on it (flagged, not cited).
- **2024 (pre-window):** Zheng 2024 (LLM text-rich sequential recommendation, UNVERIFIED registry); AnnoMI corpus (RECONSTRUCTED via citations).

## Search Area 9: Cybernetics, technodiversity, autopoiesis, new materialism

- **2025-2026 re-imports cybernetics into engineering** — Axelsson 2025 (Systems, VERIFIED): 17 engineering concerns from second-order cybernetics/autopoiesis; observer-in-the-loop as design requirement. Agent Cybernetics 2026 (arXiv preprint, VERIFIED, flagged Preliminary): six classical laws → six agent-design principles. Brailas 2025 (VERIFIED): observer-inclusion reframes reproducibility; revives von Foerster's choice-increasing imperative.
- **Technodiversity consolidates around Hui** — Hui 2024 *Machine and Sovereignty* (VERIFIED: University of Minnesota Press, open access — commonly miscited as MIT Press); Hui 2020 *Machine and Ecology* (landing page). Morozov's solutionism critique = standing caution against behaviorist tool-thought (canonical anchor).
- **Critical counter-current** — Pellizzoni 2025 (VERIFIED): new-materialist boundary-collapse narratives may serve the governance they claim to resist.
- **Canonical anchors:** Varela 1979/2025 annotated reissue (VERIFIED publisher page); Maturana & Varela 1980; Beer 1972/1974.
- **Caution (VERIFIED):** engineering appropriations are largely metaphorical — closed-loop ≠ organisational closure; pseudoscholarly "third-order cybernetics" pollutes citation space (excluded).

## Cross-Area Convergences

1. **The autonomy-capability axis is the through-line.** Every literature lands on it: skill atrophy (Area 4), assistance≠empowerment (Area 5), autonomy-supportive design (Area 3), MI spirit (Area 1), intervention timing/restraint (Area 7), von Foerster's choice-increasing imperative (Area 9). The architecture's primary objective: user long-run capability, not task completion (RECONSTRUCTED synthesis — VERIFIED across sources).
2. **Friction is protective.** Hints over answers (Bastani), scaffolded cognitive friction (Xu), silence decisions (ProACT), few-but-timed evocations (CALM-IT) — deliberate friction is a design parameter, not a UX cost.
3. **State-awareness beats content-only.** Timing to inferred user state (Liu), change-talk transition dynamics (Lim), readiness-gated outreach — all point to modeling user state explicitly.
4. **Fidelity is achievable; durability is the open problem.** AI-MI fidelity matches humans; behavior change doesn't persist (24h decay, 3/15 studies). The agent must design for repetition, spacing, and follow-up.
5. **Heterogeneity is the rule.** Novices gain most (Brynjolfsson); experience doesn't protect (Heudel); timing preferences vary (Chen). Personalization is not optional.

## Cross-Area Tensions

1. **Productivity vs capability** — Brynjolfsson's +14% vs Bastani's −17% post-access. Resolved only by measuring capability separately from performance (almost no study does).
2. **Perceived agency vs structural empowerment** — Beacock's adoption driver vs the deskilling evidence. Engagement metrics ≠ capability gains.
3. **Personalization vs privacy** — egocentric video (SERUM), physiological sensing (Liu) vs unresolved privacy constraints.
4. **Proactivity vs interruption cost** — initiation rewards vs non-interruptiveness; no standard cost-weighting.
5. **Persuasion vs evocation** — BCW's directive functions vs MI's spirit; the empowerment boundary arbitrates.
6. **Enhancement vs erosion narratives** — both true simultaneously (procedural gains, conceptual erosion — Jose 2025).

## Retraction / Integrity Flag Register

- **Wang & Fan (2025)**, "The effect of ChatGPT on students' learning performance…", Humanities and Social Sciences Communications, DOI 10.1057/s41599-025-04787-y — **RETRACTED** (CrossRef title marker; publisher notice to be confirmed before citing the retraction itself). NOT cited as evidence; flagged register-only.
- **SRSUPM (2026)**, "Sequential Recommender System Based on User Psychological Motivation" — **WITHDRAWN** by authors for experimental errors. NOT cited as evidence.
- **Pseudoscholarly exclusion:** LinkedIn "third-order cybernetics" essays, Zenodo mirror-theory items — excluded from evidence base (Area 9).
- **Seed-registry noise discarded:** several OpenAlex hits were off-topic (physics, chemistry, plant biology — phrase-collision artifacts); "Companion Animal Vaccine Hesitancy" and "I-CARE LGBTI e-learning" PubMed hits judged peripheral.

## Source Fidelity Register

- 70+ sources fetched across the two review councils (per-entry VERIFIED/RECONSTRUCTED/UNVERIFIED flags; see Annotated_Bibliography.md) (three subagents per phase; see Annotated_Bibliography.md for the consolidated list).
- Quality classes flagged: opinion articles (Jose 2025, Berzin & Topol 2025, Carey & Hogan 2025), preprints (Beacock 2026, Gutoreva 2026, SERUM, LongNAP, Agent Cybernetics, CALM-IT), record-level-only (Teng 2025, Goh 2025, Wang & Wang 2024), single-country samples (Wong HK, Liu CN, Li CN), small-N (Beacock n=51, Liu N=32).
- UNVERIFIED items: Sigre-Leirós 2026 (tandfonline no abstract), Bijker 2024, Zheng 2024, Hui 2021, NoMAD instrument, Pawson & Tilley 1997 book.
