# 019 — Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

**Research problem:** P02 — Werner–Holevo zero-capacity boundary

## Original statement

> class ExtensionSDP:
>     def __init__(self) -> None:
>         self.rho = cp.Variable((SYM_DIM, SYM_DIM), symmetric=True, name="rho")
>         self.t = cp.Variable(name="t")
>         self.x = cp.Parameter(name="x")
>         self.eta = V @ self.rho @ V.T

**Context:** V is the isometry onto A tensor Sym^2(B), of dimension 3 times 6 = 18. The frozen task asked for an extension invariant under swapping two qutrit B systems, not necessarily supported only in their symmetric subspace.

**Original locator:** Semidefinite-program script creation, 2026-07-28T22:15:31.150Z, JSONL line 130

## Why it is an error

Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

## Witness / evidence

Let v=(|01>-|10>)/sqrt(2) and X=|0><0|_A tensor |v><v|. X is positive semidefinite and obeys S X S=X because Sv=-v. It is therefore swap-invariant, but its support lies entirely in the antisymmetric B sector and cannot be written V rho V^T. In the qutrit case the omitted block has dimension 3 times 3 = 9. The code solves a restricted feasibility problem, so its infeasibility cannot certify the original criterion.

## Scope

argument_invalid

## Classification

- II: 数学知识错误. 把交换不变扩展与只支撑于对称子空间的扩展混同。反对称纯态投影仍交换不变，却不在该参数化内。

同一概念混淆造成可行集缩小，只计 II，不再把同一事实换名重复计 I/IV。 2026-09-23 核对完整 proposer 会话：原任务为正确 27 维条件，错误参数化首次见于第 130 行；48 个加密 reasoning 块无非空明文摘要，未见先行等价推导。

## Adjudication notes

Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

Let v=(|01>-|10>)/sqrt(2) and X=|0><0|_A tensor |v><v|. X is positive semidefinite and obeys S X S=X because Sv=-v. It is therefore swap-invariant, but its support lies entirely in the antisymmetric B sector and cannot be written V rho V^T. In the qutrit case the omitted block has dimension 3 times 3 = 9. The code solves a restricted feasibility problem, so its infeasibility cannot certify the original criterion.

Scope: argument_invalid

交换不变的反对称态不支撑在对称子空间；将前一种可行性替换为后一种，改变了编码模型。此 witness 不证明特定目标态在较大集合内必有扩张，也不自动建立某次最终容量 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-whgap_p1_review_20260728.md](original/M02-whgap_p1_review_20260728.md)
- [original/M04-whgap_p1_review_20260728.md](original/M04-whgap_p1_review_20260728.md)
- [original/M05-whgap_independent_review.py](original/M05-whgap_independent_review.py)
- [original/M06-whgap_full_sdp_crosscheck.py](original/M06-whgap_full_sdp_crosscheck.py)
- [original/M07-whgap_independent_results.json](original/M07-whgap_independent_results.json)
- [original/M08-whgap_support_margin_tolerance.log](original/M08-whgap_support_margin_tolerance.log)
- [original/M09-whgap_support_margin.py](original/M09-whgap_support_margin.py)
- [original/M10-whgap_proposer_reproduction.py](original/M10-whgap_proposer_reproduction.py)
- [original/M11-SHA256SUMS.txt](original/M11-SHA256SUMS.txt)
- [original/M12-SHA256SUMS.txt](original/M12-SHA256SUMS.txt)

[Back to all 65 errors](../../README.md)
