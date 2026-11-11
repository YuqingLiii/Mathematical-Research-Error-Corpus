# Record 048 — Set equality and collision

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> 结合已确认的 `R_out`，actual T-a 约 `94,172`、T-b 约 `151.84`，都低于各自 cap。

Context: The first tame c=2 gate was reported passing. Its parameters are n=18,j=6,a=b=3 and color multiplicity m=binom(6,3)=20.

Locator: Assistant message, 2026-07-22T05:14:47.680Z; raw-normalization review, section2.

## 2. Witness / adjudication

The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

The reported normalized value is160582822829/1705200. Multiplication by20 gives raw T_a=160582822829/85260. Its cap is51396202/35. Their exact ratio is36224413/28242984>1, with positive numerator excess7981429. Thus this gate fails. The second gate n=19 similarly has raw T_a=204466088827/71920 and cap137582445/64, ratio10611004/8023575>1. This refutes the physical T_a gate claim; it does not refute the original set-equality lower-bound theorem.

Scope: computation_false

保留 normalized contraction 被报成 actual physical T_a 并据此宣称门通过的错误。与047分开：047是一般T_b证明缺口；048有T_a精确失败例。

旧已核对的 factor20、两份独立归一化审查和原始PASS均在包内；本轮只是重新接上同一证据链，不改变失败结论。

## 3. Evidence and verification

