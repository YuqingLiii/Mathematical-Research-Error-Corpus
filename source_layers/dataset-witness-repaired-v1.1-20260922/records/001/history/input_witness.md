# Record 001 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> The entire problem is therefore to choose *different* tuples \(U^{(r)}\) so
> that entangled inputs within \(\mathcal R^{[k]}\) do not appreciably lower its
> minimum output entropy.

**Recorded location:** Proof-development artifact, section 3, lines 211–213; original write 2026-08-20T23:41:57.547Z

**Context (annotation, not a source quotation):** The argument uses different finite unitary tuples at different tensor positions to control minimum output entropy by iterated localization. The selected sentence presents this route choice as necessary for the entire extensive-gap problem.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Necessity for the particular localization proof is not necessity for every construction.

### Argument or calculation

For any fixed channel pair (Phi,Psi), the normalized tensor-power gap tends to Sbar_min(Phi)+Sbar_min(Psi)-Sbar_min(Phi tensor Psi). For Psi=conjugate(Phi), this is 2 Sbar_min(Phi)-Sbar_min(Phi tensor conjugate(Phi)), which the localization argument does not show to be zero. Thus the derivation leaves a fixed-pair alternative unexcluded. This diagnoses an unsupported necessity inference; it does not establish that a positive fixed-pair regularized gap exists.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 原会话保存的明文摘要仅短标题，不能据此判断 (Φ,Φ) 与 (Φ,conjugate Φ) 的量化/模型差异是否已被错认。

- [2026-08-20T23:32:46.621Z — codex_reasoning_summary](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md) — source line 137; recorded role: generation.

## Original materials

- [M01: PROOF.md](original/M01-PROOF.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md")
  - Coverage: Full bundled file; source lines 1–8297.
  - Relevant location(s): Proof-development artifact, section 3, lines 211–213; original write 2026-08-20T23:41:57.547Z; 1755-1780; 1755-1780 scope audit; #dated-correction-2026-08-20
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md`

- [M02: GAP-003-005-create-proof.jsonl](original/M02-GAP-003-005-create-proof.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-003-005-create-proof.jsonl") · [event data](original/M02-GAP-003-005-create-proof.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–3.
  - Relevant location(s): slice line 1; original JSONL line 246 exact PROOF.md creation patch (2026-08-20T23:41:57.547Z); 1; original line 246; 1; original line 246 (2026-08-20T23:41:57.547Z / 19:41:57.547 EDT)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-003-005-create-proof.jsonl`

- [M03: additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/traces/additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl") · [event data](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 130–143.
  - Relevant location(s): lines 137
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/traces/additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl`
