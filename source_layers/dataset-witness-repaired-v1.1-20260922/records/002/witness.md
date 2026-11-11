# Record 002 — Channel additivity violations

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> This explains why simply tensoring a single Hastings counterexample with
> itself cannot settle the extensive question.

Context: Lemma 4 proves a zero normalized tensor-power gap for a literal self-pair (Phi,Phi). The following explanatory sentence extends its interpretation to a Hastings counterexample, which generally uses the distinct conjugate pair (Phi,conjugate(Phi)).

Locator: Proof-development artifact, section 2, lines 150–151; original write 2026-08-20T23:41:57.547Z

## 2. Witness / adjudication

The self-pair tensor identity does not apply to a conjugate pair.

For a_m=S_min(Phi^tensor m), the self-pair gap is 2a_m-a_2m and its ratio to m tends to zero. For a conjugate pair the joint term is S_min((Phi tensor conjugate(Phi))^tensor m), not a_2m. Its normalized limit is a different regularized entropy and the cancellation used in Lemma 4 is unavailable.

Scope: argument_invalid

恢复旧确认：自配对恒等式不能覆盖共轭信道对。原文纠正明确指向原 self-tensor 排除句，并给出共轭情形仍未排除的正则化差。

原始写入与定向纠正均已恢复；不再用本轮对单句的歧义取代完整时间链。与001同一事件相关但错误推断不同，不算独立运行。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-PROOF.md](original/M01-PROOF.md) — inherited_sanitized_source
- [M02-GAP-003-005-create-proof.jsonl.readable.md](original/M02-GAP-003-005-create-proof.jsonl.readable.md) — inherited_sanitized_source
- [M02-GAP-003-005-create-proof.jsonl.visible.json](original/M02-GAP-003-005-create-proof.jsonl.visible.json) — inherited_sanitized_source
- [M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.visible.json](original/M03-additivity-gap__rollout-2026-08-20T19-28-32-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [R01-PROOF.md.context.md](reconciliation_sources/R01-PROOF.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
