# Case study — Monstare evidence-matrix source audit (2026-08-13)

Context: the Monstare research matrix (`/opt/data/Monstare_Evidence_Matrix_Source_Links_v3_Staleness_Patched_artifact.xlsx`)
carries source URLs for 129 evidence rows. A charting batch was started, and Silvey
interrupted it with a workflow directive: **stop reading/charting; verify the provided
URLs are readable and note-takable first; keep a list of bad source links.** The rule is
now: for this project (and research corpora generally), the link audit is a gate BEFORE
any reading pass.

## Scope & shape of the audit

- 129 rows, 128 with a Readable Source URL, 129 with a Source Landing URL; **A3-09 has no
  readable URL at all** (row-level NO_URL flag).
- 257 unique URLs across both columns. Host mix: 46 doi.org, 31 archive.org,
  10 link.springer.com, 9 selfdeterminationtheory.org, 5 press.uchicago.edu,
  5 pmc.ncbi.nlm.nih.gov, 4 monoskop.org, 4 arxiv.org, 4 dl.acm.org, 3 psycnet.apa.org,
  3 openlibrary.org, plus long tail.
- Access-type mix: 30 "Open PDF / DOI landing", 17 "Archive lending / publisher landing",
  24 rows "Located - restricted readable", 1 "PDF found / copyright status should be
  reviewed" (A1-01), 1 "Companion source found" (HUI-2024).
- Google Scholar / Scholar-Web-Search-URL columns exist per row but were NOT bot-testable —
  excluded from the audit by design.

## Confirmed broken/stale links (found before/during the audit)

| Row | Seed URL | Finding | Replacement path |
|---|---|---|---|
| CORE-04 (Bandura 1997) | uky.edu/~eushe2/Bandura/Bandura1997SE.pdf | dead — 302s to motivation.uky.edu homepage; Wayback CDX only ever captured the 302 redirect, never the PDF | psycnet record 1997-08589-000 is the landing; needs a live open mirror (pdfcoffee/dokumen.pub/vdoc.pub all 403 bots) — unresolved at session end |
| CORE-06 (Frey & Jegen 2001) | bsfrey.ch/articles/C_317_01.pdf | dead — 302s to publications listing; seeded DOI 10.1023/A:1017564312479 is a 404 | real DOI is 10.1111/1467-6419.00150 (J Econ Surveys 15(5):589-611); open PDF confirmed at bsfrey.ch/wp-content/uploads/2021/08/motivation-crowding-theory.pdf |

Other data points: archive.org item PDFs are live but slow (firecrawl times out on them —
use curl + pypdf instead); psycnet/Springer/ACM pages 403 bots (landing-only, not dead).

## Second pass — disambiguation results (same session, later the same day)

Pass 1 over-flagged. The second pass (pymupdf re-extraction + browser-stack retries)
rescued 9 rows and reclassified 4 true scans as OCR-READY. **Final counts across 129 rows:
57 READY / 3 OCR_READY / 45 CAVEAT / 8 BOT_HOSTILE / 15 DEAD / 1 NO_URL.**

- **False "BAD_SCANNED" (pypdf xref failures / scanned front matter):** A1-01 (Hui, 348p),
  A1-11 (Winner, 216p), A8-05 (Bell, 289p) all have real text layers — pymupdf found
  7,600-10,700 chars in the middle pages while the first 4 pages yielded <200. The
  first-4-pages heuristic alone would have wrongly required OCR for three load-bearing
  philosophy rows.
- **True scans, OCR-verified:** CORE-05 (Deci/Koestner/Ryan meta, 42p), A2-02 (Lupton ch1),
  A6-04 (Parasuraman & Riley) — 0 chars in pypdf AND pymupdf, but Firecrawl (web_extract)
  extracted full text including CORE-05's d-values → OCR_READY. A7-08 (Kirsh) also a true
  scan but the OCR attempt timed out → stayed CAVEAT.
- **curl 403 rescued by browser stack:** HUI-2024 (PhilPapers → full 891k-char book text),
  A6-05 (ResearchGate IEEE paper), A9-07 (erichorvitz.com PDF), A7-05 (DOAJ page), A5-09
  (MIT Press gateway, abstract-level) — all verified readable via web_extract.
- **BOT_HOSTILE (alive but needs manual/institutional access, NOT dead):** A2-06
  (academia.edu), A3-03 (dl.acm.org), A3-06 (Morgan & Claypool, host unreachable), A3-08
  (Worktribe repo), A4-03 (ResearchGate), A4-04 (repositorio.udd.cl), A7-06
  (leiderschapsdomeinen.nl, host unreachable), A7-09 (Aalto Pure portal). Alternate-UA +
  Google-referer curl retry confirmed 403s are host policy, not transient.
- **Final DEAD list (15, needs replacement):** CORE-04, CORE-07, CORE-09, CORE-10, CORE-15,
  CORE-20, A1-05, A1-06, A1-07, A1-08, A1-09, A2-05, A3-04, A3-05, A4-02.
- **Verified fixes recorded:** CORE-06 replacement PDF confirmed readable (23p, text OK) —
  bsfrey.ch/wp-content/uploads/2021/08/motivation-crowding-theory.pdf + DOI
  10.1111/1467-6419.00150. CORE-04 (Bandura) still unresolved — all mirrors bot-blocked;
  legal path = APA PsycBooks/library.
