# MONSTARE — BAD / BROKEN SOURCE LINKS (2026-08-13)

Row-by-row verification of Readable Source URLs and Source Landing URLs in
`Monstare_Evidence_Matrix_Source_Links_v3_Staleness_Patched_artifact.xlsx`.
A row is BROKEN if its Readable Source URL is dead, blocked, unreadable, or missing.

- Rows BROKEN or NO_URL: **28**
- Rows with CAVEAT (readable but scanned/landing-only/stub): **53**
- Rows READY (readable URL verified note-takable): **48**

Full per-URL detail: `Monstare_source_link_audit_2026-08-13.csv`.

## BROKEN / NO-URL ROWS

| RowID | Citation | Status | Readable URL result | Landing URL result |
|---|---|---|---|---|
| CORE-07 | Lepper, Greene & Nisbett — over-justification | BROKEN | BAD_DEAD: HTTP 404 | BAD_STUB: HTML stub, only 77 chars; markers: [] |
| CORE-09 | Carver & Scheier — self-regulation / control theory | BROKEN | BAD_DEAD: HTTP 404 | BAD_DEAD: HTTP 404 |
| CORE-10 | Locke & Latham — goal-setting theory | BROKEN | BAD_DEAD: HTTP 404 | BAD_STUB: HTML stub, only 76 chars; markers: [] |
| CORE-15 | Gross — emotion regulation timeline | BROKEN | BAD_DEAD: HTTP 404 | BAD_BLOCKED: HTTP 403 |
| CORE-20 | Collins — Multiphase Optimization Strategy (MOST) | BROKEN | BAD_DEAD: HTTP 404 | BAD_STUB: HTML stub, only 190 chars; markers: [] |
| A1-05 | Simondon — On the Mode of Existence of Technical Objects | BROKEN | BAD_DEAD: HTTP 404 | BAD_STUB: HTML stub, only 0 chars; markers: [] |
| A1-06 | Simondon — Individuation (Form and Information) | BROKEN | BAD_DEAD: HTTP 404 | OK (HTML 4543 chars) |
| A1-07 | Stiegler — Technics and Time v1 (Fault of Epimetheus) | BROKEN | BAD_DEAD: HTTP 404 | BAD_BLOCKED: HTTP 429 |
| A1-08 | Feenberg — Questioning Technology | BROKEN | BAD_DEAD: HTTP 404 | BAD_DEAD: HTTP 404 |
| A1-09 | Ihde — Technology and the Lifeworld | BROKEN | BAD_DEAD: HTTP 404 | LANDING-ONLY (HTML 3676 chars; markers: ['add to cart']) |
| A2-05 | Grinberg — Ethnography of an Interface | BROKEN | BAD_DEAD: HTTP 404 | BAD_STUB: HTML stub, only 0 chars; markers: [] |
| A2-06 | Sharon — Self-Tracking for Health and the QS | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_DEAD: HTTP 404 |
| A3-03 | Schroeder et al. — Goal-Directed Self-Tracking | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_BLOCKED: HTTP 403 |
| A3-04 | Baumer & Silberman — When the Implication Is Not to Design | BROKEN | BAD_DEAD: HTTP 404 | BAD_BLOCKED: HTTP 403 |
| A3-05 | Sengers, Boehner, David & Kaye — Reflective Design | BROKEN | BAD_DEAD: HTTP 404 | BAD_BLOCKED: HTTP 403 |
| A3-06 | Bardzell & Bardzell — Humanistic HCI | BROKEN | BAD_UNREACHABLE: connection error | BAD_DEAD: HTTP 404 |
| A3-08 | Light, Burgess & Duguay — The Walkthrough Method | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_BLOCKED: HTTP 403 |
| A3-09 | Pierce — Undesigning Technology | NO_URL | NOT_CHECKED | BAD_BLOCKED: HTTP 403 |
| A4-02 | Berman, Jonides & Kaplan — Cognitive Benefits of Nature | BROKEN | BAD_DEAD: HTTP 500 | BAD_BLOCKED: HTTP 403 |
| A4-03 | Scannell & Gifford — Place Attachment (tripartite framework) | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_STUB: HTML stub, only 11 chars; markers: [] |
| A4-04 | Menatti et al. — Place Attachment & Landscape Restorativeness | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_STUB: HTML stub, only 11 chars; markers: [] |
| A5-09 | Zahavi — Subjectivity and Selfhood | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_BLOCKED: HTTP 403 |
| A6-05 | Parasuraman, Sheridan & Wickens — Levels of Automation | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_STUB: HTML stub, only 0 chars; markers: [] |
| A7-05 | Molenaar — Regulation of Learning and AI | BROKEN | BAD_BLOCKED: HTTP 403 | BAD_STUB: HTML stub, only 11 chars; markers: [] |
| A7-06 | Zimmerman — Self-Regulated Learning | BROKEN | BAD_UNREACHABLE: connection error | BAD_BLOCKED: HTTP 403 |
| A7-09 | Oulasvirta — offloading and interface design | BROKEN | BAD_BLOCKED: HTTP 403 | LANDING-ONLY (HTML 8280 chars; markers: ['log in', 'login', 'sign in', 'subscribe']) |
| A9-07 | Iqbal & Horvitz — Disruption and Recovery of Computing Tasks | BROKEN | BAD_BLOCKED: HTTP 403 | LANDING-ONLY (HTML 6157 chars; markers: ['subscribe']) |
| HUI-2024 | Hui — Machine and Sovereignty: For a Planetary Thinking | BROKEN | BAD_BLOCKED: HTTP 403 | LANDING-ONLY (HTML 3843 chars; markers: ['log in', 'sign in']) |

