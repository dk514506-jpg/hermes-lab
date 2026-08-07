# Annotated Bibliography v1.0

Project: Motivational Ecology Agent Architecture — Phase 2: Recent Evidence Review
Date: 2026-08-06
Status: assembled from VERIFIED council distillations (synthesis = RECONSTRUCTED at artifact level; 70+ sources fetched; per-entry VERIFIED/RECONSTRUCTED/UNVERIFIED flags)
Evidence discipline: VERIFIED / RECONSTRUCTED / UNVERIFIED flags per entry.
Retracted works are excluded from the bibliography proper and listed in the
digest's Retraction / Integrity Flag Register.

## Purpose

Machine-checkable bibliography of the post-2024 evidence base, one entry per
source, with annotation. Phase 1 canonical anchors (Michie 2011, Cane 2012,
Ryan & Deci 2000/2017, Miller & Rollnick, May & Finch 2009, etc.) are carried
in the Foundation Matrix's source register; this bibliography is the Phase 2
increment (2024-2026).

## Entry Format

```
### [n] Author(s) (Year). Title. Venue. DOI/arXiv/PMID.
- Status: VERIFIED | RECONSTRUCTED | UNVERIFIED
- Area: <search area number(s)>
- Finding: <1-3 sentences>
- Relevance to architecture: <1-2 sentences>
```

## Bibliography (2024-2026)

### Skill atrophy / capability erosion

### [1] Bastani H, Bastani O, Sungu A, Ge H, Kabakcı Ö, Mariman R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. PNAS 122(26):e2422633122. DOI 10.1073/pnas.2422633122.
- Status: VERIFIED (full text)
- Area: 4
- Finding: RCT ~1000 students: GPT-4 access +48% practice grades, but −17% on post-access tests vs never-treated controls; hint-based Tutor guardrail eliminated harm; students metacognitively blind.
- Relevance: The decisive evidence for minimal-sufficiency assistance (hints, not answers) and objective skill telemetry.

### [2] Budzyń K, Romańczyk M, Kitala D, et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy. Lancet Gastroenterology & Hepatology 10(10):896-903. DOI 10.1016/S2468-1253(25)00133-5.
- Status: VERIFIED (PubMed PMID 40816301; author reply at 10.1016/S2468-1253(25)00324-3 also verified)
- Area: 4
- Finding: First large multicentre quantitative deskilling signal: ADR dropped 28.4%→22.4% when endoscopists reverted to non-AI after sustained AI use.
- Relevance: Assisted-expertise reversal is measurable in practice; skill health must be tracked.

### [3] Heudel PE, Crochet H, Filori Q, Bachelot T, Blay JY. (2026). Artificial intelligence in medicine: a scoping review of the risk of deskilling and loss of expertise among physicians. ESMO Real World Data & Digital Oncology 12:100693. DOI 10.1016/j.esmorw.2026.100693.
- Status: VERIFIED (full abstract)
- Area: 4
- Finding: Deskilling evidence "scarce but consistent": automation bias, 12% false-positive recall rise, >30% pathologists reversed correct diagnoses under time pressure, 80-85% case-volume collapse in cytology.
- Relevance: Structural deskilling mechanisms catalogue; experience does not protect.

### [4] Natali C, Marconi L, Dias Duran LD, et al. (2025). AI-induced Deskilling in Medicine: A Mixed-Method Review and Research Agenda. Artificial Intelligence Review 58:356. DOI 10.1007/s10462-025-11352-1.
- Status: VERIFIED (open access full text)
- Area: 4
- Finding: Distinguishes deskilling (erosion) from upskilling inhibition (blocked acquisition); maps vulnerabilities onto PACES competencies; proposes longitudinal monitoring.
- Relevance: The analytic frame — the agent must distinguish erosion from blocked acquisition in its own user.

### [5] Lee HP, Sarkar A, Tankelevitch L, et al. (2025). The Impact of Generative AI on Critical Thinking. CHI '25. DOI 10.1145/3706598.3713778.
- Status: VERIFIED (ACM full text)
- Area: 4
- Finding: 319 knowledge workers: higher GenAI confidence predicts less critical-thinking effort; over-reliance dominant.
- Relevance: Self-report is unreliable; confidence correlates inversely with actual engagement.

### [6] Berzin TM, Topol EJ. (2025). Preserving clinical skills in the age of AI assistance. Lancet 406(10513):1719. DOI 10.1016/S0140-6736(25)02075-6.
- Status: VERIFIED (PubMed PMID 41109709; commentary)
- Area: 4
- Finding: Demands skill-preservation mandates built into AI clinical deployment.
- Relevance: The mandate argument — skill preservation as a deployment requirement, not an option.

