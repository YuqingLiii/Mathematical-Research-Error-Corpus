# Record 067 — Optimal circuit distance of the Gross code

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> * weight-≤10 configurations from the weight-12 pool: **0** in both sectors.
> 
> [Excerpt break]
> 
> 1. **`d_eff = 11` is not certified.** Only the weight-12-pool disqualifier is clean. Uncovered:
>    `|gamma| <= 10` arising from weight-14 logicals, or from overlapping residual configurations
>    (`Σ|E_i| = |V| + 2m`, `m >= 1`). Weight-13 is now **provably empty** (§2, even weight). Closing
>    this is exactly the campaign's 990-slot SAT machinery, per sector.

Context: The model explicitly kept its proposed schedule as a candidate, not a proved distance-12 construction. The erroneous part is the zero-count audit and the assertion that all weight-12-pool distance-at-most-10 mechanisms had been excluded.

Locator: Candidate-search report dated 23 August 2026, section 6 audit and section 6.2(1), lines 177 and 185–188.

## 2. Witness / adjudication

The filter tested only two of four gain-positive residual shapes. In particular, a four-suffix with one qubit outside the target logical support can still give a positive gain after cancellation by a singleton. Requiring each hook to fit entirely inside the target support misses such configurations.

The same candidate admits target support V={1,3,7,11,12,14,72,73,74,77,78,80}. Use check 66's four-suffix {78,12,141,72}, check 2's two-suffix {77,80}, and eight singleton faults {1,3,7,11,14,73,74,141}. Their symmetric difference is exactly V; qubit 141 cancels. The total cost is 1+1+8=10, not more than 10. The raw order for check 66 is (68,67,78,12,141,72) at times (5,8,9,11,12,32); check 2's last two times are (12,32). The archived verifier checks V∈ker H_Z and V∉rowspace H_X and finds 72 such witnesses in each sector. The effective-distance audit is false; no false completed-root claim is attributed.

Scope: computation_false

尽管root明示未证明，局部weight12-pool分层仍被错误宣称全部排除。filter仅覆盖两个suffix形状，遗漏允许外部qubit抵消的4-suffix；明确10故障见证推翻该局部零计数。

原有已确认错误恢复为可复核；上轮已把冻结Gross矩阵、实际候选36slot和给定支撑拼接，独立精确验证，不再保留fixture pending。

## 3. Evidence and verification

本轮接续已有fresh witness_checks：10故障XOR=12点logical、HZ syndrome=0、非rowspaceHX；未声称144个历史见证全部重跑。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_dstar_hunt1_20260823.md](original/M01-circdist_dstar_hunt1_20260823.md) — inherited_sanitized_source
- [M02-circdist_dstar_hunt2_20260823.md](original/M02-circdist_dstar_hunt2_20260823.md) — inherited_sanitized_source
- [M03-circdist_dstar_hunt3_20260828.md](original/M03-circdist_dstar_hunt3_20260828.md) — inherited_sanitized_source
- [M04-circdist_sbbcert_review_20260820.md](original/M04-circdist_sbbcert_review_20260820.md) — inherited_sanitized_source
- [M05-tiled_gapcand_32.json](original/M05-tiled_gapcand_32.json) — inherited_sanitized_source
- [M06-circdist_dstar_hunt1_20260823.md](original/M06-circdist_dstar_hunt1_20260823.md) — inherited_sanitized_source
- [M07-SCHEDULER.yaml](original/M07-SCHEDULER.yaml) — inherited_sanitized_source
- [M08-CIRCDIST_PROBLEMS.md](original/M08-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M09-CIRCDIST.gross.yaml](original/M09-CIRCDIST.gross.yaml) — inherited_sanitized_source
- [M10-CIRCDIST.gross.dext-cap.yaml](original/M10-CIRCDIST.gross.dext-cap.yaml) — inherited_sanitized_source
- [M11-CIRCDIST.lift.iff.yaml](original/M11-CIRCDIST.lift.iff.yaml) — inherited_sanitized_source
- [M12-proof_dag_check.py](original/M12-proof_dag_check.py) — inherited_sanitized_source
- [M13-evidence_closure_check.py](original/M13-evidence_closure_check.py) — inherited_sanitized_source
- [R01-M01-circdist_dstar_hunt1_20260823.md.context.md](reconciliation_sources/R01-M01-circdist_dstar_hunt1_20260823.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_dstar_hunt2_20260823.md.context.md](reconciliation_sources/R02-M02-circdist_dstar_hunt2_20260823.md.context.md) — reconciliation_source_window
- [R03-M02-circdist_dstar_hunt2_20260823.md.context.md](reconciliation_sources/R03-M02-circdist_dstar_hunt2_20260823.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