## CAVEAT ROWS (readable, but not clean full-text)

| RowID | Citation | Readable URL result |
|---|---|---|
| CORE-04 | Bandura — Self-efficacy | UNKNOWN: content-type none |
| CORE-05 | Deci, Koestner & Ryan — extrinsic rewards meta-analysis | BAD_SCANNED: PDF 42p, NO text layer (scanned/image-only, needs OCR) |
| CORE-06 | Frey & Jegen — motivation crowding theory | LANDING-ONLY (HTML 61379 chars; markers: ['signin']) |
| CORE-12 | Ferster & Skinner — Schedules of Reinforcement | LANDING-ONLY (HTML 6218 chars; markers: ['log in']) |
| CORE-13 | Staddon & Cerutti — operant conditioning review | BAD_STUB: HTML stub, only 143 chars; markers: ['captcha'] |
| CORE-16 | Csikszentmihalyi — Flow | LANDING-ONLY (HTML 6246 chars; markers: ['log in', 'purchase']) |
| CORE-17 | Kazdin — Single-Case Research Designs | LANDING-ONLY (HTML 6453 chars; markers: ['log in']) |
| CORE-19 | Klasnja et al. — Micro-randomized trials | BAD_STUB: HTML stub, only 143 chars; markers: ['captcha'] |
| A1-01 | Hui — The Question Concerning Technology in China | BAD_SCANNED: PDF 348p, NO text layer (scanned/image-only, needs OCR) |
| A1-02 | Hui — Cosmotechnics as Cosmopolitics | LANDING-ONLY (HTML 7314 chars; markers: ['subscribe']) |
| A1-03 | Hui — Art and Cosmotechnics | LANDING-ONLY (HTML 4764 chars; markers: ['subscribe']) |
| A1-10 | Verbeek — What Things Do | LANDING-ONLY (HTML 6615 chars; markers: ['log in', 'purchase']) |
| A1-11 | Winner — The Whale and the Reactor | BAD_SCANNED: PDF 216p, NO text layer (scanned/image-only, needs OCR) |
| A1-13 | Borgmann — Technology and the Character of Contemporary Life | LANDING-ONLY (HTML 6255 chars; markers: ['log in']) |
| A1-14 | Mitcham — Thinking Through Technology | LANDING-ONLY (HTML 6317 chars; markers: ['log in', 'purchase']) |
| A1-16 | Mumford — Technics and Civilization | LANDING-ONLY (HTML 5851 chars; markers: ['log in']) |
| A1-17 | Ellul — The Technological Society | LANDING-ONLY (HTML 6491 chars; markers: ['log in']) |
| A1-19 | Verbeek — Moralizing Technology | LANDING-ONLY (HTML 7530 chars; markers: ['log in', 'signin']) |
| A2-02 | Lupton — The Quantified Self | BAD_SCANNED: PDF 16p, NO text layer (scanned/image-only, needs OCR) |
| A2-03 | Neff & Nafus — Self-Tracking | LANDING-ONLY (HTML 6289 chars; markers: ['log in', 'purchase']) |
| A2-04 | Rapp, Cena & Marcengo — QS/PI special issue editorial | BAD_STUB: HTML stub, only 190 chars; markers: [] |
| A2-09 | Elsden et al. — making sense of personal data | LANDING-ONLY (HTML 6285 chars; markers: ['log in', 'signin', 'subscribe']) |
| A2-10 | Selke — Lifelogging | BAD_STUB: HTML stub, only 190 chars; markers: [] |
| A3-01 | Limerick, Coyle & Moore — Experience of Agency in HCI (review) | BAD_STUB: HTML stub, only 143 chars; markers: ['captcha'] |
| A4-01 | Kaplan & Kaplan — The Experience of Nature | LANDING-ONLY (HTML 6961 chars; markers: ['log in']) |
| A4-06 | Chang et al. — Place Attachment & Pro-Environmental Intentions | BAD_STUB: HTML stub, only 143 chars; markers: ['captcha'] |
| A4-09 | Lewicka — Place Attachment: 40 years | LANDING-ONLY (HTML 29405 chars; markers: ['log in']) |
| A4-10 | Gibson — The Ecological Approach to Visual Perception | LANDING-ONLY (HTML 6253 chars; markers: ['log in']) |
| A5-01 | Varela — Neurophenomenology | LANDING-ONLY (HTML 30293 chars; markers: ['log in', 'purchase']) |
| A5-04 | Valenzuela-Moguillansky & Vasquez-Rosati — Analysis Procedure | LANDING-ONLY (HTML 12379 chars; markers: ['log in', 'login', 'not logged in']) |
| A5-07 | Depraz, Varela & Vermersch — On Becoming Aware | LANDING-ONLY (HTML 1648 chars; markers: ['log in']) |
| A5-08 | Csikszentmihalyi & Larson — Experience Sampling Method | BAD_STUB: HTML stub, only 190 chars; markers: [] |
| A5-10 | Gallagher & Zahavi — The Phenomenological Mind | LANDING-ONLY (HTML 7251 chars; markers: ['log in']) |
| A6-02 | AI and Human Autonomy: A Literature Review | BAD_STUB: HTML stub, only 190 chars; markers: [] |
| A6-04 | Parasuraman & Riley — Use, Misuse, Disuse, Abuse | BAD_SCANNED: PDF 12p, NO text layer (scanned/image-only, needs OCR) |
| A6-06 | Eubanks — Automating Inequality | LANDING-ONLY (HTML 7325 chars; markers: ['log in', 'purchase']) |
| A6-07 | Nissenbaum — Privacy in Context | LANDING-ONLY (HTML 6924 chars; markers: ['log in', 'purchase']) |
| A7-02 | Sparrow, Liu & Wegner — Google Effects on Memory | LANDING-ONLY (HTML 5788 chars; markers: ['log in']) |
| A7-08 | Kirsh — The Intelligent Use of Space | BAD_SCANNED: PDF 38p, NO text layer (scanned/image-only, needs OCR) |
| A7-10 | Recent GenAI & perceived self-regulated learning (empirical) | LANDING-ONLY (HTML 8820 chars; markers: ['log in', 'sign in']) |
| A8-01 | Hobson, Schroeder, Risen, Xygalatas & Inzlicht — Psychology of Rituals | BAD_STUB: HTML stub, only 0 chars; markers: [] |
| A8-03 | Van Gennep — The Rites of Passage | LANDING-ONLY (HTML 5938 chars; markers: ['log in']) |
| A8-05 | Bell — Ritual Theory, Ritual Practice | BAD_SCANNED: PDF 289p, NO text layer (scanned/image-only, needs OCR) |
| A8-08 | McCauley & Lawson — Bringing Ritual to Mind | LANDING-ONLY (HTML 7411 chars; markers: ['log in']) |
| A8-10 | Whitehouse — Modes of Religiosity | LANDING-ONLY (HTML 6734 chars; markers: ['log in', 'purchase']) |
| A9-04 | Leroy — Attention Residue | LANDING-ONLY (HTML 7691 chars; markers: ['login']) |
| A9-05 | Arnold, Goldschmitt & Rigotti — Information Overload (review) | BAD_STUB: HTML stub, only 143 chars; markers: ['captcha'] |
| A9-06 | Rick et al. — Work Interruptions of Office Workers | BAD_STUB: HTML stub, only 0 chars; markers: [] |
| A9-09 | Microsoft Work Trend Index (reports) | LANDING-ONLY (HTML 31640 chars; markers: ['signin']) |
| A9-10 | Newport — Deep Work | LANDING-ONLY (HTML 7844 chars; markers: ['log in', 'purchase']) |
| A9-11 | Allen — Getting Things Done | LANDING-ONLY (HTML 6794 chars; markers: ['log in', 'purchase']) |
| A10-06 | Schweder — Thinking Through Cultures | LANDING-ONLY (HTML 7295 chars; markers: ['log in']) |
| A10-07 | Nisbett — The Geography of Thought | LANDING-ONLY (HTML 7748 chars; markers: ['log in', 'purchase']) |
