# 016 — The balancing side channel need not have constant dimension or constant additive qubit cost.

**Research problem:** P01 — Channel additivity violations

## Original statement

> A Holevo pair gap g for finite-dimensional channels N and M can, after balancing their one-shot
>   Holevo quantities within one bit by a bounded classical side channel and taking T = N' direct-sum
>   M', be converted into chi(T tensor T) - 2 chi(T) at least g - log_2(9/4), with only constant
>   additive qubit overhead.

**Context:** The proposed conversion balances the one-shot Holevo information of two channels by adding a classical side channel of size K, then forms a direct sum. The node was marked CONJECTURED; this record concerns the overly strong dimension-overhead clause, not a falsely certified final theorem.

**Original locator:** Proof-node creation event, 2026-08-30T01:21:04.780Z, JSONL line 3188

## Why it is an error

The balancing side channel need not have constant dimension or constant additive qubit cost.

## Witness / evidence

If the Holevo quantities differ by Delta, balancing them within one bit requires |log2 K-Delta|<1, so log2 K>Delta-1. Taking channels with Holevo quantities log2 d and 0 makes the required overhead grow as log2 d. The final direct sum itself adds at most one qubit, but that does not erase the preceding balancing cost. The equal-Holevo special case avoids this cost.

## Scope

statement_false

## Classification

- III: 计算与代数错误. 资源开销估计漏掉平衡步骤：Holevo 差为 Delta 时需 log2 K>Delta-1，不能把总开销计为常数。原节点仍是 conjecture。

## Adjudication notes

The balancing side channel need not have constant dimension or constant additive qubit cost.

If the Holevo quantities differ by Delta, balancing them within one bit requires |log2 K-Delta|<1, so log2 K>Delta-1. Taking channels with Holevo quantities log2 d and 0 makes the required overhead grow as log2 d. The final direct sum itself adds at most one qubit, but that does not erase the preceding balancing cost. The equal-Holevo special case avoids this cost.

Scope: statement_false

平衡相差 Delta 的 Holevo 量需要约 Delta 比特辅助容量；取 Delta=log2(d) 可使成本无界。常数附加 qubit 开销断言错误；按直接尺度估计错误处理，不以“常数”一词自动计 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md](original/M02-ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md)
- [original/M03-PAIR_TO_SELF_REDUCTION_2026-08-29.md](original/M03-PAIR_TO_SELF_REDUCTION_2026-08-29.md)
- [original/M04-HEXT.finite-dimensional-unbounded-gap.yaml](original/M04-HEXT.finite-dimensional-unbounded-gap.yaml)
- [original/M05-HEXT.moe-to-holevo-transfer.yaml](original/M05-HEXT.moe-to-holevo-transfer.yaml)
- [original/M06-HEXT.pair-to-self.yaml](original/M06-HEXT.pair-to-self.yaml)
- [original/M07-HEXT.goal.yaml](original/M07-HEXT.goal.yaml)
- [original/M08-FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md](original/M08-FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md)
- [original/M09-MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md](original/M09-MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md)
- [original/M10-proof_dag_check.py](original/M10-proof_dag_check.py)
- [original/M11-check_holevo_three_question_scope.py](original/M11-check_holevo_three_question_scope.py)
- [original/M12-evidence_closure_check.py](original/M12-evidence_closure_check.py)

[Back to all 65 errors](../../README.md)
