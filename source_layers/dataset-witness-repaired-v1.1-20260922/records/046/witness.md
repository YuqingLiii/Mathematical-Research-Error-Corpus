# Record 046 — Set equality and collision

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> 证明完成了。核心比预想的简单：**SE 是 Collision 的一个固定承诺子问题**，所以 SE 的显式矩阵可以原封不动嵌入 Collision。

Context: The proposed explicit collision lower bound imported a set-equality adversary matrix. The completion statement was made before the formal upstream withdrawal; the zero-padding embedding itself was correct.

Locator: Assistant message, 2026-07-16T10:55:28.849Z; mathematical follow-up, 13:49:09.641Z.

## 2. Witness / adjudication

Preserving the numerator and masked matrix norms transfers only the bound already established for the source matrix; it cannot establish an unproved source norm bound.

For the coordinate isometry J, Gamma_Col=J Gamma_SE gives ||Gamma_Col||=||Gamma_SE|| and ||Gamma_Col o Delta_i||=||Gamma_SE o Delta_i||. The inherited denominator still needs ||K_N* G K_N|| <= C^2/j. Its proposed derivation lacked the identity j U(K_N* G K_N)U*=M/[B_theta(q)^2 omega] in a common normalization. Thus the displayed Omega(N^(1/3)) certificate remains conditional on that identity. Finite checks at N=2,4,6 establish the embedding, not the uniform bound.

Scope: argument_invalid

保留正确的 SE→Collision 零填充嵌入被当作完整显式下界证书这一缺口。必须撤掉旧金库标题的‘已经撤回后再次继承’时间叙事：正文完成声明在正式上游撤回前；错误仍是上游未证范数桥被当作闭合。

旧 GOLD3 审计有时间先后与措辞夸张，不能原样继承；但原会话明确承认同一 operator bridge 未证，足以保留数学缺口，不需再找设备。

## 3. Evidence and verification

原始完成声明、同轨后续逐项审查和明确缺失恒等式已对应；保留已有 source-bound 数学审查，不声称重新实现所有上游 Fourier/CG 计算。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md](original/M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.visible.json](original/M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M02-GOLD3_collision_reclaim.md](original/M02-GOLD3_collision_reclaim.md) — inherited_sanitized_source
- [R01-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md](reconciliation_sources/R01-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md) — reconciliation_source_window
- [R02-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md](reconciliation_sources/R02-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md) — reconciliation_source_window
- [R03-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md](reconciliation_sources/R03-M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
