# MONSTARE — SOURCE MATERIAL VERIFICATION (FINAL) — 2026-08-13

Two-pass verification: (1) full link audit of all 257 matrix URLs (status + text-layer/
paywall probes), (2) second pass resolving false signals (pymupdf re-extraction for
'scanned' PDFs; browser-stack retries for curl-blocked hosts).

- Total rows: 129
- READY (note-takable now): 57
- OCR-READY (scanned PDF, OCR pipeline verified): 3
- CAVEAT (landing-only/stub/OCR-unverified): 45
- BOT-HOSTILE (link live but needs manual/institutional access): 8
- DEAD (needs replacement URL): 15
- NO_URL (missing readable link): 1

## DEAD — NEEDS REPLACEMENT URL

| RowID | Citation | What happened |
|---|---|---|
| A1-05 | Simondon — On the Mode of Existence of Technical Objects | HTTP 404 (BAD_DEAD) |
| A1-06 | Simondon — Individuation (Form and Information) | HTTP 404 (BAD_DEAD) |
| A1-07 | Stiegler — Technics and Time v1 (Fault of Epimetheus) | HTTP 404 (BAD_DEAD) |
| A1-08 | Feenberg — Questioning Technology | HTTP 404 (BAD_DEAD) |
| A1-09 | Ihde — Technology and the Lifeworld | HTTP 404 (BAD_DEAD) |
| A2-05 | Grinberg — Ethnography of an Interface | HTTP 404 (BAD_DEAD) |
| A3-04 | Baumer & Silberman — When the Implication Is Not to Design | HTTP 404 (BAD_DEAD) |
| A3-05 | Sengers, Boehner, David & Kaye — Reflective Design | HTTP 404 (BAD_DEAD) |
| A4-02 | Berman, Jonides & Kaplan — Cognitive Benefits of Nature | HTTP 500 (BAD_DEAD) |
| CORE-04 | Bandura — Self-efficacy | Readable URL redirects to motivation.uky.edu homepage (source gone). Needs a replacement copy of Bandura 1997 (book, W.H. Freeman). Known legal path: APA PsycBooks / library. |
| CORE-07 | Lepper, Greene & Nisbett — over-justification | HTTP 404 (BAD_DEAD) |
| CORE-09 | Carver & Scheier — self-regulation / control theory | HTTP 404 (BAD_DEAD) |
| CORE-10 | Locke & Latham — goal-setting theory | HTTP 404 (BAD_DEAD) |
| CORE-15 | Gross — emotion regulation timeline | HTTP 404 (BAD_DEAD) |
| CORE-20 | Collins — Multiphase Optimization Strategy (MOST) | HTTP 404 (BAD_DEAD) |

## BOT-HOSTILE — LINK EXISTS BUT NEEDS MANUAL/INSTITUTIONAL ACCESS

| RowID | Citation | Host / problem |
|---|---|---|
| A2-06 | Sharon — Self-Tracking for Health and the QS | academia.edu — bot-hostile (403 curl, 504 Firecrawl). Needs manual browser session. |
| A3-03 | Schroeder et al. — Goal-Directed Self-Tracking | ACM DL — bot-hostile (403 curl, 504 Firecrawl). Institutional/ACM access. |
| A3-06 | Bardzell & Bardzell — Humanistic HCI | Morgan & Claypool — unreachable from container (000); landing 404. Needs manual access. |
| A3-08 | Light, Burgess & Duguay — The Walkthrough Method | Worktribe repository — 403 even with browser UA. Needs manual download. |
| A4-03 | Scannell & Gifford — Place Attachment (tripartite framework) | ResearchGate — bot-hostile. Needs manual session. |
| A4-04 | Menatti et al. — Place Attachment & Landscape Restorativeness | UDD repository — 403. Needs manual download. |
| A7-06 | Zimmerman — Self-Regulated Learning | Host unreachable from container (000). Transient or geo-blocked. |
| A7-09 | Oulasvirta — offloading and interface design | Aalto Pure portal — 403 (Elsevier Pure blocks bots). Needs manual download. |

## NO URL — MISSING READABLE LINK

- **A3-09** — Pierce — Undesigning Technology: no readable URL in matrix (landing link blocked 403). Needs source discovery.

## VERIFIED FIXES (from second pass)

- **CORE-06** (Frey & Jegen): replacement PDF verified readable — https://www.bsfrey.ch/wp-content/uploads/2021/08/motivation-crowding-theory.pdf (23p). Correct DOI: 10.1111/1467-6419.00150.
- **CORE-04** (Bandura 1997): no live open copy found from container (original uky.edu copy gone; mirrors blocked). Legal paths: APA PsycBooks / library. Replacement needed before charting.

## CAVEAT ROWS — ABSTRACT/LANDING-ONLY (full text needs institution)

