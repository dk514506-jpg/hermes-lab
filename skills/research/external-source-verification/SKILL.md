---
name: external-source-verification
description: "Verify repos and source links are live and readable before review."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [verification, github, research, anti-fabrication, source-checking]
---

# External Source Verification

Verify user-supplied links, repos, and artifacts EXIST and are ACCESSIBLE before reviewing them, cloning them, or making claims about them. Verification is cheap (a few curl calls); fabricating a review of something you never saw is expensive (destroys trust). Never substitute a similarly-named artifact and review it as if it were the requested one — always surface the discrepancy and ask.

## When to use

- User asks you to "review this repo / this link / this tool" (especially before committing to a plan that depends on it).
- User references an artifact by name/URL and you are about to base recommendations on it.
- Any time a fetch fails with 404/auth-prompt — before concluding "doesn't exist", run the full ladder below.
- A research table/matrix/corpus carries source URLs (potentially hundreds) and a reading, note-taking, or charting pass is about to start — run the mass audit below FIRST. Silvey's rule: nail the source material before any reading begins.

## The verification ladder (GitHub example)

Run these in order; each answers a different question:

1. **Page status** — `curl -s -o /dev/null -w "%{http_code}\n" https://github.com/OWNER/REPO` → 404 = missing or private; 200 = public.
2. **API existence** — `curl -s https://api.github.com/repos/OWNER/REPO` → `{"message": "Not Found"}` = missing OR private (GitHub returns 404 for private repos to unauthenticated callers — a 404 does NOT prove non-existence).
3. **Clone behavior** — `git clone --depth 1 https://github.com/OWNER/REPO` → a prompt for Username ("could not read Username") means GitHub wants auth: private or nonexistent.
4. **Owner exists?** — `curl -s -o /dev/null -w "%{http_code}\n" https://github.com/OWNER` and `curl -s https://api.github.com/users/OWNER` (200 = real account, 404 = typo'd username).
5. **Owner's public repos** — `curl -s "https://api.github.com/users/OWNER/repos?per_page=100"` → zero repos = nothing public under that name.
6. **Find candidates** — `curl -s "https://api.github.com/search/repositories?q=NAME+in:name&per_page=10"` → look for same-named repos under OTHER owners. Distinguish them by stars/language/description before offering them as possibilities.

## Reading the results

| Evidence | Diagnosis | Fix path |
|---|---|---|
| Page 404, API 404, clone auth-prompt, owner EXISTS but has 0 public repos | Private or deleted | Ask user to make it public or paste contents |
| Owner itself 404s | Typo in username | Ask for corrected URL |
| Same name exists under a different owner | Wrong repo / different project | Present candidates WITH metadata, ask which |
| Page 200, clone works | Public — clone and review | Proceed |

## Mass source-corpus audit (liveness + readability, before reading)

When a whole corpus is on the line — an evidence matrix, a citation table, a reading list —
verifying every link is a GATE that runs BEFORE any reading/note-taking/charting pass. The
user wants source material nailed first: links live, and the text actually note-takable.
Deliver a bad-links list as a file artifact, not just a chat summary.

Workflow (script: `scripts/matrix_url_audit.py` — `uv run --with pypdf python3 matrix_url_audit.py rows.json`):

1. Dump every URL column from the table (readable URL + landing URL per row) into a JSON list
   of `{ID, Citation, Readable Source URL, Source Landing URL, Access Type, ...}`.
2. Dedupe globally; test each unique URL once, map results back to every row that uses it.
3. Parallel `curl -sL` with a browser UA: status code, redirect target, content-type, size;
   one retry on connection failure.
4. Readability probe (can notes actually be taken?):
   - PDF → extract first ~4 pages with pypdf; `<~300` text chars = candidate scanned/image-
     only PDF → flag BAD_SCANNED (provisional — see second pass, step 5). Char count alone can
     still lie in the OTHER direction: PDFs with broken ToUnicode/font-encoding maps extract as
     high char counts of control-character garbage. Spot-check the extracted head for
     recognizable words (title/abstract keywords) before declaring TEXT_OK; if the head is
     garbled, the copy is OCR-required, not text-readable.
   - HTML → strip tags/scripts, count text chars; `<~800` chars or login/paywall/captcha
     markers = stub/landing page, not full text.
5. **Second pass — disambiguation, ALWAYS run before trusting pass-1 verdicts** (script:
   `scripts/second_pass_disambiguation.py`). Pass 1 produces false positives in both
   directions; the second pass is what makes the audit trustworthy:
   - pypdf "BAD_SCANNED" is frequently WRONG. pypdf's xref parser fails on malformed xref
     tables (log noise: "Ignoring wrong pointing object") and returns 0 chars from PDFs
     that DO have a text layer. Re-extract the flagged PDFs with **pymupdf** (`uv run
     --with pymupdf`), and if the first pages still yield nothing, sample ~10 pages around
     the MIDDLE — books often have scanned front matter (title pages, plates) with a real
     text layer in the body. Middle pages > 300 chars = READY, not scanned.
   - curl 403 is NOT dead. Retry every 403/unreachable READABLE URL with the browser stack
     (`web_extract`, which renders via Firecrawl) before classifying: PhilPapers, ACM,
     ResearchGate, DOAJ, and author sites routinely block curl but serve full text to the
     browser stack. Firecrawl also OCRs scanned PDFs, so a true scan that firecrawl reads
     becomes OCR_READY, not dead.
   - For repo-hosted PDFs (institutional repositories, Pure portals), retry once with an
     alternate UA + `Referer: https://www.google.com/`. Still 403 = bot-hostile (needs
     manual/institutional access), NOT dead.
6. Classify per row (six states): READY (verified note-takable now) / OCR_READY (scanned
   but OCR pipeline verified readable) / CAVEAT (landing-only, stub, or OCR-unverified) /
   BOT_HOSTILE (link alive but needs manual/institutional access) / DEAD (needs
   replacement URL) / NO_URL (no readable URL at all).

   **6.5 Content-identity gate (mandatory for stub/bot-challenged verdicts).** Liveness +
   readability is NOT identity: a live, readable URL can be the WRONG article. For any
   row whose URL content was never read (BAD_STUB, JS-shell, captcha — PMC, publisher
   landings), verify the article identity against the row's citation BEFORE charting, via
   NCBI eutils esummary
   (`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id=PMCxxxxxx`) or
   CrossRef (`https://api.crossref.org/works/<doi>`) title/author match. Worked case
   (Monstare CORE-19, 2026-08-13): the seeded PMC readable URL (PMC5820391) was an
   entirely different study (Aasdahl et al. 2018 return-to-work scale) than the row's
   citation (Klasnja et al. 2015 microrandomized trials), and the seeded landing DOI
   (10.1016/j.cct.2015.07.003) was yet a THIRD wrong article (Broglio et al., dose
   escalation) — all passed liveness checks; only content identity caught them. A BAD_STUB
   verdict means the content was never read, so identity was never checked.
7. Write a CSV (every URL + verdict), a dedicated bad-links markdown list, and a full report.
   Cache small verified PDFs locally so the reading phase reuses them without re-downloading.

Session case study: `references/monstare-source-audit-2026-08.md`.

## Replacement hunting + additive patch-back (fix the corpus, don't fork it)

The audit's DEAD rows get verified replacements, and the corpus table is the SINGLE
canonical database — Silvey's law: *update the one matrix in place each pass; never
create a new knowledge base / workbook / derived table after a pass.* The patch is
additive and logged; it is never a rebuild. (Pattern bank: `references/replacement-hunting-patterns.md`;
generic patcher: `templates/additive_matrix_patch.py`.)

Hunt per dead row — web_search per row, verify EVERY candidate (HTTP status + `%PDF` sniff
+ pymupdf text-layer check on first ~4 pages) before it touches the matrix:

- Paywalled classic papers → ERIC full text (`files.eric.ed.gov/fulltext/EDxxxxxx.pdf`);
  if only a working-paper/final-report version of the SAME study exists (same authors,
  same experiment), use it and note the difference from the canonical citation.
- Books → for in-copyright books, check the AUTHOR's faculty homepage first (prefaces, "[Full Text of Book]" links, chapters "adapted from" the book — clean provenance, often the only open pieces). Then archive.org controlled-digital-lending items (`archive.org/details/<id>`) as the legal readable path (confirm lending-only via the metadata API — derivative PDFs marked `"private":"true"`, `_encrypted.pdf`, or `.lcpdf` are CDL, not open; `advancedsearch.php` with `fl[]=access-restricted-item` enumerates every scan's status in one call); publisher landing for preview. Monoskop hosts theory-book full texts (PDF/EPUB; resolve the direct `monoskop.org/images/<x>/<xx>/<file>` URL from the File: page, or via the MediaWiki `api.php?action=query...prop=imageinfo&iiprop=url` when the File: page 500s; full-book EPUBs count as open full-text — report FOUND with an explicit format note). Pure/Elsevier research portals (e.g. ris.utwente.nl) serve author-deposited accepted manuscripts at `ws/files/<id>/...` directly to curl — "Access to Document" showing only a DOI means closed access. Full recipe + worked cases (Feenberg *Questioning Technology* 1999 PARTIAL; Ihde *Technology and the Lifeworld* 1990 FOUND via monoskop EPUB; Verbeek *What Things Do* 2005 PARTIAL via UT-repository chapters): `references/open-fulltext-hunting.md`.
- Journal articles → PMC OA (`pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxxx/`; curl sees a JS
  shell — verify via browser-stack/web_extract, then record as readable); author-lab
  copies (psych labs, alumni hosts); DOAJ for OA records.