### [7] Gutoreva A, Tsim F, Papakonstantinou T. (2026). Position: AI as Part of Self — Extending the Mind Requires Cognitive Co-Regulation. arXiv:2605.16197.
- Status: VERIFIED (preprint, flagged)
- Area: 4
- Finding: Names unstructured-delegation risk cluster (deskilling, automation bias, epistemic-authority transfer); alignment must target the human-AI system ("System 0").
- Relevance: Co-regulation framing — the agent's design target is the user+agent system.

### [8] Choudhury A, Chaudhry Z. (2024). Large Language Models and User Trust: Self-Referential Learning Loop and the Deskilling of Health Care Professionals. J Med Internet Res 26:e56764. DOI 10.2196/56764.
- Status: VERIFIED (pre-window)
- Area: 4
- Finding: AI-generated data feeding AI training (self-referential loop) plus clinician deskilling; expert oversight as mitigation.
- Relevance: The framing Natali et al. systematized.

### Empowerment-based assistive agents

### [9] Brynjolfsson E, Li D, Raymond L. (2025). Generative AI at Work. Quarterly Journal of Economics 140(2):889-949. DOI 10.1093/qje/qjae044.
- Status: VERIFIED (OUP landing page + NBER w31161)
- Area: 5
- Finding: RCT on 5,179 customer-support agents: +14% productivity, +34% for novices, minimal for experts; assistance compresses the skill gradient.
- Relevance: Empowerment is unevenly distributed; largest where capability is lowest — assistive allocation must be personalized.

### [10] Beacock I, Xu R, Murray L, et al. (2026). AI usage patterns are shaped by perceived gains in human agency. arXiv:2607.02313.
- Status: VERIFIED (preprint, n=51)
- Area: 5, 3, 8
- Finding: Sustained use driven by perceived agency gains outweighing accuracy concerns; perceived agency ≠ structural empowerment ("empowerment theater" risk).
- Relevance: The agent must not mistake engagement for capability; monitor agency illusion.

### [11] Wang Y, et al. (2026). User Autonomy in Human-LLM Interaction: A Scoping Review. CHI EA '26. DOI 10.1145/3772363.3798855.
- Status: VERIFIED (ACM abstract)
- Area: 5
- Finding: 80-article review: autonomy = sustained capacity to author one's goals while the system co-participates; five categories of autonomy-support mechanisms.
- Relevance: The design-mechanism taxonomy for autonomy support.

### [12] Astobiza AM. (2025). Do AI agents trump human agency? Discover Artificial Intelligence 5:348. DOI 10.1007/s44163-025-00608-y.
- Status: VERIFIED (open access)
- Area: 5
- Finding: "Obsolescence regime" thesis: efficiency-optimized agents can marginalize human evaluator discretion.
- Relevance: The normative warning for agent design.

### [13] Xu K, Shen Y, Yan L, Ren Y. (2026). Cognitive Agency Surrender: Defending Epistemic Sovereignty via Scaffolded AI Friction. arXiv:2603.21735.
- Status: VERIFIED
- Area: 5
- Finding: Bibliometric: epistemic-sovereignty research declining (19.1%→13.1%) while agent optimization surges; proposes scaffolded cognitive friction.
- Relevance: Friction as a first-class design parameter.

### [14] Yu F, Moehring A, Banerjee O, et al. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine 30:837-849. DOI 10.1038/s41591-024-02850-w.
- Status: VERIFIED (pre-window)
- Area: 5
- Finding: 140 radiologists, 15 tasks: experience/AI familiarity don't predict benefit; AI error incidence dominates outcomes.
- Relevance: Canonical case for personalized assistive strategies.

### [15] Yu R, Wan S, Wang Y, et al. (2025). Reward Models in Deep Reinforcement Learning: A Survey. IJCAI 2025. arXiv:2506.15421.
- Status: VERIFIED
- Area: 5
- Finding: Information-theoretic empowerment (Klyubin): maximizing influence over future outcomes; formalizable objective for assistive agents.
- Relevance: A technical sense of empowerment to adapt for user-empowerment objectives.

### LLM role-play and conversational training

### [16] Fang Z, Zhang Y, Huang Y. (2026). AgentForge: An Immersive Role-Playing Platform for Learning Agentic Software Engineering. arXiv:2608.04148.
- Status: VERIFIED (abstract; preprint)
- Area: 6
- Finding: N=37 novices in four SE roles; role with visible coordination demands and intermediate artifacts = most effective learning.
- Relevance: Role-play design: visible coordination demands + intermediate artifacts.

### [17] Shouqi S, Nazly A, Wanniarachchi J, De Alwis R. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. arXiv:2608.03166 (ADScAI).
- Status: VERIFIED
- Area: 6
- Finding: Six progressive adversarial strategies; robustness drops 0.17-0.20; Authority Challenge and Emotional Manipulation most effective; judge aligns with humans (r=0.82, κ=0.71).
- Relevance: Safety gate requirement before deploying any role-play partner.