- A1-02: Hui — Cosmotechnics as Cosmopolitics — HTML 7314 chars; markers: ['subscribe']
- A1-03: Hui — Art and Cosmotechnics — HTML 4764 chars; markers: ['subscribe']
- A1-10: Verbeek — What Things Do — HTML 6615 chars; markers: ['log in', 'purchase']
- A1-13: Borgmann — Technology and the Character of Contemporary Life — HTML 6255 chars; markers: ['log in']
- A1-14: Mitcham — Thinking Through Technology — HTML 6317 chars; markers: ['log in', 'purchase']
- A1-16: Mumford — Technics and Civilization — HTML 5851 chars; markers: ['log in']
- A1-17: Ellul — The Technological Society — HTML 6491 chars; markers: ['log in']
- A1-19: Verbeek — Moralizing Technology — HTML 7530 chars; markers: ['log in', 'signin']
- A10-06: Schweder — Thinking Through Cultures — HTML 7295 chars; markers: ['log in']
- A10-07: Nisbett — The Geography of Thought — HTML 7748 chars; markers: ['log in', 'purchase']
- A2-03: Neff & Nafus — Self-Tracking — HTML 6289 chars; markers: ['log in', 'purchase']
- A2-04: Rapp, Cena & Marcengo — QS/PI special issue editorial — HTML stub, only 190 chars; markers: []
- A2-09: Elsden et al. — making sense of personal data — HTML 6285 chars; markers: ['log in', 'signin', 'subscribe']
- A2-10: Selke — Lifelogging — HTML stub, only 190 chars; markers: []
- A3-01: Limerick, Coyle & Moore — Experience of Agency in HCI (review) — HTML stub, only 143 chars; markers: ['captcha']
- A4-01: Kaplan & Kaplan — The Experience of Nature — HTML 6961 chars; markers: ['log in']
- A4-06: Chang et al. — Place Attachment & Pro-Environmental Intentions — HTML stub, only 143 chars; markers: ['captcha']
- A4-09: Lewicka — Place Attachment: 40 years — HTML 29405 chars; markers: ['log in']
- A4-10: Gibson — The Ecological Approach to Visual Perception — HTML 6253 chars; markers: ['log in']
- A5-01: Varela — Neurophenomenology — HTML 30293 chars; markers: ['log in', 'purchase']
- A5-04: Valenzuela-Moguillansky & Vasquez-Rosati — Analysis Procedure — HTML 12379 chars; markers: ['log in', 'login', 'not logged in']
- A5-07: Depraz, Varela & Vermersch — On Becoming Aware — HTML 1648 chars; markers: ['log in']
- A5-08: Csikszentmihalyi & Larson — Experience Sampling Method — HTML stub, only 190 chars; markers: []
- A5-10: Gallagher & Zahavi — The Phenomenological Mind — HTML 7251 chars; markers: ['log in']
- A6-02: AI and Human Autonomy: A Literature Review — HTML stub, only 190 chars; markers: []
- A6-06: Eubanks — Automating Inequality — HTML 7325 chars; markers: ['log in', 'purchase']
- A6-07: Nissenbaum — Privacy in Context — HTML 6924 chars; markers: ['log in', 'purchase']
- A7-02: Sparrow, Liu & Wegner — Google Effects on Memory — HTML 5788 chars; markers: ['log in']
- A7-08: Kirsh — The Intelligent Use of Space — Scanned PDF (no text layer, 38p); OCR attempt timed out — needs local OCR or retry
- A7-10: Recent GenAI & perceived self-regulated learning (empirical) — HTML 8820 chars; markers: ['log in', 'sign in']
- A8-01: Hobson, Schroeder, Risen, Xygalatas & Inzlicht — Psychology of Rituals — HTML stub, only 0 chars; markers: []
- A8-03: Van Gennep — The Rites of Passage — HTML 5938 chars; markers: ['log in']
- A8-08: McCauley & Lawson — Bringing Ritual to Mind — HTML 7411 chars; markers: ['log in']
- A8-10: Whitehouse — Modes of Religiosity — HTML 6734 chars; markers: ['log in', 'purchase']
- A9-04: Leroy — Attention Residue — HTML 7691 chars; markers: ['login']
- A9-05: Arnold, Goldschmitt & Rigotti — Information Overload (review) — HTML stub, only 143 chars; markers: ['captcha']
- A9-06: Rick et al. — Work Interruptions of Office Workers — HTML stub, only 0 chars; markers: []
- A9-09: Microsoft Work Trend Index (reports) — HTML 31640 chars; markers: ['signin']
- A9-10: Newport — Deep Work — HTML 7844 chars; markers: ['log in', 'purchase']
- A9-11: Allen — Getting Things Done — HTML 6794 chars; markers: ['log in', 'purchase']
- CORE-12: Ferster & Skinner — Schedules of Reinforcement — HTML 6218 chars; markers: ['log in']
- CORE-13: Staddon & Cerutti — operant conditioning review — HTML stub, only 143 chars; markers: ['captcha']
- CORE-16: Csikszentmihalyi — Flow — HTML 6246 chars; markers: ['log in', 'purchase']
- CORE-17: Kazdin — Single-Case Research Designs — HTML 6453 chars; markers: ['log in']
- CORE-19: Klasnja et al. — Micro-randomized trials — HTML stub, only 143 chars; markers: ['captcha']

