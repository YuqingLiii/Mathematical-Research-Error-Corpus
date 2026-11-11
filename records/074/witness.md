# 074 — A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> A short shift of the frozen value (offset $\delta$ with $|\delta|\le C_0-kK-1$) then realizes every target $t$, at the slightly larger threshold $q\ge(k-1)(kK+k+2)$, with no parity condition.

**Context:** 交付TeX第234行的同一证明先把k−2个坐标冻结到共同值C0=floor(q/(k−1))、目标t0=(k−2)C0，然后声称对这个共同值作短位移覆盖所有目标。不是已修复稿中只移动某个坐标或逐坐标不同取值的构造。

**Original locator:** See reconciliation source window 1

## Why it is an error

A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold.

## Witness / evidence

Choose k=4, K=2, q=42. The stated condition q≥(k−1)(kK+k+2) holds with equality, and C0=floor(42/3)=14. The common frozen sum after shifting is 2(14+δ)=28+2δ mod42. Every reachable target is even. Under the stated restriction |δ|≤C0−kK−1=5, the image is {18,20,22,24,26,28,30,32,34,36,38}; it excludes t=1. Allowing an additional global translation of all k coordinates adds4a and still yields only even residues. Thus the written common-shift proof cannot establish every target with no parity condition. This does not refute a repaired construction using independently chosen frozen coordinates.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 共同位移只能改变目标 (k-2)delta，不能保证覆盖所有剩余类。k=4,q=42 的构造只能到偶数目标，故“任意目标”推断错误。

## Adjudication notes

A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold.

Choose k=4, K=2, q=42. The stated condition q≥(k−1)(kK+k+2) holds with equality, and C0=floor(42/3)=14. The common frozen sum after shifting is 2(14+δ)=28+2δ mod42. Every reachable target is even. Under the stated restriction |δ|≤C0−kK−1=5, the image is {18,20,22,24,26,28,30,32,34,36,38}; it excludes t=1. Allowing an additional global translation of all k coordinates adds4a and still yields only even residues. Thus the written common-shift proof cannot establish every target with no parity condition. This does not refute a repaired construction using independently chosen frozen coordinates.

Scope: argument_invalid

已将旧 KSUM-002 对回真正的交付论文版本：common frozen value 的短统一位移被说成覆盖 every target、no parity condition。压缩包先前仅选到已修复的单坐标位移稿，不能因此把历史错误降为缺源。

historical_provenance_report 的538–588行指向 publish 交付 TeX 第234行；该文件当前就在本地。新定位纠正的是版本选取，不是新增错误，也不是再次要求设备恢复。旧 q=6 示意反例未满足原 theorem 阈值，本轮改用满足阈值的 q=42。

替换的是错配的来源版本与不在原阈值内的q=6示意例；保留历史KSUM-002原本的统一位移错误单位。完整原稿已有本地文件，不是待找资料。

## Original materials

- [original/M03-DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md)

[Back to all 65 errors](../../README.md)
