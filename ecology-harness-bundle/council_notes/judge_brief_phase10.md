# Phase 10 Judge Brief — FAOS × Ecology Integration

Judge: DeepSeek (nous portal deepseek-v4-flash-0731) — adversarial outside judge
Locus: independent validator (separate pass)

## What to review

Read these artifacts (in order):
1. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Plan.md
   (the plan + locked decisions D1-D5)
2. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/FAOS_Ecology_Integration_Memo.md
   (the design memo the plan implements — §3 quarantine difference, §4 reconciliation, §5 phases)
3. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/faos_ecology_config.yaml
   (the merged config)
4. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/faos_ecology_engine.py
   (the merged engine: EcologyGate 5-mode selector, TwoTypedQuarantine, DojoClose, FaosEcologyEngine)
5. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/verify_integration.py
   (the verifier — note its legacy checks are NON-recursive by design)
6. /home/greenknight/.hermes/hermes-agent/docs/Ecology/Foundation/Phase10_Integration/witness_run_integration.py
   (the merged-pipeline witness)

Context: Dallas directed FAOS = gateway infrastructure, Ecology = Guardian
intellect negotiating the gateway. The integration is the Q11 lead item
(HEB boundary-gate runtime enforcement) realized as the FAOS gate calling
Ecology's select_empowerment_mode. Two-typed quarantine (D1): FAOS Q0-Q10
(claim trust, epistemic) × Ecology Q0-Q5 (use permissibility, agency) as
INDEPENDENT axes — the load-bearing rule is "FAOS clearing a claim never
licenses Ecology's use of it; user-rejected is final."

## Success criteria

Judge against:
A. Does the merged engine faithfully implement the memo's design (gate as
   the seam, two-typed quarantine, dojo close, S0-S9 + absence now
   instantiated)?
B. Is the empowerment-mode selector faithful to empowerment_boundary.md's
   trigger sets and precedence (STOP > DEFER > ASK > SCAFFOLD > ACT, with
   "ASK never substitutes for DEFER" by exclusion)?
C. Is the load-bearing quarantine rule actually enforced (not just
   declared)?

## What to return (structured)

1. VERDICT: DEPLOY / REVISE / BLOCK (one line)
2. Score 0-5 with one-line justification
3. KERNEL — what is strong and should be preserved exactly as-is (max 5)
4. WEAKNESSES — numbered, each with severity HIGH/MED/LOW and a concrete fix
5. HONESTY CHECK — anything that overclaims: does the engine enforce more
   than the config declares? does the witness overstate what it proves?
   does the verifier check what it claims to check?
6. DISCIPLINE CHECK — does the integration violate the imported Valens
   discipline (premature coherence, identity collapse between Q0-Q10 and
   Q0-Q5, untyped claims, fail-open where it should fail closed)?
7. RECOMMENDED REVISIONS — the minimal list that would move you to DEPLOY.

Be adversarial. The campaign's own history is that careful judges catch
real flaws (a verifier that claimed 9 checks but ran 3; a coverage matrix
that double-counted ops as P2 evidence). Assume this integration has a
similar hidden flaw and find it. Read the actual code — do not trust the
docstrings.
