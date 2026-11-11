# Record 047 — Set equality and collision

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> 有效秩证明严格成立，uniform physical \(T_b\) 对所有 admissible tame sector、所有正 LR 重数 \(c\) 全部关闭。

Context: The completion message applies a normalized effective-rank calculation to the unnormalized physical trace quantity T_b.

Locator: Assistant message, 2026-07-22T13:19:00.659Z.

## 2. Witness / adjudication

A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.

The raw physical maps obey S_gamma S_gamma*=m K_gamma, so their nonzero A_gamma=S_gamma* S_gamma eigenvalues are m times the normalized k_gamma,mu. The common-line formulas are r_mu=||t_mu||^2/m and a_gamma,mu=m|d_gamma,mu|^2. Contracting |d|^2*r_mu instead of a_mass*r_mu computes the divided quantity T_b/m. A derived bound T_b/m<=B implies only T_b<=mB, not T_b<=B when m>1. This defeats the claimed uniform proof. The corrected finite T_b examples still pass; no physical T_b counterexample is claimed.

Scope: argument_invalid

保留关于 T_b/m 的有效秩界被用于关闭 physical T_b 的证据对象替换。分类 yes 的依据是从归一化量的有效证明跨到不同物理量且明确声称统一关闭，不是把所有漏因子都自动算 overclaim。

旧 witness 明确只否定 T_b 的现有证明，并未提供 T_b 反例；这个边界维持。原结论由 proposer/coordinator 写出，不能说是独立 reviewer 发明的错误。

## 3. Evidence and verification

完整归一化审计及原声明已保留；逐式复核 m 因子，不以本轮没有重跑大矩阵否定此前核验。

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
- [M89-GOLD4_taper_Tb_over_m.md](original/M89-GOLD4_taper_Tb_over_m.md) — inherited_sanitized_source
- [M90-se_bigate_20260719.md](original/M90-se_bigate_20260719.md) — inherited_sanitized_source
- [M91-se_trace_t3_report_20260721.md](original/M91-se_trace_t3_report_20260721.md) — inherited_sanitized_source
- [R01-M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md.context.md](reconciliation_sources/R01-M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md.context.md) — reconciliation_source_window
- [R02-M76-REPORT.md.context.md](reconciliation_sources/R02-M76-REPORT.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
