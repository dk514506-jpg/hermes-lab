#!/usr/bin/env python3
"""Apply Purist revisions (Wave 2) to Monstare_batch_3_charting_final.json atomically."""
import json

P = "/opt/data/Monstare_batch_3_charting_final.json"
d = json.load(open(P))

def sub(rid, field, old, new):
    v = d[rid][field]
    assert old in v, f"MISSING in {rid}.{field}: {old[:60]}..."
    d[rid][field] = v.replace(old, new)
    print(f"OK {rid}.{field}")

# CORE-03
sub("CORE-03", "dimpl",
    "Unify the tool's motivational grammar around volition (autonomy support: choice, rationale, acknowledgment of resistance); M2 need-support profile stays a design heuristic, not a validated manipulation (batch-1 pilot rule). Telos remains the person's own (CORE-02 ruling carries).",
    "The tool's register supports the person's own volitional process (choice, rationale, acknowledgment of resistance) - never a tool-owned motivational layer; volitional outcomes are the person's, not engagement metrics. M2 need-support profile stays a design heuristic, not a validated manipulation (batch-1 pilot rule). Telos remains the person's own (CORE-02 ruling carries).")
sub("CORE-03", "cimpl",
    "Volition over compliance - the tool must never purchase behavior through compliance-shaped grammar; autonomy support is the criterion, and coercion-by-nudge is a false integration (Tier-P application under A1-01/HUI-2024 criterion).",
    "Volition over compliance - the tool must never purchase behavior through compliance-shaped grammar; the person's own volitional process is the criterion (autonomy support is the means, not a lever), and coercion-by-nudge is a false integration (Tier-P application under A1-01/HUI-2024 criterion).")

# CORE-12
sub("CORE-12", "dimpl",
    "Contingency/schedule design (M4c) - import direction + bounded band only; never a point schedule rule; the tool's reward grammar must respect schedule dynamics (extinction, satiation, contrast) as failure modes.",
    "Contingency/schedule design (M4c) - schedule dynamics (extinction, satiation, contrast) are veto criteria for any tool-side reinforcement layer: the tool must not possess one; where schedule concepts inform the design grammar, import direction + bounded band only, never a point rule.")
sub("CORE-12", "cimpl",
    "Slot-machine schedules risk dependency - variable-ratio reward architectures in a productivity tool are the dependency failure mode (CF-3). NOTE: this linkage leans on the UNVERIFIED VR-extinction textbook reading - Tier-P hypothesis, not charted finding; aligns with CORE-16's 'self becomes captive of a certain kind of order' passage.",
    "Any contingency-scheduled reward architecture in a tool is veto territory (CF-3): schedule control of the person is the dependency/captive-self failure mode per the CORE-16 criterion ('the self becomes captive of a certain kind of order'). The specific variable-ratio mechanism remains an UNVERIFIED hypothesis (abstract-level row), not a charted finding.")

# CORE-13
sub("CORE-13", "cimpl",
    "Consequence engineering has hidden costs - a behaviorist reward grammar applied to the person is the manipulation paradigm (HUI-2024 cybernetics guard; consistent with batch-2 CORE-09 refusal: the loop must not treat the person as the plant). Consequences as mirror, not leash (Tier-P).",
    "Consequence engineering has hidden costs - a behaviorist reward grammar applied to the person is the manipulation paradigm (HUI-2024 cybernetics guard; consistent with batch-2 CORE-09 refusal: the loop must not treat the person as the plant). Consequences as mirror, not leash: the tool surfaces consequences as information for the person's judgment, with no contingent scheduling or withholding on the tool side - the mirror is disclosure, not a loop; any contingency pairing is person-authored (Tier-P).")

# CORE-14
sub("CORE-14", "cimpl",
    "Cognitive design is also world-design - externalization is not neutral; designing the cognitive environment is designing the person's world (organology/proportion per HUI-2024); extended mind licenses locality, not colonization (criterion-derived Tier-P application, not Hui's finding).",
    "Cognitive design is also world-design - externalization is not neutral; designing the cognitive environment is designing the person's world (organology per HUI-2024 - exteriorized memory is an organ of the person; locality per A1-01's human-milieu cosmotechnics); extended mind licenses locality, not colonization, and locality means the person retains authorship and revision authority over a SHARED environment - not exclusion, which would forfeit prosthesis (criterion-derived Tier-P application under the C&C parity criterion, not Hui's finding).")

# CORE-16
sub("CORE-16", "dimpl",
    "Conditions suppliable; state not forceable - the tool can supply flow's conditions (clear goals, immediate feedback, calibrated challenge) but must not command or extract the state;",
    "Conditions suppliable; state not forceable - the tool can supply flow's conditions (clear goals, immediate feedback, challenge options at the person's choosing) but must not command or extract the state;")

# CORE-17
sub("CORE-17", "cimpl",
    "Rigorous N-of-1 inference vs false generalization - single-case rigor honors the person's singularity; the pilot must never present per-case results as population-causal.",
    "Per-case claims stay per-case - the pilot never trades the person's singular record for a population average (Tier-P: an inference-scope application, not a moral valuation of uniqueness); rigorous N-of-1 inference is the guard against false generalization.")

# CORE-19
sub("CORE-19", "dimpl",
    "Best for high-frequency digital prompts/JITAI - the tool's component testing (Digital Capture Architecture) uses microrandomization for proximal-effect attribution; full-system claims require a confirming phase (CORE-20); decision points must be defined in the capture architecture.",
    "For JITAI-style component testing - used only where the person opts into prompt density; prompt frequency is person-capped, never a tool-tuned scalar. The tool's component testing (Digital Capture Architecture) uses microrandomization for proximal-effect attribution; full-system claims require a confirming phase (CORE-20); decision points must be defined in the capture architecture.")
sub("CORE-19", "cimpl",
    "Rigor for the digital channel - honest causal attribution of digital components serves the person; but component optimization must never optimize the person's attention away (S1/S10 guard; the tool stays a locality, not an optimizer of the user).",
    "Rigor for the digital channel - honest causal attribution of digital components serves the person; but component optimization must never treat the person's attention or engagement as an optimizable resource (S1/S10 guard; the tool stays a locality, not an optimizer of the user).")

# CORE-20
sub("CORE-20", "cimpl",
    "Avoid confounding the whole ecology - the tool must not optimize the person's total environment as if it were a component set; the ecology is the person's locality, not the optimizer's (S1; HUI-2024 locality/localism guard).",
    "Avoid confounding the whole ecology - the tool must not optimize the person's total environment as if it were a component set; the ecology is the person's locality, not the optimizer's. The operative distinction is standpoint: the person may optimize their own locality; the tool may not (S1; matrix locality guard anchored in A1-01's human-milieu cosmotechnics and HUI-2024's technodiversity/organology - matrix vocabulary, not a Hui-2024 phrase).")

json.dump(d, open(P, "w"), indent=2)
print("ALL PURIST REVISIONS APPLIED")
