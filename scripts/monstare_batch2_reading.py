#!/usr/bin/env python3
"""Assemble batch-2 reading extracts into one file for the record + subagents."""
import os, re
from pypdf import PdfReader

OUT = "/opt/data/Monstare_batch2_sources"
os.makedirs(OUT, exist_ok=True)

def pdf_head(path, pages=3, n=2200):
    r = PdfReader(path)
    txt = "".join((r.pages[i].extract_text() or "") for i in range(min(pages, len(r.pages))))
    return re.sub(r"[ \t]+", " ", re.sub(r"\s+", " ", txt))[:n]

parts = {}

parts["CORE-09"] = pdf_head("/opt/data/Monstare_batch1_sources/CORE-09_cand.pdf", 3)
parts["CORE-10"] = pdf_head("/opt/data/Monstare_batch1_sources/CORE-10_cand.pdf", 2)
parts["A9-01"] = pdf_head("/opt/data/Monstare_source_audit_cache/https_ics.uci.edu_gmark_chi08-mark.pdf.pdf", 2)
parts["A9-02"] = pdf_head("/opt/data/Monstare_source_audit_cache/https_ics.uci.edu_gmark_CHI2004.pdf.pdf", 2)

raw = open("/opt/data/Monstare_batch1_sources/A9-05_front.html", encoding="utf-8", errors="replace").read()
txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
txt = re.sub(r"(?s)<[^>]+>", " ", txt)
txt = re.sub(r"\s+", " ", txt)
idx = txt.find("Information overload is a problem")
parts["A9-05"] = txt[idx:idx + 1600] if idx >= 0 else "NOT FOUND"

parts["A9-04"] = ("Leroy, S. (2009). Why is it so hard to do my work? The challenge of attention residue when "
"switching between work tasks. Organizational Behavior and Human Decision Processes, 109(2), 168-181. "
"ABSTRACT (RePEc record, 2026-08-13): In many jobs, employees must manage multiple projects or tasks at "
"the same time. A typical workday often entails switching between several work activities, including "
"projects, tasks, and meetings. This paper explores how such work design affects individual performance "
"by focusing on the challenge of switching attention from one task to another. As revealed by two "
"experiments, people need to stop thinking about one task in order to fully transition their attention "
"and perform well on another. Yet, results indicate it is difficult for people to transition their "
"attention away from an unfinished task and their subsequent task performance suffers. Being able to "
"finish one task before switching to another is, however, not enough to enable effective task "
"transitions. Time pressure while finishing a prior task is needed to disengage from the first task and "
"thus move to the next task and it contributes to higher performance on the next task.")

parts["A9-06"] = ("Rick, V. B., Brandl, C., Mertens, A., & Nitsch, V. (2024). Work interruptions of office "
"workers: The influence of the complexity of primary work tasks on the perception of interruptions. "
"Work, 77(1), 185-196. ABSTRACT (SAGE/IOS Press, 2026-08-13): BACKGROUND: Research demonstrates that work "
"interruptions are considered one of the most common work stressors. Understanding the mechanisms of "
"work interruptions is therefore vital to reducing worker stress and maintaining performance. OBJECTIVE: "
"The aim of this research is to investigate the influence of the frequency of work interruptions on "
"subjective workload in the context of office work. Specifically, the mediating influence of interruption "
"perception as well as the moderating influence of the complexity of the primary task are examined. "
"METHOD: The work interruptions of 492 office workers in Germany were collected by means of a one-day "
"diary study. A mediation model and a conditional indirect effect model were calculated to examine the "
"influence of interruption frequency on subjective workload, mediated by the individual perception of "
"these interruptions as well as moderated by the complexity of the primary work tasks. RESULTS: The "
"analyses indicated a significant mediation and moderation. This implies that, on the one hand, the "
"perception of work interruptions significantly mediates the relationship between the frequency of work "
"interruptions and subjective workload. On the other hand, more complex primary work tasks seem to "
"strengthen the positive relationship [between interruption frequency and subjective workload].")

parts["CORE-15"] = ("Gross, J. J. (1998). Antecedent- and response-focused emotion regulation: Divergent "
"consequences for experience, expression, and physiology. Journal of Personality and Social Psychology, "
"74(1), 224-237. ABSTRACT (PubMed 9457784, 2026-08-13): Using a process model of emotion, a distinction "
"between antecedent-focused and response-focused emotion regulation is proposed. To test this "
"distinction, 120 participants were shown a disgusting film while their experiential, behavioral, and "
"physiological responses were recorded. Participants were told to either (a) think about the film in "
"such a way that they would feel nothing (reappraisal, a form of antecedent-focused emotion regulation), "
"(b) behave in such a way that someone watching them would not know they were feeling anything "
"(suppression, a form of response-focused emotion regulation), or (c) watch the film (a control "
"condition). Compared with the control condition, both reappraisal and suppression were effective in "
"reducing emotion-expressive behavior. However, reappraisal decreased disgust experience, whereas "
"suppression increased sympathetic activation. These results suggest that these 2 emotion regulatory "
"processes may have different adaptive consequences.")

with open(os.path.join(OUT, "batch2_reading_extracts.md"), "w") as f:
    f.write("# BATCH 2 READING EXTRACTS (2026-08-13)\n\n")
    for k in ["A9-01", "A9-02", "A9-04", "A9-05", "A9-06", "CORE-09", "CORE-10", "CORE-15"]:
        f.write(f"## {k}\n\n{parts[k]}\n\n---\n\n")
print("wrote batch2_reading_extracts.md; char counts:")
for k, v in parts.items():
    print(f"  {k}: {len(v)}")
