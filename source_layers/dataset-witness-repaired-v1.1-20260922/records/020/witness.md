# Record 020 — Werner–Holevo zero-capacity boundary

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> - **Pure-input structure (verify exactly first):** for a pure qutrit psi (take real psi and
>   generic complex psi), spec Λ_x(psi) = {x/2, x/2, 1-x} and
>   spec Λ_x^c(psi) = {1-x, x/2, x/2, 0} — B-side full rank, E-side one-dimensional kernel.

Context: The claim concerns Lambda_x(rho)=(1-x)rho+(x/2)(Tr(rho)I-rho^T), and is explicitly requested for both real and generic complex pure inputs. The commission says “verify exactly first,” so this is an asserted working formula being tested, not a completed theorem.

Locator: Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522

## 2. Witness / adjudication

The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

Take x=9/20 and psi=(1,i,1)/sqrt(3). Then |psi^T psi|^2=1/9. Writing a=1-x and b=x/2, Lambda_x(|psi><psi|)=bI+a|psi><psi|-b|bar(psi)><bar(psi)| has eigenvalues b and [(1-b) +/- sqrt((1-b)^2-4ab|psi^T psi|^2)]/2. These are 9/40 and (31 +/- 3 sqrt(97))/80, not {11/20,9/40,9/40}.

Scope: statement_false

复输入的特征多项式不等于所列固定谱。原任务明确要求先验证工作公式；保留为研究中被推翻的候选公式，不描述成已证明结果或完成声明。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-WHGAP-main-c5b96aec.jsonl.readable.md](original/M01-WHGAP-main-c5b96aec.jsonl.readable.md) — inherited_sanitized_source
- [M01-WHGAP-main-c5b96aec.jsonl.visible.json](original/M01-WHGAP-main-c5b96aec.jsonl.visible.json) — inherited_sanitized_source
- [M02-whgap_p9_necessary_20260729.md](original/M02-whgap_p9_necessary_20260729.md) — inherited_sanitized_source
- [M03-WHGAP-P9-019faef9.jsonl.readable.md](original/M03-WHGAP-P9-019faef9.jsonl.readable.md) — inherited_sanitized_source
- [M03-WHGAP-P9-019faef9.jsonl.visible.json](original/M03-WHGAP-P9-019faef9.jsonl.visible.json) — inherited_sanitized_source
- [M04-WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M04-WERNER-HOLEVO-GAP_PROOF_DAG.md) — inherited_sanitized_source
- [M05-whgap_p9_g0.py](original/M05-whgap_p9_g0.py) — inherited_sanitized_source
- [M06-whgap_p9_distillation.py](original/M06-whgap_p9_distillation.py) — inherited_sanitized_source
- [M07-whgap_lean_t1t2_20260730.md](original/M07-whgap_lean_t1t2_20260730.md) — inherited_sanitized_source
- [M08-whgap_r8_review_20260730.md](original/M08-whgap_r8_review_20260730.md) — inherited_sanitized_source
- [M09-whgap_r7_review_20260730.md](original/M09-whgap_r7_review_20260730.md) — inherited_sanitized_source
- [M10-whgap_r6_review_20260730.md](original/M10-whgap_r6_review_20260730.md) — inherited_sanitized_source
- [M11-whgap_p9b_noascent_20260729.md](original/M11-whgap_p9b_noascent_20260729.md) — inherited_sanitized_source
- [M12-whgap_p6_relaxation_20260729.md](original/M12-whgap_p6_relaxation_20260729.md) — inherited_sanitized_source
- [M13-whgap_p5_derivation_package_20260729.md](original/M13-whgap_p5_derivation_package_20260729.md) — inherited_sanitized_source
- [M14-whgap_p3_review_20260729.md](original/M14-whgap_p3_review_20260729.md) — inherited_sanitized_source
- [M15-whgap_p3_qonset_20260729.md](original/M15-whgap_p3_qonset_20260729.md) — inherited_sanitized_source
- [M16-whgap_external_review_chatgpt_20260728.md](original/M16-whgap_external_review_chatgpt_20260728.md) — inherited_sanitized_source
- [M17-main.tex](original/M17-main.tex) — inherited_sanitized_source
- [M18-whgap_p4_review_20260728.md](original/M18-whgap_p4_review_20260728.md) — inherited_sanitized_source
- [M19-RESEARCH_STRUCTURE_PROTOCOL.md](original/M19-RESEARCH_STRUCTURE_PROTOCOL.md) — inherited_sanitized_source
- [M20-DAG_PROTOCOL.md](original/M20-DAG_PROTOCOL.md) — inherited_sanitized_source
- [M21-proof_dag_check.py](original/M21-proof_dag_check.py) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