### [18] Rudolph E, Steigerwald P, Albrecht J. (2025). Comparing Human Roleplayers and LLM-Simulated Clients in Online Counselling Training. EDM 2025.
- Status: VERIFIED
- Area: 6
- Finding: 64 human-human vs 74 human-LLM sessions, sentence-level GeCCo coding; LLM clients replicate many dynamics but measurable differences in disclosure and session structure.
- Relevance: Quantifies the authenticity gap; feasibility anchor for AI client simulation.

### [19] Voigt H, Sugamiya Y, Lawonn K, Zarrieß S, Takanishi A. (2025). LLM-Powered Virtual Patient Agents for Interactive Clinical Skills Training with Automated Feedback. arXiv:2508.13943.
- Status: VERIFIED (preprint)
- Area: 6
- Finding: Extends LLM simulated patients with action space + virtual tutors giving real-time feedback; separation of patient-simulation and feedback components.
- Relevance: The architecture pattern (persona module ≠ feedback module).

### [20] Zhang B, Liu X, Wang Y, et al. (2025 v3 2026). Human or LLM as Standardized Patients? (EasyMED + SPBench). arXiv:2511.14783.
- Status: VERIFIED (preprint under revision)
- Area: 6
- Finding: Multi-agent virtual SP separating case-grounded disclosure from response generation; 4-week controlled study: outcomes comparable to human SPs, stronger early novice gains, better psychological safety.
- Relevance: Direct evidence structured LLM role-play matches human role-players for training outcomes.

### [21] Ma X, Zhu R, Wang Z, et al. (2025). Enhancing Patient-Centric Communication: Leveraging LLMs to Simulate Patient Perspectives. arXiv:2501.06964.
- Status: VERIFIED
- Area: 6
- Finding: Persona priming with education background: 88% accurate guidance; adding demographic info dropped performance below random chance with bias against underserved populations.
- Relevance: Critical caution: persona banks can degrade reliability; audit for bias.

### [22] Louie R, et al. (2024). Roleplay-doh: Enabling New-Concept Immersion via LLM-Enabled Role-Playing. CHI 2024.
- Status: RECONSTRUCTED (via Rudolph 2025 citation)
- Area: 6 (pre-window)
- Finding: Early demonstration of LLM role-players for novel-perspective immersion.
- Relevance: Feasibility anchor.

### User modeling / behavior latticing / motivation inference

### [23] Lim K, Jung Y-C, Kim B-H. (2025). Evaluating motivational interview quality using large language models and hidden Markov models. BMC Psychiatry 25:908. DOI 10.1186/s12888-025-07391-1; PMID 41034852.
- Status: VERIFIED
- Area: 8, 1
- Finding: LLM-scored change-talk valence → HMM transition dynamics; high-quality sessions show fluid state transitions (p<.001); transition features predict quality at 0.80 LOOCV.
- Relevance: Direct empirical grounding for modeling motivation as a tracked latent state with transition dynamics.

### [24] Phu AJ, Mooney J, de Langis K, Le KC, Kang D. (2026). SERUM: State Extraction and Refinement for User Modeling. arXiv:2607.29181.
- Status: VERIFIED (preprint)
- Area: 8
- Finding: Finite-state behavioral models from egocentric screen video via hierarchical VLM annotation; "schematic equilibrium" convergence; Markov models beat frequency baselines.
- Relevance: The "latticing" operation is becoming automatable.

### [25] Shaikh O, Teutschbein V, Gandhi K, et al. (2026). Learning Next Action Predictors from Human-Computer Interaction. arXiv:2603.05923.
- Status: VERIFIED (preprint)
- Area: 8
- Finding: 360K actions / 1800 hours / 20 users; LongNAP beats baselines 79%/39% but only 17.1% trajectories align (26% high-confidence).
- Relevance: Next-action predictions are low-confidence priors for timing, not autonomous action.

### [26] Liu A, Karoui Y, Draxler F, Kreuter F, Chiossi F. (2026). Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling. arXiv:2602.00880 (CHI 2026).
- Status: VERIFIED (conference-accepted)
- Area: 8, 7
- Finding: EDA + mouse-movement user-state classifiers; aligned-adaptive timing +21% accuracy, false negatives 50.9%→22.9%.
- Relevance: Readiness-sensitive intervention design; timing is a personalization axis.

### [27] Wu Z, et al. (2023). AnnoMI: A Dataset of Expert-Motivational-Interviewing Annotated Transcripts.
- Status: RECONSTRUCTED (via Lim 2025, Mahmood 2025)
- Area: 8 (pre-window anchor)
- Finding: Standard expert-annotated corpus linking client language to motivational state.
- Relevance: Foundational for motivation-inference-from-language.

