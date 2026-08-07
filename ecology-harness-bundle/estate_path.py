"""estate_path.py — portable estate root resolution for the harness bundle.

The Motivational Ecology harness must run in three contexts:
  1. The home lab:  ~/.hermes/hermes-agent/docs/Ecology/Foundation/
  2. The cloud bundle: any directory containing GitHub_PoC/ + Phase10..13/
  3. An explicit override via the ECOLOGY_ESTATE_ROOT environment variable.

Resolution order:
  $ECOLOGY_ESTATE_ROOT  (explicit, highest priority)
  -> walk up from this file's location looking for GitHub_PoC/
  -> the home-lab path (last resort, keeps existing deployments working)

The bundle layout mirrors the Foundation dir:
  <root>/GitHub_PoC/           canonical estate (skills, routines, lattices, ...)
  <root>/Phase10_Integration/  merged engine + config + verifier
  <root>/Phase11_Intervention/ BCW/BCT layer
  <root>/Phase12_Activation/   conditional packages
  <root>/Phase13_Wiring/       live-wire verifier
  <root>/council_notes/        campaign gate + verifiers
  <root>/skill/                the motivational-ecology skill (SKILL.md + scripts)
"""

import os


def find_estate_root() -> str:
    """Return the absolute path of the estate root, or raise if not found."""
    # 1. Explicit override.
    env = os.environ.get("ECOLOGY_ESTATE_ROOT")
    if env and os.path.isdir(os.path.join(env, "GitHub_PoC")):
        return os.path.abspath(env)

    # 2. Walk up from this file looking for the canonical estate marker.
    here = os.path.dirname(os.path.abspath(__file__))
    probe = here
    while True:
        if os.path.isdir(os.path.join(probe, "GitHub_PoC")):
            return probe
        parent = os.path.dirname(probe)
        if parent == probe:  # reached filesystem root
            break
        probe = parent

    # 3. Home-lab fallback (the campaign's original location).
    home = os.path.expanduser("~")
    lab = os.path.join(home, ".hermes", "hermes-agent", "docs",
                       "Ecology", "Foundation")
    if os.path.isdir(os.path.join(lab, "GitHub_PoC")):
        return lab

    raise FileNotFoundError(
        "Motivational Ecology estate not found: set ECOLOGY_ESTATE_ROOT to a "
        "directory containing GitHub_PoC/ (bundle layout) or run from the "
        "home-lab path.")


ESTATE_ROOT = find_estate_root()
