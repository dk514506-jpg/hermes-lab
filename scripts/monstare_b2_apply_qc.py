#!/usr/bin/env python3
"""Apply Purist CI revisions + Ethics dimpl hardenings to batch-2 final JSON."""
import json

P = "/opt/data/Monstare_batch_2_charting_final.json"
d = json.load(open(P))

CIS = {
    "A9-01": "The interruption regime is a candidate technics of attention (Tier-P, lab-bounded): it orders the person's attention - what may interrupt, when, and at what felt cost; the felt cost is irreducibly the person's own, varying with the person (openness, need for personal structure).",
    "A9-02": "Working spheres are a documented ordering of the person's work-activity (emic by researchers' interpretation, not direct self-report); the felt toll of constant switching is the lived face of discontinuity; the tool should mirror the user's sphere structure - as a REVISABLE locality (the user can restructure it, S10), not a frozen identity (localism).",
    "A9-04": "Attention residue is measured as a next-task performance decrement; the charting reads it as a phenomenological remainder (Tier-P, interpretive - the source does not measure the felt experience): the unfinished task persists into the next; the tool's switch-design shapes the continuity of the person's attention and the felt weight of the unfinished.",
    "A9-05": "Information overload is a milieu condition: the felt excess is the phenomenon (the source's own 'as experienced' framing); the intervention taxonomy charts the response surface - it does not calibrate the felt condition; the tool must address perceived overload before optimizing message flows; structural responsibility for the informational environment is a proposal-level claim (mixed evidence; Tier-P).",
    "A9-06": "The perceived interruption is the locus of cost: appraisal (what the interruption felt like, why it felt costly) mediates the frequency->workload relation (Tier-P - statistical mediation, cross-sectional, causal order not established; no magnitude equality licensed); the tool's interruption grammar participates in shaping the person's experienced ordering of work.",
    "CORE-09": "Self-regulation as governed return: the loop models the felt discrepancy-experience - the tool must keep the person's own standards as the reference (S1 guard) and support the felt return, not merely the correction; the cybernetic frame itself must not be operationalized as a steerable-system design - HUI-2024 (with Heidegger) identifies cybernetics with the completion of the manipulation paradigm (steuerbare Einrichtung), so a loop-based tool that treats the person as the plant is precisely the capture the cosmotechnic reading must refuse (medium Cosmo Rel.).",
    "CORE-10": "Goal-setting is a technics of directed attention (source-sanctioned mechanism: direction of attention, effort, persistence); the cosmotechnic content is the telos guard - the goal's telos must remain the person's own; under the criterion that a technics must serve the person's affirmed order of value (A1-01), goal-assignment by the tool converts the person's directedness into the tool's output function, an output instrument (Tier-P - a verdict derived from the criterion, NOT a source claim; the source's paradigm imposes goals and shows performance gains).",
    "CORE-15": "Emotion regulation grammar: antecedent-focused regulation changes the felt state at its source (reappraisal reduced disgust experience); response-focused suppression splits felt experience from expressed behavior at a physiological price (increased sympathetic activation; 'cost' interpretive, Tier-P, with boundary conditions - reappraisal may fail under load, suppression has situational uses); the tool's temporal structure (when it interrupts, when it asks for emotion work) is morally consequential under the criterion that a technics must not force the person's affective life into a hidden split (S7: no morally hollow productivity).",
}
for rid, ci in CIS.items():
    d[rid]["cimpl"] = ci

# Ethics dimpl hardenings
d["A9-06"]["dimpl"] = ("Workday Interruption Protocol: protect complex-task phases from interruption, with complexity PERSON-DESIGNATED or person-confirmed "
                       "(never a tool-side classifier - S1/S10 guard, Ethics Auditor); treat interruption perception/appraisal as a measured mediator AND as an "
                       "intervention target in the legibility/support sense (making interruptions understandable, resumable, chosen - the tool responds to the "
                       "person's appraisal; explicitly NOT felt-cost down-regulation to preserve output - the batch's moral-hollowing failure mode, Ethics "
                       "Auditor); subjective workload as a key outcome metric; use objective interruption logs alongside self-report; context-sensitive policy, "
                       "not blanket rules; direction-only import (no coefficients at abstract level).")
d["CORE-10"]["dimpl"] = ("Monstare Protocol vNext: goal specificity and difficulty as levers, gated on commitment, feedback, and task complexity; use learning "
                         "goals for complex tasks; watch the interaction with incentives (crowding risk per CORE-05/06); avoid goal imposition - the goal's telos "
                         "stays the person's own (S1 guard) and the goal architecture itself is user-revisable/removable (S10, Ethics Auditor); the felt/affective "
                         "side of goal pursuit (satisfaction, commitment) is part of the design space, not an afterthought.")

json.dump(d, open(P, "w"), indent=1)
print("updated cimpl for:", list(CIS.keys()))
print("updated dimpl for: A9-06, CORE-10")
