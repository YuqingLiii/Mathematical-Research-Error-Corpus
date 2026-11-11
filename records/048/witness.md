# 048 — The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

**Research problem:** P10 — Set equality and collision

## Original statement

> 结合已确认的 `R_out`，actual T-a 约 `94,172`、T-b 约 `151.84`，都低于各自 cap。

**Context:** The first tame c=2 gate was reported passing. Its parameters are n=18,j=6,a=b=3 and color multiplicity m=binom(6,3)=20.

**Original locator:** Assistant message, 2026-07-22T05:14:47.680Z; raw-normalization review, section2.

## Why it is an error

The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

## Witness / evidence

The reported normalized value is160582822829/1705200. Multiplication by20 gives raw T_a=160582822829/85260. Its cap is51396202/35. Their exact ratio is36224413/28242984>1, with positive numerator excess7981429. Thus this gate fails. The second gate n=19 similarly has raw T_a=204466088827/71920 and cap137582445/64, ratio10611004/8023575>1. This refutes the physical T_a gate claim; it does not refute the original set-equality lower-bound theorem.

## Scope

computation_false

## Classification

- IV: 逻辑推理错误. 将压缩计算所得值标成 actual T_a，并与物理 cap 比较。归一化量的计算不能直接用于物理量；恢复 m=20 后精确比值大于一。

与 047 一致：此条的压缩值被错误标为 physical actual value，再据此判门通过；不把正确压缩计算重新说成算术错误。

## Adjudication notes

The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

The reported normalized value is160582822829/1705200. Multiplication by20 gives raw T_a=160582822829/85260. Its cap is51396202/35. Their exact ratio is36224413/28242984>1, with positive numerator excess7981429. Thus this gate fails. The second gate n=19 similarly has raw T_a=204466088827/71920 and cap137582445/64, ratio10611004/8023575>1. This refutes the physical T_a gate claim; it does not refute the original set-equality lower-bound theorem.

Scope: computation_false

保留 normalized contraction 被报成 actual physical T_a 并据此宣称门通过的错误。与047分开：047是一般T_b证明缺口；048有T_a精确失败例。

旧已核对的 factor20、两份独立归一化审查和原始PASS均在包内；本轮只是重新接上同一证据链，不改变失败结论。

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
- [original/M89-se_bigate_20260719.md](original/M89-se_bigate_20260719.md)
- [original/M90-se_trace_t3_report_20260721.md](original/M90-se_trace_t3_report_20260721.md)
- [original/context/R02-M76-REPORT.md.context.md](original/context/R02-M76-REPORT.md.context.md)

[Back to all 65 errors](../../README.md)