本轮用有理数重新算出同一精确比值；各块原数据与独立重建代码仍属已存历史证据，此次没有重新生成全部 CG 矩阵。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md](original/M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.visible.json](original/M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M02-COMMANDS.txt](original/M02-COMMANDS.txt) — inherited_sanitized_source
- [M03-REPORT.md](original/M03-REPORT.md) — inherited_sanitized_source
- [M04-SHA256SUMS.txt](original/M04-SHA256SUMS.txt) — inherited_sanitized_source
- [M05-independent_audit.json](original/M05-independent_audit.json) — inherited_sanitized_source
- [M06-independent_audit.log](original/M06-independent_audit.log) — inherited_sanitized_source
- [M07-independent_audit.py](original/M07-independent_audit.py) — inherited_sanitized_source
- [M08-probe_rerun.log](original/M08-probe_rerun.log) — inherited_sanitized_source
- [M09-rerun_common_line_exact.json](original/M09-rerun_common_line_exact.json) — inherited_sanitized_source
- [M10-rerun_common_line_exact.log](original/M10-rerun_common_line_exact.log) — inherited_sanitized_source
- [M11-source_sha_verification.log](original/M11-source_sha_verification.log) — inherited_sanitized_source
- [M12-COMMANDS.txt](original/M12-COMMANDS.txt) — inherited_sanitized_source
- [M13-REPORT.md](original/M13-REPORT.md) — inherited_sanitized_source
- [M14-SHA256SUMS.txt](original/M14-SHA256SUMS.txt) — inherited_sanitized_source
- [M15-carrier_dimension_review.json](original/M15-carrier_dimension_review.json) — inherited_sanitized_source
- [M16-carrier_dimension_review.log](original/M16-carrier_dimension_review.log) — inherited_sanitized_source
- [M17-review_carrier_dimension.py](original/M17-review_carrier_dimension.py) — inherited_sanitized_source
- [M18-COMMANDS.txt](original/M18-COMMANDS.txt) — inherited_sanitized_source
- [M19-REPORT.md](original/M19-REPORT.md) — inherited_sanitized_source
- [M20-SHA256SUMS.txt](original/M20-SHA256SUMS.txt) — inherited_sanitized_source
- [M21-effective_rank_review.json](original/M21-effective_rank_review.json) — inherited_sanitized_source
- [M22-effective_rank_review.log](original/M22-effective_rank_review.log) — inherited_sanitized_source
- [M23-review_effective_rank.py](original/M23-review_effective_rank.py) — inherited_sanitized_source
- [M24-verify_artifact.py](original/M24-verify_artifact.py) — inherited_sanitized_source
- [M25-COMMANDS.txt](original/M25-COMMANDS.txt) — inherited_sanitized_source
- [M26-REPORT.md](original/M26-REPORT.md) — inherited_sanitized_source
- [M27-SHA256SUMS.txt](original/M27-SHA256SUMS.txt) — inherited_sanitized_source
- [M28-log.txt](original/M28-log.txt) — inherited_sanitized_source
- [M29-se_trace_t5_long_cap.json](original/M29-se_trace_t5_long_cap.json) — inherited_sanitized_source
- [M30-se_trace_t5_long_cap.py](original/M30-se_trace_t5_long_cap.py) — inherited_sanitized_source
- [M31-COMMANDS.txt](original/M31-COMMANDS.txt) — inherited_sanitized_source
- [M32-REPORT.md](original/M32-REPORT.md) — inherited_sanitized_source
- [M33-SHA256SUMS.txt](original/M33-SHA256SUMS.txt) — inherited_sanitized_source
- [M34-construct_rout.py](original/M34-construct_rout.py) — inherited_sanitized_source
- [M35-tame_c2_rout.json](original/M35-tame_c2_rout.json) — inherited_sanitized_source
- [M36-tame_c2_rout.log](original/M36-tame_c2_rout.log) — inherited_sanitized_source
- [M37-tame_c2_rout.npz](original/M37-tame_c2_rout.npz) — inherited_sanitized_source
- [M38-COMMANDS.txt](original/M38-COMMANDS.txt) — inherited_sanitized_source
- [M39-REPORT.md](original/M39-REPORT.md) — inherited_sanitized_source
- [M40-SHA256SUMS.txt](original/M40-SHA256SUMS.txt) — inherited_sanitized_source
- [M41-construct_rcol.py](original/M41-construct_rcol.py) — inherited_sanitized_source
- [M42-tame_c2_rcol.json](original/M42-tame_c2_rcol.json) — inherited_sanitized_source
- [M43-tame_c2_rcol.log](original/M43-tame_c2_rcol.log) — inherited_sanitized_source
- [M44-tame_c2_rcol.npz](original/M44-tame_c2_rcol.npz) — inherited_sanitized_source
- [M45-verify_rcol.log](original/M45-verify_rcol.log) — inherited_sanitized_source
- [M46-verify_rcol.py](original/M46-verify_rcol.py) — inherited_sanitized_source
- [M47-COMMANDS.txt](original/M47-COMMANDS.txt) — inherited_sanitized_source
- [M48-REPORT.md](original/M48-REPORT.md) — inherited_sanitized_source
- [M49-SHA256SUMS.txt](original/M49-SHA256SUMS.txt) — inherited_sanitized_source
- [M50-rcol_review.json](original/M50-rcol_review.json) — inherited_sanitized_source
- [M51-rcol_review.log](original/M51-rcol_review.log) — inherited_sanitized_source
- [M52-review_rcol.py](original/M52-review_rcol.py) — inherited_sanitized_source
- [M53-COMMANDS.txt](original/M53-COMMANDS.txt) — inherited_sanitized_source
- [M54-REPORT.md](original/M54-REPORT.md) — inherited_sanitized_source
- [M55-SHA256SUMS.txt](original/M55-SHA256SUMS.txt) — inherited_sanitized_source
- [M56-second_gate.json](original/M56-second_gate.json) — inherited_sanitized_source
- [M57-second_gate.log](original/M57-second_gate.log) — inherited_sanitized_source
- [M58-second_gate_inventory.npz](original/M58-second_gate_inventory.npz) — inherited_sanitized_source
- [M59-second_gate_witness.npz](original/M59-second_gate_witness.npz) — inherited_sanitized_source
- [M60-second_tame_c2_gate.py](original/M60-second_tame_c2_gate.py) — inherited_sanitized_source
- [M61-verify_second_gate.py](original/M61-verify_second_gate.py) — inherited_sanitized_source
- [M62-COMMANDS.txt](original/M62-COMMANDS.txt) — inherited_sanitized_source
- [M63-REPORT.md](original/M63-REPORT.md) — inherited_sanitized_source
- [M64-SHA256SUMS.txt](original/M64-SHA256SUMS.txt) — inherited_sanitized_source
- [M65-review_second_gate.py](original/M65-review_second_gate.py) — inherited_sanitized_source
- [M66-second_gate_review.json](original/M66-second_gate_review.json) — inherited_sanitized_source
- [M67-second_gate_review.log](original/M67-second_gate_review.log) — inherited_sanitized_source
- [M68-COMMANDS.txt](original/M68-COMMANDS.txt) — inherited_sanitized_source
- [M69-REPORT.md](original/M69-REPORT.md) — inherited_sanitized_source
- [M70-SHA256SUMS.txt](original/M70-SHA256SUMS.txt) — inherited_sanitized_source
- [M71-uniform_ta_two_frame.json](original/M71-uniform_ta_two_frame.json) — inherited_sanitized_source
- [M72-uniform_ta_two_frame.log](original/M72-uniform_ta_two_frame.log) — inherited_sanitized_source
- [M73-uniform_ta_two_frame.py](original/M73-uniform_ta_two_frame.py) — inherited_sanitized_source
- [M74-verify_artifact.py](original/M74-verify_artifact.py) — inherited_sanitized_source
- [M75-COMMANDS.txt](original/M75-COMMANDS.txt) — inherited_sanitized_source
- [M76-REPORT.md](original/M76-REPORT.md) — inherited_sanitized_source
- [M77-SHA256SUMS.txt](original/M77-SHA256SUMS.txt) — inherited_sanitized_source
- [M78-independent_raw_audit.json](original/M78-independent_raw_audit.json) — inherited_sanitized_source
- [M79-independent_raw_audit.log](original/M79-independent_raw_audit.log) — inherited_sanitized_source
- [M80-independent_raw_audit.py](original/M80-independent_raw_audit.py) — inherited_sanitized_source
- [M81-verify_artifact.py](original/M81-verify_artifact.py) — inherited_sanitized_source
- [M82-COMMANDS.txt](original/M82-COMMANDS.txt) — inherited_sanitized_source
- [M83-REPORT.md](original/M83-REPORT.md) — inherited_sanitized_source
- [M84-SHA256SUMS.txt](original/M84-SHA256SUMS.txt) — inherited_sanitized_source
- [M85-normalization_review.json](original/M85-normalization_review.json) — inherited_sanitized_source
- [M86-normalization_review.log](original/M86-normalization_review.log) — inherited_sanitized_source
- [M87-normalization_review.py](original/M87-normalization_review.py) — inherited_sanitized_source
- [M88-verify_artifact.py](original/M88-verify_artifact.py) — inherited_sanitized_source
- [M89-se_bigate_20260719.md](original/M89-se_bigate_20260719.md) — inherited_sanitized_source
- [M90-se_trace_t3_report_20260721.md](original/M90-se_trace_t3_report_20260721.md) — inherited_sanitized_source
- [R01-M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md.context.md](reconciliation_sources/R01-M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md.context.md) — reconciliation_source_window
- [R02-M76-REPORT.md.context.md](reconciliation_sources/R02-M76-REPORT.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