- Dead DOI → find the correct DOI via web_search (e.g. 10.1111/1467-6419.00150 replaced a
  dead 10.1023/A:...); pair the DOI landing with an open PDF.
- Nothing open → PubMed record as landing-only replacement with an explicit "full text
  needs institutional access" note. Never invent a readable copy.

Patch the canonical workbook additively (openpyxl — see `templates/additive_matrix_patch.py`):

- Load WITHOUT `data_only=True` (preserves formulas); patch URL/access/status/notes cells
  only; save in place. Never rebuild or replace the workbook.
- Idempotent notes: guard appends on a marker (`REPLACEMENT <date>`) so re-runs don't duplicate.
- One patch-log entry per pass: date, type, rows touched, 0 removed, 0 existing cells
  removed, what was verified.
- Read back the patched rows after saving; confirm formula cells still exist
  (count `=`-prefixed cells in formula sheets).
- openpyxl strips cached formula values — without LibreOffice (`soffice`) to recalc, say
  so; Excel recomputes on open.

## Pitfalls

- **NEVER write a review, rating, or impression of something you could not access.** Report the blocker plainly and offer the paths forward.
- **NEVER silently review a different-but-similar artifact** (e.g. the same repo name under another owner) — the user may have a private fork or a typo; reviewing the wrong thing actively misleads.
- Don't conclude "deleted" from a 404 alone — private repos are indistinguishable from missing ones without the owner's confirmation.
- Include the evidence in your report (status codes, API messages) so the user can act on it (flip visibility, re-share link).
- **Dead DOIs are common in seeded tables** — resolve with `curl -sIL https://doi.org/<id>`; a 404 DOI usually means the seeded link is stale. Find the real DOI via web_search and prefer an author-hosted open PDF.
- **University-hosted PDFs rot silently** — a link that once worked may now 302 to the department homepage. Wayback CDX (`web.archive.org/cdx/search/cdx?url=<url>&output=json`) tells you whether the file was ever captured — a captured 302 redirect is NOT a captured PDF.
- **Publisher pages (Springer/APA/ACM) often 403 bots** — that is "landing exists, full text needs institutional access", not "dead". Record as landing-only/caveat, not BROKEN.
- **pypdf "BAD_SCANNED" verdicts are frequently false** — malformed xref tables make pypdf return 0 chars from text-bearing PDFs (watch for "Ignoring wrong pointing object" noise). Always re-verify with pymupdf, and sample the MIDDLE of the document: books with scanned front matter (title pages/plates) still have a text layer in the body. Never call a book "scanned" from first-4-pages output alone.
- **curl 403 ≠ unreadable** — before flagging a readable URL dead, retry it through the browser stack (`web_extract`/Firecrawl). PhilPapers, ResearchGate, ACM, DOAJ and author sites block curl but serve full text to a rendering fetch; Firecrawl additionally OCRs scanned PDFs. HUI-2024 (891k-char book) and three journal PDFs were rescued exactly this way.
- **True scans are salvageable via the OCR pipeline** — a scanned PDF (no text layer in pymupdf either) is OCR_READY, not dead, if `web_extract` pulls real text from it. Record it as OCR_READY and note the OCR dependency for the reading pass.
- **Char count ≠ readability (broken ToUnicode maps)** — some PDFs have a text layer that extracts as control-character garbage (broken font/ToUnicode encoding); pymupdf can report TEXT_OK on it (high char count, unreadable bytes). Spot-check the extracted head for recognizable words before declaring a replacement "text-layer verified". If garbled, the copy is OCR-only — record "OCR-only" in the matrix note, never "text-layer verified". (CORE-06's Frey & Jegen replacement PDF bit exactly this way; Firecrawl OCR read it cleanly and the matrix note had to be corrected.)
- **Bot-hostile ≠ dead** — academia.edu, ACM DL, ResearchGate, Elsevier Pure portals, and some institutional repositories 403 every automated fetch (curl AND Firecrawl). Classify as BOT_HOSTILE (needs manual/institutional access), keep them out of the DEAD list, and don't burn budget grinding retries. Academia.edu full-book uploads stay login-walled (`attachments/<id>/download_file` → 403) even when uploaded on the AUTHOR's own profile; Google Scholar's "[PDF]" link for a book record may resolve to only the preface — inspect the resolved filename and page-count before trusting it (worked case: `references/open-fulltext-hunting.md`).
- **Publisher "Preview PDF" links from search engines are pre-signed S3 URLs that expire** (Taylor & Francis: `X-Amz-Expires=172800` ≈ 2 days) — a 403 on them is expiry, not absence, and the preview is usually ch. 1 + front matter anyway. Report the publisher landing page, never the signed URL.
- **Google Scholar / search-query URLs are not bot-testable** — exclude them from automated audits; they are search links, not sources.
- **Audit verdicts go stale when URLs are replaced** — a CSV verdict keyed by RowID+URL_Kind silently misattributes to the row's CURRENT URL. Compare the audited URL string to the table's current URL before acting on a verdict (Monstare CORE-20, 2026-08-13: CSV "BAD_DEAD 404" belonged to a superseded PSU overview PDF; the current PMC2062525 is live and correct). Match by URL equality, not just row ID.
- **Mirror hosts (pdfcoffee, dokumen.pub, vdoc.pub) 403 automated fetches** — don't grind on them; find open mirrors via web_search and record the rights caveat.
- **Replacement URLs must be verified before writing** — status code + `%PDF` sniff + text-layer check (pymupdf, first ~4 pages) for every candidate; an unverified replacement is just a new dead link. Prefer legal paths (archive.org lending, ERIC, PMC OA, author copies) and record rights caveats (course mirrors, working-paper versions) in the row notes.
- **Formula-bearing workbooks:** openpyxl preserves formulas but strips cached values; without LibreOffice (`soffice`) to recalc, tell the user Excel will recompute on open. Never rebuild/replace the canonical workbook.
- **Run audit/patch scripts from files, not heredocs** — long inline `python3 - <<EOF` / `-c` one-liners can be rejected by the command guard in some environments; write the script to a file and run `uv run --with ... python3 scripts/...`.

## Reporting + clarifying

1. Present the evidence compactly (status codes, API response, clone behavior, repo count).
2. List any real candidates found by search, each with stars/language/description so the user can recognize theirs.
3. Use `clarify` with concrete options: specific candidate repos, "make it public / paste contents", or "send correct URL".
