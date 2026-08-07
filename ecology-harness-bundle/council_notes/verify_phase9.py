#!/usr/bin/env python3
"""Phase 9 verification: Valens × Ecology Meld artifacts.

Run: python3 council_notes/verify_phase9.py
Verifies the Phase 9 changed paths (meld deliverables):
  1. governance/valens_operating_logics.md exists with 10 principles + S0-S9 + Q0-Q10
  2. README corpus pointer present
  3. persona_profile_schema.json node exists + registered in lattice_index.json
  4. Witness-comparison cross-link present in Contrary_Findings_and_Limits.md
  5. Printed/reconstructed footnote convention documented
  6. meld/ecology_valens_meld_charter.md exists with key decisions
  7. meld/valens_principle_coverage.md exists with 10x8 matrix + verdict
  8. Wiki synthesis exists (valens_wiki syntheses/ecology-valens-meld.md)
  9. Journal entry for 2026-08-07 exists in valens_wiki/journal/
  10. Harness verifier still passes (verify_harness.py exit 0)
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FOUNDATION = os.path.join(ROOT, "..")
POC = os.path.join(FOUNDATION, "GitHub_PoC")
WIKI = os.path.expanduser("~/Documents/digital_brain/valens_wiki")

fails = []


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def read(p):
    with open(p) as f:
        return f.read()


# 1. Governance doc: 10 principles + S0-S9 + Q0-Q10 + non-identity
g = os.path.join(POC, "governance", "valens_operating_logics.md")
gl = read(g) if os.path.exists(g) else ""
# Content-anchored principle presence (judge W5 / Locus note c): each
# principle matched by a distinctive content anchor, not bare numbering.
PRINCIPLE_ANCHORS = {
    1: "Strict pipeline ordering",
    2: "Object-tagged authority",
    3: "Condition-state logic",
    4: "witness preservation",
    5: "Topic-driven routing",
    6: "Directed-graph",
    7: "Typed numerics",
    8: "Safety as a first-class layer",
    9: "Evidence-as-test-vector",
    10: "Anti-premature-coherence",
}
for i in range(1, 11):
    anchor = PRINCIPLE_ANCHORS[i]
    check(f"logics: principle P{i} present ({anchor})", anchor in gl, "in governance doc" if gl else "MISSING FILE")
for token in ["S0 source input", "S9 unresolved", "Q0", "Q10", "Non-Identity", "deny-by-default", "deny_by_default"]:
    check(f"logics contains: {token}", token in gl)
check("logics: claim-level quarantine stated", "claims" in gl and ("deny-by-default" in gl or "deny_by_default" in gl))
check("logics: mapped-not-instantiated markers", "MAPPED-NOT-INSTANTIATED" in gl, "state-lineage + absence rows honest")

# 2. README corpus pointer
r = read(os.path.join(POC, "README.md")).lower()
check("README: corpus pointer", "corpus pointer" in r or "corpus itself" in r)
check("README: meld decision refs", "method, not findings" in r or "method, not" in r)

# 3. persona_profile schema + lattice registration
ps = os.path.join(POC, "lattices", "persona_profile_schema.json")
check("persona schema exists", os.path.exists(ps))
if os.path.exists(ps):
    pj = json.loads(read(ps))
    check("persona schema: schema id", pj.get("schema", "").startswith("ecology-lattice/persona_profile"))
    check("persona schema: boundary_gate required", pj.get("required", [])[-1] == "boundary_gate" or "boundary_gate" in pj.get("required", []))
li = json.loads(read(os.path.join(POC, "lattices", "lattice_index.json")))
check("lattice index: persona_profile layer", "persona_profile" in li.get("lattice_layers", {}))

# 4. Witness cross-link (two-way — judge W5 / rec 4)
cf = read(os.path.join(POC, "evidence", "Contrary_Findings_and_Limits.md"))
check("contrary findings: meld cross-link", "witness-comparison" in cf and "cross-link" in cf)
WIKI_REG = os.path.expanduser("~/Documents/digital_brain/valens_wiki/registers")
ar = read(os.path.join(WIKI_REG, "absence-register.md")) if os.path.exists(os.path.join(WIKI_REG, "absence-register.md")) else ""
nr = read(os.path.join(WIKI_REG, "non-operational-registry.md")) if os.path.exists(os.path.join(WIKI_REG, "non-operational-registry.md")) else ""
check("wiki absence-register: reverse cross-link", "cross-link" in ar and "Contrary_Findings" in ar)
check("wiki non-op-registry: reverse cross-link", "cross-link" in nr and "Contrary_Findings" in nr)

# 5. Footnote convention
check("footnote convention documented", "printed" in gl and "reconstructed" in gl and "(Valens" in gl)

# 6. Charter
ch = os.path.join(POC, "meld", "ecology_valens_meld_charter.md")
cl = read(ch) if os.path.exists(ch) else ""
for token in ["interface rule", "Q2.3", "Q4.1", "Q4.5", "deny-by-default", "sovereignty"]:
    check(f"charter contains: {token}", token.lower() in cl.lower())

# 7. Coverage matrix
cov = os.path.join(POC, "meld", "valens_principle_coverage.md")
check("coverage matrix exists", os.path.exists(cov))
if os.path.exists(cov):
    cv = read(cov)
    check("coverage: matrix rows", all(f"P{i}" in cv for i in range(1, 11)))
    check("coverage: packages named", all(p in cv for p in ["Human_Empowerment_Boundary", "COMB_Behavioral_Diagnosis", "TDF_Barrier_Facilitator_Grid", "SDT_Need_Support_Check", "MI_Ambivalence_Conversation", "Proximal_Practice_Selector", "Motivational_Lattice_Generator", "ConvoDojo_Practice_Sparring"]))
    check("coverage: verdict line", "verdict" in cv.lower() or "hold" in cv.lower())
    # Grounding pass (judge W5): every op/state NAME cited in EMBEDDED cells
    # must exist in the corresponding package's atomic_ops.json or
    # state_schema.json. Only snake_case tokens WITH underscores are treated
    # as artifact names (spirit_gate, quarantine_status…) — prose words
    # never contain underscores, so this cannot flag documentation prose.
    import re
    pkgs_dir = os.path.join(POC, "skills")
    ungrounded = []
    for cell_token in sorted(set(re.findall(r"[a-z][a-z0-9_]*_[a-z0-9_]+", cv))):
        found = False
        for pkg in os.listdir(pkgs_dir):
            pkg_dir = os.path.join(pkgs_dir, pkg)
            if not os.path.isdir(pkg_dir):
                continue
            for fn in ["atomic_ops.json", "state_schema.json", "edge_map.json", "skill_node.json"]:
                fp = os.path.join(pkg_dir, fn)
                if os.path.exists(fp) and cell_token in read(fp):
                    found = True
                    break
            if found:
                break
        if not found:
            ungrounded.append(cell_token)
    # Known-good cross-references that are NOT package op/state names:
    # FAOS-side mechanisms (field_model, authority_weights, relation_types),
    # estate file names (edge_map.json, recovery_ops.md, atomic_ops.json,
    # skill_node.json), and meld doc names. These are legitimate citations,
    # not ungrounded EMBEDDED evidence.
    KNOWN_EXTERNAL = {"atomic_ops", "authority_weights", "ecology_valens_meld_charter",
                      "edge_map", "field_model", "recovery_ops", "relation_types", "skill_node",
                      "state_schema"}
    ungrounded = [t for t in ungrounded if t not in KNOWN_EXTERNAL]
    check("coverage: EMBEDDED cells grounded on disk", len(ungrounded) == 0,
          f"ungrounded tokens: {ungrounded[:8]}" if ungrounded else "all snake_case artifact names resolve")
    check("coverage: P2 honesty (no EMBEDDED P2 cell)", "P2" in cv and "FAOS-inherited" in cv)

# 8. Wiki synthesis
ws = os.path.join(WIKI, "syntheses", "ecology-valens-meld.md")
check("wiki synthesis exists", os.path.exists(ws))
if os.path.exists(ws):
    w = read(ws)
    check("wiki synthesis: one-paragraph", "In one paragraph" in w)
    check("wiki synthesis: division of labor", "division of labor" in w or "Division of labor" in w)

# 9. Journal entry
je = os.path.join(WIKI, "journal", "2026-08-07.md")
check("journal entry 2026-08-07 exists", os.path.exists(je))

# 10. Harness verifier still green
hv = os.path.join(POC, "verify", "verify_harness.py")
if os.path.exists(hv):
    try:
        res = subprocess.run([sys.executable, hv], capture_output=True, text=True, timeout=120, cwd=POC)
        check("harness verifier still passes", res.returncode == 0, res.stdout.strip().splitlines()[-1] if res.stdout.strip() else "no output")
    except Exception as e:
        check("harness verifier still passes", False, str(e))
else:
    check("harness verifier still passes", False, "verify_harness.py missing")

# 11. Full post-meld witness run — all 5 dojos (judge rec 7, extended)
wr = os.path.join(POC, "meld", "witness_run_all_dojos.py")
if os.path.exists(wr):
    try:
        res = subprocess.run([sys.executable, wr], capture_output=True, text=True, timeout=180, cwd=POC)
        tail = res.stdout.strip().splitlines()[-1] if res.stdout.strip() else "no output"
        check("witness run: all 5 dojos pass", res.returncode == 0, tail)
    except Exception as e:
        check("witness run: all 5 dojos pass", False, str(e))
else:
    check("witness run: all 5 dojos pass", False, "witness_run_all_dojos.py missing")

print()
print("=== RESULT:", f"{len(fails)} FAILURES" if fails else "PASS — Phase 9 meld verified", "===")
sys.exit(1 if fails else 0)
