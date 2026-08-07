#!/usr/bin/env python3
"""Test harness for phase2_api_probe.py — live API checks + import-guard check."""
import json
import importlib.util
import os
import re
import sys
import tempfile

SRC = os.path.join(os.path.dirname(__file__), "phase2_api_probe.py")
failures = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        failures.append(name)


# 1. Import guard: importing a temp copy (output paths redirected to a fresh
#    temp dir) must NOT write any files — proves top-level side effects are gone.
tmp = tempfile.mkdtemp()
src = open(SRC).read()
src = re.sub(r'OUT_JSONL = ".*"', f'OUT_JSONL = "{tmp}/seed.jsonl"', src)
src = re.sub(r'OUT_MD    = ".*"', f'OUT_MD    = "{tmp}/seed.md"', src)
copy_path = os.path.join(tmp, "probe_copy.py")
open(copy_path, "w").write(src)

spec = importlib.util.spec_from_file_location("p2p_copy", copy_path)
p2p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p2p)  # the import itself
check("import guard: no side-effect files written by import",
      not os.path.exists(f"{tmp}/seed.jsonl") and not os.path.exists(f"{tmp}/seed.md"),
      f"jsonl={os.path.exists(f'{tmp}/seed.jsonl')} md={os.path.exists(f'{tmp}/seed.md')}")

# 2. Live API function checks (per=2, small)
try:
    n, out = p2p.openalex('"skill atrophy" OR "deskilling"', per=2)
    check("openalex: returns (count, list)", isinstance(n, int) and isinstance(out, list) and n > 0, f"total={n} returned={len(out)}")
    check("openalex: record shape", bool(out) and all(k in out[0] for k in ("title", "year", "authors", "venue", "cited", "doi", "url")),
          str(list(out[0].keys()) if out else "empty"))
except Exception as e:
    check("openalex: live call", False, repr(e))

try:
    out = p2p.pubmed("motivational interviewing", per=2)
    check("pubmed: returns list", isinstance(out, list) and len(out) > 0, f"returned={len(out)}")
    check("pubmed: record shape", bool(out) and all(k in out[0] for k in ("title", "year", "authors", "venue", "pmid")),
          str(list(out[0].keys()) if out else "empty"))
except Exception as e:
    check("pubmed: live call", False, repr(e))

try:
    out = p2p.arxiv("role-play", per=2)
    check("arxiv: returns list", isinstance(out, list) and len(out) > 0, f"returned={len(out)}")
    check("arxiv: record shape", bool(out) and all(k in out[0] for k in ("title", "year", "authors", "arxiv_id", "url")),
          str(list(out[0].keys()) if out else "empty"))
except Exception as e:
    check("arxiv: live call", False, repr(e))

try:
    out = p2p.s2("empowerment human agency", per=2)
    check("s2: returns list (may be empty on rate limit)", isinstance(out, list), f"returned={len(out)}")
except Exception as e:
    check("s2: live call", False, repr(e))

# 3. End-to-end: run main() against the temp output paths, then validate JSONL
try:
    p2p.main()
    check("e2e: main() completes", os.path.exists(p2p.OUT_JSONL) and os.path.exists(p2p.OUT_MD))
    recs = [json.loads(l) for l in open(p2p.OUT_JSONL) if l.strip()]
    check("e2e: jsonl records valid", len(recs) > 0 and all(isinstance(r, dict) and "_api" in r and "_query" in r for r in recs), f"records={len(recs)}")
    check("e2e: every record has title+year", all(r.get("title") and r.get("year") for r in recs))
    md = open(p2p.OUT_MD).read()
    check("e2e: md digest has sections", md.startswith("# Phase 2 API Seed Registry") and "## " in md)
except Exception as e:
    check("e2e: main() run", False, repr(e))

print(f"\n{len(failures)} failure(s)" if failures else "\nALL CHECKS PASSED")
sys.exit(1 if failures else 0)
