# 042 — Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> \Q\bigl(\kSum_{\Zq,t,N}\bigr)\;=\;\Omega_k\!\left(\sqrt N\, q^{1/6}\right)
> \qquad\text{for all } q\ \text{up to}\ \Theta_k(N).

**Context:** The displayed 'in particular' conclusion ranges over all small q, although the preceding construction has a sufficiently-large-alphabet condition.

**Original locator:** Full-manuscript Write event, 2026-07-17T20:31:31.554Z; inherited-floor theorem.

## Why it is an error

Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

## Witness / evidence

Set k=3, q=3, t=0, N>=7. Among N residues in Z3, some residue a occurs at least three times. Their sum is3a=0 mod3, so every input is a YES instance and Q=0. This contradicts a positive Omega(sqrt(N)*3^(1/6)) lower bound stated for all q up to a linear ceiling. The counterexample does not refute the preceding theorem restricted by q>=(k-1)(kK+k+2).

## Scope

statement_false

## Classification

- IV: 逻辑推理错误. 从有字母表下限的构造推出所有小 q 的下界，丢掉定理应用前提。q=3、k=3、N>=7 时问题恒 YES，复杂度为零。

## Adjudication notes

Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

Set k=3, q=3, t=0, N>=7. Among N residues in Z3, some residue a occurs at least three times. Their sum is3a=0 mod3, so every input is a YES instance and Q=0. This contradicts a positive Omega(sqrt(N)*3^(1/6)) lower bound stated for all q up to a linear ceiling. The counterexample does not refute the preceding theorem restricted by q>=(k-1)(kK+k+2).

Scope: statement_false

保留从有 alphabet 下限的构造扩展成 all q up to Theta_k(N) 的书面范围错误；不能将其反例描述为同时推翻前面有 q 下限的定理。

KSUM-005 的鸽笼 witness 与交付稿原句直接匹配，旧恢复结论不变。

## Original materials

- [original/M02-DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md)

[Back to all 65 errors](../../README.md)
