#!/usr/bin/env python3
"""Second-pass re-check: pymupdf extraction on pypdf 'BAD_SCANNED' PDFs to
distinguish genuine scans from pypdf xref failures."""
import os, re

FILES = {
    "CORE-05 DeciKoestnerRyan_Meta": "/opt/data/Monstare_source_audit_cache/https_selfdeterminationtheory.org_wp-content_uploads_2014_04_1999_DeciKoestnerRyan_Meta.pdf.pdf",
    "A1-01 Hui_QuestionConcerningTech": "/opt/data/Monstare_source_audit_cache/https_ia800505.us.archive.org_20_items_cyclonopedia-negarestani-reza_The_Question_Concerning_Technology_in_China--_Yuk_Hui.pdf.pdf",
    "A1-11 Winner_WhaleAndReactor": "/opt/data/Monstare_source_audit_cache/https_ratical.org_ratville_AoS_WhaleAndReactor.pdf.pdf",
    "A2-02 Lupton_QuantifiedSelf_ch1": "/opt/data/Monstare_source_audit_cache/https_bpb-us-e2.wpmucdn.com_sites.middlebury.edu_dist_b_5028_files_2020_02_lupton-quantified-self-ch1.pdf.pdf",
    "A6-04 Parasuraman_UseMisuseDisuseAbuse": "/opt/data/Monstare_source_audit_cache/https_web.mit.edu_16.459_www_parasuraman.pdf_source_post_page---------------------------.pdf",
    "A7-08 Kirsh_IntelligentUseOfSpace": "/opt/data/Monstare_source_audit_cache/https_adrenaline.ucsd.edu_kirsh_Articles_Space_intelligent_useof_space.pdf.pdf",
    "A8-05 Bell_RitualTheoryPractice": "/opt/data/Monstare_source_audit_cache/https_web.vu.lt_rstc_a.pazeraite_files_2014_09_Catherine-Bell-Ritual-Theory-Ritual-Practice-Oxford-University-Press-USA-2009.pdf.pdf",
}

import fitz  # pymupdf

for label, path in FILES.items():
    try:
        doc = fitz.open(path)
        n = min(len(doc), 4)
        txt = ""
        for i in range(n):
            txt += doc[i].get_text() or ""
        chars = len(re.sub(r"\s+", "", txt))
        print(f"{label}: pages={len(doc)} chars_first{n}p={chars} -> {'TEXT_OK' if chars >= 300 else 'NO_TEXT'}")
        if chars < 300 and len(doc) > 4:
            # maybe text starts later; scan 10 pages in the middle
            mid = len(doc) // 2
            txt2 = "".join((doc[i].get_text() or "") for i in range(mid, min(mid + 5, len(doc))))
            chars2 = len(re.sub(r"\s+", "", txt2))
            print(f"   middle check pages {mid}-{mid+5}: chars={chars2} -> {'TEXT_OK' if chars2 >= 300 else 'NO_TEXT'}")
        doc.close()
    except Exception as e:
        print(f"{label}: ERROR {type(e).__name__}: {str(e)[:120]}")
