# Record 012 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> $$
> \boxed{
> \sum \theta^2K^{(4)}_\theta
> =
> 7149371020340881916998112.
> }
> \tag{32}

**Recorded location:** round-51-response.md, lines 681–687

**Context (annotation, not a source quotation):** K_theta^(4) is the exact support count in a saved critical scan with 150150 distinct theta values. The excerpt reports its second-moment checksum.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The printed checksum differs from exact summation of the archived scan.

### Argument or calculation

Parsing the archived rows as (theta,K_theta) and evaluating sum(theta*theta*K_theta) using integers gives 7149371020340889916998112. The printed integer is 7149371020340881916998112, smaller by 8000000000. A reproducible check is: rows={int(t):int(k) for t,k in re.findall(r"^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$",scan,re.M)}; assert len(rows)==150150; sum(t*t*k for t,k in rows.items()). The scan must accompany this record as a verification fixture.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-51-response.md](original/M01-round-51-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-51-response.md")
  - Coverage: Full bundled file; source lines 1–1226.
  - Relevant location(s): round-51-response.md, lines 681–687; lines 681-687
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-51-response.md`

- [M02: round51-critical-full-scan.txt](original/M02-round51-critical-full-scan.txt "holevo-full-size/work/round51-critical-full-scan.txt")
  - Coverage: Full bundled file; source lines 1–150151.
  - Source: `holevo-full-size/work/round51-critical-full-scan.txt`

- [M03: concentrated_audit_3_rounds_43_58.md](original/M03-concentrated_audit_3_rounds_43_58.md "holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md")
  - Coverage: Full bundled file; source lines 1–1348.
  - Relevant location(s): package F finding for M18
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md`

- [M04: 03_r043_r058_finite_slope_foundation_CORE.md](original/M04-03_r043_r058_finite_slope_foundation_CORE.md "holevo-full-size/central-audit-2026-09-18/generated/03_r043_r058_finite_slope_foundation_CORE.md")
  - Coverage: Full bundled file; source lines 1–24691.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/generated/03_r043_r058_finite_slope_foundation_CORE.md`

- [M05: MASTER_AUDIT_PROTOCOL.md](original/M05-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M06: BASELINE.md](original/M06-BASELINE.md "holevo-full-size/central-audit-2026-09-18/BASELINE.md")
  - Coverage: Full bundled file; source lines 1–89.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/BASELINE.md`

- [M07: verify_round43_translation.py](original/M07-verify_round43_translation.py "holevo-full-size/work/verify_round43_translation.py")
  - Coverage: Full bundled file; source lines 1–178.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round43_translation.py`

- [M08: verify_round43_web_response.py](original/M08-verify_round43_web_response.py "holevo-full-size/work/verify_round43_web_response.py")
  - Coverage: Full bundled file; source lines 1–313.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round43_web_response.py`

- [M09: verify_round44_candidate.py](original/M09-verify_round44_candidate.py "holevo-full-size/work/verify_round44_candidate.py")
  - Coverage: Full bundled file; source lines 1–77.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round44_candidate.py`

- [M10: verify_round44_web_response.py](original/M10-verify_round44_web_response.py "holevo-full-size/work/verify_round44_web_response.py")
  - Coverage: Full bundled file; source lines 1–152.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round44_web_response.py`

- [M11: enumerate_round45_matchings.py](original/M11-enumerate_round45_matchings.py "holevo-full-size/work/enumerate_round45_matchings.py")
  - Coverage: Full bundled file; source lines 1–101.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round45_matchings.py`

- [M12: verify_round45_web_response.py](original/M12-verify_round45_web_response.py "holevo-full-size/work/verify_round45_web_response.py")
  - Coverage: Full bundled file; source lines 1–223.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round45_web_response.py`

- [M13: enumerate_round46_one_defect.py](original/M13-enumerate_round46_one_defect.py "holevo-full-size/work/enumerate_round46_one_defect.py")
  - Coverage: Full bundled file; source lines 1–76.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round46_one_defect.py`

- [M14: verify_round46_web_response.py](original/M14-verify_round46_web_response.py "holevo-full-size/work/verify_round46_web_response.py")
  - Coverage: Full bundled file; source lines 1–256.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round46_web_response.py`

- [M15: enumerate_round47_ratio_two.py](original/M15-enumerate_round47_ratio_two.py "holevo-full-size/work/enumerate_round47_ratio_two.py")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round47_ratio_two.py`

- [M16: verify_round47_web_response.py](original/M16-verify_round47_web_response.py "holevo-full-size/work/verify_round47_web_response.py")
  - Coverage: Full bundled file; source lines 1–177.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round47_web_response.py`

- [M17: enumerate_round48_kappa_frontier.py](original/M17-enumerate_round48_kappa_frontier.py "holevo-full-size/work/enumerate_round48_kappa_frontier.py")
  - Coverage: Full bundled file; source lines 1–83.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round48_kappa_frontier.py`

- [M18: verify_round48_web_response.py](original/M18-verify_round48_web_response.py "holevo-full-size/work/verify_round48_web_response.py")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round48_web_response.py`

- [M19: verify_round49_frontier.cpp](original/M19-verify_round49_frontier.cpp "holevo-full-size/work/verify_round49_frontier.cpp")
  - Coverage: Full bundled file; source lines 1–296.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round49_frontier.cpp`

- [M20: verify_round49_web_response.py](original/M20-verify_round49_web_response.py "holevo-full-size/work/verify_round49_web_response.py")
  - Coverage: Full bundled file; source lines 1–105.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round49_web_response.py`

- [M21: enumerate_round50_three_ratio.cpp](original/M21-enumerate_round50_three_ratio.cpp "holevo-full-size/work/enumerate_round50_three_ratio.cpp")
  - Coverage: Full bundled file; source lines 1–248.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round50_three_ratio.cpp`

- [M22: verify_round50_pre_send.py](original/M22-verify_round50_pre_send.py "holevo-full-size/work/verify_round50_pre_send.py")
  - Coverage: Full bundled file; source lines 1–78.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round50_pre_send.py`

- [M23: enumerate_round51_four_ratio.cpp](original/M23-enumerate_round51_four_ratio.cpp "holevo-full-size/work/enumerate_round51_four_ratio.cpp")
  - Coverage: Full bundled file; source lines 1–281.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round51_four_ratio.cpp`

- [M24: verify_round51_low_collision.cpp](original/M24-verify_round51_low_collision.cpp "holevo-full-size/work/verify_round51_low_collision.cpp")
  - Coverage: Full bundled file; source lines 1–299.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round51_low_collision.cpp`

- [M25: verify_round51_web_response.py](original/M25-verify_round51_web_response.py "holevo-full-size/work/verify_round51_web_response.py")
  - Coverage: Full bundled file; source lines 1–238.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round51_web_response.py`

- [M26: verify_round52_laurent.cpp](original/M26-verify_round52_laurent.cpp "holevo-full-size/work/verify_round52_laurent.cpp")
  - Coverage: Full bundled file; source lines 1–475.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round52_laurent.cpp`

- [M27: verify_round52_web_response.py](original/M27-verify_round52_web_response.py "holevo-full-size/work/verify_round52_web_response.py")
  - Coverage: Full bundled file; source lines 1–243.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round52_web_response.py`

- [M28: verify_round53_web_response.py](original/M28-verify_round53_web_response.py "holevo-full-size/work/verify_round53_web_response.py")
  - Coverage: Full bundled file; source lines 1–226.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round53_web_response.py`

- [M29: verify_round54_lowfiber.cpp](original/M29-verify_round54_lowfiber.cpp "holevo-full-size/work/verify_round54_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–505.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round54_lowfiber.cpp`

- [M30: verify_round55_lowfiber.cpp](original/M30-verify_round55_lowfiber.cpp "holevo-full-size/work/verify_round55_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–512.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round55_lowfiber.cpp`

- [M31: verify_round56_lowfiber.cpp](original/M31-verify_round56_lowfiber.cpp "holevo-full-size/work/verify_round56_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–512.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round56_lowfiber.cpp`

- [M32: verify_round57_lowfiber.cpp](original/M32-verify_round57_lowfiber.cpp "holevo-full-size/work/verify_round57_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–493.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round57_lowfiber.cpp`

- [M33: verify_round58_lowfiber.cpp](original/M33-verify_round58_lowfiber.cpp "holevo-full-size/work/verify_round58_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–594.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round58_lowfiber.cpp`

- [M34: round58_size2_merge.cpp](original/M34-round58_size2_merge.cpp "holevo-full-size/work/round58_bundle/round58_size2_merge.cpp")
  - Coverage: Full bundled file; source lines 1–17.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round58_bundle/round58_size2_merge.cpp`

- [M35: round58_size2_merge_detail.cpp](original/M35-round58_size2_merge_detail.cpp "holevo-full-size/work/round58_bundle/round58_size2_merge_detail.cpp")
  - Coverage: Full bundled file; source lines 1–19.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round58_bundle/round58_size2_merge_detail.cpp`

- [M36: round58_response.md](original/M36-round58_response.md "holevo-full-size/work/round59_bundle/round58_response.md")
  - Coverage: Full bundled file; source lines 1–1058.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round59_bundle/round58_response.md`
