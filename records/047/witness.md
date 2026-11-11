# 047 — A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.

**Research problem:** P10 — Set equality and collision

## Original statement

> 有效秩证明严格成立，uniform physical \(T_b\) 对所有 admissible tame sector、所有正 LR 重数 \(c\) 全部关闭。

**Context:** The completion message applies a normalized effective-rank calculation to the unnormalized physical trace quantity T_b.

**Original locator:** Assistant message, 2026-07-22T13:19:00.659Z.

## Why it is an error

A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.

## Witness / evidence

The raw physical maps obey S_gamma S_gamma*=m K_gamma, so their nonzero A_gamma=S_gamma* S_gamma eigenvalues are m times the normalized k_gamma,mu. The common-line formulas are r_mu=||t_mu||^2/m and a_gamma,mu=m|d_gamma,mu|^2. Contracting |d|^2*r_mu instead of a_mass*r_mu computes the divided quantity T_b/m. A derived bound T_b/m<=B implies only T_b<=mB, not T_b<=B when m>1. This defeats the claimed uniform proof. The corrected finite T_b examples still pass; no physical T_b counterexample is claimed.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 已算的是 T_b/m，却将其界直接作为物理 T_b 的界；有效推论只有 T_b<=mB。现有有限修正例仍可通过，witness 否定的是这条证明桥梁。

III/IV 边界：归一化量本身可以计算正确；所定位错误是把它的证据用于另一物理量，故归 IV。

## Adjudication notes

A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.

The raw physical maps obey S_gamma S_gamma*=m K_gamma, so their nonzero A_gamma=S_gamma* S_gamma eigenvalues are m times the normalized k_gamma,mu. The common-line formulas are r_mu=||t_mu||^2/m and a_gamma,mu=m|d_gamma,mu|^2. Contracting |d|^2*r_mu instead of a_mass*r_mu computes the divided quantity T_b/m. A derived bound T_b/m<=B implies only T_b<=mB, not T_b<=B when m>1. This defeats the claimed uniform proof. The corrected finite T_b examples still pass; no physical T_b counterexample is claimed.

Scope: argument_invalid

保留关于 T_b/m 的有效秩界被用于关闭 physical T_b 的证据对象替换。分类 yes 的依据是从归一化量的有效证明跨到不同物理量且明确声称统一关闭，不是把所有漏因子都自动算 overclaim。

旧 witness 明确只否定 T_b 的现有证明，并未提供 T_b 反例；这个边界维持。原结论由 proposer/coordinator 写出，不能说是独立 reviewer 发明的错误。

## Original materials

