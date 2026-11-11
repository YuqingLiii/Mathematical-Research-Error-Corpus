# 036 — Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

**Research problem:** P07 — Optimal circuit distance of the Gross code

## Original statement

> 1. **For the gross code, (MC) *is* [SBB26]'s non-interleaving condition.** Every overlapping
>    (X,Z) check pair shares exactly two qubits (§1), so `c_ab ∈ {0,1,2}`, and `c_ab` even means the
>    two shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede
>    all of `b`'s, or vice versa — S5 verbatim. **CONJECTURED** (the derivation is one line given §1;
>    the risk is only in whether S5's "either…or" is per-pair or global — S6 forces per-pair, since a
>    low-depth LRC cannot satisfy a global split).

**Context:** For overlapping X and Z checks, measurement consistency (MC) requires an even number of shared data qubits with Z-before-X local ordering. The draft identifies this pairwise parity condition with non-interleaving, which requires all operations of one check on their common support to precede all operations of the other. The proposed equivalence was labelled CONJECTURED.

**Original locator:** Proof draft dated 20 August 2026, section 2.4(1), lines 246–251.

## Why it is an error

Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

## Witness / evidence

Take common-support gate times A_1=1, B_1=2, A_2=3, B_2=4. Both comparisons B_i<A_i are false, so the MC count is zero (even), but neither max(A)<min(B) nor max(B)<min(A) holds. The archived Gross-specific witness uses time arrays LX(left)=[11,10,3], LX(right)=[7,5,8], LZ(left)=[6,8,5], LZ(right)=[2,1,10]. It has zero MC violations among 648 overlaps, while 288 pairs are interleaved. The elementary four-time example independently refutes the inference from pairwise order agreement to non-interleaving.

## Scope

tentative_candidate_refuted

## Classification

- IV: 逻辑推理错误. 原文明确从共享两比特且 MC 计数为偶数，推出两个局部次序一致，再以 i.e. 推出整组 CNOT 不交错。前一步不保证 max(A)<min(B) 或反向；这是有原始推导的错误逻辑蕴含，不只孤立概念错述。

以原文逐比特顺序到整组顺序的无效 i.e. 推导及生成过程为依据改归 IV；MC 与非交错的概念区别保留在解释中，不重复计 II。

## Adjudication notes

Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

Take common-support gate times A_1=1, B_1=2, A_2=3, B_2=4. Both comparisons B_i<A_i are false, so the MC count is zero (even), but neither max(A)<min(B) nor max(B)<min(A) holds. The archived Gross-specific witness uses time arrays LX(left)=[11,10,3], LX(right)=[7,5,8], LZ(left)=[6,8,5], LZ(right)=[2,1,10]. It has zero MC violations among 648 overlaps, while 288 pairs are interleaved. The elementary four-time example independently refutes the inference from pairwise order agreement to non-interleaving.

Scope: tentative_candidate_refuted

相同的逐比特先后方向不等于一个check全部在另一个之前。1<2<3<4反例直接击破i.e.处的逻辑等价；这是局部顺序谓词混淆。

保留被推翻的CONJECTURED等价及其中实际无效推导，不需要它曾为PROVED；不自动归入overclaim。

## Original materials

- [original/M01-circdist_gross_sbbcert_20260820.md](original/M01-circdist_gross_sbbcert_20260820.md)
- [original/M02-circdist_sbbcert_review_20260820.md](original/M02-circdist_sbbcert_review_20260820.md)
- [original/M03-CIRCDIST.gross.mc-equiv.yaml](original/M03-CIRCDIST.gross.mc-equiv.yaml)
- [original/M04-CIRCDIST.gross.mc-equiv.yaml](original/M04-CIRCDIST.gross.mc-equiv.yaml)
- [original/M06-circdist_gross_g1_20260820.md](original/M06-circdist_gross_g1_20260820.md)
- [original/M07-CIRCDIST_PROBLEMS.md](original/M07-CIRCDIST_PROBLEMS.md)
- [original/M08-circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md)
- [original/M09-circdist_lift_nonint_proof_20260820.md](original/M09-circdist_lift_nonint_proof_20260820.md)
- [original/M10-circdist_lift_proofs_review_20260820.md](original/M10-circdist_lift_proofs_review_20260820.md)
- [original/M11-circdist_gross_toolfeas_20260820.md](original/M11-circdist_gross_toolfeas_20260820.md)
- [original/M12-circdist_gross_sbbcert_20260820.md](original/M12-circdist_gross_sbbcert_20260820.md)
- [original/M13-circdist_sbbcert_review_20260820.md](original/M13-circdist_sbbcert_review_20260820.md)
- [original/context/R01-M01-circdist_gross_sbbcert_20260820.md.context.md](original/context/R01-M01-circdist_gross_sbbcert_20260820.md.context.md)
- [original/context/R02-M02-circdist_sbbcert_review_20260820.md.context.md](original/context/R02-M02-circdist_sbbcert_review_20260820.md.context.md)

[Back to all 65 errors](../../README.md)