### [28] Zheng Z, Chao W, Qiu Z, et al. (2024). Harnessing Large Language Models for Text-Rich Sequential Recommendation. WWW '24. DOI 10.1145/3589334.3645358.
- Status: UNVERIFIED (registry record)
- Area: 8 (pre-window)
- Finding: LLM-based user modeling over text-rich interaction sequences.
- Relevance: Language-grounded user-state encoding.

### MI across settings (incl. AI-delivered MI)

### [29] Karve Z, Calpey J, Machado C, Knecht M, Mejia MC. (2025). New Doc on the Block: Scoping Review of AI Systems Delivering Motivational Interviewing for Health Behavior Change. JMIR 27:e78417. DOI 10.2196/78417; PMID 40957014.
- Status: VERIFIED
- Area: 1
- Finding: Of 1,001 records, 15 studies (9 rule-based, 4 LLM, 2 virtual agents); 13/15 feasibility; 6/15 MI fidelity; only 3/15 substantial behavior change; 3 RCTs.
- Relevance: The authoritative sobering snapshot of AI-delivered MI.

### [30] Mahmood Z, Ali S, Zhu J, et al. (2025). A Fully Generative Motivational Interviewing Counsellor Chatbot for Smoking Cessation (MIBot). Findings of ACL 2025.
- Status: VERIFIED (full text)
- Area: 1
- Finding: 106 smokers; quit confidence +1.7/10; 98% MI-adherent utterances (higher than typical humans) but perceived empathy lower.
- Relevance: First fully generative MI chatbot with adherence + human-readiness outcomes.

### [31] Han G, Murphy JG, Ladd BO. (2026). Leveraging Multimodal Self-Consistency Reasoning in Coding Motivational Interviewing for Alcohol Use Reduction. Military Medicine. PMID 42560216.
- Status: VERIFIED
- Area: 1, 8
- Finding: Audio-language models, four analytic prompt families, majority voting: 52.6% accuracy / 46.4% macro-F1 — modest.
- Relevance: Automatic MI coding improving but not expert-grade; fidelity claims rest on imperfect measurement.

### [32] Pinto e Silva T, Gouveia C, Santirso FA, Cunha O, Caridade S. (2025). Effectiveness of Motivational Interviewing with Justice-involved People: A Systematic Review and Meta-analysis. Psychosocial Intervention 34(2):89-102. DOI 10.5093/pi2025a8; PMID 40405915.
- Status: VERIFIED
- Area: 1
- Finding: 22 studies; MI improved attendance, reduced dropout, reduced recidivism in official records.
- Relevance: MI's mechanism transfers to coercive/low-autonomy settings.

### [33] Livingston JA, Kerr E, Bichon J. (2026). Peer-Based Motivational Interviewing to Reduce Alcohol Use and Sexual Violence Among U.S. Sailors: Feasibility Study. Military Medicine. PMID 42560206.
- Status: VERIFIED
- Area: 1
- Finding: N=23 sailors; peer MI acceptable in military culture; culture-specific barriers identified.
- Relevance: Feasibility of peer-mediated MI in workplace/military settings.

### [34] Verhoeven DJ, Ferenschild FTJ, Verhoeven BH. (2025). Learning Motivational Interviewing in VR: A Feasibility Study. Journal of Medical Extended Reality. PMID 42558095.
- Status: VERIFIED
- Area: 1, 6
- Finding: 20 medical students; SUS 69.5, confidence improved, but only 40% empathy with virtual patients; speech-recognition broke flow.
- Relevance: Simulation modality quality gates MI-skill transfer.

### [35] Li Y, Li M, Yorke J, et al. (2025). Effects of a Theory- and Evidence-Based, MI-Oriented AI Digital Assistant on Vaccine Attitudes: RCT. JMIR 27:e72637. DOI 10.2196/72637.
- Status: VERIFIED
- Area: 1
- Finding: N=177; significant readiness (d=0.52) and confidence (d=0.54) gains, NOT on primary hesitancy outcome.
- Relevance: AI-MI moves readiness more reliably than it resolves ambivalence.

### [36] Shenoi A, Li T, Jabir AI, et al. (2026). Structured Large Language Model Workflows for Motivational Interviewing (Aimi). JMIR Form Res 10:e94036. DOI 10.2196/94036.
- Status: VERIFIED
- Area: 1
- Finding: N=18; structured-workflow LLM matched novice human coach on MISC-2 fidelity (reflection/question 0.84 vs 0.62; complex reflections 66.7% vs 50%; change talk 90.8% vs 73.2%).
- Relevance: Structured workflow orchestration — not free-form prompting — preserves MI fidelity.

