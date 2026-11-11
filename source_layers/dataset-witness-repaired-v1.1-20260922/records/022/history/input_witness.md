# Record 022 — Werner–Holevo zero-capacity boundary

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> [2/5, 1)**. Below the onset the same machinery is *strictly stronger than at n = 1* — at x = 7/20 an
> entangled 2-copy input gives the exact value **1102933/9570000 = 0.115249007…** versus
> d₁(7/20) = 13/132 = 0.098484848… (17 % larger, exact rationals) — so the n = 2 layer is genuinely
> more powerful, yet it dies at exactly the same threshold 2/5.

**Recorded location:** Two-copy analysis artifact, 2026-07-30, lines 22–25

**Context (annotation, not a source quotation):** The raw two-use first-order coherent-information coefficient is compared against a one-use coefficient at x=7/20. Capacity is normalized per channel use. The same sentence also asserts a common zero-crossing threshold.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The comparison omits division by two and the entangled-family threshold is not 2/5.

### Argument or calculation

The comparable two-use coefficient is (1102933/9570000)/2=1102933/19140000, whereas the one-use coefficient is 13/132. Their exact ratio is 84841/145000, approximately 0.5851<1, so the two-use value is about 41.5% lower per use. The entangled family changes sign at the unique root in (0,1) of 19x^4-21x^3-14x^2+28x-8, approximately 0.3912977695<0.4; substitution x=2/5 gives 64/625>0, not a zero.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 把两次信道使用的块量直接同单次量比较，推理已给出 17% stronger 的错误结论，随后输出沿用；事后除以 2 的更正不计作生成时推理。

- [2026-07-30T10:51:43.316Z — claude_visible_thinking](original/M05-WHGAP-main-c5b96aec.jsonl.readable.md) — source line 2441; recorded role: generation.

## Original materials

- [M01: whgap_p13b_n2_layer_20260730.md](original/M01-whgap_p13b_n2_layer_20260730.md "artifacts/whgap_p13b_n2_layer_20260730.md")
  - Coverage: Full bundled file; source lines 1–750.
  - Relevant location(s): Two-copy analysis artifact, 2026-07-30, lines 22–25; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `artifacts/whgap_p13b_n2_layer_20260730.md`

