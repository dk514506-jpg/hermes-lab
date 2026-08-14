from pathlib import Path
import re
root=Path('/opt/data/hermes-lab')
checks={
'docs/campaign/OVERVIEW.md':['Monstare v5 Kernel','REBASED','Dallas disposes; Silvey'],
'docs/campaign/Monstare_Cosmotechnic_V5_Rebase.md':['Monstare_v5_Kernel.md','S1 Telic','FAOS clearing a claim never licenses'],
'docs/campaign/Phase13_Plan.md':['Safety first','One lineage','No hidden thresholds','REVISE'],
'skills/motivational-ecology/SKILL.md':['Safety precedes coaching','Canonical states','Dallas disposes; Silvey','Do not claim'],
}
errs=[]
for rel,need in checks.items():
 p=root/rel; t=p.read_text()
 for n in need:
  if n not in t: errs.append(f'{rel}: missing {n}')
 print(rel,'OK' if not any(e.startswith(rel+':') for e in errs) else 'FAIL')
# Ensure all copied local pertinent skills exist and compile their markdown frontmatter minimally.
for rel in ['skills/evidence-matrix-orchestration/SKILL.md','skills/evidence-matrix-charting-qc/SKILL.md','skills/council-review/SKILL.md','skills/continuity-package-authoring/SKILL.md']:
 print(rel,'EXISTS', (root/rel).exists())
print('RESULT','PASS' if not errs else 'FAIL')
for e in errs: print('ERROR',e)
if errs: raise SystemExit(1)
