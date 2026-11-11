# Record 043 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> The bad
> event $\dist_q(T_\mu,t)\le P$ constrains the nonzero linear form $\nu\cdot w'$ to a set of at most
> $2P+1$ residues, so it forbids at most $(2P+1)q^{k-2}$ of the $q^{k-1}$ vectors $w'$.

Context: The appendix uses a fiber count for a nonzero linear form over Z_q without assuming its coefficients generate the whole ring modulo q.

Locator: Appendix all-targets lemma Edit event, 2026-07-18T02:44:18.919Z.

## 2. Witness / adjudication

A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

For k=3, choose wrong block multiplicities mu=(3,0,0), so nu=(3,0), and choose t=0, q=228, P=12. There are9 multiples of3 in the circular interval[-12,12]. Each equation3w1=r mod228 for such a residue has3 solutions, and w2 is arbitrary. Thus the bad set has9*3*228=6156 pairs, exceeding (2P+1)q=25*228=5700. Here q>9(2P+1)=225, so even the displayed counting threshold does not validate the faulty per-pattern estimate. A gcd factor or an invertibility hypothesis is needed.

Scope: computation_false

保留合数模上非零线性形式纤维计数错误。不能仅因它出现在全称引理里便自动标 overclaim；直接缺陷是把 nonzero 当作满射从而漏 gcd 倍数。

KSUM-006 的原追加附录 Edit 已恢复。此前反复找机器解决的是版本绑定，本轮无需再降级。

## 3. Evidence and verification

本轮重新枚举228^2个(w1,w2)得到6156，既有 witness 的适用阈值同时检查通过。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md](original/M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md) — inherited_sanitized_source
- [M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.visible.json](original/M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.visible.json) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.readable.md](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.visible.json](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json) — inherited_sanitized_source
- [M03-DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md) — inherited_sanitized_source
- [R01-M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md.context.md](reconciliation_sources/R01-M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
