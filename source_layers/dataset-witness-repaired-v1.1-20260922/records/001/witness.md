# Record 001 — Channel additivity violations

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> The entire problem is therefore to choose *different* tuples \(U^{(r)}\) so
> that entangled inputs within \(\mathcal R^{[k]}\) do not appreciably lower its
> minimum output entropy.

Context: The argument uses different finite unitary tuples at different tensor positions to control minimum output entropy by iterated localization. The selected sentence presents this route choice as necessary for the entire extensive-gap problem.

Locator: Proof-development artifact, section 3, lines 211–213; original write 2026-08-20T23:41:57.547Z

## 2. Witness / adjudication

Necessity for the particular localization proof is not necessity for every construction.

For any fixed channel pair (Phi,Psi), the normalized tensor-power gap tends to Sbar_min(Phi)+Sbar_min(Psi)-Sbar_min(Phi tensor Psi). For Psi=conjugate(Phi), this is 2 Sbar_min(Phi)-Sbar_min(Phi tensor conjugate(Phi)), which the localization argument does not show to be zero. Thus the derivation leaves a fixed-pair alternative unexcluded. This diagnoses an unsupported necessity inference; it does not establish that a positive fixed-pair regularized gap exists.

Scope: argument_invalid

恢复旧确认：同一来源的 dated correction 明确限定不同 tuples 只对所给 iterated-localization 路线必要，并指名原“entire problem”过强；这不是假设全局替代路线已成功，而是该必要性推断没有成立。

上一轮把路线措辞当孤立歧义，遗漏原文对同一句的定向纠正以及固定共轭对的精确公式。恢复为论证范围错误，不称全局定理已被反例推翻。

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
