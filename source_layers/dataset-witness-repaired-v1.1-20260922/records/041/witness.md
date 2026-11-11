# Record 041 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> With $u_j=\omega^{\,j-1}$ for $\omega=2R-1$, a cross-block $k$-tuple sums to $\sum_j u_j(g_j-g_k)$-type combinations that vanish iff all payloads are equal (base-$\omega$ uniqueness), while every other block-multiset pattern is killed by choosing the tags separated at scale larger than the total payload spread, which forces $q=\Theta_k(R^{k-1})$.

Context: The original manuscript labels the encoding explicit but gives a proof sketch without the tag values, the special final payload coefficient, or a quantified modular separation argument.

Locator: Full-manuscript Write event, 2026-07-17T20:31:31.554Z; k-collision embedding proof sketch.

## 2. Witness / adjudication

The stated recipe does not supply enough data or inequalities to verify the claimed encoding.

For one position from every block, the sum is sum_j w_j+sum_j u_j a_j. With sum_j w_j=0, equal payloads a_j=a require a sum_j u_j=0 mod q; the final coefficient must be specified to enforce this. Literal positive powers for all k coefficients do not: k=3, R=2 gives omega=3 and sum u=1+3+9=13, nonzero mod76. For each wrong multiset mu one must additionally prove dist_q(sum_j mu_j w_j,0)>max|sum_j u_j s_j|. 'Tags separated at scale larger' specifies neither the tags nor this inequality for every multiset. This records an incomplete manuscript proof, not impossibility of a repaired embedding.

Scope: argument_invalid

保留稿件 explicit encoding 引理中的真实局部错误：正文给所有 u_j 取正幂，却宣称等 payload 时和为零；正确脚本有特殊末位负和系数。稿件还把未展开的 tag 分离义务作为已证显式构造。不能把脚本中存在正确完整构造误说成整个 embedding 不可能。

KSUM-003 旧溯源已比较脚本与交付稿，不是资料没找到。此次保留同一稿件压缩丢项错误；witness 严格限制于所写公式及其证明缺口。

## 3. Evidence and verification

直接读交付 TeX；精确代数反例与既有脚本/稿件对照一致。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-KSUM-main-b5fea9c2.jsonl.readable.md](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md) — inherited_sanitized_source
- [M01-KSUM-main-b5fea9c2.jsonl.visible.json](original/M01-KSUM-main-b5fea9c2.jsonl.visible.json) — inherited_sanitized_source
- [M02-DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md) — inherited_sanitized_source
- [R01-ksum_small_alphabet.tex.context.md](reconciliation_sources/R01-ksum_small_alphabet.tex.context.md) — reconciliation_source_window
- [R02-historical_provenance_report.md.context.md](reconciliation_sources/R02-historical_provenance_report.md.context.md) — reconciliation_source_window
- [A01-ksum_small_alphabet.tex](reconciliation_sources/A01-ksum_small_alphabet.tex) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
