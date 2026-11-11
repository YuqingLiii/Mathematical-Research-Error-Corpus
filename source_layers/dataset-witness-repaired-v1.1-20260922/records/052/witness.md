# Record 052 — Finite-dimensional Grothendieck bounds

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> Here the direct covariant product map in irrep \(\rho\) is exactly
> `14400/d_rho` times the canonical K-pencil adjoint

Context: The draft reused a single-vector Schur normalization after contraction over representation indices.

Locator: Exact certificate draft write, 2026-08-31T03:29:17.319Z; correction at03:30:16.130Z.

## 2. Witness / adjudication

The contraction supplies a dimension factor that cancels the divisor d_rho.

The single-vector formula has prefactor14400/d_rho. In Q^T J Q, contraction with J^{-1} contributes Tr(J^{-1}J)=d_rho. Thus the direct contracted coefficient map has prefactor(14400/d_rho)*d_rho=14400, independent of representation degree. The old code used ORDER*inverse(degree) modulo24001; the corrected code uses ORDER. Residual minor values consequently change from1400 and15799 to13280 and7143 modulo24001. The normalized Schur stage is unaffected.

Scope: computation_false

单向量系数 14400/d_rho 经 Q^T J Q 收缩还乘 Tr(J^-1 J)=d_rho，故直接映射系数应为 14400。原错误在收缩因子；不影响另行归一化的 Schur 阶段。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.readable.md](original/M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.visible.json](original/M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M02-01a0546f-67e8-7241-9a01-d3c89324279e.md.excerpt.md](original/M02-01a0546f-67e8-7241-9a01-d3c89324279e.md.excerpt.md) — inherited_sanitized_source
- [M03-d4-two-minimal-five-block-linear-nogo-certificate-20260830.json](original/M03-d4-two-minimal-five-block-linear-nogo-certificate-20260830.json) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
