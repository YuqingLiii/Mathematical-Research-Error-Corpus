# Record 059 — Channel additivity violations

**Review status:** `interpretation_check_pending`.

The original paragraph already says that the published display replaced R by a generic bound. Its phrase “Retaining ... instead gives” is a proposed derivation, not a straightforward false attribution. Primary-source proof must be compared in full before treating this as a confirmed mathematical error.

## Original statement and context

> 
> The same statement holds for a non-self-adjoint polynomial after its
> standard \(2\)-by-\(2\) self-adjoint dilation.
> 
> **Proof.**  In the proof of Theorem 1.5 in the cited source, denote
> \(\widetilde q_0=q_0(1+\log q_0)\).  Immediately before the final choice
> of the tail constant, their displayed estimate has the two controlling
> terms
> 
> \[
>  \left({R(P)^3\widetilde q_0\,m^{1+2u}
>        \over\varepsilon^{1+2u}u n}\right)^m,
>  \qquad
>  \left({R(P)^6\widetilde q_0^2\,m^{1+4u}
>        \over\varepsilon^{2(1+2u)}u^2 n}\right)^m.             \tag{210}
> \]
> 
> In the published display, \(R(P)\) has already been replaced by the
> generic estimate \((Cr)^{q_0}\), proved there by counting every reduced
> word of length at most \(q_0\).  Retaining \(K_{\rm full}/\|X_{\rm F}\|\)
> instead gives (210), because the preceding test-function argument uses the
> full norm only as the radius of the interval containing every finite
> evaluation.  Their choices

**Recorded location:** Proof-development artifact, Lemma 44, lines 3860–3883; original write 2026-08-21T16:10:22.317Z

**Context (annotation, not a source quotation):** The local lemma claims a coefficient-sensitive tensor-Haar tail bound with inverse tail constant bounded by C R(P)^6 [q0(1+log q0)]^2, where R is the full-to-limit norm ratio. The paragraph attributes the required terms to an imported proof.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The imported result and its displayed bound do not by themselves license the retained-radius, tensor-Haar estimate in the local lemma.

### Argument or calculation

The quoted source replaces K/||X_F|| by the generic bound (Cr)^q0 before its final display; the local claim instead keeps R(P)=K/||X_F|| and requires uniform control over a coefficient net. Its tensor theorem is stated for GUE, with a Haar extension only mentioned separately. A valid citation does not discharge the missing rederivation tracking R and all coefficient-uniform thresholds. The later correction explicitly identifies this missing bridge and attempts a retained-radius proof; that correction does not retroactively supply the original derivation.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 短摘要说明在查看 tensor-Haar 文献，但不包含可检验的系数一致尾界推断。

- [2026-08-21T16:06:04.811Z — codex_reasoning_summary](original/M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.readable.md) — source line 64; recorded role: generation.

## Original materials

- [M01: PROOF.md](original/M01-PROOF.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md")
  - Coverage: Full bundled file; source lines 1–8297.
  - Relevant location(s): Proof-development artifact, Lemma 44, lines 3860–3883; original write 2026-08-21T16:10:22.317Z; 4149-4184; #uniformity-audit
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md`

- [M02: GAP-007-source-attribution.jsonl](original/M02-GAP-007-source-attribution.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-007-source-attribution.jsonl") · [event data](original/M02-GAP-007-source-attribution.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–3.
  - Relevant location(s): slice lines 1-2; original JSONL lines 137-138 exact PROOF.md patch and completed write (2026-08-21T16:10:22.317Z); 1-2; original lines 137-138; 1; original line 137 (2026-08-21T16:10:22.317Z / 12:10:22.317 EDT)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-007-source-attribution.jsonl`

- [M03: GAP-008-uniformity.jsonl](original/M03-GAP-008-uniformity.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-008-uniformity.jsonl") · [event data](original/M03-GAP-008-uniformity.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–7.
  - Relevant location(s): 1; original next-session line 138 (2026-08-21T16:15:33.756Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GAP-008-uniformity.jsonl`

- [M04: rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl](original/M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/21/rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl") · [event data](original/M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 57–70.
  - Relevant location(s): lines 64
  - Source: `local-session-archive/2026/08/21/rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl`
