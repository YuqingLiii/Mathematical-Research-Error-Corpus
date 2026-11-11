# Record 022 — Werner–Holevo zero-capacity boundary

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> [2/5, 1)**. Below the onset the same machinery is *strictly stronger than at n = 1* — at x = 7/20 an
> entangled 2-copy input gives the exact value **1102933/9570000 = 0.115249007…** versus
> d₁(7/20) = 13/132 = 0.098484848… (17 % larger, exact rationals) — so the n = 2 layer is genuinely
> more powerful, yet it dies at exactly the same threshold 2/5.

Context: The raw two-use first-order coherent-information coefficient is compared against a one-use coefficient at x=7/20. Capacity is normalized per channel use. The same sentence also asserts a common zero-crossing threshold.

Locator: Two-copy analysis artifact, 2026-07-30, lines 22–25

## 2. Witness / adjudication

The comparison omits division by two and the entangled-family threshold is not 2/5.

The comparable two-use coefficient is (1102933/9570000)/2=1102933/19140000, whereas the one-use coefficient is 13/132. Their exact ratio is 84841/145000, approximately 0.5851<1, so the two-use value is about 41.5% lower per use. The entangled family changes sign at the unique root in (0,1) of 19x^4-21x^3-14x^2+28x-8, approximately 0.3912977695<0.4; substitution x=2/5 gives 64/625>0, not a zero.

Scope: statement_false

两次使用的值须除以 2 才能比较；修正后比值 84841/145000<1，不能支持“更强”的结论。阈值 2/5 也不是给定多项式的零点；后者是同条记录中的额外计算错误。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-whgap_p13b_n2_layer_20260730.md](original/M01-whgap_p13b_n2_layer_20260730.md) — inherited_sanitized_source
- [M02-<session-id-redacted>.jsonl.readable.md](original/M02-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M02-<session-id-redacted>.jsonl.visible.json](original/M02-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M03-whgap_r7_review_20260730.md](original/M03-whgap_r7_review_20260730.md) — inherited_sanitized_source
- [M04-whgap_r7_threshold.py](original/M04-whgap_r7_threshold.py) — inherited_sanitized_source
- [M05-WHGAP-main-c5b96aec.jsonl.readable.md](original/M05-WHGAP-main-c5b96aec.jsonl.readable.md) — inherited_sanitized_source
- [M05-WHGAP-main-c5b96aec.jsonl.visible.json](original/M05-WHGAP-main-c5b96aec.jsonl.visible.json) — inherited_sanitized_source
- [M06-WHGAP_COMMISSION_P13B_20260730.md](original/M06-WHGAP_COMMISSION_P13B_20260730.md) — inherited_sanitized_source
- [M07-WHGAP_REVIEW_COMMISSION_R5_20260729.md](original/M07-WHGAP_REVIEW_COMMISSION_R5_20260729.md) — inherited_sanitized_source
- [M08-PRETASK_RELOAD_PROMPT.md](original/M08-PRETASK_RELOAD_PROMPT.md) — inherited_sanitized_source
- [M09-DAG_PROTOCOL.md](original/M09-DAG_PROTOCOL.md) — inherited_sanitized_source
- [M10-RESEARCH_STRUCTURE_PROTOCOL.md](original/M10-RESEARCH_STRUCTURE_PROTOCOL.md) — inherited_sanitized_source
- [M11-README.md](original/M11-README.md) — inherited_sanitized_source
- [M12-WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M12-WERNER-HOLEVO-GAP_PROOF_DAG.md) — inherited_sanitized_source
- [M13-NODE_INDEX.md](original/M13-NODE_INDEX.md) — inherited_sanitized_source
- [M14-whgap_p13a_sanity.py](original/M14-whgap_p13a_sanity.py) — inherited_sanitized_source
- [M15-exact_s1.json](original/M15-exact_s1.json) — inherited_sanitized_source
- [M16-SHA256SUMS_p13b.txt](original/M16-SHA256SUMS_p13b.txt) — inherited_sanitized_source
- [M17-whgap_p13b_core.py](original/M17-whgap_p13b_core.py) — inherited_sanitized_source
- [M18-whgap_p13b_exact.py](original/M18-whgap_p13b_exact.py) — inherited_sanitized_source
- [M19-exact_s1.log](original/M19-exact_s1.log) — inherited_sanitized_source
- [M20-whgap_p13b_interval.py](original/M20-whgap_p13b_interval.py) — inherited_sanitized_source
- [M21-whgap_p13b_sweep.py](original/M21-whgap_p13b_sweep.py) — inherited_sanitized_source
- [M22-sweep_all.json](original/M22-sweep_all.json) — inherited_sanitized_source
- [M23-sweep_all.log](original/M23-sweep_all.log) — inherited_sanitized_source
- [M24-whgap_p13b_validate.py](original/M24-whgap_p13b_validate.py) — inherited_sanitized_source
- [M25-validation.json](original/M25-validation.json) — inherited_sanitized_source
- [M26-whgap_p13b_gates.py](original/M26-whgap_p13b_gates.py) — inherited_sanitized_source
- [M27-gates.json](original/M27-gates.json) — inherited_sanitized_source
- [M28-whgap_p13b_variety.py](original/M28-whgap_p13b_variety.py) — inherited_sanitized_source
- [M29-whgap_p13b_s2.py](original/M29-whgap_p13b_s2.py) — inherited_sanitized_source
- [M30-interval_certificate.json](original/M30-interval_certificate.json) — inherited_sanitized_source
- [M31-s2_symbolic.json](original/M31-s2_symbolic.json) — inherited_sanitized_source
- [M32-sweep_F2.json](original/M32-sweep_F2.json) — inherited_sanitized_source
- [M33-variety.json](original/M33-variety.json) — inherited_sanitized_source
- [M34-f2_condfloor_1e-3.log](original/M34-f2_condfloor_1e-3.log) — inherited_sanitized_source
- [M35-s2_symbolic.log](original/M35-s2_symbolic.log) — inherited_sanitized_source
- [M36-sweep_F2_recheck.log](original/M36-sweep_F2_recheck.log) — inherited_sanitized_source
- [M37-whgap_p13b_artifact_diagnosis.py](original/M37-whgap_p13b_artifact_diagnosis.py) — inherited_sanitized_source
- [M38-whgap_p13b_condfloor_probe.py](original/M38-whgap_p13b_condfloor_probe.py) — inherited_sanitized_source
- [M39-WHGAP_REVIEW_COMMISSION_R7_20260730.md](original/M39-WHGAP_REVIEW_COMMISSION_R7_20260730.md) — inherited_sanitized_source
- [M40-whgap_r7_s2.py](original/M40-whgap_r7_s2.py) — inherited_sanitized_source
- [M41-whgap_r7_checks.py](original/M41-whgap_r7_checks.py) — inherited_sanitized_source
- [M42-whgap_r7_variety.py](original/M42-whgap_r7_variety.py) — inherited_sanitized_source
- [M43-whgap_r7_exact.py](original/M43-whgap_r7_exact.py) — inherited_sanitized_source
- [M44-whgap_r7_interval.py](original/M44-whgap_r7_interval.py) — inherited_sanitized_source
- [M45-SHA256SUMS_r7.txt](original/M45-SHA256SUMS_r7.txt) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
