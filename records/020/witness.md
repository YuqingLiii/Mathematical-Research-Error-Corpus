# 020 — The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

**Research problem:** P02 — Werner–Holevo zero-capacity boundary

## Original statement

> - **Pure-input structure (verify exactly first):** for a pure qutrit psi (take real psi and
>   generic complex psi), spec Λ_x(psi) = {x/2, x/2, 1-x} and
>   spec Λ_x^c(psi) = {1-x, x/2, x/2, 0} — B-side full rank, E-side one-dimensional kernel.

**Context:** The claim concerns Lambda_x(rho)=(1-x)rho+(x/2)(Tr(rho)I-rho^T), and is explicitly requested for both real and generic complex pure inputs. The commission says “verify exactly first,” so this is an asserted working formula being tested, not a completed theorem.

**Original locator:** Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522

## Why it is an error

The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

## Witness / evidence

Take x=9/20 and psi=(1,i,1)/sqrt(3). Then |psi^T psi|^2=1/9. Writing a=1-x and b=x/2, Lambda_x(|psi><psi|)=bI+a|psi><psi|-b|bar(psi)><bar(psi)| has eigenvalues b and [(1-b) +/- sqrt((1-b)^2-4ab|psi^T psi|^2)]/2. These are 9/40 and (31 +/- 3 sqrt(97))/80, not {11/20,9/40,9/40}.

## Scope

statement_false

## Classification

- III: 计算与代数错误. 所报纯输入谱公式不等于合法复输入的精确特征值。这里只将谱计算结果判错，不推测其内部怎样产生，也不把待检验公式写成已证定理。

III/IV 边界：直接可检验的错误是具体谱值，归 III；不推测其源自实输入向复输入推广的心理过程。

## Adjudication notes

The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

Take x=9/20 and psi=(1,i,1)/sqrt(3). Then |psi^T psi|^2=1/9. Writing a=1-x and b=x/2, Lambda_x(|psi><psi|)=bI+a|psi><psi|-b|bar(psi)><bar(psi)| has eigenvalues b and [(1-b) +/- sqrt((1-b)^2-4ab|psi^T psi|^2)]/2. These are 9/40 and (31 +/- 3 sqrt(97))/80, not {11/20,9/40,9/40}.

Scope: statement_false

复输入的特征多项式不等于所列固定谱。原任务明确要求先验证工作公式；保留为研究中被推翻的候选公式，不描述成已证明结果或完成声明。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-whgap_p9_necessary_20260729.md](original/M02-whgap_p9_necessary_20260729.md)
- [original/M04-WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M04-WERNER-HOLEVO-GAP_PROOF_DAG.md)
- [original/M05-whgap_p9_g0.py](original/M05-whgap_p9_g0.py)
- [original/M06-whgap_p9_distillation.py](original/M06-whgap_p9_distillation.py)
- [original/M07-whgap_lean_t1t2_20260730.md](original/M07-whgap_lean_t1t2_20260730.md)
- [original/M08-whgap_r8_review_20260730.md](original/M08-whgap_r8_review_20260730.md)
- [original/M09-whgap_r7_review_20260730.md](original/M09-whgap_r7_review_20260730.md)
- [original/M10-whgap_r6_review_20260730.md](original/M10-whgap_r6_review_20260730.md)
- [original/M11-whgap_p9b_noascent_20260729.md](original/M11-whgap_p9b_noascent_20260729.md)
- [original/M12-whgap_p6_relaxation_20260729.md](original/M12-whgap_p6_relaxation_20260729.md)
- [original/M13-whgap_p5_derivation_package_20260729.md](original/M13-whgap_p5_derivation_package_20260729.md)
- [original/M14-whgap_p3_review_20260729.md](original/M14-whgap_p3_review_20260729.md)
- [original/M15-whgap_p3_qonset_20260729.md](original/M15-whgap_p3_qonset_20260729.md)
- [original/M16-whgap_external_review_chatgpt_20260728.md](original/M16-whgap_external_review_chatgpt_20260728.md)
- [original/M18-whgap_p4_review_20260728.md](original/M18-whgap_p4_review_20260728.md)
- [original/M19-RESEARCH_STRUCTURE_PROTOCOL.md](original/M19-RESEARCH_STRUCTURE_PROTOCOL.md)
- [original/M20-DAG_PROTOCOL.md](original/M20-DAG_PROTOCOL.md)
- [original/M21-proof_dag_check.py](original/M21-proof_dag_check.py)

[Back to all 65 errors](../../README.md)
