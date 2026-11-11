# Record 019 — Werner–Holevo zero-capacity boundary

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> class ExtensionSDP:
>     def __init__(self) -> None:
>         self.rho = cp.Variable((SYM_DIM, SYM_DIM), symmetric=True, name="rho")
>         self.t = cp.Variable(name="t")
>         self.x = cp.Parameter(name="x")
>         self.eta = V @ self.rho @ V.T

**Recorded location:** Semidefinite-program script creation, 2026-07-28T22:15:31.150Z, JSONL line 130

**Context (annotation, not a source quotation):** V is the isometry onto A tensor Sym^2(B), of dimension 3 times 6 = 18. The frozen task asked for an extension invariant under swapping two qutrit B systems, not necessarily supported only in their symmetric subspace.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

### Argument or calculation

Let v=(|01>-|10>)/sqrt(2) and X=|0><0|_A tensor |v><v|. X is positive semidefinite and obeys S X S=X because Sv=-v. It is therefore swap-invariant, but its support lies entirely in the antisymmetric B sector and cannot be written V rho V^T. In the qutrit case the omitted block has dimension 3 times 3 = 9. The code solves a restricted feasibility problem, so its infeasibility cannot certify the original criterion.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: WHGAP-P1-019faab6.jsonl](original/M01-WHGAP-P1-019faab6.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P1-019faab6.jsonl") · [event data](original/M01-WHGAP-P1-019faab6.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 124–137.
  - Relevant location(s): Semidefinite-program script creation, 2026-07-28T22:15:31.150Z, JSONL line 130; JSONL line 130 (exact script-creation patch); 130; 130 (2026-07-28T22:15:31.150Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P1-019faab6.jsonl`

- [M02: whgap_p1_review_20260728.md](original/M02-whgap_p1_review_20260728.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md")
  - Coverage: Full bundled file; source lines 1–281.
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md`

- [M03: WHGAP-main-c5b96aec.jsonl](original/M03-WHGAP-main-c5b96aec.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl") · [event data](original/M03-WHGAP-main-c5b96aec.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 286–298.
  - Relevant location(s): 292 and :298
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl`

- [M04: whgap_p1_review_20260728.md](original/M04-whgap_p1_review_20260728.md "artifacts/whgap_p1_review_20260728.md")
  - Coverage: Full bundled file; source lines 1–281.
  - Source: `artifacts/whgap_p1_review_20260728.md`

- [M05: whgap_independent_review.py](original/M05-whgap_independent_review.py "artifacts/logs_whgap_review_20260728/whgap_independent_review.py")
  - Coverage: Full bundled file; source lines 1–623.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_independent_review.py`

- [M06: whgap_full_sdp_crosscheck.py](original/M06-whgap_full_sdp_crosscheck.py "artifacts/logs_whgap_review_20260728/whgap_full_sdp_crosscheck.py")
  - Coverage: Full bundled file; source lines 1–124.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_full_sdp_crosscheck.py`

- [M07: whgap_independent_results.json](original/M07-whgap_independent_results.json "artifacts/logs_whgap_review_20260728/whgap_independent_results.json")
  - Coverage: Full bundled file; source lines 1–733.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_independent_results.json`

- [M08: whgap_support_margin_tolerance.log](original/M08-whgap_support_margin_tolerance.log "artifacts/logs_whgap_review_20260728/whgap_support_margin_tolerance.log")
  - Coverage: Full bundled file; source lines 1–35.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_support_margin_tolerance.log`

- [M09: whgap_support_margin.py](original/M09-whgap_support_margin.py "artifacts/logs_whgap_review_20260728/whgap_support_margin.py")
  - Coverage: Full bundled file; source lines 1–196.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_support_margin.py`

- [M10: whgap_proposer_reproduction.py](original/M10-whgap_proposer_reproduction.py "artifacts/logs_whgap_review_20260728/whgap_proposer_reproduction.py")
  - Coverage: Full bundled file; source lines 1–52.
  - Relevant location(s): Referenced by paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/artifacts/whgap/whgap_p1_review_20260728.md; Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/whgap_proposer_reproduction.py`

- [M11: SHA256SUMS.txt](original/M11-SHA256SUMS.txt "artifacts/logs_whgap_20260728/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–10.
  - Relevant location(s): Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_20260728/SHA256SUMS.txt`

- [M12: SHA256SUMS.txt](original/M12-SHA256SUMS.txt "artifacts/logs_whgap_review_20260728/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–30.
  - Relevant location(s): Referenced by artifacts/whgap_p1_review_20260728.md
  - Source: `artifacts/logs_whgap_review_20260728/SHA256SUMS.txt`
