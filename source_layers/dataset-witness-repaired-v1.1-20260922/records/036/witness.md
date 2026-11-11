# Record 036 — Optimal circuit distance of the Gross code

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> 1. **For the gross code, (MC) *is* [SBB26]'s non-interleaving condition.** Every overlapping
>    (X,Z) check pair shares exactly two qubits (§1), so `c_ab ∈ {0,1,2}`, and `c_ab` even means the
>    two shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede
>    all of `b`'s, or vice versa — S5 verbatim. **CONJECTURED** (the derivation is one line given §1;
>    the risk is only in whether S5's "either…or" is per-pair or global — S6 forces per-pair, since a
>    low-depth LRC cannot satisfy a global split).

Context: For overlapping X and Z checks, measurement consistency (MC) requires an even number of shared data qubits with Z-before-X local ordering. The draft identifies this pairwise parity condition with non-interleaving, which requires all operations of one check on their common support to precede all operations of the other. The proposed equivalence was labelled CONJECTURED.

Locator: Proof draft dated 20 August 2026, section 2.4(1), lines 246–251.

## 2. Witness / adjudication

Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

Take common-support gate times A_1=1, B_1=2, A_2=3, B_2=4. Both comparisons B_i<A_i are false, so the MC count is zero (even), but neither max(A)<min(B) nor max(B)<min(A) holds. The archived Gross-specific witness uses time arrays LX(left)=[11,10,3], LX(right)=[7,5,8], LZ(left)=[6,8,5], LZ(right)=[2,1,10]. It has zero MC violations among 648 overlaps, while 288 pairs are interleaved. The elementary four-time example independently refutes the inference from pairwise order agreement to non-interleaving.

Scope: tentative_candidate_refuted

相同的逐比特先后方向不等于一个check全部在另一个之前。1<2<3<4反例直接击破i.e.处的逻辑等价；这是局部顺序谓词混淆。

保留被推翻的CONJECTURED等价及其中实际无效推导，不需要它曾为PROVED；不自动归入overclaim。

## 3. Evidence and verification

四时间解析反例本轮复核；Gross专用648对/288交错是已存审计的更强实例。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_gross_sbbcert_20260820.md](original/M01-circdist_gross_sbbcert_20260820.md) — inherited_sanitized_source
- [M02-circdist_sbbcert_review_20260820.md](original/M02-circdist_sbbcert_review_20260820.md) — inherited_sanitized_source
- [M03-CIRCDIST.gross.mc-equiv.yaml](original/M03-CIRCDIST.gross.mc-equiv.yaml) — inherited_sanitized_source
- [M04-CIRCDIST.gross.mc-equiv.yaml](original/M04-CIRCDIST.gross.mc-equiv.yaml) — inherited_sanitized_source
- [M05-agent-ace09be0f0bec8908.jsonl.readable.md](original/M05-agent-ace09be0f0bec8908.jsonl.readable.md) — inherited_sanitized_source
- [M05-agent-ace09be0f0bec8908.jsonl.visible.json](original/M05-agent-ace09be0f0bec8908.jsonl.visible.json) — inherited_sanitized_source
- [M06-circdist_gross_g1_20260820.md](original/M06-circdist_gross_g1_20260820.md) — inherited_sanitized_source
- [M07-CIRCDIST_PROBLEMS.md](original/M07-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M08-circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M09-circdist_lift_nonint_proof_20260820.md](original/M09-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M10-circdist_lift_proofs_review_20260820.md](original/M10-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [M11-circdist_gross_toolfeas_20260820.md](original/M11-circdist_gross_toolfeas_20260820.md) — inherited_sanitized_source
- [M12-circdist_gross_sbbcert_20260820.md](original/M12-circdist_gross_sbbcert_20260820.md) — inherited_sanitized_source
- [M13-circdist_sbbcert_review_20260820.md](original/M13-circdist_sbbcert_review_20260820.md) — inherited_sanitized_source
- [R01-M01-circdist_gross_sbbcert_20260820.md.context.md](reconciliation_sources/R01-M01-circdist_gross_sbbcert_20260820.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_sbbcert_review_20260820.md.context.md](reconciliation_sources/R02-M02-circdist_sbbcert_review_20260820.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
