import fitz
d = fitz.open('/opt/data/Monstare_batch3_sources/CORE-16.pdf')
print("pages:", d.page_count)
for i in range(3):
    txt = d[i].get_text()[:400].replace('\n', ' | ')
    print(f"--- page {i+1}: {txt}")
