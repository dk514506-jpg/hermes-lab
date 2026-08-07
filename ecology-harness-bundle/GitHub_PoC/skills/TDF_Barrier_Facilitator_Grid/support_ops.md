## Support Operations
Use these when prerequisites are missing before another skill can proceed.

### Require_Target_Behavior
The grid needs a pinned target behavior (verb + context). If missing, run
COMB_Behavioral_Diagnosis.specify_target_behavior first — never code into a
vacuum.

### Seed_From_COMB_Profile
If a COM-B profile exists, use its flagged components as coding priors (e.g.,
M-Au strong → attend to Reinforcement, Memory/Attention/Decision,
Behavioural Regulation codes). Priors lower, never raise, confidence thresholds.

### Reopen_Construct_Assignment
When the user rejects a code, re-code with their correction recorded in
user_corrections; the grid stays coder-level inference throughout.

### Downgrade_Confidence
Lower a construct's confidence weight when evidence is thin, the utterance is
ambiguous, or the domain's own validation is fragile (Cane 2012 silhouette
0.29 < 0.50 — encode fragility, do not hide it).

### Hold_In_Confirmation_Queue
When an identity-level claim (domain 3) appears, draft the code but hold it in
confirmation_queue pending explicit user confirmation. It does not contribute
to salience or compression until confirmed.

### Reencode_Version_Metadata
If a grid was built against only one version of the TDF (12 or 14), restore the
witness conflict record: both readings preserved, never harmonized.
