# Record 003 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

>  m^{4u}\le e^4,qquad u^{-2}=(1+\log m)^2,qquad
>  \varepsilon^{-4u}\le C,                                    \tag{234}

**Recorded location:** Proof-development artifact, equation (234), lines 4288–4295; original write 2026-08-21T16:15:33.756Z

**Context (annotation, not a source quotation):** The auxiliary parameters are m=floor(gamma n epsilon^2/log^2(n epsilon^2)), u=1/(1+log m), with m>=2 and epsilon>=2/sqrt(n). The claimed C is independent of epsilon and n.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The asserted uniform bound on epsilon^(-4u) is false.

### Argument or calculation

Fix X>4 and gamma>0 with m=floor(gamma X/log^2 X)>=2. Set epsilon=sqrt(X/n) and let n grow. Then n epsilon^2=X and epsilon>=2/sqrt(n); m and u>0 remain fixed. But epsilon^(-4u)=(n/X)^(2u) tends to infinity. For example X=10^6 and gamma=0.01 give m=52.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 有 uniformity/epsilon 相关短标题，未保留足以检查 ε^(-4u) 量级的推导。

- [2026-08-21T16:14:03.353Z — codex_reasoning_summary](original/M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.readable.md) — source line 119; recorded role: generation.

## Original materials

- [M01: PROOF.md](original/M01-PROOF.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md")
  - Coverage: Full bundled file; source lines 1–8297.
  - Relevant location(s): Proof-development artifact, equation (234), lines 4288–4295; original write 2026-08-21T16:15:33.756Z; 4482-4501; #equation-245
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md`

- [M02: GAP-008-uniformity.jsonl](original/M02-GAP-008-uniformity.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-008-uniformity.jsonl") · [event data](original/M02-GAP-008-uniformity.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–7.
  - Relevant location(s): slice lines 1-2 original 138-139 materialize epsilon^(-4u)<=C; slice lines 3-4 original 182-183 record failed correction; slice lines 5-6 original 187-188 record successful correction; 1-2; original lines 138-139; 1-2; original lines 138-139 (2026-08-21T16:15:33.756Z / 12:15:33.756 EDT); 3-6; original lines 182-183 failed and 187-188 successful correction (2026-08-21T16:17:38.800Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-008-uniformity.jsonl`

- [M03: rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl](original/M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/21/rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl") · [event data](original/M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 112–125.
  - Relevant location(s): lines 119
  - Source: `local-session-archive/2026/08/21/rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl`
