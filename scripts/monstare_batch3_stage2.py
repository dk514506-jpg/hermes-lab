#!/usr/bin/env python3
"""Stage batch-3 reading materials: full text for local PDFs (CORE-03/11/16/19), consolidated extracts file, and rows JSON."""
import os, json, re
import pymupdf

OUT = "/opt/data/Monstare_batch3_sources"
os.makedirs(OUT, exist_ok=True)

# 1) Full-text extraction for local PDFs
PDFS = {"CORE-03": "CORE-03.pdf", "CORE-11": "CORE-11.pdf", "CORE-16": "CORE-16.pdf", "CORE-19": "CORE-19.pdf"}
for rid, fn in PDFS.items():
    p = os.path.join(OUT, fn)
    if not os.path.exists(p):
        continue
    doc = pymupdf.open(p)
    txt = "\n".join(doc[i].get_text() for i in range(doc.page_count))
    dst = os.path.join(OUT, f"{rid}_fulltext.txt")
    with open(dst, "w") as f:
        f.write(txt)
    print(f"{rid}: fulltext {len(txt)} chars -> {dst}")

# 2) Consolidated extracts (head + tail windows per row)
def window(path, head_n=90, tail_n=50):
    with open(path) as f:
        lines = f.read().splitlines()
    if len(lines) <= head_n + tail_n:
        return "\n".join(lines)
    head = "\n".join(lines[:head_n])
    tail = "\n".join(lines[-tail_n:])
    return f"[HEAD {head_n} lines]\n{head}\n\n[... body omitted, {len(lines)-head_n-tail_n} lines ...]\n\n[TAIL {tail_n} lines]\n{tail}"

EXTRACTS = {
    "CORE-03": f"{OUT}/CORE-03_fulltext.txt",
    "CORE-11": f"{OUT}/CORE-11_fulltext.txt",
    "CORE-13": "/opt/data/cache/web/pmc.ncbi.nlm.nih.gov-ac42206ab2.md",
    "CORE-14": "/opt/data/cache/web/consc.net-c23211ffe8.md",
    "CORE-16": f"{OUT}/CORE-16_fulltext.txt",
    "CORE-18": "/opt/data/cache/web/doi.org-168d65fcf9.md",
    "CORE-19": f"{OUT}/CORE-19_fulltext.txt",
    "CORE-20": "/opt/data/cache/web/pmc.ncbi.nlm.nih.gov-f08736b57a.md",
}
with open(f"{OUT}/batch3_reading_extracts.md", "w") as out:
    out.write("# Monstare batch 3 — reading extracts (2026-08-13)\n")
    out.write("Extracts are head+tail windows for QC/reading. Full text at the listed paths.\n\n")
    for rid, p in EXTRACTS.items():
        if not os.path.exists(p):
            out.write(f"\n## {rid}\n(MISSING: {p})\n")
            continue
        out.write(f"\n## {rid} — source: {p}\n")
        out.write(window(p))
        out.write("\n")
print("extracts written:", f"{OUT}/batch3_reading_extracts.md")

