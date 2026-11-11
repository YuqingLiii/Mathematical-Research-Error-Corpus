# Record 059 — Channel additivity violations

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> The same statement holds for a non-self-adjoint polynomial after its
> standard \(2\)-by-\(2\) self-adjoint dilation.
> 
> **Proof.**  In the proof of Theorem 1.5 in the cited source, denote
> \(\widetilde q_0=q_0(1+\log q_0)\).  Immediately before the final choice
> of the tail constant, their displayed estimate has the two controlling
> terms
> 
> \[
>  \left({R(P)^3\widetilde q_0\,m^{1+2u}
>        \over\varepsilon^{1+2u}u n}\right)^m,
>  \qquad
>  \left({R(P)^6\widetilde q_0^2\,m^{1+4u}
>        \over\varepsilon^{2(1+2u)}u^2 n}\right)^m.             \tag{210}
> \]
> 
> In the published display, \(R(P)\) has already been replaced by the
> generic estimate \((Cr)^{q_0}\), proved there by counting every reduced
> word of length at most \(q_0\).  Retaining \(K_{\rm full}/\|X_{\rm F}\|\)
> instead gives (210), because the preceding test-function argument uses the
> full norm only as the radius of the interval containing every finite
> evaluation.  Their choices

Context: The local lemma claims a coefficient-sensitive tensor-Haar tail bound with inverse tail constant bounded by C R(P)^6 [q0(1+log q0)]^2, where R is the full-to-limit norm ratio. The paragraph attributes the required terms to an imported proof.

Locator: Proof-development artifact, Lemma 44, lines 3860–3883; original write 2026-08-21T16:10:22.317Z

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

初始补丁已经说明文献显示的是通用半径，并明确提出 retaining R 的推导；原参考文献也确实在9.7证明后说明Haar扩展。现 witness 不能仅由这两点建立误引或缺口。

旧恢复成功找到了写入，但旧摘要对写入内容的概括不准确。此次核对初始patch和一次文献，不把后来自我纠正当作独立数学反证。003另有精确估计错误，仍保留。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-PROOF.md](original/M01-PROOF.md) — inherited_sanitized_source
- [M02-GAP-007-source-attribution.jsonl.readable.md](original/M02-GAP-007-source-attribution.jsonl.readable.md) — inherited_sanitized_source
- [M02-GAP-007-source-attribution.jsonl.visible.json](original/M02-GAP-007-source-attribution.jsonl.visible.json) — inherited_sanitized_source
- [M03-GAP-008-uniformity.jsonl.readable.md](original/M03-GAP-008-uniformity.jsonl.readable.md) — inherited_sanitized_source
- [M03-GAP-008-uniformity.jsonl.visible.json](original/M03-GAP-008-uniformity.jsonl.visible.json) — inherited_sanitized_source
- [M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.readable.md](original/M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.visible.json](original/M04-rollout-2026-08-21T12-05-17-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [R01-M02-GAP-007-source-attribution.jsonl.readable.md.context.md](reconciliation_sources/R01-M02-GAP-007-source-attribution.jsonl.readable.md.context.md) — reconciliation_source_window
- [R02-PROOF.md.context.md](reconciliation_sources/R02-PROOF.md.context.md) — reconciliation_source_window
- [A01-reconciliation_059_reference.md](reconciliation_sources/A01-reconciliation_059_reference.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

后来的自我纠正没有准确概括最初补丁。

最初补丁已经区分文献的通用半径与 retaining-R 推导；文献也写了 Haar 扩展。另一个确切估计错误已在 003，不能重复挪到本条。

该导入步骤的旧 witness 不成立；本轮未建立另一个独立数学错误。