### [37] Eiroa-Solans C, Inzlicht M. (2025). From extrinsic to intrinsic motivation: Testing an AI-powered motivational interviewing system (Intrinsic AI). Computers in Human Behavior Reports 21:100882. DOI 10.1016/j.chbr.2025.100882.
- Status: VERIFIED
- Area: 1, 3
- Finding: Preregistered RCT N=237: 15-min GPT-4 MI+SDT chatbot raised readiness/importance/confidence vs unmodified GPT-4; gains decayed at 24h; no behavior change.
- Relevance: Single-session AI MI moves readiness, not behavior — spaced repetition required.

### [38] Nguyen VC, Nguyen NY, Candan KA, et al. (2026). CALM-IT: Generating Realistic Long-Form Motivational Interviewing Dialogues with Dual-Actor Dynamics Tracking. arXiv:2601.10085.
- Status: VERIFIED (EMNLP-submission preprint)
- Area: 1
- Finding: Tracks motivation/resistance and counselor strategy over long dialogues; best MITI-4.2 ratings with minimal degradation at length; highest acceptance (64.3%) despite fewer change-directed prompts.
- Relevance: Fewer, better-timed evocations beat push — MI spirit preserved in LLM design.

### [39] Cohen A, et al. (2024). Using Large Language Models to Automate Counsellor and Client Coding in Motivational Interviewing.
- Status: RECONSTRUCTED (via Mahmood 2025)
- Area: 1 (pre-window)
- Finding: First LLM-based automated MITI/CLEAR coding; established the evaluation stack.
- Relevance: The evaluation-stack origin.

### [40] Steenstra I, et al. (2024). Fully generative LLM virtual agent for alcohol counseling.
- Status: RECONSTRUCTED (via Mahmood 2025)
- Area: 1 (pre-window)
- Finding: Evaluated linguistic soundness, safety, MI competency vs human counselors.
- Relevance: Direct predecessor proving fully-generative MI delivery feasible.

### COM-B/TDF in implementation

### [41] Wong AKC, Lee JHT, Zhao Y, et al. (2025). Exploring Older Adults' Perspectives and Acceptance of AI-Driven Health Technologies: Qualitative Study. JMIR Aging 8:e66778. DOI 10.2196/66778.
- Status: VERIFIED
- Area: 2
- Finding: 27 older adults; 9 of 14 TDF domains mapped to 6 COM-B components; acceptance hinges on usability, privacy, "AI as supportive tool, not replacement."
- Relevance: The flagship TDF×AI study; the "tool not replacement" stance is the design default.

### [42] Derksen C, Walter FM, Akbar AB, et al. (2025). The implementation challenge of computerised clinical decision support systems. Implementation Science 20:33. DOI 10.1186/s13012-025-01445-4.
- Status: VERIFIED (preregistered PROSPERO CRD42024517054)
- Area: 2
- Finding: 99 studies, 2,563 barriers/facilitators via TDF, solutions via BCW; most primary CDSS studies had "very limited stakeholder involvement or theoretical underpinning."
- Relevance: Self-critical finding — framework popularity ≠ theoretical rigour.

### [43] Liu S, Hu Y, Pfaff H, Lei X, et al. (2025). Barriers and facilitators to seeking psychological support among healthcare professionals. BMC Public Health 25:848. DOI 10.1186/s12889-025-21912-3.
- Status: VERIFIED
- Area: 2
- Finding: 34 interviews; 7 TDF domains; privacy/stigma/time/role conflict dominate.
- Relevance: Domain-salience exemplar.

### [44] Carey S, Hogan S. (2025). Using the Theoretical Domains Framework and Behavior Change Wheel Framework within the world of nutrition support. Nutrition in Clinical Practice 40(6):1379-1386. DOI 10.1002/ncp.70021.
- Status: VERIFIED (invited review)
- Area: 2
- Finding: Canonical 3-step pipeline restated; ~20% research-to-practice translation rate.
- Relevance: The pipeline the agent should encode; the translation-rate honesty.

### [45] Brown CE, Richardson K, Halil-Pizzirani B, et al. (2024). Key influences on university students' physical activity: systematic review using TDF and COM-B. BMC Public Health 24:330. DOI 10.1186/s12889-023-17621-4.
- Status: VERIFIED (pre-window)
- Area: 2
- Finding: Full barrier→TDF→COM-B→intervention-target pipeline at scale.
- Relevance: Seed-registry anchor.

### [46] Yang Y, Gao Y, An R, Wan Q. (2024). Barriers and facilitators to exercise adherence in community-dwelling older adults: COM-B and TDF. International Journal of Nursing Studies. DOI 10.1016/j.ijnurstu.2024.104808; PMID 38823146.
- Status: VERIFIED (pre-window)
- Area: 2
- Finding: COM-B/TDF synthesis extended with BCT and implementation-strategy mapping.
- Relevance: Full-pipeline exemplar.

### SDT in GenAI contexts