- [M02: <session-id-redacted>.jsonl](original/M02-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl") · [event data](original/M02-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 2435–2447.
  - Relevant location(s): JSONL lines 2441,2485
  - Source: `tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl`

- [M03: whgap_r7_review_20260730.md](original/M03-whgap_r7_review_20260730.md "artifacts/whgap_r7_review_20260730.md")
  - Coverage: Full bundled file; source lines 1–605.
  - Relevant location(s): #MAJOR-1
  - Source: `artifacts/whgap_r7_review_20260730.md`

- [M04: whgap_r7_threshold.py](original/M04-whgap_r7_threshold.py "tools/whgap_r7_threshold.py")
  - Coverage: Full bundled file; source lines 1–50.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_threshold.py`

- [M05: WHGAP-main-c5b96aec.jsonl](original/M05-WHGAP-main-c5b96aec.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl") · [event data](original/M05-WHGAP-main-c5b96aec.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 2435–2450.
  - Relevant location(s): lines 2441; lines 2443
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl`

- [M06: WHGAP_COMMISSION_P13B_20260730.md](original/M06-WHGAP_COMMISSION_P13B_20260730.md "channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P13B_20260730.md")
  - Coverage: Full bundled file; source lines 1–113.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P13B_20260730.md`

- [M07: WHGAP_REVIEW_COMMISSION_R5_20260729.md](original/M07-WHGAP_REVIEW_COMMISSION_R5_20260729.md "channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`

- [M08: PRETASK_RELOAD_PROMPT.md](original/M08-PRETASK_RELOAD_PROMPT.md "research/PRETASK_RELOAD_PROMPT.md")
  - Coverage: Full bundled file; source lines 1–90.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `research/PRETASK_RELOAD_PROMPT.md`

- [M09: DAG_PROTOCOL.md](original/M09-DAG_PROTOCOL.md "research/DAG_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–316.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `research/DAG_PROTOCOL.md`

- [M10: RESEARCH_STRUCTURE_PROTOCOL.md](original/M10-RESEARCH_STRUCTURE_PROTOCOL.md "publish/QuantumOpenQuestion/research/RESEARCH_STRUCTURE_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–179.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `publish/QuantumOpenQuestion/research/RESEARCH_STRUCTURE_PROTOCOL.md`

- [M11: README.md](original/M11-README.md "channel-capacity/werner-holevo-gap/README.md")
  - Coverage: Full bundled file; source lines 1–9.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/README.md`

- [M12: WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M12-WERNER-HOLEVO-GAP_PROOF_DAG.md "channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md")
  - Coverage: Full bundled file; source lines 1–369.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`

- [M13: NODE_INDEX.md](original/M13-NODE_INDEX.md "channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md")
  - Coverage: Full bundled file; source lines 1–129.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md; Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`

- [M14: whgap_p13a_sanity.py](original/M14-whgap_p13a_sanity.py "tools/whgap_p13a_sanity.py")
  - Coverage: Full bundled file; source lines 1–859.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13a_sanity.py`

- [M15: exact_s1.json](original/M15-exact_s1.json "artifacts/logs_whgap_p13b_20260730/exact_s1.json")
  - Coverage: Full bundled file; source lines 1–3129.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/exact_s1.json`

- [M16: SHA256SUMS_p13b.txt](original/M16-SHA256SUMS_p13b.txt "artifacts/logs_whgap_p13b_20260730/SHA256SUMS_p13b.txt")
  - Coverage: Full bundled file; source lines 1–25.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/SHA256SUMS_p13b.txt`

- [M17: whgap_p13b_core.py](original/M17-whgap_p13b_core.py "tools/whgap_p13b_core.py")
  - Coverage: Full bundled file; source lines 1–285.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_core.py`

- [M18: whgap_p13b_exact.py](original/M18-whgap_p13b_exact.py "tools/whgap_p13b_exact.py")
  - Coverage: Full bundled file; source lines 1–292.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_exact.py`

- [M19: exact_s1.log](original/M19-exact_s1.log "artifacts/logs_whgap_p13b_20260730/exact_s1.log")
  - Coverage: Full bundled file; source lines 1–92.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/exact_s1.log`

- [M20: whgap_p13b_interval.py](original/M20-whgap_p13b_interval.py "tools/whgap_p13b_interval.py")
  - Coverage: Full bundled file; source lines 1–70.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_interval.py`

- [M21: whgap_p13b_sweep.py](original/M21-whgap_p13b_sweep.py "tools/whgap_p13b_sweep.py")
  - Coverage: Full bundled file; source lines 1–154.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_sweep.py`

- [M22: sweep_all.json](original/M22-sweep_all.json "artifacts/logs_whgap_p13b_20260730/sweep_all.json")
  - Coverage: Full bundled file; source lines 1–989.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/sweep_all.json`

- [M23: sweep_all.log](original/M23-sweep_all.log "artifacts/logs_whgap_p13b_20260730/sweep_all.log")
  - Coverage: Full bundled file; source lines 1–47.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/sweep_all.log`

- [M24: whgap_p13b_validate.py](original/M24-whgap_p13b_validate.py "tools/whgap_p13b_validate.py")
  - Coverage: Full bundled file; source lines 1–70.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_validate.py`

- [M25: validation.json](original/M25-validation.json "artifacts/logs_whgap_p13b_20260730/validation.json")
  - Coverage: Full bundled file; source lines 1–192.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/validation.json`

- [M26: whgap_p13b_gates.py](original/M26-whgap_p13b_gates.py "tools/whgap_p13b_gates.py")
  - Coverage: Full bundled file; source lines 1–233.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_gates.py`

- [M27: gates.json](original/M27-gates.json "artifacts/logs_whgap_p13b_20260730/gates.json")
  - Coverage: Full bundled file; source lines 1–182.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/gates.json`

- [M28: whgap_p13b_variety.py](original/M28-whgap_p13b_variety.py "tools/whgap_p13b_variety.py")
  - Coverage: Full bundled file; source lines 1–133.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_variety.py`

- [M29: whgap_p13b_s2.py](original/M29-whgap_p13b_s2.py "tools/whgap_p13b_s2.py")
  - Coverage: Full bundled file; source lines 1–157.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_s2.py`

- [M30: interval_certificate.json](original/M30-interval_certificate.json "artifacts/logs_whgap_p13b_20260730/interval_certificate.json")
  - Coverage: Full bundled file; source lines 1–198.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/interval_certificate.json`

- [M31: s2_symbolic.json](original/M31-s2_symbolic.json "artifacts/logs_whgap_p13b_20260730/s2_symbolic.json")
  - Coverage: Full bundled file; source lines 1–383.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/s2_symbolic.json`

- [M32: sweep_F2.json](original/M32-sweep_F2.json "artifacts/logs_whgap_p13b_20260730/sweep_F2.json")
  - Coverage: Full bundled file; source lines 1–260.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/sweep_F2.json`

- [M33: variety.json](original/M33-variety.json "artifacts/logs_whgap_p13b_20260730/variety.json")
  - Coverage: Full bundled file; source lines 1–1995.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/variety.json`

- [M34: f2_condfloor_1e-3.log](original/M34-f2_condfloor_1e-3.log "artifacts/logs_whgap_p13b_20260730/f2_condfloor_1e-3.log")
  - Coverage: Full bundled file; source lines 1–3.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/f2_condfloor_1e-3.log`

- [M35: s2_symbolic.log](original/M35-s2_symbolic.log "artifacts/logs_whgap_p13b_20260730/s2_symbolic.log")
  - Coverage: Full bundled file; source lines 1–31.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/s2_symbolic.log`

- [M36: sweep_F2_recheck.log](original/M36-sweep_F2_recheck.log "artifacts/logs_whgap_p13b_20260730/sweep_F2_recheck.log")
  - Coverage: Full bundled file; source lines 1–14.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/sweep_F2_recheck.log`

- [M37: whgap_p13b_artifact_diagnosis.py](original/M37-whgap_p13b_artifact_diagnosis.py "tools/whgap_p13b_artifact_diagnosis.py")
  - Coverage: Full bundled file; source lines 1–36.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_artifact_diagnosis.py`

- [M38: whgap_p13b_condfloor_probe.py](original/M38-whgap_p13b_condfloor_probe.py "tools/whgap_p13b_condfloor_probe.py")
  - Coverage: Full bundled file; source lines 1–21.
  - Relevant location(s): Referenced by artifacts/whgap_p13b_n2_layer_20260730.md
  - Source: `tools/whgap_p13b_condfloor_probe.py`

- [M39: WHGAP_REVIEW_COMMISSION_R7_20260730.md](original/M39-WHGAP_REVIEW_COMMISSION_R7_20260730.md "channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R7_20260730.md")
  - Coverage: Full bundled file; source lines 1–56.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R7_20260730.md`

- [M40: whgap_r7_s2.py](original/M40-whgap_r7_s2.py "tools/whgap_r7_s2.py")
  - Coverage: Full bundled file; source lines 1–181.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_s2.py`

- [M41: whgap_r7_checks.py](original/M41-whgap_r7_checks.py "tools/whgap_r7_checks.py")
  - Coverage: Full bundled file; source lines 1–323.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_checks.py`

- [M42: whgap_r7_variety.py](original/M42-whgap_r7_variety.py "tools/whgap_r7_variety.py")
  - Coverage: Full bundled file; source lines 1–73.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_variety.py`

- [M43: whgap_r7_exact.py](original/M43-whgap_r7_exact.py "tools/whgap_r7_exact.py")
  - Coverage: Full bundled file; source lines 1–245.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_exact.py`

- [M44: whgap_r7_interval.py](original/M44-whgap_r7_interval.py "tools/whgap_r7_interval.py")
  - Coverage: Full bundled file; source lines 1–94.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `tools/whgap_r7_interval.py`

- [M45: SHA256SUMS_r7.txt](original/M45-SHA256SUMS_r7.txt "artifacts/logs_whgap_p13b_20260730/SHA256SUMS_r7.txt")
  - Coverage: Full bundled file; source lines 1–31.
  - Relevant location(s): Referenced by artifacts/whgap_r7_review_20260730.md
  - Source: `artifacts/logs_whgap_p13b_20260730/SHA256SUMS_r7.txt`