## OCR-READY ROWS

- A2-02: Lupton — The Quantified Self — Scanned chapter PDF (no text layer, 16p); OCR pipeline verified (Firecrawl extracted full chapter text)
- A6-04: Parasuraman & Riley — Use, Misuse, Disuse, Abuse — Scanned PDF (no text layer, 12p); OCR pipeline verified (Firecrawl extracted full text)
- CORE-05: Deci, Koestner & Ryan — extrinsic rewards meta-analysis — PDF is scanned (no text layer per pypdf+pymupdf, 42p) BUT OCR pipeline verified: Firecrawl extracted full text incl. abstract statistics

## READY ROWS (verified note-takable)

- A1-01: Hui — The Question Concerning Technology in China
- A1-04: Hui & Lemmens (eds.) — Cosmotechnics (Anthropocene)
- A1-11: Winner — The Whale and the Reactor
- A1-12: Latour — Where Are the Missing Masses?
- A1-15: Heidegger — The Question Concerning Technology
- A1-18: Haraway — A Cyborg Manifesto
- A10-01: Chirkov, Ryan, Kim & Kaplan — Autonomy vs Individualism
- A10-02: Nalipay, King & Cai — Autonomy Across East and West
- A10-03: Beyers, Soenens & Vansteenkiste — Autonomy in Adolescence
- A10-04: Markus & Kitayama — Culture and the Self
- A10-05: Henrich, Heine & Norenzayan — The Weirdest People in the World?
- A10-08: Technodiversity project / ITS Rio (white paper & library)
- A2-01: Li, Dey & Forlizzi — Stage-Based Model of Personal Informatics
- A2-07: Whittaker — critiques of QS/personal informatics
- A2-08: Rapp & Tirassa — PI for sport and healthy behavior
- A3-02: Bennett, Metatla, Roudaut & Mekler — HCI Agency/Autonomy
- A3-07: Friedman & Kahn — Value Sensitive Design
- A3-10: Rapp & Boldi — open issues in persuasive technologies
- A4-05: Yoon et al. — Perceived Restorativeness & Place Attachment
- A4-07: Hartig et al. — Perceived Restorativeness Scale
- A4-08: Korpela — restorative environments & self-regulation
- A5-02: Petitmengin — Describing Experience in the Second Person
- A5-03: Petitmengin et al. — micro-phenomenology studies
- A5-05: Hurlburt & Heavey — Descriptive Experience Sampling
- A5-06: Bass-Krueger et al. — DES vs Micro-Phenomenological Interviews
- A5-09: Zahavi — Subjectivity and Selfhood
- A6-01: Laitinen & Sahlgren — AI Systems and Respect for Human Autonomy
- A6-03: Shneiderman — Human-Centered AI
- A6-05: Parasuraman, Sheridan & Wickens — Levels of Automation
- A6-08: Mittelstadt et al. — The Ethics of Algorithms
- A6-09: Wachter, Mittelstadt & Floridi — transparent/explainable AI
- A6-10: Calo — Robotics and the Lessons of Cyberlaw
- A7-01: Risko & Gilbert — Cognitive Offloading
- A7-03: Zhu et al. — Dependent vs Autonomous Offloading to GenAI
- A7-04: Chirayath et al. — Cognitive Offloading or Overload?
- A7-05: Molenaar — Regulation of Learning and AI
- A7-07: Salomon, Perkins & Globerson — Partners in Cognition
- A8-02: Norton & Gino — Rituals Alleviate Grieving
- A8-04: Turner — The Ritual Process
- A8-05: Bell — Ritual Theory, Ritual Practice
- A8-06: Xygalatas — Ritual (2022)
- A8-07: Tian et al. — Enacting Rituals to Improve Self-Control
- A8-09: Durkheim — The Elementary Forms of Religious Life
- A9-01: Mark, Gudith & Klocke — The Cost of Interrupted Work
- A9-02: Gonzalez & Mark — Multi-tasking Craziness (working spheres)
- A9-03: Mark, Gonzalez & Harris — No Task Left Behind?
- A9-07: Iqbal & Horvitz — Disruption and Recovery of Computing Tasks
- A9-08: Bailey & Konstan — On the Need for Attention-Aware Systems
- CORE-01: Ryan & Deci — Self-Determination Theory (needs)
- CORE-02: Markland, Ryan, Tobin & Rollnick — MI + SDT
- CORE-03: Vansteenkiste, Williams & Resnicow — SDT/MI integration
- CORE-06: Frey & Jegen — motivation crowding theory
- CORE-08: Reijula & Hertwig — self-nudging & citizen choice architect
- CORE-11: Ordonez et al. — Goals Gone Wild
- CORE-14: Clark & Chalmers — The Extended Mind
- CORE-18: Tate et al. — SCRIBE 2016 reporting guideline
- HUI-2024: Hui — Machine and Sovereignty: For a Planetary Thinking