# Record 032 — Circuit versus effective distance

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> **CONJECTURED 5.10 (saturation and one-round decidability).** Consequences of 5.9:
> 
> 1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
>    `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model.

Context: The historical saturation index was defined as the first round count after which circuit distance equals the static code distance d forever, with infinity if this never happens. It was not the index of convergence to an arbitrary lower limiting value. The quoted corollary was labelled CONJECTURED.

Locator: Proof draft dated 20 August 2026, conjectured Corollary 5.10(1), lines 855–858.

## 2. Witness / adjudication

Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

Take the Steane [[7,1,3]] code with X- and Z-check supports {3,4,5,6}, {1,2,5,6}, and {0,2,4,6}. Use increasing within-check orders, all X checks followed by all Z checks, and ideal temporal boundaries. In the X check ordered (0,2,4,6), an ancilla-X fault after the second CNOT produces residual X on {4,6}. Add one data-X fault on qubit 1 before the Z-check block. The net support {1,4,6} meets each listed Z check in zero or two positions, and is not an X stabilizer: every nonzero word in their X-check rowspace has weight four, whereas this support has weight three. Thus two faults produce an undetected logical X. Appending fault-free rounds preserves this witness, so d_R≤2 for every R; it can never equal the static distance d=3 eventually. Therefore R_sat=infinity, contradicting R_sat≤3. Only the saturation-to-d claim is refuted, not eventual constancy at a lower value. The original archived calculation also reports d_eff=2 and d_R=2 for R=1,2,3,4.

Scope: tentative_candidate_refuted

原文从d_R最终常数推出按冻结定义“最终等于静态d”的R_sat≤d，把已支持的较弱稳定结论当成较强饱和结论。CONJECTURED标签不消除其中明确写出的错误推论。

维持既有候选推论错误；用户包含未完成证明，故不得因CONJECTURED删除。

## 3. Evidence and verification

Steane两故障支撑{1,4,6}的零syndrome和非稳定子核对已完成；归纳补空轮使d_R≤2<d=3。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M02-circdist_lift_proofs_review_20260820.md](original/M02-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [M03-circdist_lift_iff_amendment1_20260820.md](original/M03-circdist_lift_iff_amendment1_20260820.md) — inherited_sanitized_source
- [M04-circdist_lift_nonint_proof_20260820.md](original/M04-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M05-agent-afd9b18b206ce896f.jsonl.readable.md](original/M05-agent-afd9b18b206ce896f.jsonl.readable.md) — inherited_sanitized_source
- [M05-agent-afd9b18b206ce896f.jsonl.visible.json](original/M05-agent-afd9b18b206ce896f.jsonl.visible.json) — inherited_sanitized_source
- [M06-CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M07-circdist_lift_litverify2_20260820.md](original/M07-circdist_lift_litverify2_20260820.md) — inherited_sanitized_source
- [M08-circdist_lift_nonint_proof_20260820.md](original/M08-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M09-circdist_lift_d3gate_20260820.md](original/M09-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M10-circdist_lift_iff_proof_20260820.md](original/M10-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M11-circdist_lift_proofs_review_20260820.md](original/M11-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [R01-M01-circdist_lift_iff_proof_20260820.md.context.md](reconciliation_sources/R01-M01-circdist_lift_iff_proof_20260820.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_lift_proofs_review_20260820.md.context.md](reconciliation_sources/R02-M02-circdist_lift_proofs_review_20260820.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