# 3) Rows JSON for subagents
ROWS = [
    {"ID": "CORE-03", "Citation": "Vansteenkiste, Williams & Resnicow (2012) — Toward systematic integration between SDT and motivational interviewing. Int J Behav Nutr Phys Act 9:23.", "Readable Source URL": "https://selfdeterminationtheory.org/wp-content/uploads/2014/04/2012_VansteenkisteWilliamsResnicow_InterventionDevelopment_IJBNPA.pdf", "Source Landing URL": "https://link.springer.com/article/10.1186/1479-5868-9-23", "Access Type": "Open PDF", "Evidence Type": "review", "Causal Status": "conceptual", "Cosmo Rel.": "medium", "H1": "yes", "H2": "partial", "Pri": "B", "Area": "core", "Function": "MECHANISM", "Fail Mode": "CF-3", "Artifact Affected": "Self-Nudging Design Card", "extract": f"{OUT}/CORE-03_fulltext.txt"},
    {"ID": "CORE-11", "Citation": "Ordonez, Schweitzer, Galinsky & Bazerman (2009) — Goals Gone Wild: The Systematic Side Effects of Over-Prescribing Goal Setting. HBS WP 09-083 / Acad Mgmt Perspect 23(1):6-16.", "Readable Source URL": "https://www.hbs.edu/ris/Publication%20Files/09-083.pdf", "Source Landing URL": "https://www.jstor.org/stable/27747490", "Access Type": "Open PDF / JSTOR landing", "Evidence Type": "review", "Causal Status": "conceptual", "Cosmo Rel.": "medium", "H1": "partial", "H2": "yes", "Pri": "B", "Area": "core", "Function": "WARNING", "Fail Mode": "CF-1", "Artifact Affected": "Design Veto Catalogue", "extract": f"{OUT}/CORE-11_fulltext.txt"},
    {"ID": "CORE-12", "Citation": "Ferster & Skinner (1957) — Schedules of Reinforcement. Appleton-Century-Crofts, New York (741 pp).", "Readable Source URL": "https://archive.org/details/schedulesofreinf0000fers", "Source Landing URL": "https://www.worldcat.org/title/191941", "Access Type": "Archive lending / catalog landing", "Evidence Type": "empirical", "Causal Status": "causal", "Cosmo Rel.": "medium", "H1": "yes", "H2": "no", "Pri": "A", "Area": "core", "Function": "MECHANISM", "Fail Mode": "CF-3", "Artifact Affected": "Design Veto Catalogue", "extract": "ABSTRACT-LEVEL (documented decision): archive lending only; catalog metadata captured in Discovery Notes. No open full text found in audit pass. Chart at catalog/known-content level with caveat."},
    {"ID": "CORE-13", "Citation": "Staddon & Cerutti (2003) — Operant Conditioning. Annu Rev Psychol 54:115-144 (NIHMS manuscript, PMC1473025).", "Readable Source URL": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1473025/", "Source Landing URL": "https://scholars.duke.edu/publication/915302", "Access Type": "Open full text / DOI landing", "Evidence Type": "review", "Causal Status": "causal", "Cosmo Rel.": "low", "H1": "yes", "H2": "no", "Pri": "B", "Area": "core", "Function": "MECHANISM/REVIEW", "Fail Mode": "CF-3", "Artifact Affected": "Motivation Crowding Watch Card", "extract": "/opt/data/cache/web/pmc.ncbi.nlm.nih.gov-ac42206ab2.md"},
    {"ID": "CORE-14", "Citation": "Clark & Chalmers (1998) — The Extended Mind. Analysis 58(1):7-19 (author HTML).", "Readable Source URL": "https://consc.net/papers/extended.html", "Source Landing URL": "https://doi.org/10.1093/analys/58.1.7 (REPLACEMENT; old 019823682X.003.0002 dead)", "Access Type": "Author HTML / DOI landing", "Evidence Type": "philosophical", "Causal Status": "conceptual", "Cosmo Rel.": "high", "H1": "partial", "H2": "yes", "Pri": "A", "Area": "core", "Function": "TELOS", "Fail Mode": "None", "Artifact Affected": "Digital Capture Architecture", "extract": "/opt/data/cache/web/consc.net-c23211ffe8.md"},
    {"ID": "CORE-16", "Citation": "Csikszentmihalyi (1990) — Flow: The Psychology of Optimal Experience. Harper & Row (312 pp).", "Readable Source URL": "https://archive.org/details/flowpsychologyof0000csik", "Source Landing URL": "https://www.harpercollins.com/products/flow-mihaly-csikszentmihalyi", "Access Type": "Archive lending / publisher landing (+ course-hosted mirror for reading)", "Evidence Type": "theoretical", "Causal Status": "conceptual", "Cosmo Rel.": "medium", "H1": "yes", "H2": "partial", "Pri": "A", "Area": "core", "Function": "MECHANISM", "Fail Mode": "None", "Artifact Affected": "Arousal/Flow/Task-Switching Layer", "extract": f"{OUT}/CORE-16_fulltext.txt"},
    {"ID": "CORE-17", "Citation": "Kazdin (1982) — Single-Case Research Designs: Methods for Clinical and Applied Settings. Oxford UP (companion: Kazdin 2021 JEAB 115(1):56-85, abstract-level).", "Readable Source URL": "https://archive.org/details/singlecaseresear00alan", "Source Landing URL": "https://books.google.com/books/about/Single_Case_Research_Designs.html?id=RvrTEQAAQBAJ", "Access Type": "Borrow/controlled digital lending or book preview", "Evidence Type": "methods", "Causal Status": "conceptual", "Cosmo Rel.": "low", "H1": "partial", "H2": "no", "Pri": "A", "Area": "methods", "Function": "METHOD", "Fail Mode": "None", "Artifact Affected": "SCED Phase Plan", "extract": "ABSTRACT-LEVEL (documented decision): 1982 book lending-only; Kazdin 2021 JEAB paywalled (abstract readable, Wiley). No open full text. Chart at abstract/known-content level with caveat."},
    {"ID": "CORE-18", "Citation": "Tate et al. (2016) — The Single-Case Reporting Guideline In BEhavioural Interventions (SCRIBE) 2016 Statement. Arch Sci Psychol 4(1):1-9 (OA; also 9 journals).", "Readable Source URL": "https://www.equator-network.org/reporting-guidelines/scribe-statement/", "Source Landing URL": "https://academic.oup.com/ptj/article/96/7/e1/2864911", "Access Type": "Open guideline page / article page / checklist PDF", "Evidence Type": "methods", "Causal Status": "conceptual", "Cosmo Rel.": "low", "H1": "partial", "H2": "no", "Pri": "A", "Area": "methods", "Function": "METHOD", "Fail Mode": "None", "Artifact Affected": "Preregistration Packet", "extract": "/opt/data/cache/web/doi.org-168d65fcf9.md"},
    {"ID": "CORE-19", "Citation": "Klasnja, Hekler, Shiffman, Boruvka, Almirall, Tewari & Murphy (2015) — Microrandomized trials: An experimental design for developing just-in-time adaptive interventions. Health Psychol 34(S):1220-1228. [URL REPLACED 2026-08-13]", "Readable Source URL": "https://www.ambujtewari.com/research/klasnja15microrandomized.pdf", "Source Landing URL": "https://doi.org/10.1037/hea0000305", "Access Type": "Author-hosted PDF / DOI landing", "Evidence Type": "methods", "Causal Status": "causal", "Cosmo Rel.": "low", "H1": "partial", "H2": "no", "Pri": "A", "Area": "methods", "Function": "METHOD", "Fail Mode": "None", "Artifact Affected": "Digital Capture Architecture", "extract": f"{OUT}/CORE-19_fulltext.txt"},
    {"ID": "CORE-20", "Citation": "Collins, Murphy & Strecher (2007) — The Multiphase Optimization Strategy (MOST) and the Sequential Multiple Assignment Randomized Trial (SMART). Am J Prev Med 32(5 Suppl):S112-S118 (PMC OA).", "Readable Source URL": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2062525/", "Source Landing URL": "https://doi.org/10.1016/j.amepre.2007.01.022", "Access Type": "Open full text (PMC OA; readable via browser-stack, curl sees JS shell) / DOI landing", "Evidence Type": "methods", "Causal Status": "causal", "Cosmo Rel.": "low", "H1": "partial", "H2": "no", "Pri": "A", "Area": "methods", "Function": "METHOD", "Fail Mode": "None", "Artifact Affected": "Intervention Component Library", "extract": "/opt/data/cache/web/pmc.ncbi.nlm.nih.gov-f08736b57a.md"},
]
with open("/opt/data/Monstare_batch_3_rows.json", "w") as f:
    json.dump(ROWS, f, indent=2)
print("rows json written: /opt/data/Monstare_batch_3_rows.json")
