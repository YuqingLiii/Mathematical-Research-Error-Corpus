# Record 012 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> $$
> \boxed{
> \sum \theta^2K^{(4)}_\theta
> =
> 7149371020340881916998112.
> }
> \tag{32}

Context: K_theta^(4) is the exact support count in a saved critical scan with 150150 distinct theta values. The excerpt reports its second-moment checksum.

Locator: round-51-response.md, lines 681–687

## 2. Witness / adjudication

The printed checksum differs from exact summation of the archived scan.

Parsing the archived rows as (theta,K_theta) and evaluating sum(theta*theta*K_theta) using integers gives 7149371020340889916998112. The printed integer is 7149371020340881916998112, smaller by 8000000000. A reproducible check is: rows={int(t):int(k) for t,k in re.findall(r"^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$",scan,re.M)}; assert len(rows)==150150; sum(t*t*k for t,k in rows.items()). The scan must accompany this record as a verification fixture.

Scope: computation_false

重新读取 150150 条扫描数据，精确二阶矩为 7149371020340889916998112，比打印值大 8000000000；无需假定新扫描结果。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-51-response.md](original/M01-round-51-response.md) — inherited_sanitized_source
- [M02-round51-critical-full-scan.txt](original/M02-round51-critical-full-scan.txt) — inherited_sanitized_source
- [M03-concentrated_audit_3_rounds_43_58.md](original/M03-concentrated_audit_3_rounds_43_58.md) — inherited_sanitized_source
- [M04-03_r043_r058_finite_slope_foundation_CORE.md](original/M04-03_r043_r058_finite_slope_foundation_CORE.md) — inherited_sanitized_source
- [M05-MASTER_AUDIT_PROTOCOL.md](original/M05-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M06-BASELINE.md](original/M06-BASELINE.md) — inherited_sanitized_source
- [M07-verify_round43_translation.py](original/M07-verify_round43_translation.py) — inherited_sanitized_source
- [M08-verify_round43_web_response.py](original/M08-verify_round43_web_response.py) — inherited_sanitized_source
- [M09-verify_round44_candidate.py](original/M09-verify_round44_candidate.py) — inherited_sanitized_source
- [M10-verify_round44_web_response.py](original/M10-verify_round44_web_response.py) — inherited_sanitized_source
- [M11-enumerate_round45_matchings.py](original/M11-enumerate_round45_matchings.py) — inherited_sanitized_source
- [M12-verify_round45_web_response.py](original/M12-verify_round45_web_response.py) — inherited_sanitized_source
- [M13-enumerate_round46_one_defect.py](original/M13-enumerate_round46_one_defect.py) — inherited_sanitized_source
- [M14-verify_round46_web_response.py](original/M14-verify_round46_web_response.py) — inherited_sanitized_source
- [M15-enumerate_round47_ratio_two.py](original/M15-enumerate_round47_ratio_two.py) — inherited_sanitized_source
- [M16-verify_round47_web_response.py](original/M16-verify_round47_web_response.py) — inherited_sanitized_source
- [M17-enumerate_round48_kappa_frontier.py](original/M17-enumerate_round48_kappa_frontier.py) — inherited_sanitized_source
- [M18-verify_round48_web_response.py](original/M18-verify_round48_web_response.py) — inherited_sanitized_source
- [M19-verify_round49_frontier.cpp](original/M19-verify_round49_frontier.cpp) — inherited_sanitized_source
- [M20-verify_round49_web_response.py](original/M20-verify_round49_web_response.py) — inherited_sanitized_source
- [M21-enumerate_round50_three_ratio.cpp](original/M21-enumerate_round50_three_ratio.cpp) — inherited_sanitized_source
- [M22-verify_round50_pre_send.py](original/M22-verify_round50_pre_send.py) — inherited_sanitized_source
- [M23-enumerate_round51_four_ratio.cpp](original/M23-enumerate_round51_four_ratio.cpp) — inherited_sanitized_source
- [M24-verify_round51_low_collision.cpp](original/M24-verify_round51_low_collision.cpp) — inherited_sanitized_source
- [M25-verify_round51_web_response.py](original/M25-verify_round51_web_response.py) — inherited_sanitized_source
- [M26-verify_round52_laurent.cpp](original/M26-verify_round52_laurent.cpp) — inherited_sanitized_source
- [M27-verify_round52_web_response.py](original/M27-verify_round52_web_response.py) — inherited_sanitized_source
- [M28-verify_round53_web_response.py](original/M28-verify_round53_web_response.py) — inherited_sanitized_source
- [M29-verify_round54_lowfiber.cpp](original/M29-verify_round54_lowfiber.cpp) — inherited_sanitized_source
- [M30-verify_round55_lowfiber.cpp](original/M30-verify_round55_lowfiber.cpp) — inherited_sanitized_source
- [M31-verify_round56_lowfiber.cpp](original/M31-verify_round56_lowfiber.cpp) — inherited_sanitized_source
- [M32-verify_round57_lowfiber.cpp](original/M32-verify_round57_lowfiber.cpp) — inherited_sanitized_source
- [M33-verify_round58_lowfiber.cpp](original/M33-verify_round58_lowfiber.cpp) — inherited_sanitized_source
- [M34-round58_size2_merge.cpp](original/M34-round58_size2_merge.cpp) — inherited_sanitized_source
- [M35-round58_size2_merge_detail.cpp](original/M35-round58_size2_merge_detail.cpp) — inherited_sanitized_source
- [M36-round58_response.md](original/M36-round58_response.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
