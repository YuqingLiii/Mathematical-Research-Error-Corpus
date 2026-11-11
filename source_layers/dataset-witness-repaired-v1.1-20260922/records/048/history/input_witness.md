# Record 048 — Set equality and collision

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 结合已确认的 `R_out`，actual T-a 约 `94,172`、T-b 约 `151.84`，都低于各自 cap。

**Recorded location:** Assistant message, 2026-07-22T05:14:47.680Z; raw-normalization review, section2.

**Context (annotation, not a source quotation):** The first tame c=2 gate was reported passing. Its parameters are n=18,j=6,a=b=3 and color multiplicity m=binom(6,3)=20.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

### Argument or calculation

The reported normalized value is160582822829/1705200. Multiplication by20 gives raw T_a=160582822829/85260. Its cap is51396202/35. Their exact ratio is36224413/28242984>1, with positive numerator excess7981429. Thus this gate fails. The second gate n=19 similarly has raw T_a=204466088827/71920 and cap137582445/64, ratio10611004/8023575>1. This refutes the physical T_a gate claim; it does not refute the original set-equality lower-bound theorem.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl](original/M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/gold4_taper/rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl") · [event data](original/M01-rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 6426–6439, 6491–6504, 6674–6691, 6980–6993, 7401–7415, 7569–7583, 11662–11675, 11747–11760, 11877–11890, 12014–12027.
  - Relevant location(s): agent_message 2026-07-22T05:14:47Z、05:25:56Z、05:57:03Z、06:30:22Z、07:09:10Z、07:29:16Z（声称）；15:27:18Z、15:33:51Z、15:49:23Z、16:08:51Z（纠正）
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/gold4_taper/rollout-2026-07-20T00-49-03-<session-id-redacted>.jsonl`

- [M02: COMMANDS.txt](original/M02-COMMANDS.txt "artifacts/logs_se_trace_t5_common_line_review_20260721/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–53.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/COMMANDS.txt`

- [M03: REPORT.md](original/M03-REPORT.md "artifacts/logs_se_trace_t5_common_line_review_20260721/REPORT.md")
  - Coverage: Full bundled file; source lines 1–270.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/REPORT.md`

- [M04: SHA256SUMS.txt](original/M04-SHA256SUMS.txt "artifacts/logs_se_trace_t5_common_line_review_20260721/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–10.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/SHA256SUMS.txt`

- [M05: independent_audit.json](original/M05-independent_audit.json "artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.json")
  - Coverage: Full bundled file; source lines 1–64.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.json`

- [M06: independent_audit.log](original/M06-independent_audit.log "artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.log")
  - Coverage: Full bundled file; source lines 1–8.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.log`

- [M07: independent_audit.py](original/M07-independent_audit.py "artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.py")
  - Coverage: Full bundled file; source lines 1–318.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/independent_audit.py`

- [M08: probe_rerun.log](original/M08-probe_rerun.log "artifacts/logs_se_trace_t5_common_line_review_20260721/probe_rerun.log")
  - Coverage: Full bundled file; source lines 1–10.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/probe_rerun.log`

- [M09: rerun_common_line_exact.json](original/M09-rerun_common_line_exact.json "artifacts/logs_se_trace_t5_common_line_review_20260721/rerun_common_line_exact.json")
  - Coverage: Full bundled file; source lines 1–197.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/rerun_common_line_exact.json`

- [M10: rerun_common_line_exact.log](original/M10-rerun_common_line_exact.log "artifacts/logs_se_trace_t5_common_line_review_20260721/rerun_common_line_exact.log")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/rerun_common_line_exact.log`

- [M11: source_sha_verification.log](original/M11-source_sha_verification.log "artifacts/logs_se_trace_t5_common_line_review_20260721/source_sha_verification.log")
  - Coverage: Full bundled file; source lines 1–12.
  - Source: `artifacts/logs_se_trace_t5_common_line_review_20260721/source_sha_verification.log`

- [M12: COMMANDS.txt](original/M12-COMMANDS.txt "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–45.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/COMMANDS.txt`

- [M13: REPORT.md](original/M13-REPORT.md "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–197.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/REPORT.md`

- [M14: SHA256SUMS.txt](original/M14-SHA256SUMS.txt "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–6.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/SHA256SUMS.txt`

- [M15: carrier_dimension_review.json](original/M15-carrier_dimension_review.json "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/carrier_dimension_review.json")
  - Coverage: Full bundled file; source lines 1–298.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/carrier_dimension_review.json`

- [M16: carrier_dimension_review.log](original/M16-carrier_dimension_review.log "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/carrier_dimension_review.log")
  - Coverage: Full bundled file; source lines 1–13.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/carrier_dimension_review.log`

- [M17: review_carrier_dimension.py](original/M17-review_carrier_dimension.py "artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/review_carrier_dimension.py")
  - Coverage: Full bundled file; source lines 1–320.
  - Source: `artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/review_carrier_dimension.py`

- [M18: COMMANDS.txt](original/M18-COMMANDS.txt "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/COMMANDS.txt`

- [M19: REPORT.md](original/M19-REPORT.md "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–132.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/REPORT.md`

- [M20: SHA256SUMS.txt](original/M20-SHA256SUMS.txt "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/SHA256SUMS.txt`

- [M21: effective_rank_review.json](original/M21-effective_rank_review.json "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/effective_rank_review.json")
  - Coverage: Full bundled file; source lines 1–205.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/effective_rank_review.json`

- [M22: effective_rank_review.log](original/M22-effective_rank_review.log "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/effective_rank_review.log")
  - Coverage: Full bundled file; source lines 1–11.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/effective_rank_review.log`

- [M23: review_effective_rank.py](original/M23-review_effective_rank.py "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/review_effective_rank.py")
  - Coverage: Full bundled file; source lines 1–361.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/review_effective_rank.py`

- [M24: verify_artifact.py](original/M24-verify_artifact.py "artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/verify_artifact.py")
  - Coverage: Full bundled file; source lines 1–41.
  - Source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722/verify_artifact.py`

- [M25: COMMANDS.txt](original/M25-COMMANDS.txt "artifacts/logs_se_trace_t5_long_cap_20260721/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–6.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/COMMANDS.txt`

- [M26: REPORT.md](original/M26-REPORT.md "artifacts/logs_se_trace_t5_long_cap_20260721/REPORT.md")
  - Coverage: Full bundled file; source lines 1–304.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/REPORT.md`

- [M27: SHA256SUMS.txt](original/M27-SHA256SUMS.txt "artifacts/logs_se_trace_t5_long_cap_20260721/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–6.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/SHA256SUMS.txt`

- [M28: log.txt](original/M28-log.txt "artifacts/logs_se_trace_t5_long_cap_20260721/log.txt")
  - Coverage: Full bundled file; source lines 1–10.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/log.txt`

- [M29: se_trace_t5_long_cap.json](original/M29-se_trace_t5_long_cap.json "artifacts/logs_se_trace_t5_long_cap_20260721/se_trace_t5_long_cap.json")
  - Coverage: Full bundled file; source lines 1–1529.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/se_trace_t5_long_cap.json`

- [M30: se_trace_t5_long_cap.py](original/M30-se_trace_t5_long_cap.py "artifacts/logs_se_trace_t5_long_cap_20260721/se_trace_t5_long_cap.py")
  - Coverage: Full bundled file; source lines 1–289.
  - Source: `artifacts/logs_se_trace_t5_long_cap_20260721/se_trace_t5_long_cap.py`

- [M31: COMMANDS.txt](original/M31-COMMANDS.txt "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–4.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/COMMANDS.txt`

- [M32: REPORT.md](original/M32-REPORT.md "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/REPORT.md")
  - Coverage: Full bundled file; source lines 1–168.
  - Relevant location(s): Referenced by artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/REPORT.md
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/REPORT.md`

- [M33: SHA256SUMS.txt](original/M33-SHA256SUMS.txt "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/SHA256SUMS.txt`

- [M34: construct_rout.py](original/M34-construct_rout.py "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/construct_rout.py")
  - Coverage: Full bundled file; source lines 1–415.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/construct_rout.py`

- [M35: tame_c2_rout.json](original/M35-tame_c2_rout.json "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.json")
  - Coverage: Full bundled file; source lines 1–1007.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.json`

- [M36: tame_c2_rout.log](original/M36-tame_c2_rout.log "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.log")
  - Coverage: Full bundled file; source lines 1–43.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.log`

- [M37: tame_c2_rout.npz](original/M37-tame_c2_rout.npz "artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.npz")
  - Coverage: full_binary_file.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.npz`

- [M38: COMMANDS.txt](original/M38-COMMANDS.txt "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–4.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/COMMANDS.txt`

- [M39: REPORT.md](original/M39-REPORT.md "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/REPORT.md")
  - Coverage: Full bundled file; source lines 1–68.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/REPORT.md`

- [M40: SHA256SUMS.txt](original/M40-SHA256SUMS.txt "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/SHA256SUMS.txt`

- [M41: construct_rcol.py](original/M41-construct_rcol.py "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/construct_rcol.py")
  - Coverage: Full bundled file; source lines 1–684.
  - Relevant location(s): Referenced by artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/REPORT.md
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/construct_rcol.py`

- [M42: tame_c2_rcol.json](original/M42-tame_c2_rcol.json "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json")
  - Coverage: Full bundled file; source lines 1–309.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json`

- [M43: tame_c2_rcol.log](original/M43-tame_c2_rcol.log "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.log")
  - Coverage: Full bundled file; source lines 1–309.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.log`

- [M44: tame_c2_rcol.npz](original/M44-tame_c2_rcol.npz "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.npz")
  - Coverage: full_binary_file.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.npz`

- [M45: verify_rcol.log](original/M45-verify_rcol.log "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/verify_rcol.log")
  - Coverage: Full bundled file; source lines 1–2.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/verify_rcol.log`

- [M46: verify_rcol.py](original/M46-verify_rcol.py "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/verify_rcol.py")
  - Coverage: Full bundled file; source lines 1–32.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/verify_rcol.py`

- [M47: COMMANDS.txt](original/M47-COMMANDS.txt "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–18.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/COMMANDS.txt`

- [M48: REPORT.md](original/M48-REPORT.md "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–199.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/REPORT.md`

- [M49: SHA256SUMS.txt](original/M49-SHA256SUMS.txt "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–6.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/SHA256SUMS.txt`

- [M50: rcol_review.json](original/M50-rcol_review.json "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/rcol_review.json")
  - Coverage: Full bundled file; source lines 1–901.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/rcol_review.json`

- [M51: rcol_review.log](original/M51-rcol_review.log "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/rcol_review.log")
  - Coverage: Full bundled file; source lines 1–15.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/rcol_review.log`

- [M52: review_rcol.py](original/M52-review_rcol.py "artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/review_rcol.py")
  - Coverage: Full bundled file; source lines 1–539.
  - Source: `artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722/review_rcol.py`

- [M53: COMMANDS.txt](original/M53-COMMANDS.txt "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/COMMANDS.txt`

- [M54: REPORT.md](original/M54-REPORT.md "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–131.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/REPORT.md`

- [M55: SHA256SUMS.txt](original/M55-SHA256SUMS.txt "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/SHA256SUMS.txt`

- [M56: second_gate.json](original/M56-second_gate.json "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.json")
  - Coverage: Full bundled file; source lines 1–971.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.json`

- [M57: second_gate.log](original/M57-second_gate.log "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.log")
  - Coverage: Full bundled file; source lines 1–10.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.log`

- [M58: second_gate_inventory.npz](original/M58-second_gate_inventory.npz "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate_inventory.npz")
  - Coverage: full_binary_file.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate_inventory.npz`

- [M59: second_gate_witness.npz](original/M59-second_gate_witness.npz "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate_witness.npz")
  - Coverage: full_binary_file.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate_witness.npz`

- [M60: second_tame_c2_gate.py](original/M60-second_tame_c2_gate.py "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_tame_c2_gate.py")
  - Coverage: Full bundled file; source lines 1–218.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_tame_c2_gate.py`

- [M61: verify_second_gate.py](original/M61-verify_second_gate.py "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/verify_second_gate.py")
  - Coverage: Full bundled file; source lines 1–49.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/verify_second_gate.py`

- [M62: COMMANDS.txt](original/M62-COMMANDS.txt "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/COMMANDS.txt`

- [M63: REPORT.md](original/M63-REPORT.md "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–93.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/REPORT.md`

- [M64: SHA256SUMS.txt](original/M64-SHA256SUMS.txt "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–6.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/SHA256SUMS.txt`

- [M65: review_second_gate.py](original/M65-review_second_gate.py "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/review_second_gate.py")
  - Coverage: Full bundled file; source lines 1–494.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/review_second_gate.py`

- [M66: second_gate_review.json](original/M66-second_gate_review.json "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/second_gate_review.json")
  - Coverage: Full bundled file; source lines 1–358.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/second_gate_review.json`

- [M67: second_gate_review.log](original/M67-second_gate_review.log "artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/second_gate_review.log")
  - Coverage: Full bundled file; source lines 1–14.
  - Source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722/second_gate_review.log`

- [M68: COMMANDS.txt](original/M68-COMMANDS.txt "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/COMMANDS.txt`

- [M69: REPORT.md](original/M69-REPORT.md "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–175.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/REPORT.md`

- [M70: SHA256SUMS.txt](original/M70-SHA256SUMS.txt "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/SHA256SUMS.txt`

- [M71: uniform_ta_two_frame.json](original/M71-uniform_ta_two_frame.json "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.json")
  - Coverage: Full bundled file; source lines 1–369.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.json`

- [M72: uniform_ta_two_frame.log](original/M72-uniform_ta_two_frame.log "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.log")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.log`

- [M73: uniform_ta_two_frame.py](original/M73-uniform_ta_two_frame.py "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.py")
  - Coverage: Full bundled file; source lines 1–238.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.py`

- [M74: verify_artifact.py](original/M74-verify_artifact.py "artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/verify_artifact.py")
  - Coverage: Full bundled file; source lines 1–33.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/verify_artifact.py`

- [M75: COMMANDS.txt](original/M75-COMMANDS.txt "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–3.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/COMMANDS.txt`

- [M76: REPORT.md](original/M76-REPORT.md "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–157.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/REPORT.md`

- [M77: SHA256SUMS.txt](original/M77-SHA256SUMS.txt "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/SHA256SUMS.txt`

- [M78: independent_raw_audit.json](original/M78-independent_raw_audit.json "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.json")
  - Coverage: Full bundled file; source lines 1–395.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.json`

- [M79: independent_raw_audit.log](original/M79-independent_raw_audit.log "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.log")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.log`

- [M80: independent_raw_audit.py](original/M80-independent_raw_audit.py "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.py")
  - Coverage: Full bundled file; source lines 1–299.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/independent_raw_audit.py`

- [M81: verify_artifact.py](original/M81-verify_artifact.py "artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/verify_artifact.py")
  - Coverage: Full bundled file; source lines 1–33.
  - Source: `artifacts/logs_se_trace_t5_ta_raw_audit_review_20260722/verify_artifact.py`

- [M82: COMMANDS.txt](original/M82-COMMANDS.txt "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/COMMANDS.txt")
  - Coverage: Full bundled file; source lines 1–3.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/COMMANDS.txt`

- [M83: REPORT.md](original/M83-REPORT.md "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/REPORT.md")
  - Coverage: Full bundled file; source lines 1–103.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/REPORT.md`

- [M84: SHA256SUMS.txt](original/M84-SHA256SUMS.txt "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–7.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/SHA256SUMS.txt`

- [M85: normalization_review.json](original/M85-normalization_review.json "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.json")
  - Coverage: Full bundled file; source lines 1–215.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.json`

- [M86: normalization_review.log](original/M86-normalization_review.log "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.log")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.log`

- [M87: normalization_review.py](original/M87-normalization_review.py "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.py")
  - Coverage: Full bundled file; source lines 1–100.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/normalization_review.py`

- [M88: verify_artifact.py](original/M88-verify_artifact.py "artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/verify_artifact.py")
  - Coverage: Full bundled file; source lines 1–22.
  - Source: `artifacts/logs_se_trace_t5_uniform_ta_normalization_review_20260722/verify_artifact.py`

- [M89: se_bigate_20260719.md](original/M89-se_bigate_20260719.md "artifacts/se_bigate_20260719.md")
  - Coverage: Full bundled file; source lines 1–332.
  - Relevant location(s): Referenced by artifacts/logs_se_trace_t5_carrier_dimension_review_20260722/REPORT.md
  - Source: `artifacts/se_bigate_20260719.md`

- [M90: se_trace_t3_report_20260721.md](original/M90-se_trace_t3_report_20260721.md "artifacts/logs_se_trace_t3_20260721/se_trace_t3_report_20260721.md")
  - Coverage: Full bundled file; source lines 1–500.
  - Relevant location(s): Referenced by artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/REPORT.md
  - Source: `artifacts/logs_se_trace_t3_20260721/se_trace_t3_report_20260721.md`