- Deliverables for the next session: Monstare_source_verification_FINAL_2026-08-13.md
  (master report), Monstare_source_verification_FINAL_2026-08-13.csv (per-row),
  Monstare_source_link_audit_2026-08-13.csv (raw per-URL), verified PDF cache under
  /opt/data/Monstare_source_audit_cache/. Batch-1 charting remains PAUSED until the
  source material is nailed (user directive).

## Technique notes (see scripts/matrix_url_audit.py)

- `uv run --with openpyxl` / `uv run --with pypdf` — no pip on this host; ephemeral deps
  this way (PEP 668 safe).
- PDF readability probe = pypdf text extraction of first ~4 pages; <300 chars => scanned.
  HTML probe = stripped-text char count + paywall/login marker grep.
- Small verified PDFs cached under a source-audit cache dir for the reading phase.
- Batch-1 charting was PAUSED per user directive; parked source files:
  `/opt/data/Monstare_batch1_sources/` (CORE-06_raw.pdf = motivation-crowding-theory.pdf;
  A1-01_raw.pdf = archive.org Hui book PDF). The 8-row spine batch and role prompts stay
  as built (role prompts in `/opt/data/Monstare_role_prompts/`).

## Phase 3 — replacement hunt + additive patch-back (same day, later session)

Silvey directed: find replacements for the DEAD rows and patch the canonical matrix in
place, adding the explicit correction: **"exit/update the evidence matrix with each pass;
do not create a new knowledge base after every reading."** Working law for the project:
ONE canonical workbook, additive patches, one patch-log entry per pass; no derived
workbooks/reports/KBs per pass.

Verified replacement table (17 rows patched into the canonical xlsx on 2026-08-13; every
URL passed HTTP-200 + pymupdf text-layer check before write):

| Row | Replacement readable URL | Class |
|---|---|---|
| CORE-04 Bandura 1997 | archive.org/details/selfefficacyexer0000band | Archive lending (PsycBooks = institutional path); resolves the earlier "unresolved" note |
| CORE-06 Frey & Jegen | bsfrey.ch/wp-content/uploads/2021/08/motivation-crowding-theory.pdf | Open PDF + corrected DOI 10.1111/1467-6419.00150 |
| CORE-07 Lepper et al | files.eric.ed.gov/fulltext/ED084210.pdf | ERIC final-report of the SAME overjustification study (JPSP paywalled) — noted as working-paper version |
| CORE-09 Carver & Scheier | erlanbakiev.weebly.com/uploads/1/0/8/3/10833829/controltheory.pdf | Course mirror (26p, text OK) |
| CORE-10 Locke & Latham | home.ubalt.edu/tmitch/642/Articles%20syllabus/locke%20pract%20goal%20setting%202002%20am%20psy.pdf | Course mirror (13p) |
| CORE-15 Gross 1998 | pubmed.ncbi.nlm.nih.gov/9457784/ | Landing-only; full text institutional (no open copy found) |
| CORE-20 Collins MOST | pmc.ncbi.nlm.nih.gov/articles/PMC2062525/ | PMC OA; browser-stack readable (curl sees JS shell) |
| A1-05 Simondon MEOT | livingindigitalarchives.wordpress.com/wp-content/uploads/2018/07/gilbert-simondon-on-the-mode-of-existence-of-technical-objects.pdf | Univocal 2016 trans. (294p); alt rybn.org 1980 Mellamphy trans. |
| A1-06 Simondon Individuation | philpapers.org/rec/SIMIIL | Record + Google Books preview only; no open full text |
| A1-07 Stiegler TT1 | monoskop.org/images/6/6f/Stiegler_Bernard_Technics_and_Time_1_The_Fault_of_Epimetheus.pdf | Monoskop PDF (313p); alt archive.org lending |
| A1-08 Feenberg | archive.org/details/questioningtechn0000feen | Archive lending |
| A1-09 Ihde | archive.org/details/technologylifewo00ihde | Archive lending |
| A2-05 Grinberg | cambridge.org/core/books/ethnography-of-an-interface/2F0A3EDF02855E14AEDCF64F600A31AA | CUP landing/preview (2025 book) |
| A3-04 Baumer & Silberman | ics.uci.edu/~djp3/classes/2011_01_INF134/papers/impl9-rev.pdf | Course mirror (4p) |
| A3-05 Sengers et al | alumni.media.mit.edu/~jofish/writing/sengersetalRDfinalfinal.pdf | Author copy (10p) |
| A3-09 Pierce | dl.acm.org/doi/10.1145/2207676.2208540 + S2 record | Landing (was NO_URL); no open PDF — manual |
| A4-02 Berman et al | sites.lsa.umich.edu/jonides-lab/wp-content/uploads/sites/439/2016/10/2008_2.pdf | Author lab (6p) |
| HUI-2024 | note only | Local verified copy /opt/data/machine and sovereignty yuk hui.pdf (352p, UMN OA edition) |

Patch mechanics used (see templates/additive_matrix_patch.py): openpyxl load WITHOUT
data_only (44 Dashboard formulas survived); idempotent note appends guarded on
"REPLACEMENT 2026-08-13"; one Source Patch Log row (17 rows + HUI-2024 note, 0 removed);
readback verified. No LibreOffice on host → cached formula values stripped; Excel
recalcs on open (disclosed to user).

Still open: the 8 BOT_HOSTILE rows need manual/institutional retrieval before their
reading pass; A1-06 and CORE-15 remain landing-only (no open full text).
