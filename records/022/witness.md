# 022 — The comparison omits division by two and the entangled-family threshold is not 2/5.

**Research problem:** P02 — Werner–Holevo zero-capacity boundary

## Original statement

> [2/5, 1)**. Below the onset the same machinery is *strictly stronger than at n = 1* — at x = 7/20 an
> entangled 2-copy input gives the exact value **1102933/9570000 = 0.115249007…** versus
> d₁(7/20) = 13/132 = 0.098484848… (17 % larger, exact rationals) — so the n = 2 layer is genuinely
> more powerful, yet it dies at exactly the same threshold 2/5.

**Context:** The raw two-use first-order coherent-information coefficient is compared against a one-use coefficient at x=7/20. Capacity is normalized per channel use. The same sentence also asserts a common zero-crossing threshold.

**Original locator:** Two-copy analysis artifact, 2026-07-30, lines 22–25

## Why it is an error

The comparison omits division by two and the entangled-family threshold is not 2/5.

## Witness / evidence

The comparable two-use coefficient is (1102933/9570000)/2=1102933/19140000, whereas the one-use coefficient is 13/132. Their exact ratio is 84841/145000, approximately 0.5851<1, so the two-use value is about 41.5% lower per use. The entangled family changes sign at the unique root in (0,1) of 19x^4-21x^3-14x^2+28x-8, approximately 0.3912977695<0.4; substitution x=2/5 gives 64/625>0, not a zero.

## Scope

statement_false

## Classification

- IV: 逻辑推理错误. 两次使用的原始系数直接与单次使用系数比较，不能推出每次使用更强；正确除以二后比值约 0.5851。
- III: 计算与代数错误. 另有独立的零点数值判断错误：对应多项式在 2/5 的值为 64/625，不是零；实际零点约 0.3913。

两个标签有两个不同的 source/witness 子依据：每次使用比较的逻辑失配，以及多项式零点计算错误。

## Adjudication notes

The comparison omits division by two and the entangled-family threshold is not 2/5.

The comparable two-use coefficient is (1102933/9570000)/2=1102933/19140000, whereas the one-use coefficient is 13/132. Their exact ratio is 84841/145000, approximately 0.5851<1, so the two-use value is about 41.5% lower per use. The entangled family changes sign at the unique root in (0,1) of 19x^4-21x^3-14x^2+28x-8, approximately 0.3912977695<0.4; substitution x=2/5 gives 64/625>0, not a zero.

Scope: statement_false

两次使用的值须除以 2 才能比较；修正后比值 84841/145000<1，不能支持“更强”的结论。阈值 2/5 也不是给定多项式的零点；后者是同条记录中的额外计算错误。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-whgap_p13b_n2_layer_20260730.md](original/M01-whgap_p13b_n2_layer_20260730.md)
- [original/M03-whgap_r7_review_20260730.md](original/M03-whgap_r7_review_20260730.md)
- [original/M04-whgap_r7_threshold.py](original/M04-whgap_r7_threshold.py)
- [original/M06-WHGAP_COMMISSION_P13B_20260730.md](original/M06-WHGAP_COMMISSION_P13B_20260730.md)
- [original/M07-WHGAP_REVIEW_COMMISSION_R5_20260729.md](original/M07-WHGAP_REVIEW_COMMISSION_R5_20260729.md)
- [original/M08-PRETASK_RELOAD_PROMPT.md](original/M08-PRETASK_RELOAD_PROMPT.md)
- [original/M09-DAG_PROTOCOL.md](original/M09-DAG_PROTOCOL.md)
- [original/M10-RESEARCH_STRUCTURE_PROTOCOL.md](original/M10-RESEARCH_STRUCTURE_PROTOCOL.md)
- [original/M11-README.md](original/M11-README.md)
- [original/M12-WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M12-WERNER-HOLEVO-GAP_PROOF_DAG.md)
- [original/M13-NODE_INDEX.md](original/M13-NODE_INDEX.md)
- [original/M14-whgap_p13a_sanity.py](original/M14-whgap_p13a_sanity.py)
- [original/M15-exact_s1.json](original/M15-exact_s1.json)
- [original/M16-SHA256SUMS_p13b.txt](original/M16-SHA256SUMS_p13b.txt)
- [original/M17-whgap_p13b_core.py](original/M17-whgap_p13b_core.py)
- [original/M18-whgap_p13b_exact.py](original/M18-whgap_p13b_exact.py)
- [original/M19-exact_s1.log](original/M19-exact_s1.log)
- [original/M20-whgap_p13b_interval.py](original/M20-whgap_p13b_interval.py)
- [original/M21-whgap_p13b_sweep.py](original/M21-whgap_p13b_sweep.py)
- [original/M22-sweep_all.json](original/M22-sweep_all.json)
- [original/M23-sweep_all.log](original/M23-sweep_all.log)
- [original/M24-whgap_p13b_validate.py](original/M24-whgap_p13b_validate.py)
- [original/M25-validation.json](original/M25-validation.json)
- [original/M26-whgap_p13b_gates.py](original/M26-whgap_p13b_gates.py)
- [original/M27-gates.json](original/M27-gates.json)
- [original/M28-whgap_p13b_variety.py](original/M28-whgap_p13b_variety.py)
- [original/M29-whgap_p13b_s2.py](original/M29-whgap_p13b_s2.py)
- [original/M30-interval_certificate.json](original/M30-interval_certificate.json)
- [original/M31-s2_symbolic.json](original/M31-s2_symbolic.json)
- [original/M32-sweep_F2.json](original/M32-sweep_F2.json)
- [original/M33-variety.json](original/M33-variety.json)
- [original/M34-f2_condfloor_1e-3.log](original/M34-f2_condfloor_1e-3.log)
- [original/M35-s2_symbolic.log](original/M35-s2_symbolic.log)
- [original/M36-sweep_F2_recheck.log](original/M36-sweep_F2_recheck.log)
- [original/M37-whgap_p13b_artifact_diagnosis.py](original/M37-whgap_p13b_artifact_diagnosis.py)
- [original/M38-whgap_p13b_condfloor_probe.py](original/M38-whgap_p13b_condfloor_probe.py)
- [original/M39-WHGAP_REVIEW_COMMISSION_R7_20260730.md](original/M39-WHGAP_REVIEW_COMMISSION_R7_20260730.md)
- [original/M40-whgap_r7_s2.py](original/M40-whgap_r7_s2.py)
- [original/M41-whgap_r7_checks.py](original/M41-whgap_r7_checks.py)
- [original/M42-whgap_r7_variety.py](original/M42-whgap_r7_variety.py)
- [original/M43-whgap_r7_exact.py](original/M43-whgap_r7_exact.py)
- [original/M44-whgap_r7_interval.py](original/M44-whgap_r7_interval.py)
- [original/M45-SHA256SUMS_r7.txt](original/M45-SHA256SUMS_r7.txt)

[Back to all 65 errors](../../README.md)
