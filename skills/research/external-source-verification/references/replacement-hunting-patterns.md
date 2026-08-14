# Replacement-hunting patterns for dead source links (verified 2026-08-13)

When an audit flags DEAD rows, these source classes worked as verified replacements
(HTTP 200 + text-layer checked) for an academic/philosophy-heavy evidence corpus.

| Need | Working pattern | Example | Caveats |
|---|---|---|---|
| Paywalled classic psych paper | ERIC full text | `files.eric.ed.gov/fulltext/ED084210.pdf` (Lepper overjustification study final report) | May be a working-paper/final-report version — verify SAME study/authors, note the difference from the canonical citation |
| Book (1990s philosophy/psych) | archive.org controlled digital lending | `/details/selfefficacyexer0000band`, `/details/questioningtechn0000feen`, `/details/technologylifewo00ihde` | Lending, not open download; needs archive.org account; verify item exists (HTTP 200) |
| Theory book PDF | monoskop.org File: pages | `monoskop.org/images/6/6f/Stiegler_Bernard_Technics_and_Time_1_...pdf` | Resolve the direct `/images/<x>/<xx>/` URL from the File page (guessing the path 404s); verify rights |
| OA journal article | PMC OA article page | `pmc.ncbi.nlm.nih.gov/articles/PMC2062525/` | curl gets a JS shell — verify full text via web_extract (Firecrawl), then record as readable |
| Author/faculty copy | lab sites, alumni hosts | `sites.lsa.umich.edu/jonides-lab/...`, `alumni.media.mit.edu/~jofish/...` | Stable and legal-ish; check pagination against the published version during charting |
| Dead DOI | find correct DOI via web_search | `10.1111/1467-6419.00150` (J Econ Surveys) replaced dead `10.1023/A:1017564312479` | Pair DOI landing + open PDF |
| Nothing open | PubMed record + DOI | `pubmed.ncbi.nlm.nih.gov/9457784/` (Gross 1998) | Landing-only; note "full text institutional"; never fake a copy |
| Brand-new book (2025) | publisher landing/preview | Cambridge Core books pages | Preview chapters only; full text institutional |

## Host behavior notes (one container's empirical map)

- **403 curl but serve the browser stack (web_extract/Firecrawl)** — philpapers.org, PMC,
  DOAJ, MIT Press Direct, erichorvitz.com. These are READABLE, not dead.
- **403 curl AND Firecrawl** — academia.edu, dl.acm.org, researchgate.net, Elsevier Pure
  portals (research.aalto.fi), Morgan & Claypool, Worktribe repositories,
  repositorio.udd.cl. Classify BOT_HOSTILE (manual/institutional), don't grind retries.
- **Hosts that time out Firecrawl but serve curl** — archive.org item PDFs (big, slow);
  use curl + pypdf/pymupdf for those.
- **Course mirrors rot silently** — a once-live `uky.edu/~eushe2/...` PDF now 302s to a
  homepage; Wayback CDX shows only the 302 was ever captured. When replacing, prefer
  author-hosted/legal copies over arbitrary mirrors, and flag mirror copies in row notes.

## Verify-everything rule

A replacement you haven't read is a new dead link. Every candidate URL must pass:
(1) HTTP status (2xx after redirects), (2) `%PDF` magic-byte sniff (or HTML text > ~800
chars), (3) pymupdf text-layer extraction on the first ~4 pages before it enters the matrix.
