# Record 044 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> There exist constants
> \(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
> \(3\le q\le N\)

Context: The report explicitly labels this a conjectured asymptotic witness lemma and states that it has not been proved. The source-writing command uses the placeholder § for a backslash before saving.

Locator: Report-writing event, 2026-07-19T18:54:14.287Z; P4 conjectured joint-histogram witness lemma.

## 2. Witness / adjudication

The uncapped exponent is impossible at the top endpoint q=N.

The proposed signed measure has unit l1 norm, correlation at least1/3+delta, and annihilates every query polynomial of degree below c0*sqrt(N)*q^eta. It would therefore force approximate degree Omega(N^(1/2+eta)) at q=N. A bounded-error quantum-walk algorithm uses O(N^(2/3)) queries for2-sum; constant-error amplification gives an approximating polynomial of degree O(N^(2/3)) at the required fixed accuracy. For eta>1/6, N^(1/2+eta) grows faster. This refutes the candidate as stated, not a claimed completed proof.

Scope: tentative_candidate_refuted

保留被已知上界反驳的候选 witness lemma。原文明确写 Conjectured、Proof plan only、No step ... proved，因此不是把已经建立的证据夸成完成证明。用户允许未完成证明过程中的错误，此项仍入核心数学错误集合。

KSUM-007 的候选为真错误，但旧 overclaim 口径必须与原文 epistemic status 区分；只是类型重判，不是原始材料缺失或错误撤销。

## 3. Evidence and verification

原候选与历史独立审查完整；本轮复算指数比较并保留文献上界依赖，没有声称重证量子 walk 算法。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-KSUM-L2-019f7bb0.jsonl.readable.md](original/M01-KSUM-L2-019f7bb0.jsonl.readable.md) — inherited_sanitized_source
- [M01-KSUM-L2-019f7bb0.jsonl.visible.json](original/M01-KSUM-L2-019f7bb0.jsonl.visible.json) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.readable.md](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.visible.json](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json) — inherited_sanitized_source
- [M03-KSUM_PROOF_DAG.md](original/M03-KSUM_PROOF_DAG.md) — inherited_sanitized_source
- [R01-ksum_L2_phase1.md.context.md](reconciliation_sources/R01-ksum_L2_phase1.md.context.md) — reconciliation_source_window
- [R02-ksum_L2p1_review.md.context.md](reconciliation_sources/R02-ksum_L2p1_review.md.context.md) — reconciliation_source_window
- [A01-ksum_L2_phase1.md](reconciliation_sources/A01-ksum_L2_phase1.md) — supplementary_artifact
- [A02-ksum_L2p1_review.md](reconciliation_sources/A02-ksum_L2p1_review.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
