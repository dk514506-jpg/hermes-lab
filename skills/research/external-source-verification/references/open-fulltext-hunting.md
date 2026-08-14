# Hunting open full texts of in-copyright academic books

Worked case (Monstare A1-08, 2026-08-13): Andrew Feenberg, *Questioning Technology*
(Routledge 1999) — no open English full book exists; result was an honest PARTIAL
(author-hosted preface + one adapted chapter + archive.org lending fallback).
The techniques below are the reusable core; the row-specific outcome is in the report.

## Lead order that works (in-copyright, post-1990 book)

1. **Author's faculty homepage FIRST.** Authors routinely host prefaces, "Full Text of
   Book" links, and chapters *adapted from* the book. Feenberg's SFU site
   (`www.sfu.ca/~andrewf/`) kept `books/` directory listings and a publications page
   with `[Full Text of Book]` links. Grep the publications/selected-articles pages for
   the title + "Full Text"/"adapted from" before searching anywhere else.
   - Author-hosted adapted chapters are legitimately usable as PARTIAL coverage — label
     which part of the book they cover (Feenberg's "From Essentialism to Constructivism:
     Philosophy of Technology at the Crossroads" PDF = adapted from book pp. 183–236 =
     the book's Part III).
   - Author sites also host full translations (e.g. `~andrewf/TEKNIKK.pdf`, the whole
     book in Norwegian) — mention only as a bonus, never as the English requirement.
2. **archive.org metadata API, not the details page** (one curl beats a browser):
   - `curl -s https://archive.org/metadata/<id>` → PDF/epub entries with
     `"private":"true"` = CDL/lending-only, NOT open. Lending items' derivative PDFs are
     always private; don't chase them.
   - Enumerate ALL scans of a title + access status in one call:
     `curl -s "https://archive.org/advancedsearch.php?q=title%3A(<title>)%20AND%20creator%3A(<author>)&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=access-restricted-item&fl%5B%5D=publicdate&rows=20&output=json"`
     → `"access-restricted-item":"true"` = lending; no open scan exists if the only hit
     is restricted.
3. **Google Scholar `[PDF]` link resolution.** Scholar's result page shows a `[PDF]
   host` link; clicking it (browser) reveals the real file URL. Inspect the RESOLVED
   filename/URL before believing it: Scholar's "[PDF] academia.edu" for the Feenberg
   book resolved to `Questioning_Technology_preface-libre.pdf` — the preface only, not
   the book. The filename (or a pypdf page-count) disambiguates "full book" from
   "front matter only".
4. **Wayback CDX wildcard to retire a filename.** For a known-dead URL, ask whether it
   was EVER captured anywhere:
   `curl -s "https://web.archive.org/cdx/search/cdx?url=*<Filename>.pdf&output=text&limit=50&collapse=urlkey&fl=timestamp,original,statuscode,mimetype,length"`
   Empty result = never archived; stop hunting that filename. (The Feenberg PDF at
   `~andrewf/Feenberg_Questioning_Technology.pdf` had zero captures — the "former copy"
   was never in the Wayback Machine.)

## Pitfalls specific to book full-text hunting

- **Publisher "Preview PDF" URLs in search results are pre-signed S3 URLs that expire**
  (Taylor & Francis: `X-Amz-Expires=172800` = ~2 days). A 403 on the search-engine URL
  is expiry, not availability — and the preview is usually only ch. 1 + front matter
  anyway. Never report a signed S3/cloudfront URL as a stable open link; use the
  publisher landing page instead.
- **Academia.edu full-book uploads are login-walled even when uploaded by the author's
  own profile** (Feenberg's uploads on `sfu.academia.edu/Feenberg`): direct
  `academia.edu/attachments/<id>/download_file` → 403, page is Cloudflare-gated to
  curl. Classify BOT_HOSTILE (manual/institutional), NOT open — and note that one of
  the two "Questioning Technology" uploads was preface-only.
- **A book-named upload ≠ the book.** Always page-count/extract-head any PDF you're
  about to report (short `uv run --with pypdf python3 -c "from pypdf import PdfReader; ..."`
  works when pdftotext is absent; keep it a one-liner or write a script file to dodge
  the command guard). 9 pages = preface, whatever the title says.
- **Google Books "No eBook available" + HathiTrust record-only are the norm** for
  in-copyright Routledge-era books — don't spend more than one probe each.
- **Report PARTIAL honestly**: open full book OR labeled partial (preface + substantial
  adapted chapter + lending fallback record) with explicit "which chapters are NOT
  openly available". A definitive NOT_FOUND/PARTIAL after a real search beats a
  lending link dressed up as open.
- Publisher paywalled pages (taylorfrancis.com "Get Access" per chapter) = landing-only;
  the DOI landing (`doi.org/10.4324/9780203022313`) is the citable record.

## Second worked set (Monstare A1-09/A1-10, 2026-08-13): two very different outcomes

**A1-09 Don Ihde, *Technology and the Lifeworld* (Indiana UP 1990) → FOUND**, but as a
full-book **EPUB**, not PDF: monoskop hosts the complete scan at
`monoskop.org/images/f/f1/Ihde_Don_Technology_and_the_Lifeworld_From_Garden_to_Earth.epub`
(605,433 B; HTTP 200, application/octet-stream). Verify an EPUB is really the whole book
by unzipping and listing entries: 266 entries of `content/page_NNN.xml` + front matter
(page_viii etc.) = OCR page-based full text, readable in any e-reader/Calibre. EPUB is
outside the parent's FOUND taxonomy (which names PDF/full HTML), so report STATUS FOUND
with an explicit "format = EPUB, not PDF" note — a complete open full-text supersedes the
2–3-chapter PARTIAL bar. Monoskop scan of an in-copyright book = unauthorized
reproduction: record the copyright caution, treat as a reading/research copy only.
Fallbacks recorded: archive.org lending details page (lending-only), publisher page
(iupress.org) with legit $9.99 e-book, Google Books preview.

**A1-10 Peter-Paul Verbeek, *What Things Do* (Penn State UP 2005) → PARTIAL**: no open
full English text exists on legitimate hosts. Cleanest partial = author-deposited
accepted manuscripts at the University of Twente Pure repository, directly curl-able
(no portal scraping needed): `ris.utwente.nl/ws/files/<id>/<name>.pdf`. Verified pair
covering the book's core argument (both HTTP 200, application/pdf):
- `ris.utwente.nl/ws/files/21754033/` — "Toward a Theory of Technological Mediation"
  (chapter in *Technoscience and Postphenomenology: The Manhattan Papers*, Lexington
  2016) = book ch. 5–6 (postphenomenology + mediation) core; 339,139 B.
- `ris.utwente.nl/ws/files/116199772/Verbeek2013technology.pdf` — "Technology Design as
  Experimental Ethics" (chapter in *Ethics on the Laboratory Floor*, Palgrave 2013) =
  book ch. 8 (design ethics), extends ch. 7; 211,636 B.
The book's ch. 7 article version ("Materializing Morality", ST&HV 2006) is paywalled
everywhere (Sage `doi/pdf` → 403 to curl; UT portal record lists only a DOI under
"Access to Document" = closed access; academia.edu copy login-walled/unverifiable).
Dutch original *De daadkracht der dingen* (2000) has no open scan (archive.org + UT: 0
hits). Fallbacks: archive.org lending details page, PSU Press page, Project MUSE.

## New leads/pitfalls from the second set

- **Monoskop direct URL via MediaWiki API when the File: page 500s** (DB errors are
  common): `curl -s "https://monoskop.org/api.php?action=query&titles=File:<Name>&prop=imageinfo&iiprop=url&format=json"` → `imageinfo[].url` is the direct
  `monoskop.org/images/<x>/<xx>/<file>` link (the file server still serves 200 even
  when the wiki DB is down). Person pages (e.g. `Don_Ihde`) often don't exist; find
  files with Google `site:monoskop.org` queries instead (monoskop's own search API
  also 500s).
- **archive.org CDL markers**: beyond `"private":"true"` derivatives, the metadata API
  shows `"access-restricted-item":"true"` and derivatives named `_encrypted.pdf` /
  `.lcpdf` (LCP-encrypted) — all = lending-only, NOT open. The advancedsearch
  `fl[]=access-restricted-item` enumeration (existing lead #2) confirms whether ANY
  open scan exists for a title.
- **Pure/Elsevier research portals** (ris.utwente.nl, research.utwente.nl): an
  "Access to Document" section showing only a DOI = closed access, stop there; direct
  `ws/files/...` URLs serve the PDF to plain curl. Author-deposited chapters are legit
  PARTIAL coverage — label which book chapters they map to in the report.
- **Google Books API**: keyless `googleapis.com/books/v1/volumes/<id>` lookups can
  return empty/None (blocked) — don't rely on it; in-copyright academic books are
  preview-only there anyway (one probe max).
- **PhilArchive full-book .docx** linked from a PhilPapers book record →
  `philpapers.org/archive/<ID>.docx` 403s curl and is unverifiable; do not report it.
- **More shadow-library tells to exclude** (beyond dokumen.pub): memoof.me (PDF.js
  viewer serving complete books), are.na blocks naming z-lib files, slideshare posts
  with "download ebook" links, Scribd full-book uploads (login-walled + unauthorized
  uploads). None count as FOUND/PARTIAL.
- **Terminal guard also trips on piped `curl | python3 -c`** — fetch to /tmp with curl
  first, then inspect with execute_code (stdlib zipfile handles EPUB verification
  fine); consistent with the "run scripts from files" rule.
- **Hunt output format** (parent-specified, reproduce exactly per row): `ROW: <id>;`
  `STATUS: FOUND|PARTIAL|NOT_FOUND;` `URLS: <url> (http_code, content_type,
  size_bytes, note);` `NOTES: coverage, provenance, copyright caution.` Verify every
  candidate with `curl -sL -A 'Mozilla/5.0' -o /dev/null -w '%{http_code}
  %{content_type} %{size_download}\n' <URL>`; good = 200 / application/pdf /
  >100,000 B.
