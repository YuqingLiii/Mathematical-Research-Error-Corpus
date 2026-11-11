# Record 055 — Finite-dimensional Grothendieck bounds

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> A feasible unrestricted degree-4 moment/SOS dual whose objective equals the stated integer is a global upper bound on the sign optimization problem.

Context: The implication names the full 746825-coordinate system with 20 PSD blocks as its premise and directly cites the archived system constructor. That constructor defines a moment functional L, with theta_empty=L(1), and imposes C*theta_empty-sum_t objective_B[t]*theta_t=-1. Thus the specifically referenced feasibility problem has L(f)=-1 for f=C-a^T A b; it is a separating moment problem, not an upper-bounding SOS certificate. The generic statement about a correctly oriented SOS dual is not the error.

Locator: Exact proof-node creation event, 2026-08-30T01:29:22.886Z; first event. Referenced archived system constructor, Mathematics represented by the output, lines22–45; archived JSON normalization and feasibility fields.

## 2. Witness / adjudication

The direction of the moment/SOS separation was reversed.

If a degree-four functional L is nonnegative on every allowed square and respects the Boolean relations, then any SOS representation f=sum_j p_j^2 modulo those relations implies L(f)=sum_j L(p_j^2)>=0. A feasible separating functional with L(f)<0 therefore excludes that SOS representation; it does not prove f>=0 on Boolean inputs. Such separation also need not supply an actual negative Boolean input.

Scope: argument_invalid

上下文中的 L(f)<0、L 对允许平方非负，仅证明不存在指定 SOS 表示；不能证明 f 在 Boolean 输入上非负。证书方向/用途错误，使有效分离证据被用于它不能支撑的上界结论。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-GROTH-H4-001-duality-direction.jsonl.readable.md](original/M01-GROTH-H4-001-duality-direction.jsonl.readable.md) — inherited_sanitized_source
- [M01-GROTH-H4-001-duality-direction.jsonl.visible.json](original/M01-GROTH-H4-001-duality-direction.jsonl.visible.json) — inherited_sanitized_source
- [M02-h4_full_invariant_dual_spec.py](original/M02-h4_full_invariant_dual_spec.py) — inherited_sanitized_source
- [M03-h4_full_invariant_dual_spec.json](original/M03-h4_full_invariant_dual_spec.json) — inherited_sanitized_source
- [M04-d4-duality-direction-audit-20260829.md](original/M04-d4-duality-direction-audit-20260829.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
