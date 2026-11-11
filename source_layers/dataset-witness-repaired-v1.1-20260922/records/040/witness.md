# Record 040 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> the relabeling is an input-independent unitary on the value register applied around each query, so one query to either oracle simulates one query to the other.

Context: The manuscript asserted exact one-query equivalence for arbitrary per-symbol bijections in the XOR oracle O_x|i,b>=|i,b XOR x_i>.

Locator: Manuscript Edit event, 2026-07-17T21:36:50.131Z, query-model paragraph.

## 2. Witness / adjudication

Arbitrary bijections of symbol labels need not respect XOR translations, so they cannot generally be implemented by the asserted fixed conjugation around a single oracle call.

Take three-bit symbols and a bijection phi that swaps 1 and 2 and fixes 0,3,4,5,6,7. Fixed before/after value-register unitaries implementing every relabeled oracle, with phi(0)=0, would conjugate X_a to X_phi(a), where X_a|b>=|b XOR a>. Since X_a X_b=X_(a XOR b), this requires phi(a XOR b)=phi(a) XOR phi(b). But phi(1 XOR 4)=phi(5)=5, whereas phi(1) XOR phi(4)=2 XOR 4=6. Querying into an ancilla, applying phi, updating the response, and uncomputing uses two oracle calls; constant-factor asymptotic transfers may survive.

Scope: argument_invalid

保留任意逐坐标字母双射被升级为 XOR oracle 精确一查询等价这一局部错误。原思考已写出 compute-copy-uncompute 的两查询方案，却在正文保留一查询和 Q(g)=Q(f)。错误不是经典谓词编码，也不是否定常数开销的渐近转移。

KSUM-001 的旧审计指向同一 query-model 段；恢复库已绑定具体 Edit，不能因本轮未重做 oracle 实验而降级。分类为 overclaim 的依据是两查询／特殊相容置换可用的证据被扩成任意置换的一查询精确等价，而不是仅因出现模型混淆。

## 3. Evidence and verification

原始思考与 Edit 已读；群同态障碍可逐项精确核验；本轮沿用已恢复原事件，不重新要求机器来源。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md](original/M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md) — inherited_sanitized_source
- [M01-KSUM-agent-a9938705d211bef32.jsonl.visible.json](original/M01-KSUM-agent-a9938705d211bef32.jsonl.visible.json) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.readable.md](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md) — inherited_sanitized_source
- [M02-KSUM-main-b5fea9c2.jsonl.visible.json](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json) — inherited_sanitized_source
- [M03-DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md) — inherited_sanitized_source
- [R01-M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md.context.md](reconciliation_sources/R01-M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md.context.md) — reconciliation_source_window
- [R02-M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md.context.md](reconciliation_sources/R02-M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
