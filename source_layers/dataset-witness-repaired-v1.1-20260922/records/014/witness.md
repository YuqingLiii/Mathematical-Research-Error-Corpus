# Record 014 — Channel additivity violations

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census gives
> 
> $$
> \boxed{
> \Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
> }
> $$
> 
> [...]
> 
> $$
> \Delta_{\rm ray}
> +\Delta_{\rm flat}
> +\Delta_{\rm Young}
> +\Delta_{\rm group}<HE.
> \tag{1.3}
> $$
> 
> Then, individually,
> 
> $$
> \Delta_{\rm ray}<HE,\qquad
> \Delta_{\rm flat}<HE.
> \tag{1.4}
> $$

Context: The proof introduces four nonnegative slacks: ray, flat, Young, and group. Its detailed argument assumes their total is less than H E as a contradiction hypothesis, with H=3318 in this case.

Locator: round-59-response.md, lines 14–20, 118–132

## 2. Witness / adjudication

A consequence derived only inside a contradiction branch was stated as an unconditional strict bound on a subset of the slacks.

Let T=Delta_ray+Delta_flat+Delta_Young+Delta_group. The argument derives (T<HE) => (Delta_ray+Delta_flat>HE), contradicting T<HE because all slacks are nonnegative. The valid unconditional conclusion is T>=HE, not Delta_ray+Delta_flat>HE. For a logical counterassignment, E=H=1, Delta_ray=Delta_flat=0, Delta_Young=1, Delta_group=0 makes T>=HE true and the claimed subsidiary bound false, while the contradiction implication holds vacuously.

Scope: argument_invalid

分支内推出的条件性结论被改成无条件的子集严格界。逻辑赋值已表明该蕴含不成立；不声称该赋值是原物理模型的一个实现，也不宣称目标定理为假。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-59-response.md](original/M01-round-59-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_4_rounds_59_81.md](original/M02-concentrated_audit_4_rounds_59_81.md) — inherited_sanitized_source
- [M03-round58_response.md](original/M03-round58_response.md) — inherited_sanitized_source
- [M04-round59_size3_reproducer.cpp](original/M04-round59_size3_reproducer.cpp) — inherited_sanitized_source
- [M05-round59_size2_keycounts.cpp](original/M05-round59_size2_keycounts.cpp) — inherited_sanitized_source
- [M06-round59_size2_merge_audit.cpp](original/M06-round59_size2_merge_audit.cpp) — inherited_sanitized_source
- [M07-round59_verify_global.py](original/M07-round59_verify_global.py) — inherited_sanitized_source
- [M08-round59_lowfiber_summary.csv](original/M08-round59_lowfiber_summary.csv) — inherited_sanitized_source
- [M09-round59_size3_summary.csv](original/M09-round59_size3_summary.csv) — inherited_sanitized_source
- [M10-round59_global_size2_summary.csv](original/M10-round59_global_size2_summary.csv) — inherited_sanitized_source
- [M11-round59_global_size2_detail.txt](original/M11-round59_global_size2_detail.txt) — inherited_sanitized_source
- [M12-round59_size2_checks.txt](original/M12-round59_size2_checks.txt) — inherited_sanitized_source
- [M13-round59_stream_sha256.txt](original/M13-round59_stream_sha256.txt) — inherited_sanitized_source
- [M14-round59_exact_inequality_checks.txt](original/M14-round59_exact_inequality_checks.txt) — inherited_sanitized_source
- [M15-round59_digest.txt](original/M15-round59_digest.txt) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
