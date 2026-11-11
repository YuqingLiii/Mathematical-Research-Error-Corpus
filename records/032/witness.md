# 032 — Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

**Research problem:** P06 — Circuit versus effective distance

## Original statement

> **CONJECTURED 5.10 (saturation and one-round decidability).** Consequences of 5.9:
> 
> 1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
>    `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model.

**Context:** The historical saturation index was defined as the first round count after which circuit distance equals the static code distance d forever, with infinity if this never happens. It was not the index of convergence to an arbitrary lower limiting value. The quoted corollary was labelled CONJECTURED.

**Original locator:** Proof draft dated 20 August 2026, conjectured Corollary 5.10(1), lines 855–858.

## Why it is an error

Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

## Witness / evidence

Take the Steane [[7,1,3]] code with X- and Z-check supports {3,4,5,6}, {1,2,5,6}, and {0,2,4,6}. Use increasing within-check orders, all X checks followed by all Z checks, and ideal temporal boundaries. In the X check ordered (0,2,4,6), an ancilla-X fault after the second CNOT produces residual X on {4,6}. Add one data-X fault on qubit 1 before the Z-check block. The net support {1,4,6} meets each listed Z check in zero or two positions, and is not an X stabilizer: every nonzero word in their X-check rowspace has weight four, whereas this support has weight three. Thus two faults produce an undetected logical X. Appending fault-free rounds preserves this witness, so d_R≤2 for every R; it can never equal the static distance d=3 eventually. Therefore R_sat=infinity, contradicting R_sat≤3. Only the saturation-to-d claim is refuted, not eventual constancy at a lower value. The original archived calculation also reports d_eff=2 and d_R=2 for R=1,2,3,4.

## Scope

tentative_candidate_refuted

## Classification

- IV: 逻辑推理错误. 原推导由有限窗口得到 d_R 最终恒定，接着以 i.e. 推出 R_sat<=d；但 R_sat 要求最终等于静态码距 d。缺失的是 d_infinity=d，错误推断直接见于原文 5.10(1) 与其 Derivation；可见过程亦先区分过 R_sat=无穷的情形。

以已定位推导为依据改归 IV：最终恒定不能推出恒等于目标 d。不是纯输出抄写，也不因同一错误可描述为概念混淆而再加 II。

## Adjudication notes

Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

Take the Steane [[7,1,3]] code with X- and Z-check supports {3,4,5,6}, {1,2,5,6}, and {0,2,4,6}. Use increasing within-check orders, all X checks followed by all Z checks, and ideal temporal boundaries. In the X check ordered (0,2,4,6), an ancilla-X fault after the second CNOT produces residual X on {4,6}. Add one data-X fault on qubit 1 before the Z-check block. The net support {1,4,6} meets each listed Z check in zero or two positions, and is not an X stabilizer: every nonzero word in their X-check rowspace has weight four, whereas this support has weight three. Thus two faults produce an undetected logical X. Appending fault-free rounds preserves this witness, so d_R≤2 for every R; it can never equal the static distance d=3 eventually. Therefore R_sat=infinity, contradicting R_sat≤3. Only the saturation-to-d claim is refuted, not eventual constancy at a lower value. The original archived calculation also reports d_eff=2 and d_R=2 for R=1,2,3,4.

Scope: tentative_candidate_refuted

原文从d_R最终常数推出按冻结定义“最终等于静态d”的R_sat≤d，把已支持的较弱稳定结论当成较强饱和结论。CONJECTURED标签不消除其中明确写出的错误推论。

维持既有候选推论错误；用户包含未完成证明，故不得因CONJECTURED删除。

## Original materials

- [original/M01-circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md)
- [original/M02-circdist_lift_proofs_review_20260820.md](original/M02-circdist_lift_proofs_review_20260820.md)
- [original/M03-circdist_lift_iff_amendment1_20260820.md](original/M03-circdist_lift_iff_amendment1_20260820.md)
- [original/M04-circdist_lift_nonint_proof_20260820.md](original/M04-circdist_lift_nonint_proof_20260820.md)
- [original/M06-CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md)
- [original/M07-circdist_lift_litverify2_20260820.md](original/M07-circdist_lift_litverify2_20260820.md)
- [original/M08-circdist_lift_nonint_proof_20260820.md](original/M08-circdist_lift_nonint_proof_20260820.md)
- [original/M09-circdist_lift_d3gate_20260820.md](original/M09-circdist_lift_d3gate_20260820.md)
- [original/M10-circdist_lift_iff_proof_20260820.md](original/M10-circdist_lift_iff_proof_20260820.md)
- [original/M11-circdist_lift_proofs_review_20260820.md](original/M11-circdist_lift_proofs_review_20260820.md)
- [original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md](original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md)
- [original/context/R02-M02-circdist_lift_proofs_review_20260820.md.context.md](original/context/R02-M02-circdist_lift_proofs_review_20260820.md.context.md)

[Back to all 65 errors](../../README.md)
