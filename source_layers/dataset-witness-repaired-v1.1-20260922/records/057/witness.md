# Record 057 — Group-orbit Bell matrices

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> For every r>=3 and 0<=lambda<=1/2, the full D_r root projection A_r=WW^T/[4(r-1)], n=2r(r-1), satisfies
>   beta_cl(A_r-lambda I)=2r(2r-1)/3-n*lambda.

Context: The universal affine formula was registered as a candidate and later retained as refuted. beta_cl(B)=max_{s,t in {−1,+1}^n} s^T B t.

Locator: Registered shift-linear candidate, claim lines1–4; exact D3 envelope dossier, D3-1 and D3-3–D3-4.

## 2. Witness / adjudication

A competing sign pair outperforms the extrapolated affine branch beyond lambda=1/4.

For r=3 let W have rows(-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),(-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),(0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1), and A=WW^T/8. Take s=(1,1,1,1,-1,1,-1,1,-1,1,-1,1) and t=(-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1). Then s^TAt=8 and s^Tt=4. At lambda=1/2 their value is8-2=6, whereas the claimed formula gives10-12/2=4. One allowed pair already refutes the universal equality; no exhaustive upper-bound enumeration is needed.

Scope: tentative_candidate_refuted

D3、lambda=1/2 的合法符号对给值 6，而候选通式给 4；精确反例足以否定通式。作为探索中被否定的候选保留，不标为已证明或 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-GROTHORB.shift-linear-candidate.yaml](original/M01-GROTHORB.shift-linear-candidate.yaml) — inherited_sanitized_source
- [M02-d3-classical-envelope-20260907.md](original/M02-d3-classical-envelope-20260907.md) — inherited_sanitized_source
- [M03-d3-envelope-review-20260907.md](original/M03-d3-envelope-review-20260907.md) — inherited_sanitized_source
- [M04-d3-classical-envelope-certificate-20260907.json](original/M04-d3-classical-envelope-certificate-20260907.json) — inherited_sanitized_source
- [M05-classical-exploration-summary-20260907.md](original/M05-classical-exploration-summary-20260907.md) — inherited_sanitized_source
- [M06-classical-family-registration-20260907.md](original/M06-classical-family-registration-20260907.md) — inherited_sanitized_source
- [M07-check_d3_classical_envelope.py](original/M07-check_d3_classical_envelope.py) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
