# MONSTARE — BATCH 4 SOURCE HUNT RESULTS (A1 philosophy-of-technology spine)
Date: 2026-08-13 · Hunter: Locus-orchestrated subagent wave (2 waves, 4 agents) + direct re-verification by Locus · Purpose: resolve open-full-text availability for the 10 A1 rows previously marked landing/lending-only; feed the batch-4 handoff (`/opt/data/Monstare_Handoff_Prompt_Batch4.txt`) and the matrix URL cells.

> **UPDATE 2026-08-13 22:48 (user action):** the user dropped 5 full-text files into `/opt/data/Monstare_batch4_sources/`, upgrading four rows from the PARTIAL/NOT_FOUND states below: **A1-08** Feenberg (full book, epdf.pub copy, 263pp), **A1-03** Hui (full book, JSTOR-downloaded copy, 341pp), **A1-13** Borgmann (full book, OceanofPDF copy, 364pp), **A1-06** Simondon (full EN text, Univocal 2020 trans., 743pp), plus the Higgs/Light/Strong 2003 volume as A1-08/A1-13 supporting material. The batch-4 handoff memo's Step 3 §4b now maps each file to its row (with provenance/copyright cautions). USER ACTIONS items 1–4 below are superseded accordingly; A1-10 remains PARTIAL (2 staged chapters) and A1-19 remains the only no-full-text row. Pre-inspection (pypdf: magic + page count + title) done 22:48; charting session must still verify text layer + provenance per convention.
Halting principle: each row resolves to FOUND (verified readable full text) | PARTIAL (chapter/excerpt coverage, documented) | NOT_FOUND (in-copyright, no legitimate open copy — user action or abstract-level fallback). All URLs below were curl-re-verified by Locus on 2026-08-13 (HTTP status, content-type, size; PDF magic bytes checked on staged files) — subagent reports are NOT the verification basis.
Legitimacy policy: author-hosted, university/institutional repositories, archive.org open items (incl. DLI), monoskop, open-access journals, publisher OA only. Piracy mirrors (libgen, sci-hub, z-lib, annas-archive, dokumen.pub, aaaaarg, are.na user uploads) deliberately excluded; none are recorded here.

---

