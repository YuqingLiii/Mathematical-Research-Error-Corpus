# Record 003 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> m^{4u}\le e^4,qquad u^{-2}=(1+\log m)^2,qquad
>  \varepsilon^{-4u}\le C,                                    \tag{234}

Context: The auxiliary parameters are m=floor(gamma n epsilon^2/log^2(n epsilon^2)), u=1/(1+log m), with m>=2 and epsilon>=2/sqrt(n). The claimed C is independent of epsilon and n.

Locator: Proof-development artifact, equation (234), lines 4288–4295; original write 2026-08-21T16:15:33.756Z

## 2. Witness / adjudication

The asserted uniform bound on epsilon^(-4u) is false.

Fix X>4 and gamma>0 with m=floor(gamma X/log^2 X)>=2. Set epsilon=sqrt(X/n) and let n grow. Then n epsilon^2=X and epsilon>=2/sqrt(n); m and u>0 remain fixed. But epsilon^(-4u)=(n/X)^(2u) tends to infinity. For example X=10^6 and gamma=0.01 give m=52.

Scope: statement_false

固定 n·epsilon²=10^6 时 m=52，而 epsilon^(-4u) 随 n 无界；直接推翻统一常数 C。这里确认的是错误估计，不额外推定存在一项已成立的受限结果被升级。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-PROOF.md](original/M01-PROOF.md) — inherited_sanitized_source
- [M02-GAP-008-uniformity.jsonl.readable.md](original/M02-GAP-008-uniformity.jsonl.readable.md) — inherited_sanitized_source
- [M02-GAP-008-uniformity.jsonl.visible.json](original/M02-GAP-008-uniformity.jsonl.visible.json) — inherited_sanitized_source
- [M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.readable.md](original/M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.visible.json](original/M03-rollout-2026-08-21T12-11-11-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
