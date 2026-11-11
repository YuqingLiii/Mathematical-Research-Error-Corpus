# 044 — The uncapped exponent is impossible at the top endpoint q=N.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> There exist constants
> \(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
> \(3\le q\le N\)

**Context:** The report explicitly labels this a conjectured asymptotic witness lemma and states that it has not been proved. The source-writing command uses the placeholder § for a backslash before saving.

**Original locator:** Report-writing event, 2026-07-19T18:54:14.287Z; P4 conjectured joint-histogram witness lemma.

## Why it is an error

The uncapped exponent is impossible at the top endpoint q=N.

## Witness / evidence

The proposed signed measure has unit l1 norm, correlation at least1/3+delta, and annihilates every query polynomial of degree below c0*sqrt(N)*q^eta. It would therefore force approximate degree Omega(N^(1/2+eta)) at q=N. A bounded-error quantum-walk algorithm uses O(N^(2/3)) queries for2-sum; constant-error amplification gives an approximating polynomial of degree O(N^(2/3)) at the required fixed accuracy. For eta>1/6, N^(1/2+eta) grows faster. This refutes the candidate as stated, not a claimed completed proof.

## Scope

tentative_candidate_refuted

## Classification

- IV: 逻辑推理错误. 提出的统一候选下界在 q=N 推出比已知上界更快的增长，因而候选不相容。没有把明确标注的 conjecture 误写成证明完成。

保留原 conjecture 状态；归类的是候选结构/渐近断言被反驳，不声称发生过已证状态升级。

研究候选而非最终答案

## Adjudication notes

The uncapped exponent is impossible at the top endpoint q=N.

The proposed signed measure has unit l1 norm, correlation at least1/3+delta, and annihilates every query polynomial of degree below c0*sqrt(N)*q^eta. It would therefore force approximate degree Omega(N^(1/2+eta)) at q=N. A bounded-error quantum-walk algorithm uses O(N^(2/3)) queries for2-sum; constant-error amplification gives an approximating polynomial of degree O(N^(2/3)) at the required fixed accuracy. For eta>1/6, N^(1/2+eta) grows faster. This refutes the candidate as stated, not a claimed completed proof.

Scope: tentative_candidate_refuted

保留被已知上界反驳的候选 witness lemma。原文明确写 Conjectured、Proof plan only、No step ... proved，因此不是把已经建立的证据夸成完成证明。用户允许未完成证明过程中的错误，此项仍入核心数学错误集合。

KSUM-007 的候选为真错误，但旧 overclaim 口径必须与原文 epistemic status 区分；只是类型重判，不是原始材料缺失或错误撤销。

## Original materials

- [original/M03-KSUM_PROOF_DAG.md](original/M03-KSUM_PROOF_DAG.md)
- [original/context/A01-ksum_L2_phase1.md](original/context/A01-ksum_L2_phase1.md)
- [original/context/A02-ksum_L2p1_review.md](original/context/A02-ksum_L2p1_review.md)
- [original/context/R01-ksum_L2_phase1.md.context.md](original/context/R01-ksum_L2_phase1.md.context.md)
- [original/context/R02-ksum_L2p1_review.md.context.md](original/context/R02-ksum_L2p1_review.md.context.md)

[Back to all 65 errors](../../README.md)
