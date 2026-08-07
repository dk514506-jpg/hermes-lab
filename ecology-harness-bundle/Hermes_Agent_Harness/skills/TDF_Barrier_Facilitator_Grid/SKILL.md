## TDF Barrier / Facilitator Grid

### Purpose
This skill codes user statements about a stuck goal or habit into the 14 TDF
domains over 84 constructs, emits a salience-ordered barrier/facilitator grid,
compresses the grid to a COM-B binding constraint (14→3), and carries version
metadata for the 12-vs-14 domain witness conflict (preserved, never harmonized).
It is the finest-grained diagnostic layer of the ecology: COMB_Behavioral_Diagnosis
decomposes into this skill when the six-component profile needs resolution.
Grounded in Cane 2012 (full text; 37-expert card sort, 112 constructs → 14
domains / 84 constructs; silhouette 0.29 below the 0.50 stated threshold — encode
this fragility), Michie 2005 (12 domains), Zhou 2024 (1382 pubs), and Wu 2024
(40 clinicians, 19 barriers / 7 enablers). All domain assignments are coder-level
inference: labeled RECONSTRUCTED, user-correctable.

### Trigger Conditions
Use this skill when any of the following are true:
- A COM-B profile exists and one or more components need finer resolution.
- The user describes barriers or facilitators in detail ("I'd do it if...", "The
  reason it never happens is...", "What helps is...").
- An implementation question needs a domain-level answer (why does this routine
  not stick?).
- A Proximal_Practice_Selector or BCW/BCT selection step needs a barrier grid.
- The user asks "what is really in the way?" and the answer must not be a
  single-component guess.

### Inputs
Required inputs:
- target_behavior: The behavior under analysis (verb + context).
- user_statements: Utterances about barriers, facilitators, and the stuck behavior.
- component_profile: Optional — the COM-B profile this grid refines.
Optional inputs:
- interview_or_reflection_log: Longer user reflections (TDF interview-guide style).
- motivational_lattice_insights: Provisional, evidence-cited insights only.
- schedule_or_social_data: Opt-in context for domains 11–12.
- prior_grids: Earlier grids for salience change tracking (N-of-1 loop).

### Outputs
Primary output: barrier_grid — 14-domain × salience record (none / weak /
moderate / strong), each populated domain carrying construct-level codes with
confidence weights, polarity (barrier / facilitator / mixed), and evidence quotes.
Secondary outputs:
- facilitator_grid: Salience-ordered facilitators (what works, to be protected).
- binding_constraint_comb: COM-B compression result (C / O / M) via verified 14→3 mapping. NOTE: renamed from binding_constraint (Phase 4 decision 4 — collision fix with COMB's six-component binding_constraint).
- version_metadata: The 12-vs-14 witness conflict record (see encode_version_metadata).
- hypothesis_status: "coder-level inference — user-correctable" label.
- confirmation_queue: Items needing explicit user confirmation (domain 3
  identity-level interpretations; any high-confidence construct on thin evidence).
- next_skill_candidates: Proximal_Practice_Selector, SDT_Need_Support_Check,
  MI_Ambivalence_Conversation, revised COM-B profile.

### State Variables
- target_behavior: string
- utterance_log: array of {quote, polarity, provisional_construct}
- construct_codes: array of {construct_id, domain, construct, confidence, polarity, evidence_quote}
- domain_salience: object over the 14 domains {none|weak|moderate|strong}
- barrier_grid: array (salience-ordered)
- facilitator_grid: array (salience-ordered)
- binding_constraint_comb: enum C | O | M | none (renamed Phase 4 — collision fix)
- version_metadata: object {domains_14, domains_12, conflict: "preserved", mapping_notes}
- hypothesis_status: true (coder-level inference)
- confirmation_queue: array of {claim, reason, status}
- user_corrections: array of {construct, user_statement, accepted}

### Atomic Operations
- code_utterance_to_construct — Map a user utterance to a construct, then a
  domain, with a confidence weight (Cane 2012 provenance; low confidence when the
  utterance is ambiguous or the domain's own validation is fragile). Labeled
  RECONSTRUCTED inference, user-correctable.
- label_barrier_facilitator — Assign polarity (barrier / facilitator / mixed) per
  coded construct, using the user's own framing where possible.
- aggregate_domain_salience — Roll construct codes up to the 14 domains; compute
  salience from count, confidence, and user emphasis.
- order_grid_by_salience — Emit the barrier grid (and facilitator grid) sorted by
  salience, most load-bearing first.
- compress_to_COMB — Compress the 14-domain grid to C / O / M via the verified
  TDF→COM-B mapping (Cane 2012 / Michie 2011 linkage); output the binding constraint.
- encode_version_metadata — Record the 12-vs-14 witness conflict (Michie 2005 vs
  Cane 2012): which domains differ, what the 12-domain set collapsed, and the
  rule "preserve both readings; never harmonize."
- ask_identity_domain_confirmation — Before any domain-3 (Social/Professional Role
  & Identity) or identity-level claim is used, get explicit user confirmation;
  otherwise hold it in the confirmation queue.
- separate_evidence_interpretation — Keep utterance quote, construct code,
  confidence, and implication in disciplined layers in every grid cell.
- emit_barrier_grid — Render the ordered grid with evidence quotes and confidence
  in user language.
- record_grid — Write grid, version metadata, and confirmation queue to task state.

### Typed Edges
#### decomposes_to
- code_utterance_to_construct, label_barrier_facilitator, aggregate_domain_salience,
  order_grid_by_salience, compress_to_COMB, encode_version_metadata,
  ask_identity_domain_confirmation, separate_evidence_interpretation,
  emit_barrier_grid, record_grid
#### can_follow
- Proximal_Practice_Selector (barrier grid → proximal practice design — RECONSTRUCTED)
- SDT_Need_Support_Check (M-domain and identity-domain barriers → need support — RECONSTRUCTED)
- MI_Ambivalence_Conversation (Intentions/Emotions/Behavioural-Regulation barriers → evocation — RECONSTRUCTED)
- COMB_Behavioral_Diagnosis (grid → revised component profile — RECONSTRUCTED reverse pass)
#### compatible_with
- Feedback_Ecology_Map (domain 11–12 feedback evidence — RECONSTRUCTED)
- Material_Arrangement_Scan (domain 11 environmental evidence — RECONSTRUCTED)
- Motivational_Lattice_Generator (provisional insights as construct evidence — RECONSTRUCTED)
#### supports
- COMB_Behavioral_Diagnosis (14-domain grid refines the six-component profile — VERIFIED, Cane 2012 mapping)
- Proximal_Practice_Selector (domain salience is a proximal-state input)
#### recovers_with
- Human_Empowerment_Boundary (identity overreach, premature closure, user correction)
- Reopen_Construct_Assignment, Downgrade_Confidence, Mark_Identity_Claim_Provisional,
  Reencode_Version_Metadata (see recovery_ops.md)

### Empowerment Boundary
The agent may do automatically:
- code utterances to constructs/domains (labeled inference); aggregate salience;
  order grids; compress to COM-B; draft version metadata; organize evidence quotes.
The agent must preserve for the user:
- the final interpretation of what the grid means for them; acceptance or
  correction of any construct code; every identity-level claim (domain 3 and any
  "this says something about who you are" reading); whether a barrier is real to
  them; whether a facilitator is worth protecting.

### Learnability / Skill-Atrophy Check
Before emitting a grid, ask:
- Is this grid teaching the user the domain vocabulary so they can code their own
  barriers next time (fade to self-coding), or is it a black-box verdict?
- Does the user know which codes are mine (coder-level inference) versus which
  statements are theirs (quoted verbatim)?
- Am I resolving ambiguity for the user or asking them to resolve it? Domain
  assignment is the agent's job; meaning-making is the user's.
- Would hiding the confidence weights create false certainty the user cannot audit?
- Attribution clarity: the user must always be able to distinguish their own
  contribution from the agent's coded interpretation.

### Motivational-Lattice Interface
This skill may use motivational-lattice insights only as candidate construct
evidence: provisional, observation-cited, relevant, and user-revisable.
Quarantine (hard rules):
- Identity-level interpretations (domain 3 and any identity-adjacent claim) must
  not be applied without explicit user confirmation.
- No normative claims ("you are the kind of person who...") derived from grid
  codes — coder-level inference is not a verdict.
- Never let an uncited lattice insight raise a construct's confidence weight.

### Conversational / Practice Mode
In practice or sparring mode, this skill trains the user to distinguish barriers
from facilitators and to spot their own dominant domains:
- Present one sample statement; ask the user to pick the domain; give rubric
  feedback keyed to Cane 2012 construct definitions, not verdicts.
- Sparring move: challenge overgeneralized coding ("You put everything under
  Social Influences — where does Environmental Context live in your account?").
- Practice the 12-vs-14 difference as a witnessing exercise: the user sees that
  both readings exist and that the conflict is preserved, not resolved.
- If the user is overwhelmed, present the top-3 salience domains only, then expand.

### Guardrails
- Every grid cell separates quote, code, confidence, and implication.
- Identity-level claims (domain 3) require explicit user confirmation — always.
- Never harmonize the 12-vs-14 domain conflict; preserve it as metadata.
- Never present coder-level inference as fact (Cane 2012 silhouette fragility:
  encode low confidence where the domain validation itself was weak).
- Knowledge is not an independent cluster in Cane's own data — flag it when a
  Knowledge code would carry the whole diagnosis.
- Social data only with opt-in (domains 11–12).
- No medical advice under domain 1/2 adjacent claims; refer to professional care.
- Never use grid codes to manipulate, shame, or coerce.

### Failure Modes
- Overconfidence: high-confidence construct codes on thin evidence.
- Identity overreach: domain-3 claims used without confirmation.
- Version harmonization: silently merging the 12 and 14 domain sets.
- Grid-as-verdict: coder inference presented as fact (fragile validation ignored).
- Knowledge-dominance error: over-weighting Knowledge codes despite Cane's own
  finding that Knowledge is not an independent cluster.
- Salience illusion: count-weighted salience ignoring user emphasis.
- Compression loss: 14→3 compression hiding the domain-level story.
- False certainty: confidence weights omitted, so the user cannot audit.

### Recovery Operations
- Reopen_Construct_Assignment: Re-code any construct the user rejects, with the
  user's correction recorded in user_corrections.
- Downgrade_Confidence: Lower a construct's confidence weight when evidence is
  thin or the user disputes it.
- Mark_Identity_Claim_Provisional: Convert any domain-3 or identity-level claim
  into a labeled hypothesis pending user confirmation.
- Reencode_Version_Metadata: Restore the 12-vs-14 witness conflict if it was
  ever flattened or harmonized.
- Separate_Evidence_Interpretation: Rebuild a grid cell into quote → code →
  confidence → implication layers.
- Return_To_User_Authority: Explicitly state the user interprets the grid.
- Escalate_To_Empowerment_Boundary: Invoke Human_Empowerment_Boundary on identity
  overreach, paternalism, or interpretive closure.
(De-ossification path: Reopen_Construct_Assignment + Downgrade_Confidence —
unfreezing construct codes the agent hardened on thin evidence.)

### Examples
See examples.md.

### Handoff Notes
Place this folder at:
Hermes_Agent_Harness/skills/TDF_Barrier_Facilitator_Grid/
Pip can generate the files locally; Dallas must save or upload them into the
OneDrive/SharePoint harness location. Keep skill_node.json, edge_map.json, and
skill_graph_index.json in agreement after any edge change. The 84-construct
codebook reference is Cane 2012; this package carries representative constructs
and the coding discipline, not a re-encoding of the full inventory.
