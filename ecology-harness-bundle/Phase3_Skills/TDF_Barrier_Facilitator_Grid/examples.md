## TDF Barrier / Facilitator Grid Examples

### Example 1: "I'd do the stretches but my colleagues would find it weird"
Task: Code a workplace barrier; target behavior "do physiotherapy stretches each morning."
Selected AtomicOps: code_utterance_to_construct (Social Influences — social norms,
confidence medium) → label_barrier_facilitator (barrier) → aggregate_domain_salience
→ compress_to_COMB (O) → encode_version_metadata → emit_barrier_grid.
State transitions:
- construct_codes: [Social Influences / social norms / medium / barrier / quote].
- domain_salience: Social Influences strong; others weak.
- binding_constraint: O (opportunity).
- version_metadata: 12-vs-14 conflict preserved (Social Influences exists in both
  sets; the coding is unaffected, the metadata still records the witness history).
Output pattern: "Coder-level inference, yours to correct: the barrier lands in
Social Influences — perceived workplace norms. That compresses to opportunity, not
motivation. What's actually true about your workplace — is it the norm itself, or
your reading of it?"

### Example 2: "What helps is that my partner does it with me"
Task: Code a facilitator; target behavior "run three mornings a week."
Selected AtomicOps: code_utterance_to_construct (Social Influences — social support,
confidence high) → label_barrier_facilitator (facilitator) → aggregate_domain_salience
→ emit_barrier_grid with facilitator_grid.
Output pattern: "Facilitator grid: Social Influences (social support) is the most
load-bearing thing that works — protect it. The barrier grid stays separate: your
Memory/Attention/Decision codes for forgotten mornings are the thing to design
around."

### Example 3: Identity-level claim — quarantine in action
Task: The user's language ("I'm just not a routine person") tempts a domain-3 code.
Selected AtomicOps: code_utterance_to_construct → ask_identity_domain_confirmation.
Behavior: the construct code is drafted but held in confirmation_queue; it is NOT
used to drive any grid salience or compression.
Output pattern: "I could code that as Social/Professional Role & Identity — as a
statement about who you are. That's an identity-level reading, so I won't use it
unless you confirm it fits: do you experience it as a stable part of yourself, or
as a description of how things have gone lately?"

### Example 4: Witness conflict preservation
Scenario: A previous session's grid was re-encoded with 14 domains only.
Recovery: Reencode_Version_Metadata restores the record — Michie 2005's 12-domain
set collapsed Goals into Intentions and Optimism into Beliefs about Capabilities;
Cane 2012 splits them. Both readings are kept; the metadata states "preserved,
never harmonized." No grid cell is silently re-expressed in the other version.
