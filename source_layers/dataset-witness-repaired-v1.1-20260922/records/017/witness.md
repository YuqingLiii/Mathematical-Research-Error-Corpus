# Record 017 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> For output dimension `d`, define
> 
> `f_d(eps) = eps log_2(d-1) + h_2(eps)`.
> 
> Only sufficiently small `eps` is needed below. Audenaert's Theorem 1 gives
> 
> `|S(rho)-S(sigma)| <= f_d((1/2)||rho-sigma||_1)`
> 
> for `d`-dimensional states.

Context: The surrounding claim covers arbitrary finite output dimensions. This original write lacks the later separate treatment of one-dimensional outputs.

Locator: Proof-artifact creation event, 2026-08-30T02:02:11.343Z, JSONL line 4003

## 2. Witness / adjudication

The written continuity modulus is undefined at output dimension d=1.

Substituting d=1 produces log2(d-1)=log2(0), not a finite real number. A one-dimensional output state is uniquely [1] and its entropy is exactly zero, so that case must be handled separately with zero entropy variation; it is not covered by the displayed formula. This invalidates the stated all-dimensions argument, not its repaired conclusion.

Scope: argument_invalid

d=1 时 log2(d-1) 无定义，原通用连续性公式需要单独处理平凡输出维度。仅判此边界公式。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.visible.json](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M02-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md](original/M02-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md) — inherited_sanitized_source
- [M03-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md](original/M03-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md) — inherited_sanitized_source
- [M04-STABILITY_AND_MEASURE_PROOF_20260829.md](original/M04-STABILITY_AND_MEASURE_PROOF_20260829.md) — inherited_sanitized_source
- [M05-ADDITIVE_OPEN_REGION_PROOF_20260829.md](original/M05-ADDITIVE_OPEN_REGION_PROOF_20260829.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
