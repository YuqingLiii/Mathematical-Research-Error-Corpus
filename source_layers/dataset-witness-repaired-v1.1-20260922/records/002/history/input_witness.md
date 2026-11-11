# Record 002 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> This explains why simply tensoring a single Hastings counterexample with
> itself cannot settle the extensive question.

**Recorded location:** Proof-development artifact, section 2, lines 150–151; original write 2026-08-20T23:41:57.547Z

**Context (annotation, not a source quotation):** Lemma 4 proves a zero normalized tensor-power gap for a literal self-pair (Phi,Phi). The following explanatory sentence extends its interpretation to a Hastings counterexample, which generally uses the distinct conjugate pair (Phi,conjugate(Phi)).

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The self-pair tensor identity does not apply to a conjugate pair.

### Argument or calculation

For a_m=S_min(Phi^tensor m), the self-pair gap is 2a_m-a_2m and its ratio to m tends to zero. For a conjugate pair the joint term is S_min((Phi tensor conjugate(Phi))^tensor m), not a_2m. Its normalized limit is a different regularized entropy and the cancellation used in Lemma 4 is unavailable.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 原会话保存的明文摘要仅短标题，不能据此判断 (Φ,Φ) 与 (Φ,conjugate Φ) 的量化/模型差异是否已被错认。

- [2026-08-20T23:32:46.621Z — codex_reasoning_summary](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md) — source line 137; recorded role: generation.

## Original materials

- [M01: PROOF.md](original/M01-PROOF.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md")
  - Coverage: Full bundled file; source lines 1–8297.
  - Relevant location(s): Proof-development artifact, section 2, lines 150–151; original write 2026-08-20T23:41:57.547Z; 1755-1776; 1755-1780 composition-scope audit; #equation-99
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md`

- [M02: GAP-003-005-create-proof.jsonl](original/M02-GAP-003-005-create-proof.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-003-005-create-proof.jsonl") · [event data](original/M02-GAP-003-005-create-proof.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–3.
  - Relevant location(s): slice line 1; original JSONL line 246 exact PROOF.md creation patch (2026-08-20T23:41:57.547Z); 1; original line 246; 1; original line 246 (2026-08-20T23:41:57.547Z / 19:41:57.547 EDT)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-003-005-create-proof.jsonl`

- [M03: additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/traces/additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl") · [event data](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 130–143.
  - Relevant location(s): lines 137
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/traces/additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl`
