# Record 023 — Werner–Holevo zero-capacity boundary

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

>     # environment kernel: analytic basis  (0, conj(u+iv)) and (1, -i kappa w),
>     # kappa = sqrt(2(1-x)/x); verified below to be a basis of ker Lambda^c(P_psi).
>     kappa = sp.sqrt(2 * (1 - x) / x)
>     k1 = sp.Matrix([0, *list(sp.simplify(sp.sqrt(2) * psi_bar))])
>     k2 = sp.Matrix([1, *list(sp.simplify(-sp.I * kappa * third))])
>     analytic_kernel_pass = zero_matrix(lamc_p * k1) and zero_matrix(lamc_p * k2)
>     analytic_kernel_orthogonal = zero((k1.H * k2)[0, 0])
>     pi_e = sp.simplify(projector(k1) + projector(k2))

**Recorded location:** Preserved isotropic weight-operator script, function weight_operators, lines 92–101

**Context (annotation, not a source quotation):** The script later instantiates psi=(0,1,-i)/sqrt(2) and third=(1,0,0). It labels third as the oriented cross product and uses the displayed formula for an environment-kernel basis. This release excerpt isolates the concrete basis defect from the legacy record, which also mentioned separate sign corrections.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.

### Argument or calculation

Let kappa=sqrt(2(1-x)/x). For the script’s psi and Kraus convention, the complementary output has entries G00=1-x, G01=i sqrt(x(1-x)/2), G10=-i sqrt(x(1-x)/2), and G11=x/2. Its proposed k2=(1,-i kappa,0,0) gives G k2=(2(1-x),-i sqrt(2x(1-x)),0,0), nonzero for 0<x<1. At x=1/2 the residual is (1,-i/sqrt(2),0,0). Therefore the constructed projector and resulting weight operator are wrong. The archived script reports d1=1-x, whereas the corrected operator gives (1-x)(2-5x)/(2-x), equal to -11/124 at x=9/20 instead of 11/20.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 找到 sign 和 kernel-basis 更正摘要，但它们发生在错误之后，不能反推生成时推理已经正确。

- [2026-07-29T16:16:44.978Z — claude_visible_thinking](original/M06-WHGAP-main-c5b96aec.jsonl.readable.md) — source line 1414; recorded role: posthoc_only.
- [2026-07-30T02:28:57.870Z — claude_visible_thinking](original/M06-WHGAP-main-c5b96aec.jsonl.readable.md) — source line 1878; recorded role: posthoc_only.

## Original materials

- [M01: whgap_p6b_v2_isotropic.py](original/M01-whgap_p6b_v2_isotropic.py "tools/whgap_p6b_v2_isotropic.py")
  - Coverage: Full bundled file; source lines 1–458.
  - Relevant location(s): Preserved isotropic weight-operator script, function weight_operators, lines 92–101
  - Source: `tools/whgap_p6b_v2_isotropic.py`

- [M02: <session-id-redacted>.jsonl](original/M02-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl") · [event data](original/M02-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1408–1420, 1887–1899.
  - Relevant location(s): JSONL lines 1414,1893,1904
  - Source: `tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl`

- [M03: v2_isotropic.json](original/M03-v2_isotropic.json "artifacts/logs_whgap_p6b_20260729/v2_isotropic.json")
  - Coverage: Full bundled file; source lines 1–469.
  - Source: `artifacts/logs_whgap_p6b_20260729/v2_isotropic.json`

- [M04: whgap_p6b_v2_fable.py](original/M04-whgap_p6b_v2_fable.py "tools/whgap_p6b_v2_fable.py")
  - Coverage: Full bundled file; source lines 1–173.
  - Source: `tools/whgap_p6b_v2_fable.py`

- [M05: DATA5_whgap_ledger.md](original/M05-DATA5_whgap_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA5_whgap_ledger.md")
  - Coverage: Full bundled file; source lines 1–18.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA5_whgap_ledger.md`

- [M06: WHGAP-main-c5b96aec.jsonl](original/M06-WHGAP-main-c5b96aec.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl") · [event data](original/M06-WHGAP-main-c5b96aec.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1408–1420, 1872–1884, 4802–4814, 5062–5074.
  - Relevant location(s): lines 1414; lines 1878
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl`