## FOUND — full text verified, staged (3 rows)
### A1-14 — Mitcham, *Thinking Through Technology* (Chicago UP 1994)
- URL: https://archive.org/download/ThinkingThroughTechnologyThePathBetweenEngineeringAndPhilosophy/Thinking%20Through%20Technology%20-%20The%20path%20between%20engineering%20and%20philosophy.pdf (verified 200 / application/pdf / 23,174,105 B; %PDF magic)
- Details page: https://archive.org/details/ThinkingThroughTechnologyThePathBetweenEngineeringAndPhilosophy (community/opensource item, access-restricted-item: none; also EPUB ~11MB + DjVuTXT)
- Staged: /opt/data/Monstare_batch4_sources/A1-14_Mitcham_Thinking_Through_Technology_1994_open_scan.pdf
- Caveat: unauthorized-but-openly-hosted scan of an in-copyright book — record as "open copy with copyright caution" in the matrix (research use).
- Spare: UPRM course mirror pp.137-160 (https://ecourses.uprm.edu/pluginfile.php/2319/mod_resource/content/3/14.-%20Mitchan%2C%201994%20%5Bp137-160%5D.pdf, 200/PDF/1.65MB) — cross-check only.

### A1-16 — Mumford, *Technics and Civilization* (1934; 1963 Harvest reprint)
- URL: https://archive.org/download/in.ernet.dli.2015.49974/2015.49974.Technics-And-Civilization.pdf (verified 200 / application/pdf / 26,652,483 B; %PDF-1.1 magic)
- Alternative (higher quality, larger): https://archive.org/download/in.ernet.dli.2015.232322/2015.232322.Technics-And.pdf (200/PDF/79.9MB)
- Staged: /opt/data/Monstare_batch4_sources/A1-16_Mumford_Technics_and_Civilization_1934_DLI_scan.pdf
- Caveat: Digital Library of India scan; US copyright technically subsists (renewal -> 2029) — fair-use/research scan, NOT public domain.

### A1-17 — Ellul, *The Technological Society* (1964 Knopf, Wilkinson trans.)
- URL: https://ia803209.us.archive.org/2/items/JacquesEllulTheTechnologicalSociety/Jacques%20Ellul%20-%20The%20Technological%20Society.pdf (verified 200 / application/pdf / 11,689,365 B; %PDF-1.7 magic)
- Item: `JacquesEllulTheTechnologicalSociety` — access-restricted-item: none; full _djvu.txt text layer (1.2MB) available
- Staged: /opt/data/Monstare_batch4_sources/A1-17_Ellul_The_Technological_Society_1964_Wilkinson_open_scan.pdf
- Caveat: 1964 translation in copyright — research use of an open scan. (French original 1954 public domain in some jurisdictions; the translation is not.)

### A1-09 — Ihde, *Technology and the Lifeworld* (Indiana UP 1990)
- URL: https://monoskop.org/images/f/f1/Ihde_Don_Technology_and_the_Lifeworld_From_Garden_to_Earth.epub (verified 200 / application/octet-stream / 605,433 B; ZIP/EPUB container magic) — file page: https://monoskop.org/File:Ihde_Don_Technology_and_the_Lifeworld_From_Garden_to_Earth.epub
- Staged: /opt/data/Monstare_batch4_sources/A1-09_Ihde_Technology_and_the_Lifeworld_1990_fullbook.epub
- Caveat: EPUB (not PDF) — OCR'd page XML (page_1..page_201 + front matter); monoskop is an established open theory-text archive; in-copyright scan = research/reading copy only. NOT lending-gated (archive.org technologylifewo00ihde is lending-only; excluded).

## PARTIAL — chapter/excerpt coverage verified, staged (6 rows)
### A1-06 — Simondon, *Individuation*
- FR (PUF 1964 part 1 + start of part 2, 272pp): https://monoskop.org/images/8/85/Simondon_Gilbert_L_Individu_et_sa_genese_physico-biologique_1995.pdf (200/PDF/10,910,495 B) — staged as A1-06_Simondon_L_Individu_et_sa_genese_physico-biologique_1995_FR.pdf
- EN (Zone 1992 intro trans.): https://monoskop.org/images/b/bc/Simondon_Gilbert_1964_1992_The_Genesis_of_the_Individual.pdf (200/PDF/1,367,600 B) — staged as A1-06_Simondon_Genesis_of_the_Individual_1992_EN_intro.pdf
- EN (Parrhesia 7/2009, "Position of the Problem of Ontogenesis"): http://www.parrhesiajournal.org/parrhesia07/parrhesia07_simondon1.pdf (200/PDF/294,694 B) — staged
- EN (Interact or Die! 2007, "Technical Individualization"): https://monoskop.org/images/7/7e/Simondon_Gilbert_1958_2007_Technical_Individualization.pdf (200/PDF/3,939,815 B) — not staged (duplicative of the above EN excerpts)
- ES (full 502pp trans., Cactus/La Cebra 2009): https://monoskop.org/images/9/97/Simondon_Gilbert_La_individuacion_a_la_luz_de_las_nociones_de_forma_y_de_informacion_2009.pdf (200/PDF/37,533,650 B) — not staged; available if the matrix accepts a third language
- Charting note: matrix readable is English — chart at EN-excerpt level with documented caveat (CORE-12/17 abstract-level precedent), or user supplies the Zone/Univocal English full text. Full EN/FR texts exist only on piracy mirrors (excluded). Simondon d.1989, French copyright subsists.

### A1-08 — Feenberg, *Questioning Technology* (Routledge 1999)
- Preface + contents (author-hosted): https://www.sfu.ca/~andrewf/books/Questioning_Technology.pdf (200/PDF/161,625 B) — staged as A1-08_Feenberg_Questioning_Technology_preface_contents.pdf
- Ch. covering Part III pp.183-236, author's own adapted piece "From Essentialism to Constructivism" (Technology and the Good Life, Chicago UP 2000): https://www.sfu.ca/~andrewf/books/Essentialism_Constructivism_Philosophy_Technology_Crossroads.pdf (200/PDF/274,348 B) — staged
- NOT open: ch. 1-2, 4-6 (Democratic Rationalization). Archive.org lending-only: https://archive.org/details/questioningtechn0000feen. Wayback CDX: zero captures of any full-text URL.
- Full text needs user action (borrow/purchase) OR chart at preface+one-chapter coverage with documented caveat.

### A1-10 — Verbeek, *What Things Do* (Penn State UP 2005)
- "Toward a Theory of Technological Mediation" (≈ ch.5-6 core mediation theory; Technoscience and Postphenomenology, Lexington 2016, pp.189-204, author-deposited): https://ris.utwente.nl/ws/files/21754033/ (200/PDF/339,139 B) — staged as A1-10_Verbeek_Toward_a_Theory_of_Technological_Mediation_2016.pdf
- "Technology Design as Experimental Ethics" (≈ ch.7-8 design ethics; Ethics on the Laboratory Floor, Palgrave 2013, pp.83-100, author-deposited): https://ris.utwente.nl/ws/files/116199772/Verbeek2013technology.pdf (200/PDF/211,636 B) — staged
- Full book: archive.org lending-only (whatthingsdophil0000verb); PSU Press / Project MUSE (muse.jhu.edu/book/58784) purchase. Dutch original (2000) no open scan. Note: peterpaulverbeek.nl domain is DEAD; current site ppverbeek.org hosts papers only.

### A1-13 — Borgmann, *Technology and the Character of Contemporary Life* (Chicago UP 1984)
- Ch. "Focal Things and Practices" (16pp, course-site host): https://religioustech.org/wp-content/uploads/2019/09/Borgmann-Albert-Focal-Practices.pdf (200/PDF/374,657 B) — staged
- Full book: archive.org lending-only (technologycharac0000borg); publisher page https://press.uchicago.edu/ucp/books/book/chicago/T/bo23186480.html. No legitimate open full text.

### A1-03 — Hui, *Art and Cosmotechnics* (e-flux/Univocal 2021)
- Author's Introduction "On the Education of Sensibility" (22pp): https://www.academia.edu/50428618/Art_and_Cosmotechnics — 403 to curl; viewable in real browser; download gated behind free login. NOT staged (gated). Locus can browser-extract if user wants.
- Related open authorial material (not book text): e-flux journal #124/#125 two-part conversation: https://www.e-flux.com/journal/124/446668/a-conversation-on-art-and-cosmotechnics-part-1 and https://www.e-flux.com/journal/125/452585/a-conversation-on-art-and-cosmotechnics-part-2 (both verified 200/HTML/190KB+198KB)
- Full book: no open copy anywhere (monoskop none, archive.org none, JSTOR paywalled 10.5749/j.ctv1qgnq42, UMN Press no OA excerpt). In copyright.

## NOT_FOUND — in-copyright, no legitimate open copy (1 row)
### A1-19 — Verbeek, *Moralizing Technology* (Chicago UP 2011)
- No open full text. archive.org lending-only: https://archive.org/details/moralizingtechno0000verb. Publisher: https://press.uchicago.edu/ucp/books/book/chicago/M/bo11309162.html. Living author, book in print — legitimately not openly available.
- Related open (not the book): Verbeek 2014 "Some Misunderstandings About the Moral Significance of Technology" (author-hosted, 200/PDF/113,463 B): https://ugc.futurelearn.com/uploads/files/3b/a4/3ba44843-a6f6-4ffe-8046-2ff52cf57ddd/Misunderstandings_-_Peter_Paul_Verbeek.pdf

---

## USER ACTIONS NEEDED (only-you items)
1. **A1-19** — archive.org borrow (free account) at https://archive.org/details/moralizingtechno0000verb, or purchase. Until then: abstract-level charting (documented decision).
2. **A1-03** — full book not open; recommend: (a) Locus browser-extracts the academia.edu 22-page Introduction (free view, login only for download), or (b) purchase/library. e-flux conversations usable as adjacent authorial material regardless.
3. **A1-13** — archive.org borrow at https://archive.org/details/technologycharac0000borg for full text; 1 chapter staged meanwhile.
4. **A1-08** — archive.org borrow at https://archive.org/details/questioningtechn0000feen for full text; preface + Part III chapter staged meanwhile.
5. **A1-10** — archive.org borrow at https://archive.org/details/whatthingsdophil0000verb or Project MUSE purchase for full text; 2 core chapters staged meanwhile.
6. **A1-06** — EN full text only via purchase (Zone/Univocal 2020) or piracy (excluded); staged FR + EN excerpts cover the thesis's core — acceptable with documented caveat.

## MATRIX URL UPDATE SUGGESTIONS (for the batch-4 patch; QC-verify at patch time)
- A1-14 Readable URL -> archive.org download URL above (keep landing); Access Type -> "Open PDF (archive.org community scan; copyright caution)"
- A1-16 Readable URL -> DLI download URL above; Access Type -> "Open PDF (DLI scan; copyright caution)"
- A1-17 Readable URL -> ia803209 URL above; Access Type -> "Open PDF (archive.org scan; copyright caution)"
- A1-09 Readable URL -> monoskop EPUB URL above; Access Type -> "Open EPUB (monoskop scan; copyright caution)"
- A1-06/08/10/13 Readable URL: add staged chapter PDFs as supplementary reads with "partial coverage" caveat; keep landing/lending URLs as canonical.
- A1-03/19: unchanged (no open full text); caveat notes updated.
