# Record 013 — Channel additivity violations

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> For cofactor \(i\), pad the magnitude array with zeros to length \(S_i\), and let
> 
> $$
> \bar a_i=\frac{L_i}{S_i}.
> $$
> 
> Then
> 
> $$
> \frac{D_i}{S_i}
> =
> \sum_{\xi=1}^{S_i}
> \bigl(|A_i(\xi)|-\bar a_i\bigr)^2,
> \qquad
> D_i=S_ie_i^2-L_i^2.
> \tag{6.1}
> $$
> 
> Restrict this sum to:
> 
> * the \(G_i\) surviving unit anchors;
> * the \(N_i\) surviving complete opposite-sign pairs.
> 
> For arbitrary \(\mu\in\mathbb R\),
> 
> $$
> \frac{D_i}{S_i}
> \ge
> G_i(1-\mu)^2
> +
> \sum_{p=1}^{N_i}
> \left[
> (r_{p,+}-\mu)^2+(r_{p,-}-\mu)^2
> \right].
> \tag{6.2}
> $$

Context: D_i=S_i e_i^2-L_i^2 is S_i times the squared-deviation sum about the actual mean bar(a)_i=L_i/S_i. G_i counts retained unit anchors and N_i counts retained opposite-sign pairs with magnitudes r_(p,+),r_(p,-).

Locator: round-55-response.md, lines 577–612

## 2. Witness / adjudication

A variance about its minimizing mean cannot bound squared deviations about every arbitrary center.

For any nonempty selected coordinate set, the right side of (6.2) grows quadratically as |mu| tends to infinity, whereas D_i/S_i is fixed and finite. As a minimal exact example, one unit coordinate has S_i=L_i=e_i^2=G_i=1 and N_i=0, so D_i/S_i=0; choosing mu=0 makes the asserted right side 1. The valid route evaluates the selected deviations at the actual mean first, then lower-bounds them by their minimum over mu.

Scope: statement_false

关于均值的方差等式被用于任意 mu。单个非零坐标即使方差为零，偏离其他中心的平方仍为正；均值条件丢失是明确的适用范围扩张。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-55-response.md](original/M01-round-55-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_3_rounds_43_58.md](original/M02-concentrated_audit_3_rounds_43_58.md) — inherited_sanitized_source
- [M03-03_r043_r058_finite_slope_foundation_CORE.md](original/M03-03_r043_r058_finite_slope_foundation_CORE.md) — inherited_sanitized_source
- [M04-MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M05-BASELINE.md](original/M05-BASELINE.md) — inherited_sanitized_source
- [M06-verify_round43_translation.py](original/M06-verify_round43_translation.py) — inherited_sanitized_source
- [M07-verify_round43_web_response.py](original/M07-verify_round43_web_response.py) — inherited_sanitized_source
- [M08-verify_round44_candidate.py](original/M08-verify_round44_candidate.py) — inherited_sanitized_source
- [M09-verify_round44_web_response.py](original/M09-verify_round44_web_response.py) — inherited_sanitized_source
- [M10-enumerate_round45_matchings.py](original/M10-enumerate_round45_matchings.py) — inherited_sanitized_source
- [M11-verify_round45_web_response.py](original/M11-verify_round45_web_response.py) — inherited_sanitized_source
- [M12-enumerate_round46_one_defect.py](original/M12-enumerate_round46_one_defect.py) — inherited_sanitized_source
- [M13-verify_round46_web_response.py](original/M13-verify_round46_web_response.py) — inherited_sanitized_source
- [M14-enumerate_round47_ratio_two.py](original/M14-enumerate_round47_ratio_two.py) — inherited_sanitized_source
- [M15-verify_round47_web_response.py](original/M15-verify_round47_web_response.py) — inherited_sanitized_source
- [M16-enumerate_round48_kappa_frontier.py](original/M16-enumerate_round48_kappa_frontier.py) — inherited_sanitized_source
- [M17-verify_round48_web_response.py](original/M17-verify_round48_web_response.py) — inherited_sanitized_source
- [M18-verify_round49_frontier.cpp](original/M18-verify_round49_frontier.cpp) — inherited_sanitized_source
- [M19-verify_round49_web_response.py](original/M19-verify_round49_web_response.py) — inherited_sanitized_source
- [M20-enumerate_round50_three_ratio.cpp](original/M20-enumerate_round50_three_ratio.cpp) — inherited_sanitized_source
- [M21-verify_round50_pre_send.py](original/M21-verify_round50_pre_send.py) — inherited_sanitized_source
- [M22-enumerate_round51_four_ratio.cpp](original/M22-enumerate_round51_four_ratio.cpp) — inherited_sanitized_source
- [M23-verify_round51_low_collision.cpp](original/M23-verify_round51_low_collision.cpp) — inherited_sanitized_source
- [M24-verify_round51_web_response.py](original/M24-verify_round51_web_response.py) — inherited_sanitized_source
- [M25-verify_round52_laurent.cpp](original/M25-verify_round52_laurent.cpp) — inherited_sanitized_source
- [M26-verify_round52_web_response.py](original/M26-verify_round52_web_response.py) — inherited_sanitized_source
- [M27-verify_round53_web_response.py](original/M27-verify_round53_web_response.py) — inherited_sanitized_source
- [M28-verify_round54_lowfiber.cpp](original/M28-verify_round54_lowfiber.cpp) — inherited_sanitized_source
- [M29-verify_round55_lowfiber.cpp](original/M29-verify_round55_lowfiber.cpp) — inherited_sanitized_source
- [M30-verify_round56_lowfiber.cpp](original/M30-verify_round56_lowfiber.cpp) — inherited_sanitized_source
- [M31-verify_round57_lowfiber.cpp](original/M31-verify_round57_lowfiber.cpp) — inherited_sanitized_source
- [M32-verify_round58_lowfiber.cpp](original/M32-verify_round58_lowfiber.cpp) — inherited_sanitized_source
- [M33-round58_size2_merge.cpp](original/M33-round58_size2_merge.cpp) — inherited_sanitized_source
- [M34-round58_size2_merge_detail.cpp](original/M34-round58_size2_merge_detail.cpp) — inherited_sanitized_source
- [M35-round58_response.md](original/M35-round58_response.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
