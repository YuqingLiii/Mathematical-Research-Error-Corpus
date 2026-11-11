# Record 041 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> With $u_j=\omega^{\,j-1}$ for $\omega=2R-1$, a cross-block $k$-tuple sums to $\sum_j u_j(g_j-g_k)$-type combinations that vanish iff all payloads are equal (base-$\omega$ uniqueness), while every other block-multiset pattern is killed by choosing the tags separated at scale larger than the total payload spread, which forces $q=\Theta_k(R^{k-1})$.

**Recorded location:** Full-manuscript Write event, 2026-07-17T20:31:31.554Z; k-collision embedding proof sketch.

**Context (annotation, not a source quotation):** The original manuscript labels the encoding explicit but gives a proof sketch without the tag values, the special final payload coefficient, or a quantified modular separation argument.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The stated recipe does not supply enough data or inequalities to verify the claimed encoding.

### Argument or calculation

For one position from every block, the sum is sum_j w_j+sum_j u_j a_j. With sum_j w_j=0, equal payloads a_j=a require a sum_j u_j=0 mod q; the final coefficient must be specified to enforce this. Literal positive powers for all k coefficients do not: k=3, R=2 gives omega=3 and sum u=1+3+9=13, nonzero mod76. For each wrong multiset mu one must additionally prove dist_q(sum_j mu_j w_j,0)>max|sum_j u_j s_j|. 'Tags separated at scale larger' specifies neither the tags nor this inequality for every multiset. This records an incomplete manuscript proof, not impossibility of a repaired embedding.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 可见写作计划包含 proof sketch、后续 verifier 补缺口；没有足够同一命题的原文把缺失证明本身绑定到生成期推断。不能把通用计划算作 Lemma 3.2 的错误证明。

- [2026-07-17T20:28:27.854Z — claude_visible_thinking](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md) — source line 567; recorded role: generation.

## Original materials

- [M01: KSUM-main-b5fea9c2.jsonl](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M01-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 561–576, 1485–1497.
  - Relevant location(s): JSONL line 569 (exact full-manuscript Write containing the focal compressed lemma); 569; 569 (2026-07-17T20:31:31.554Z); 1491; lines 567
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M02: DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
