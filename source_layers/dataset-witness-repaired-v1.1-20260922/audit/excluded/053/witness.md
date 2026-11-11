# Record 053 — Finite-dimensional Grothendieck bounds

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> "natural rank-4 Gram point is an extreme non-cut elliptope "
> "point and therefore does not itself extend to the degree-4 "
> "generalized elliptope"

Context: The exported block is named elliptope_lemma_external_input but labels the claim PROVED_BY_USER_EXACT_MINOR.

Locator: Original complete-isotypic export script, lines2617–2628.

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

原指控把导出脚本中未重印外部定理误当成证明缺桥。原始网页捕获明确引用 Bandeira–Kunisky（arXiv:1812.11583v2），陈述非 cut 的 extreme elliptope point 不能延拓为 degree-4 pseudomoment，并给出 rank(X odot X)=10 的使用条件。随后协调器提供精确 minor，脚本才将其标为 external input。原始引用并未缺失；该外部命题也与所引用论文 Theorem 2.17 相符。现有 witness 只证明 checker 本身不重证外部定理，不能证明这个数学推断有错。

旧 source_reviewed/承重桥梁遗漏裁定遗漏了原 rollout 中的网页正文与定理链接；上一轮 pending 发现的问题现已通过既有原始工具输出消除。排除本条指控，不声称整个 H4 项目已被重新认证。

## 3. Evidence and verification

Read original browser tool captures and external-input export. Independently checked primary paper https://arxiv.org/html/1812.11583v2, Theorem 2.17, equations (17)-(18) and its extreme-point consequence: an extreme rank-greater-than-one correlation matrix has no degree-4 extension. Did not rerun the full Gram reconstruction or certify other H4 claims.

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-h4_complete_K_isotypic.py](original/M01-h4_complete_K_isotypic.py) — inherited_sanitized_source
- [M02-h4_hadamard_square_rank.py](original/M02-h4_hadamard_square_rank.py) — inherited_sanitized_source
- [R01-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md](reconciliation_sources/R01-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md) — reconciliation_source_window
- [R02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md](reconciliation_sources/R02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md) — reconciliation_source_window
- [R03-h4_complete_K_isotypic.py.context.md](reconciliation_sources/R03-h4_complete_K_isotypic.py.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

把检验脚本未重证外部定理，当作原论证缺桥。

原网页实际引用了所需外部定理并给出应用条件，精确 minor 负责其中的秩条件。

当前缺桥指控不成立；不等于认证整个证明。
