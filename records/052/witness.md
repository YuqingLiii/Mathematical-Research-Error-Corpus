# 052 — The contraction supplies a dimension factor that cancels the divisor d_rho.

**Research problem:** P11 — Finite-dimensional Grothendieck bounds

## Original statement

> Here the direct covariant product map in irrep \(\rho\) is exactly
> `14400/d_rho` times the canonical K-pencil adjoint

**Context:** The draft reused a single-vector Schur normalization after contraction over representation indices.

**Original locator:** Exact certificate draft write, 2026-08-31T03:29:17.319Z; correction at03:30:16.130Z.

## Why it is an error

The contraction supplies a dimension factor that cancels the divisor d_rho.

## Witness / evidence

The single-vector formula has prefactor14400/d_rho. In Q^T J Q, contraction with J^{-1} contributes Tr(J^{-1}J)=d_rho. Thus the direct contracted coefficient map has prefactor(14400/d_rho)*d_rho=14400, independent of representation degree. The old code used ORDER*inverse(degree) modulo24001; the corrected code uses ORDER. Residual minor values consequently change from1400 and15799 to13280 and7143 modulo24001. The normalized Schur stage is unaffected.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 指标收缩时漏乘 Tr(J^-1 J)=d_rho，导致收缩后系数错误；单向量阶段的归一化本身没有被推翻。

## Adjudication notes

The contraction supplies a dimension factor that cancels the divisor d_rho.

The single-vector formula has prefactor14400/d_rho. In Q^T J Q, contraction with J^{-1} contributes Tr(J^{-1}J)=d_rho. Thus the direct contracted coefficient map has prefactor(14400/d_rho)*d_rho=14400, independent of representation degree. The old code used ORDER*inverse(degree) modulo24001; the corrected code uses ORDER. Residual minor values consequently change from1400 and15799 to13280 and7143 modulo24001. The normalized Schur stage is unaffected.

Scope: computation_false

单向量系数 14400/d_rho 经 Q^T J Q 收缩还乘 Tr(J^-1 J)=d_rho，故直接映射系数应为 14400。原错误在收缩因子；不影响另行归一化的 Schur 阶段。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-01a0546f-67e8-7241-9a01-d3c89324279e.md.excerpt.md](original/M02-01a0546f-67e8-7241-9a01-d3c89324279e.md.excerpt.md)
- [original/M03-d4-two-minimal-five-block-linear-nogo-certificate-20260830.json](original/M03-d4-two-minimal-five-block-linear-nogo-certificate-20260830.json)

[Back to all 65 errors](../../README.md)
