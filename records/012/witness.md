# 012 — The printed checksum differs from exact summation of the archived scan.

**Research problem:** P01 — Channel additivity violations

## Original statement

> $$
> \boxed{
> \sum \theta^2K^{(4)}_\theta
> =
> 7149371020340881916998112.
> }
> \tag{32}

**Context:** K_theta^(4) is the exact support count in a saved critical scan with 150150 distinct theta values. The excerpt reports its second-moment checksum.

**Original locator:** round-51-response.md, lines 681–687

## Why it is an error

The printed checksum differs from exact summation of the archived scan.

## Witness / evidence

Parsing the archived rows as (theta,K_theta) and evaluating sum(theta*theta*K_theta) using integers gives 7149371020340889916998112. The printed integer is 7149371020340881916998112, smaller by 8000000000. A reproducible check is: rows={int(t):int(k) for t,k in re.findall(r"^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$",scan,re.M)}; assert len(rows)==150150; sum(t*t*k for t,k in rows.items()). The scan must accompany this record as a verification fixture.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 归档扫描行的精确二阶矩和比打印整数大 8000000000，故该数值汇总错误；仅有事后重算不能证明原生成时先算对后抄错。

## Adjudication notes

The printed checksum differs from exact summation of the archived scan.

Parsing the archived rows as (theta,K_theta) and evaluating sum(theta*theta*K_theta) using integers gives 7149371020340889916998112. The printed integer is 7149371020340881916998112, smaller by 8000000000. A reproducible check is: rows={int(t):int(k) for t,k in re.findall(r"^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$",scan,re.M)}; assert len(rows)==150150; sum(t*t*k for t,k in rows.items()). The scan must accompany this record as a verification fixture.

Scope: computation_false

重新读取 150150 条扫描数据，精确二阶矩为 7149371020340889916998112，比打印值大 8000000000；无需假定新扫描结果。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-51-response.md](original/M01-round-51-response.md)
- [original/M03-concentrated_audit_3_rounds_43_58.md](original/M03-concentrated_audit_3_rounds_43_58.md)
- [original/M04-03_r043_r058_finite_slope_foundation_CORE.md](original/M04-03_r043_r058_finite_slope_foundation_CORE.md)
- [original/M05-MASTER_AUDIT_PROTOCOL.md](original/M05-MASTER_AUDIT_PROTOCOL.md)
- [original/M06-BASELINE.md](original/M06-BASELINE.md)
- [original/M07-verify_round43_translation.py](original/M07-verify_round43_translation.py)
- [original/M08-verify_round43_web_response.py](original/M08-verify_round43_web_response.py)
- [original/M09-verify_round44_candidate.py](original/M09-verify_round44_candidate.py)
- [original/M10-verify_round44_web_response.py](original/M10-verify_round44_web_response.py)
- [original/M11-enumerate_round45_matchings.py](original/M11-enumerate_round45_matchings.py)
- [original/M12-verify_round45_web_response.py](original/M12-verify_round45_web_response.py)
- [original/M13-enumerate_round46_one_defect.py](original/M13-enumerate_round46_one_defect.py)
- [original/M14-verify_round46_web_response.py](original/M14-verify_round46_web_response.py)
- [original/M15-enumerate_round47_ratio_two.py](original/M15-enumerate_round47_ratio_two.py)
- [original/M16-verify_round47_web_response.py](original/M16-verify_round47_web_response.py)
- [original/M17-enumerate_round48_kappa_frontier.py](original/M17-enumerate_round48_kappa_frontier.py)
- [original/M18-verify_round48_web_response.py](original/M18-verify_round48_web_response.py)
- [original/M19-verify_round49_frontier.cpp](original/M19-verify_round49_frontier.cpp)
- [original/M20-verify_round49_web_response.py](original/M20-verify_round49_web_response.py)
- [original/M21-enumerate_round50_three_ratio.cpp](original/M21-enumerate_round50_three_ratio.cpp)
- [original/M22-verify_round50_pre_send.py](original/M22-verify_round50_pre_send.py)
- [original/M23-enumerate_round51_four_ratio.cpp](original/M23-enumerate_round51_four_ratio.cpp)
- [original/M24-verify_round51_low_collision.cpp](original/M24-verify_round51_low_collision.cpp)
- [original/M25-verify_round51_web_response.py](original/M25-verify_round51_web_response.py)
- [original/M26-verify_round52_laurent.cpp](original/M26-verify_round52_laurent.cpp)
- [original/M27-verify_round52_web_response.py](original/M27-verify_round52_web_response.py)
- [original/M28-verify_round53_web_response.py](original/M28-verify_round53_web_response.py)
- [original/M29-verify_round54_lowfiber.cpp](original/M29-verify_round54_lowfiber.cpp)
- [original/M30-verify_round55_lowfiber.cpp](original/M30-verify_round55_lowfiber.cpp)
- [original/M31-verify_round56_lowfiber.cpp](original/M31-verify_round56_lowfiber.cpp)
- [original/M32-verify_round57_lowfiber.cpp](original/M32-verify_round57_lowfiber.cpp)
- [original/M33-verify_round58_lowfiber.cpp](original/M33-verify_round58_lowfiber.cpp)
- [original/M34-round58_size2_merge.cpp](original/M34-round58_size2_merge.cpp)
- [original/M35-round58_size2_merge_detail.cpp](original/M35-round58_size2_merge_detail.cpp)
- [original/M36-round58_response.md](original/M36-round58_response.md)

[Back to all 65 errors](../../README.md)