### [47] Li J, Zhang J, Chai CS, Lee V. (2025). Analyzing the network structure of students' motivation to learn AI: a self-determination theory perspective. npj Science of Learning. DOI 10.1038/s41539-025-00339-w.
- Status: VERIFIED
- Area: 3
- Finding: N=1,465, 47 universities: introjected regulation most central node; intrinsic peripheral; competence satisfaction outweighs autonomy and relatedness in AI learning.
- Relevance: Competence-first mediation; introjection risk in AI learning.

### [48] Ma Y, Chen M. (2025). The human touch in AI: optimizing language learning through self-determination theory and teacher scaffolding. Frontiers in Psychology 16:1568239. DOI 10.3389/fpsyg.2025.1568239.
- Status: VERIFIED
- Area: 3
- Finding: 16-week quasi-experiment N=150: AI + teacher scaffolding beat AI-only and gamified; needs satisfaction mediated; scaffolding countered algorithmic rigidity.
- Relevance: Human-in-the-loop scaffolding multiplies GenAI benefit.

### [49] Li Y, Chiu TKF. (2025). The mediating effects of needs satisfaction on teacher support and student engagement with GenAI chatbots. Education and Information Technologies 30:20051-20070. DOI 10.1007/s10639-025-13574-w.
- Status: VERIFIED
- Area: 3
- Finding: N=364: needs partially/fully mediate teacher-support→engagement; chatbots sometimes engaged students emotionally more than teachers.
- Relevance: Need-satisfaction as the mediation layer.

### [50] Wang K, Cui W, Yuan X. (2025). Artificial Intelligence in Higher Education: The Impact of Need Satisfaction on AI Literacy Mediated by Self-Regulated Learning Strategies. Behavioral Sciences 15(2):165. DOI 10.3390/bs15020165.
- Status: VERIFIED
- Area: 3
- Finding: N=1,056: three needs drive AI literacy through SRL strategies.
- Relevance: Needs → SRL → literacy chain.

### [51] Ntoumanis N, Moller AC. (2025). Self-determination theory informed research for promoting physical activity. Psychology of Sport and Exercise. DOI 10.1016/j.psychsport.2025.102879.
- Status: VERIFIED
- Area: 3
- Finding: SDT interventions work with small-to-moderate effects, mediated by autonomous motivation and need support.
- Relevance: Calibrated effect sizes.

### [52] Teng MF. (2025). Examining longitudinal development of writing motivation in the GenAI context. Learning and Motivation. DOI 10.1016/j.lmot.2025.102157.
- Status: VERIFIED (record-level)
- Area: 3
- Finding: Longitudinal SDT writing-motivation trajectories under GenAI use.
- Relevance: Longitudinal design exemplar.

### [53] Goh AYH, Hartanto A, Majeed NM. (2025). Generative artificial intelligence dependency: scale development, validation, and correlates. Computers in Human Behavior Reports. DOI 10.1016/j.chbr.2025.100845.
- Status: VERIFIED (record-level)
- Area: 3
- Finding: Operationalises problematic GenAI dependency — the dark-side counterpart of SDT engagement.
- Relevance: Dependency detection as a monitoring axis.

### [54] Jose B, Cherian J, Verghis AM, et al. (2025). The cognitive paradox of AI in education: between enhancement and erosion. Frontiers in Psychology 16:1550621. DOI 10.3389/fpsyg.2025.1550621.
- Status: VERIFIED (opinion article — flagged)
- Area: 3, 4
- Finding: Procedural gains alongside retention/critical-thinking erosion (e.g., ChatGPT users 17% lower on conceptual tests); AI can erode autonomy and relatedness.
- Relevance: Both enhancement and erosion are real simultaneously.

### [55] Liu Y, Zhang M, Peng Y. (2026). Academic innovation behavior in the context of generative AI: SDT and MOA perspectives. PLOS ONE. PMID 42560956.
- Status: VERIFIED (PubMed record)
- Area: 3
- Finding: SDT × motivation-opportunity-ability integration for GenAI-era research behavior.
- Relevance: Cross-theory integration exemplar.

### [56] Zhang R, Talib OB, Liu S, et al. (2026). Serial mediating effects of learning motivation and engagement on gen AI literacy and EFL proficiency. Frontiers in Psychology. PMID 42558232.
- Status: VERIFIED (PubMed record)
- Area: 3
- Finding: Motivation and engagement serially mediate GenAI-literacy→perceived-proficiency.
- Relevance: Serial-mediation exemplar.

### [57] Chiu TKF. (2024). A classification tool to foster self-regulated learning with generative AI by applying self-determination theory. Educational Technology Research and Development 72:2401-2416. DOI 10.1007/s11423-024-10366-w.
- Status: VERIFIED (pre-window)
- Area: 3
- Finding: Delphi with 36 teachers → 20-activity classification tool crossing SDT needs with SRL phases.
- Relevance: The de facto design taxonomy for GenAI-SDT work.

