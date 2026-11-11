# 075 — The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> Fix any $(G,t)$ with $\sigma\ne\mathrm{id}$ (i.e.\ $\tau<q$), and let $D_0\subseteq G^n$ be the set of negative inputs. Then, already for $n=2$ and for every $n\ge2$:
> \begin{enumerate}
> \item $D_0$ is not a single $S_n\times C(\sigma)$-orbit; the number of orbits equals
> $\sum_{f} p_{\le m}(n-f)$, where $m=(q-\tau)/2$, $f$ ranges over the possible numbers of fixed-point values used, and $p_{\le m}(\cdot)$ counts partitions into at most $m$ parts; this is $\ge2$ and grows with $n$ for $m \ge 2$.

**Context:** 这是2026-07-17T20:31:31.554Z原始完整稿Write中同一Rosmanis barrier proposition的item1，尚未排除q=2。后来交付版加入q≥3并明确称q=2为single-orbit degeneracy。原包装选的item2 regularity-fails例句与其witness同方向，不应作为错误句。

**Original locator:** See reconciliation source window 2

## Why it is an error

The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two.

## Witness / evidence

Let G=Z2, t=1, and n=2. Then σ(x)=1−x swaps0 and1, so σ≠id, τ=0, and m=1, all within the quoted claim's domain. A negative input has no pair summing to1; hence D0={(0,0),(1,1)}. The alphabet swap belongs to C(σ) and sends(0,0) to(1,1). Therefore D0 is a single S2×C(σ) orbit. Equivalently, its displayed orbit-count formula specializes to p_{≤1}(2)=1, not≥2. This refutes the original universal item1. It neither refutes the later q≥3 version nor the valid q=3/q=4 examples of regularity failure.

## Scope

statement_false

## Classification

- III: 计算与代数错误. 原文自己的轨道数公式在允许的 Z2 情形给出 p_{<=1}(2)=1，而非至少二；精确轨道计数判断错误。

III/IV 边界：所给公式在合法参数处算出一轨道，原文却声称至少二；按直接计数/数量比较错误归 III。

## Adjudication notes

The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two.

Let G=Z2, t=1, and n=2. Then σ(x)=1−x swaps0 and1, so σ≠id, τ=0, and m=1, all within the quoted claim's domain. A negative input has no pair summing to1; hence D0={(0,0),(1,1)}. The alphabet swap belongs to C(σ) and sends(0,0) to(1,1). Therefore D0 is a single S2×C(σ) orbit. Equivalently, its displayed orbit-count formula specializes to p_{≤1}(2)=1, not≥2. This refutes the original universal item1. It neither refutes the later q≥3 version nor the valid q=3/q=4 examples of regularity failure.

Scope: statement_false

纠正原文与 witness 选取后保留历史 KSUM-004 的轨道分类范围错误。不能再引用 regularity-fails 的正确例句并以同方向例子反驳。历史错误单位原本是 barrier orbit classification is exhaustive；原始初稿在同一命题 item1 对任意sigma!=id声称D0不为单轨道，遗漏q=2退化情形。

这是显式修复同一 KSUM-004 审计记录的绑定与 witness，而非把与之无关的新错误填入075：corpus_50.jsonl第18行原单位就是轨道分类越界；原写入raw main:569保留缺q>=3的命题，交付TeX:276后来加了q>=3并注明q=2 single-orbit degeneracy。旧regularity例子仍可作上下文，但不得标为refutation。

明确校正历史KSUM-004（原始单位是轨道分类/范围越界）的原句与反证配对。不是声称旧regularity-fails句错误，不将该正确句及支持性例子偷偷改成反证，也不新增独立记录。

## Original materials

- [original/M02-DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md)
- [original/context/A02-ksum_stage3_module_anatomy.md](original/context/A02-ksum_stage3_module_anatomy.md)

[Back to all 65 errors](../../README.md)
