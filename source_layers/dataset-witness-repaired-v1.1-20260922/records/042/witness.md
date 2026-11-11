# Record 042 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> \Q\bigl(\kSum_{\Zq,t,N}\bigr)\;=\;\Omega_k\!\left(\sqrt N\, q^{1/6}\right)
> \qquad\text{for all } q\ \text{up to}\ \Theta_k(N).

Context: The displayed 'in particular' conclusion ranges over all small q, although the preceding construction has a sufficiently-large-alphabet condition.

Locator: Full-manuscript Write event, 2026-07-17T20:31:31.554Z; inherited-floor theorem.

## 2. Witness / adjudication

Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

Set k=3, q=3, t=0, N>=7. Among N residues in Z3, some residue a occurs at least three times. Their sum is3a=0 mod3, so every input is a YES instance and Q=0. This contradicts a positive Omega(sqrt(N)*3^(1/6)) lower bound stated for all q up to a linear ceiling. The counterexample does not refute the preceding theorem restricted by q>=(k-1)(kK+k+2).

Scope: statement_false

保留从有 alphabet 下限的构造扩展成 all q up to Theta_k(N) 的书面范围错误；不能将其反例描述为同时推翻前面有 q 下限的定理。

KSUM-005 的鸽笼 witness 与交付稿原句直接匹配，旧恢复结论不变。

## 3. Evidence and verification

原文上下限对读；鸽笼论证是独立精确 witness，无需重跑模型。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-KSUM-main-b5fea9c2.jsonl.readable.md](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md) — inherited_sanitized_source
- [M01-KSUM-main-b5fea9c2.jsonl.visible.json](original/M01-KSUM-main-b5fea9c2.jsonl.visible.json) — inherited_sanitized_source
- [M02-DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md) — inherited_sanitized_source
- [R01-ksum_small_alphabet.tex.context.md](reconciliation_sources/R01-ksum_small_alphabet.tex.context.md) — reconciliation_source_window
- [A01-ksum_small_alphabet.tex](reconciliation_sources/A01-ksum_small_alphabet.tex) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