### [58] Evans P, Vansteenkiste M, Parker PD, et al. (2024). Cognitive Load Theory and Its Relationships with Motivation: an SDT Perspective. Educational Psychology Review. DOI 10.1007/s10648-023-09841-2.
- Status: VERIFIED (pre-window, abstract via S2)
- Area: 3
- Finding: N=1,287; instructional strategies and motivating style jointly shape load, motivation, engagement, achievement.
- Relevance: CLT×SDT bridge.

### [59] Wang X, Wang S. (2024). Exploring Chinese EFL learners' engagement with large language models: an SDT perspective. Learning and Motivation. DOI 10.1016/j.lmot.2024.102014.
- Status: VERIFIED (record-level, pre-window)
- Area: 3
- Finding: LLM engagement in EFL shaped by need satisfaction/frustration dynamics.
- Relevance: Need-frustration in AI contexts.

### Proactive / personalized agents

### [60] Li G, Pan L, Wang L. (2026). ProEvent: An Event-centric Benchmark for Proactive Agents. arXiv:2607.17701.
- Status: VERIFIED
- Area: 7
- Finding: First event-centric benchmark; GPT-5.1 reacts correctly only 26.7%; overaction and missed cancellations; implicit-event detection is the core failure mode.
- Relevance: Proactivity ceiling; over-action as first-class failure.

### [61] Chen Z, Duan C, Sun K, et al. (2026). UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks. arXiv:2607.08768.
- Status: VERIFIED
- Area: 7
- Finding: 400 bilingual tasks in live Docker; five decomposed capabilities; model and framework jointly shape performance.
- Relevance: Closed-loop real-world evaluation standard.

### [62] Ma X, Qiu J, Yao Y, et al. (2026). Communication Policy Evolution for Proactive LLM Agents. arXiv:2606.14314.
- Status: VERIFIED
- Area: 7
- Finding: Communication policy under information asymmetry; text and UI channels complementary; CPE self-evolution via prompt-only refinement.
- Relevance: Communication behavior is a design dimension.

### [63] Yang S, Xu D, Pei J, Wang D. (2026). ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration. arXiv:2607.03730.
- Status: VERIFIED
- Area: 7
- Finding: Grounded in common-ground theory; explicitly decides silence vs speech; improved appropriateness/non-interruptiveness across 3,244 turns.
- Relevance: Silence as a valid agent move.

### [64] Pasternak G, Rajagopal D, White J, et al. (2025). Beyond Reactivity: Measuring Proactive Problem Solving in LLM Agents (PROBE). arXiv:2510.19771.
- Status: VERIFIED
- Area: 7
- Finding: Decomposes proactivity into search-for-unspecified-issues / identify-bottlenecks / execute-resolutions; best score 40%.
- Relevance: Proactivity decomposition + ceiling measurement.

### [65] Yang B, Xu L, Zeng L, et al. (2025). ProAgent: Harnessing On-Demand Sensory Contexts for Proactive LLM Agent Systems in the Wild. arXiv:2512.06721.
- Status: VERIFIED
- Area: 7
- Finding: AR-glasses system, on-demand tiered sensing: +27.7% prediction accuracy, −20.5% false detections, 85% satisfaction (n=20).
- Relevance: Proactivity as continuous ambient sensing.

### [66] Chen V, Zhu A, Zhao S, et al. (2025). Need Help? Designing Proactive AI Assistants for Programming. CHI '25. DOI 10.1145/3706598.3714002 / arXiv:2410.04596.
- Status: VERIFIED
- Area: 7
- Finding: Users want control over proactivity; valued intervention types differ by expertise; timing preferences heterogeneous.
- Relevance: Mixed-initiative consent design.

### [67] Xu Y, Chen Q, Ma Z, et al. (2026). Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions. arXiv:2602.22680.
- Status: VERIFIED (survey)
- Area: 7, 8
- Finding: Four interdependent capabilities: profile modeling, memory, planning, action execution; evaluation gaps flagged per capability.
- Relevance: The personalization capability taxonomy.

### Cybernetics / technodiversity / autopoiesis / new materialism

### [68] Axelsson J. (2025). Implications of Second-Order Cybernetics and Autopoiesis on Systems-of-Systems Engineering. Systems 13(2):119. DOI 10.3390/systems13020119.
- Status: VERIFIED
- Area: 9
- Finding: 17 engineering concerns from second-order cybernetics/autopoiesis; observer-in-the-loop is a design requirement.
- Relevance: Observer-position as design requirement.

### [69] Wang X, Yang C, Zhao H, Lin Z, Hu S. (2026). The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents. arXiv:2605.10754.
- Status: VERIFIED (preprint, "Preliminary Work")
- Area: 9
- Finding: Six classical cybernetics laws → six agent-design principles; three engineering desiderata.
- Relevance: Cybernetics→agent mapping attempt (metaphorical — flagged).

