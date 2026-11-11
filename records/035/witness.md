# 035 — Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.

**Research problem:** P06 — Circuit versus effective distance

## Original statement

> *Derivation.* Take an optimal certificate `(r_i, u_i)`. For each `i` choose a fault `f_i` with
> `E(f_i) = E_i` and `u(f_i) = u_i` (one exists, by definition of `U(E_i)`) and place it in round
> `r_i`; these are `w = |γ|` distinct circuit locations, since distinct residuals force distinct
> locations. Their detector chain is `(1+x)(A_0 + xC)` by 4.2. Let `D := A_0 + xC ∈ V` and write

**Context:** To construct a circuit lift, the draft chooses one elementary fault for each distinct effective residual and treats those choices as faults at distinct physical locations. The fault model allows only one Pauli assignment per location.

**Original locator:** Proof draft dated 20 August 2026, derivation of Lemma 5.3, lines 672–675.

## Why it is an error

Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.

## Witness / evidence

At a single ancilla-to-data CNOT a→q_j, the draft's own Proposition 1.13(4) lists possible residuals ∅, S_j, {q_j}, S_{j−1}. Here S_j is the subsequent data suffix and S_{j−1}=S_j⊕{q_j}. Choosing the ancilla-X and data-X faults for S_j and {q_j} selects the same physical location twice. Their product is one X⊗X fault of cost one with residual S_{j−1}, not two occupied locations. The formal effective basis vector [S_{j−1}] also need not equal [S_j]+[{q_j}]. This refutes the distinct-location inference; a repaired existence proof requires a collision argument.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 不同残差不推出不同物理位置；同一 CNOT 上可有多种残差，逐项选出的代表未必组成合法且等权的联合故障配置。

## Adjudication notes

Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.

At a single ancilla-to-data CNOT a→q_j, the draft's own Proposition 1.13(4) lists possible residuals ∅, S_j, {q_j}, S_{j−1}. Here S_j is the subsequent data suffix and S_{j−1}=S_j⊕{q_j}. Choosing the ancilla-X and data-X faults for S_j and {q_j} selects the same physical location twice. Their product is one X⊗X fault of cost one with residual S_{j−1}, not two occupied locations. The formal effective basis vector [S_{j−1}] also need not equal [S_j]+[{q_j}]. This refutes the distinct-location inference; a repaired existence proof requires a collision argument.

Scope: argument_invalid

不同残差不推出不同物理故障位置；同一CNOT位置不同Pauli可给出不同残差，原“since”推理错误。

维持局部证明缺陷；未完成状态不妨碍记录，亦不将一般无效推理自动称为overclaim。

## Original materials

- [original/M01-circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md)
- [original/M02-circdist_lift_proofs_review_20260820.md](original/M02-circdist_lift_proofs_review_20260820.md)
- [original/M03-circdist_lift_nonint_proof_20260820.md](original/M03-circdist_lift_nonint_proof_20260820.md)
- [original/M05-CIRCDIST_PROBLEMS.md](original/M05-CIRCDIST_PROBLEMS.md)
- [original/M06-circdist_lift_litverify2_20260820.md](original/M06-circdist_lift_litverify2_20260820.md)
- [original/M07-circdist_lift_nonint_proof_20260820.md](original/M07-circdist_lift_nonint_proof_20260820.md)
- [original/M08-circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md)
- [original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md](original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md)
- [original/context/R02-M02-circdist_lift_proofs_review_20260820.md.context.md](original/context/R02-M02-circdist_lift_proofs_review_20260820.md.context.md)

[Back to all 65 errors](../../README.md)
