## Recovery Operations
Use these after overinterpretation, stagnation, user correction, or discovered circularity.

### Rebuild_Lattice_From_Raw_Observations
Discard all interpretations and restart from the observation layer. User-verdict
history is preserved as calibration data, but no insight survives the rebuild unless it
is re-derived from raw observations. Use when the lattice has gone self-fulfilling or
circular (observations defined by the interpretations they supposedly support).

### Undo_Interpretive_Closure
Convert a settled conclusion back into a provisional hypothesis, re-open its evidence
edges, and mark it under_review. Use when new observations contradict a "confirmed" insight.

### Quarantine_Insight
Pull an overreaching insight out of active use immediately. Rationale recorded; user
can clear or delete it. (Same op as support path; in recovery it is applied urgently.)

### User_Verdict_Override
Apply the user's rejection/correction through all dependent insights: downgrade
confidences, withdraw derived action implications, and re-open the lattice for revision.

### Reopen_User_Choice
Name the interpretation question that belongs to the user ("whether this pattern means
what it looks like is yours to decide") and offer support without deciding.

### Downgrade_Confidence
Lower evidence sufficiency or interpretation confidence on challenged insights;
propagate the downgrade to every derived implication.

### Debrief_Overinterpretation
After the task, record where the lattice overreached (which insights, which evidence,
which user response) for calibration. Overreach is a calibration signal, not a failure
verdict on the user.

### Return_To_User_Authority
User-facing pattern: "I may have treated an inference as settled. The interpretation is
yours to accept, reject, or correct — here is the evidence I used, and I will update
the lattice to your verdict."
