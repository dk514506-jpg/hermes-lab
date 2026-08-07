"""Inject the _faos_root() DEFINITION into the verifiers (check for def, not call)."""
import os

FAOS_HELPER = '''
def _faos_root():
    """FAOS canonical suite root: bundle faos_canonical/ -> env -> home lab."""
    for cand in (os.path.join(ROOT, "..", "faos_canonical"),
                 os.environ.get("ECOLOGY_FAOS_ROOT"),
                 os.path.join(os.path.expanduser("~"), ".hermes",
                              "hermes-agent", "docs")):
        if cand and os.path.isfile(os.path.join(cand, "scripts", "run_tests.sh")):
            return os.path.abspath(cand)
    raise FileNotFoundError("FAOS canonical suite not found (run_tests.sh)")
'''


def _inject(path):
    s = open(path).read()
    if "def _faos_root" in s:
        print(f"def already present: {path}")
        return
    lines = s.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "import sys":
            idx = i
            break
    else:
        raise RuntimeError(f"no 'import sys' in {path}")
    helper = FAOS_HELPER.strip("\n").splitlines()
    lines[idx + 1:idx + 1] = helper
    open(path, "w").write("\n".join(lines))
    print(f"def injected: {path}")


for p in ["Phase10_Integration/verify_integration.py",
          "Phase12_Activation/verify_phase12.py",
          "Phase13_Wiring/verify_phase13.py"]:
    _inject(p)
print("done")
