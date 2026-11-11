# Record 052 — Finite-dimensional Grothendieck bounds

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> Here the direct covariant product map in irrep \(\rho\) is exactly
> `14400/d_rho` times the canonical K-pencil adjoint

**Recorded location:** Exact certificate draft write, 2026-08-31T03:29:17.319Z; correction at03:30:16.130Z.

**Context (annotation, not a source quotation):** The draft reused a single-vector Schur normalization after contraction over representation indices.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The contraction supplies a dimension factor that cancels the divisor d_rho.

### Argument or calculation

The single-vector formula has prefactor14400/d_rho. In Q^T J Q, contraction with J^{-1} contributes Tr(J^{-1}J)=d_rho. Thus the direct contracted coefficient map has prefactor(14400/d_rho)*d_rho=14400, independent of representation degree. The old code used ORDER*inverse(degree) modulo24001; the corrected code uses ORDER. Residual minor values consequently change from1400 and15799 to13280 and7143 modulo24001. The normalized Schur stage is unaffected.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 摘要 Correcting scaling factor 是事后更正。原登记 03:30:16 不是最早错误；新定位到 03:28:29 首次错误证书和 03:29:17 错误 prose，不能颠倒成正确推理之后抄错。

- [2026-08-31T03:29:50.216Z — codex_reasoning_summary](original/M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.readable.md) — source line 2351; recorded role: posthoc_only.

## Original materials

- [M01: rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl](original/M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/30/rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl") · [event data](original/M01-rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 2318–2330, 2336–2357.
  - Relevant location(s): line2342 exact patch; correction in paired transcript lines28037–28045; lines 2351; lines 2324; lines 2342
  - Source: `local-session-archive/2026/08/30/rollout-2026-08-30T16-49-42-<session-id-redacted>.jsonl`

- [M02: 01a0546f-67e8-7241-9a01-d3c89324279e.md](original/M02-01a0546f-67e8-7241-9a01-d3c89324279e.md.excerpt.md "research-graph/audit-bundles/2026-09-18/process-audit-v2/transcripts/01a0546f-67e8-7241-9a01-d3c89324279e.md")
  - Coverage: Selected text ranges; source lines 27997–28085, 28215–28364.
  - Relevant location(s): lines 28037-28045 and 28255-28324
  - Source: `research-graph/audit-bundles/2026-09-18/process-audit-v2/transcripts/01a0546f-67e8-7241-9a01-d3c89324279e.md`

- [M03: d4-two-minimal-five-block-linear-nogo-certificate-20260830.json](original/M03-d4-two-minimal-five-block-linear-nogo-certificate-20260830.json "research-graph/grothendieck-d4/artifacts/certificates/d4-two-minimal-five-block-linear-nogo-certificate-20260830.json")
  - Coverage: Full bundled file; source lines 1–51.
  - Source: `research-graph/grothendieck-d4/artifacts/certificates/d4-two-minimal-five-block-linear-nogo-certificate-20260830.json`