### [70] Brailas A. (2025). Replication Crisis in Psychology, Second-Order Cybernetics, and Transactional Causality. Integrative Psychological and Behavioral Science 59:14. DOI 10.1007/s12124-024-09867-3.
- Status: VERIFIED
- Area: 9
- Finding: Observer-inclusion and transactional causality reframe reproducibility; revives von Foerster's "act always so as to increase the number of choices."
- Relevance: The choice-increasing imperative as a guardrail.

### [71] Pellizzoni L. (2025). Nature, Neoliberalism, and New Materialisms: Riding the Ungovernable. Lexington Books. DOI 10.5040/9781978748019.
- Status: VERIFIED (publisher page)
- Area: 9
- Finding: Critical: boundary-collapse narratives dovetail with neoliberal rationality; Adorno and "form of life" as counterpoints.
- Relevance: The critical counter-current to celebratory posthumanism.

### [72] Varela FJ. (1979; annotated reissue 2025, eds. Di Paolo E, Thompson E). Principles of Biological Autonomy. MIT Press. DOI 10.7551/mitpress/14875.001.0001.
- Status: VERIFIED (publisher page; open access CC BY-NC-ND)
- Area: 9 (canonical anchor; 2025 = annotated reissue, not new primary work)
- Finding: Autonomy as organisational closure; autopoiesis as self-production; participatory epistemology.
- Relevance: The lineage for "autonomous agent" claims; closure as heuristic, not literal property.

### [73] Hui Y. (2024). Machine and Sovereignty: For a Planetary Thinking. University of Minnesota Press. DOI 10.5749/9781452973685.
- Status: VERIFIED (publisher page; open access — NOTE: commonly miscited as MIT Press)
- Area: 9 (canonical anchor)
- Finding: Technodiversity as recursive negotiation between local and global; fragments join through resonance, not borders.
- Relevance: Plural technics over single optimised behaviour.

### [74] Hui Y. (2020). Machine and Ecology. Angelaki 25(4). DOI 10.1080/0969725X.2020.1790835.
- Status: VERIFIED (landing page; full text paywalled)
- Area: 9 (canonical anchor)
- Finding: Reconstructs machine–ecology relation through cybernetics history.
- Relevance: Origin text for the technodiversity critique.

### [75] Hui Y. (2021). On the Limit of Artificial Intelligence. Philosophy Today. DOI 10.5840/philtoday202149392.
- Status: UNVERIFIED (OpenAlex record only)
- Area: 9
- Finding: n/a.
- Relevance: n/a — flagged.

### [76] Maturana HR, Varela FJ. (1980). Autopoiesis and Cognition: The Realization of the Living. D. Reidel.
- Status: canonical anchor (not fetched)
- Area: 9
- Finding: Autopoiesis as the organization of the living.
- Relevance: Standard edition.

### [77] Beer S. (1972/1974). Brain of the Firm / Designing Freedom.
- Status: canonical anchor (not fetched)
- Area: 9
- Finding: Viable system model and recursive control.
- Relevance: Management-cybernetics backbone for agent hierarchies.

### [78] Morozov E. (2013). To Save Everything, Click Here. PublicAffairs.
- Status: canonical anchor (not fetched)
- Area: 9
- Finding: Solutionism critique.
- Relevance: Standing caution against behaviorist tool-thought.

## Index by Search Area

| Area | Entries |
|---|---|
| 1 MI settings | 29-40 |
| 2 COM-B/TDF | 41-46 |
| 3 SDT | 47-59 |
| 4 Skill atrophy | 1-8 |
| 5 Empowerment agents | 9-15 |
| 6 LLM role-play | 16-22 |
| 7 Proactive agents | 60-67 |
| 8 User modeling/latticing | 23-28 (+31) |
| 9 Cybernetics/philosophy | 68-78 |

## Integrity Exclusions (register-only, NOT bibliography entries)

### A. Retracted / withdrawn (excluded from evidence)
- Wang & Fan (2025), HSSC, DOI 10.1057/s41599-025-04787-y — RETRACTED (CrossRef title marker; publisher notice to be confirmed before citing the retraction itself).
- SRSUPM (2026), arXiv:2602.08667 — WITHDRAWN by authors for experimental errors.

### B. Unverifiable records (metadata only; not excluded from the field, but not evidence)
- Sigre-Leirós et al. (2026), Psychology Crime & Law, DOI 10.1080/1068316X.2026.2640071 — UNVERIFIED (no abstract available; search-index metadata only).
- Pseudoscholarly "third-order cybernetics" items (LinkedIn/Zenodo) — excluded from the evidence base on quality grounds.
