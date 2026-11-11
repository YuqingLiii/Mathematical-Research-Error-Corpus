# 043 — A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> The bad
> event $\dist_q(T_\mu,t)\le P$ constrains the nonzero linear form $\nu\cdot w'$ to a set of at most
> $2P+1$ residues, so it forbids at most $(2P+1)q^{k-2}$ of the $q^{k-1}$ vectors $w'$.

**Context:** The appendix uses a fiber count for a nonzero linear form over Z_q without assuming its coefficients generate the whole ring modulo q.

**Original locator:** Appendix all-targets lemma Edit event, 2026-07-18T02:44:18.919Z.

## Why it is an error

A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

## Witness / evidence

For k=3, choose wrong block multiplicities mu=(3,0,0), so nu=(3,0), and choose t=0, q=228, P=12. There are9 multiples of3 in the circular interval[-12,12]. Each equation3w1=r mod228 for such a residue has3 solutions, and w2 is arbitrary. Thus the bad set has9*3*228=6156 pairs, exceeding (2P+1)q=25*228=5700. Here q>9(2P+1)=225, so even the displayed counting threshold does not validate the faulty per-pattern estimate. A gcd factor or an invertibility hypothesis is needed.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 模合数上线性形式的纤维数估计错误；反例中坏向量数为 6156，而所报上界只有 5700，缺少 gcd 因子。

III/IV 边界：具体落点是有限集合纤维计数不正确，归 III；同一计数缺失的可逆性条件留在解释中。

## Adjudication notes

A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

For k=3, choose wrong block multiplicities mu=(3,0,0), so nu=(3,0), and choose t=0, q=228, P=12. There are9 multiples of3 in the circular interval[-12,12]. Each equation3w1=r mod228 for such a residue has3 solutions, and w2 is arbitrary. Thus the bad set has9*3*228=6156 pairs, exceeding (2P+1)q=25*228=5700. Here q>9(2P+1)=225, so even the displayed counting threshold does not validate the faulty per-pattern estimate. A gcd factor or an invertibility hypothesis is needed.

Scope: computation_false

保留合数模上非零线性形式纤维计数错误。不能仅因它出现在全称引理里便自动标 overclaim；直接缺陷是把 nonzero 当作满射从而漏 gcd 倍数。

KSUM-006 的原追加附录 Edit 已恢复。此前反复找机器解决的是版本绑定，本轮无需再降级。

## Original materials

- [original/M03-DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md)

[Back to all 65 errors](../../README.md)