- [original/M02-COMMANDS.txt](original/M02-COMMANDS.txt)
- [original/M03-REPORT.md](original/M03-REPORT.md)
- [original/M04-SHA256SUMS.txt](original/M04-SHA256SUMS.txt)
- [original/M05-independent_audit.json](original/M05-independent_audit.json)
- [original/M06-independent_audit.log](original/M06-independent_audit.log)
- [original/M07-independent_audit.py](original/M07-independent_audit.py)
- [original/M08-probe_rerun.log](original/M08-probe_rerun.log)
- [original/M09-rerun_common_line_exact.json](original/M09-rerun_common_line_exact.json)
- [original/M10-rerun_common_line_exact.log](original/M10-rerun_common_line_exact.log)
- [original/M11-source_sha_verification.log](original/M11-source_sha_verification.log)
- [original/M12-COMMANDS.txt](original/M12-COMMANDS.txt)
- [original/M13-REPORT.md](original/M13-REPORT.md)
- [original/M14-SHA256SUMS.txt](original/M14-SHA256SUMS.txt)
- [original/M15-carrier_dimension_review.json](original/M15-carrier_dimension_review.json)
- [original/M16-carrier_dimension_review.log](original/M16-carrier_dimension_review.log)
- [original/M17-review_carrier_dimension.py](original/M17-review_carrier_dimension.py)
- [original/M18-COMMANDS.txt](original/M18-COMMANDS.txt)
- [original/M19-REPORT.md](original/M19-REPORT.md)
- [original/M20-SHA256SUMS.txt](original/M20-SHA256SUMS.txt)
- [original/M21-effective_rank_review.json](original/M21-effective_rank_review.json)
- [original/M22-effective_rank_review.log](original/M22-effective_rank_review.log)
- [original/M23-review_effective_rank.py](original/M23-review_effective_rank.py)
- [original/M24-verify_artifact.py](original/M24-verify_artifact.py)
- [original/M25-COMMANDS.txt](original/M25-COMMANDS.txt)
- [original/M26-REPORT.md](original/M26-REPORT.md)
- [original/M27-SHA256SUMS.txt](original/M27-SHA256SUMS.txt)
- [original/M28-log.txt](original/M28-log.txt)
- [original/M29-se_trace_t5_long_cap.json](original/M29-se_trace_t5_long_cap.json)
- [original/M30-se_trace_t5_long_cap.py](original/M30-se_trace_t5_long_cap.py)
- [original/M31-COMMANDS.txt](original/M31-COMMANDS.txt)
- [original/M32-REPORT.md](original/M32-REPORT.md)
- [original/M33-SHA256SUMS.txt](original/M33-SHA256SUMS.txt)
- [original/M34-construct_rout.py](original/M34-construct_rout.py)
- [original/M35-tame_c2_rout.json](original/M35-tame_c2_rout.json)
- [original/M36-tame_c2_rout.log](original/M36-tame_c2_rout.log)
- [original/M37-tame_c2_rout.npz](original/M37-tame_c2_rout.npz)
- [original/M38-COMMANDS.txt](original/M38-COMMANDS.txt)
- [original/M39-REPORT.md](original/M39-REPORT.md)
- [original/M40-SHA256SUMS.txt](original/M40-SHA256SUMS.txt)
- [original/M41-construct_rcol.py](original/M41-construct_rcol.py)
- [original/M42-tame_c2_rcol.json](original/M42-tame_c2_rcol.json)
- [original/M43-tame_c2_rcol.log](original/M43-tame_c2_rcol.log)
- [original/M45-verify_rcol.log](original/M45-verify_rcol.log)
- [original/M46-verify_rcol.py](original/M46-verify_rcol.py)
- [original/M47-COMMANDS.txt](original/M47-COMMANDS.txt)
- [original/M48-REPORT.md](original/M48-REPORT.md)
- [original/M49-SHA256SUMS.txt](original/M49-SHA256SUMS.txt)
- [original/M50-rcol_review.json](original/M50-rcol_review.json)
- [original/M51-rcol_review.log](original/M51-rcol_review.log)
- [original/M52-review_rcol.py](original/M52-review_rcol.py)
- [original/M53-COMMANDS.txt](original/M53-COMMANDS.txt)
- [original/M54-REPORT.md](original/M54-REPORT.md)
- [original/M55-SHA256SUMS.txt](original/M55-SHA256SUMS.txt)
- [original/M56-second_gate.json](original/M56-second_gate.json)
- [original/M57-second_gate.log](original/M57-second_gate.log)
- [original/M58-second_gate_inventory.npz](original/M58-second_gate_inventory.npz)
- [original/M60-second_tame_c2_gate.py](original/M60-second_tame_c2_gate.py)
- [original/M61-verify_second_gate.py](original/M61-verify_second_gate.py)
- [original/M62-COMMANDS.txt](original/M62-COMMANDS.txt)
- [original/M63-REPORT.md](original/M63-REPORT.md)
- [original/M64-SHA256SUMS.txt](original/M64-SHA256SUMS.txt)
- [original/M65-review_second_gate.py](original/M65-review_second_gate.py)
- [original/M66-second_gate_review.json](original/M66-second_gate_review.json)
- [original/M67-second_gate_review.log](original/M67-second_gate_review.log)
- [original/M68-COMMANDS.txt](original/M68-COMMANDS.txt)
- [original/M69-REPORT.md](original/M69-REPORT.md)
- [original/M70-SHA256SUMS.txt](original/M70-SHA256SUMS.txt)
- [original/M71-uniform_ta_two_frame.json](original/M71-uniform_ta_two_frame.json)
- [original/M72-uniform_ta_two_frame.log](original/M72-uniform_ta_two_frame.log)
- [original/M73-uniform_ta_two_frame.py](original/M73-uniform_ta_two_frame.py)
- [original/M74-verify_artifact.py](original/M74-verify_artifact.py)
- [original/M75-COMMANDS.txt](original/M75-COMMANDS.txt)
- [original/M76-REPORT.md](original/M76-REPORT.md)
- [original/M77-SHA256SUMS.txt](original/M77-SHA256SUMS.txt)
- [original/M78-independent_raw_audit.json](original/M78-independent_raw_audit.json)
- [original/M79-independent_raw_audit.log](original/M79-independent_raw_audit.log)
- [original/M80-independent_raw_audit.py](original/M80-independent_raw_audit.py)
- [original/M81-verify_artifact.py](original/M81-verify_artifact.py)
- [original/M82-COMMANDS.txt](original/M82-COMMANDS.txt)
- [original/M83-REPORT.md](original/M83-REPORT.md)
- [original/M84-SHA256SUMS.txt](original/M84-SHA256SUMS.txt)
- [original/M85-normalization_review.json](original/M85-normalization_review.json)
- [original/M86-normalization_review.log](original/M86-normalization_review.log)
- [original/M87-normalization_review.py](original/M87-normalization_review.py)
- [original/M88-verify_artifact.py](original/M88-verify_artifact.py)
- [original/M89-GOLD4_taper_Tb_over_m.md](original/M89-GOLD4_taper_Tb_over_m.md)
- [original/M90-se_bigate_20260719.md](original/M90-se_bigate_20260719.md)
- [original/M91-se_trace_t3_report_20260721.md](original/M91-se_trace_t3_report_20260721.md)
- [original/context/R02-M76-REPORT.md.context.md](original/context/R02-M76-REPORT.md.context.md)

[Back to all 65 errors](../../README.md)
