# Record 037 — Optimal circuit distance of the Gross code

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> `T = 6` UNSAT is the sharp statement: **the gross code has no measurement-consistent
> single-ancilla SEC with six CNOT layers at all** — a 55-second exact result over the full
> 864-edge scheduling problem, with no assumption on the within-check orders, no tiling and no
> symmetry. Rows beyond the first are whatever closed inside the box.

Context: An UNSAT result from a scheduling encoding was promoted to a universal nonexistence statement. The encoding put both ancilla families entirely within one round window, whereas the schedule class under discussion permits ancilla lifetimes crossing period boundaries.

Locator: Proof draft dated 20 August 2026, section 2.4(5), lines 315–318.

## 2. Witness / adjudication

The verified search covered only unstaggered ancilla windows. Removing that restriction from the conclusion excludes legitimate staggered schedules without evidence.

Use the Gross left/right check blocks L_X=A, R_X=B, L_Z=B^T, R_Z=A^T, each of degree three. In CNOT layers 0,1,2 run L_X in parallel with R_Z; in layers 3,4,5 run R_X in parallel with L_Z. Each layer is a matching. The X ancilla for period p lives within p; the Z ancilla labelled p is prepared before layer 3 of p and measured after layer 2 of p+1. This gives six CNOT layers per period (864 CNOTs). For each of the 648 overlapping pairs, the MC counts for X_p against Z_p and Z_{p−1} are respectively 0 and 2, both even. The archived independent simulation also found all detectors deterministic in both memory sectors. This contradicts the unqualified six-layer impossibility, not the UNSAT result for the narrower unstaggered encoding.

Scope: statement_false

unstaggered编码的UNSAT被推广成所有六CNOT层SEC不可能；交错跨周期ancilla寿命未在编码中。合法staggered六层安排满足MC，故原泛称超出搜索域。

维持旧审计；排除的不是UNSAT求解本身而是无条件推广。

## 3. Evidence and verification

核对六层块安排和两种跨周期MC计数0/2；旧Stim双扇区确定性检查沿用，不重写为新实验。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_gross_sbbcert_20260820.md](original/M01-circdist_gross_sbbcert_20260820.md) — inherited_sanitized_source
- [M02-circdist_sbbcert_review_20260820.md](original/M02-circdist_sbbcert_review_20260820.md) — inherited_sanitized_source
- [M03-sched.py](original/M03-sched.py) — inherited_sanitized_source
- [M04-stimcheck.py](original/M04-stimcheck.py) — inherited_sanitized_source
- [M05-noclass.py](original/M05-noclass.py) — inherited_sanitized_source
- [M06-agent-ace09be0f0bec8908.jsonl.readable.md](original/M06-agent-ace09be0f0bec8908.jsonl.readable.md) — inherited_sanitized_source
- [M06-agent-ace09be0f0bec8908.jsonl.visible.json](original/M06-agent-ace09be0f0bec8908.jsonl.visible.json) — inherited_sanitized_source
- [M07-circdist_gross_g1_20260820.md](original/M07-circdist_gross_g1_20260820.md) — inherited_sanitized_source
- [M08-CIRCDIST_PROBLEMS.md](original/M08-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M09-circdist_lift_d3gate_20260820.md](original/M09-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M10-circdist_lift_nonint_proof_20260820.md](original/M10-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M11-circdist_lift_proofs_review_20260820.md](original/M11-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [M12-circdist_gross_toolfeas_20260820.md](original/M12-circdist_gross_toolfeas_20260820.md) — inherited_sanitized_source
- [R01-M01-circdist_gross_sbbcert_20260820.md.context.md](reconciliation_sources/R01-M01-circdist_gross_sbbcert_20260820.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_sbbcert_review_20260820.md.context.md](reconciliation_sources/R02-M02-circdist_sbbcert_review_20260820.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
