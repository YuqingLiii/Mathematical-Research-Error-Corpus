# Record 074 — Quantum k-sum with small alphabets

**Review status:** `source_or_fixture_check_pending`.

The assigned original locator does not assert the bad uniform-shift route; retrieve the earlier statement or keep this row out of the public confirmed set.

## Original statement and context

The preceding record does not contain a directly bound original quotation; see the review note above.

**Recorded location:** Supplied July 17 write is repaired; proof-history note records an earlier abandoned uniform-shift route.

**Context (annotation, not a source quotation):** The ledger describes a naive shift of all k-2 frozen coordinates that was intended to cover every target. The supplied original write already uses a repaired constant-freeze/window construction and explicitly accounts for gcd(k,q).

**Source binding:** `original_binding_pending` (inherited; not rechecked here).

## Witness

A uniform shift delta of k-2 frozen coordinates moves their sum by (k-2)delta, which is not necessarily surjective modulo q.

### Argument or calculation

For k=4 and q=6, the map delta -> (k-2)delta mod q=2delta mod6 has image {0,2,4}; it cannot move a base target to every residue. This is a valid diagnostic of that naive route, not a refutation of the repaired construction in the currently assigned source.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 旧恢复报告把另一个版本的正确 shift 推理当成错误形成证据。S14 处理 gcd(k,q) 与最后一个 frozen 坐标；待审原文是 common shift 的 gcd(k−2,q) 问题，两者不能混用。

- [2026-07-17T16:03:26.389Z — claude_visible_thinking](original/M01-KSUM-agent-abd75f1f5fe6b3d3b.jsonl.readable.md) — source line 78; recorded role: generation.

## Original materials

- [M01: KSUM-agent-abd75f1f5fe6b3d3b.jsonl](original/M01-KSUM-agent-abd75f1f5fe6b3d3b.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-abd75f1f5fe6b3d3b.jsonl") · [event data](original/M01-KSUM-agent-abd75f1f5fe6b3d3b.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 72–87.
  - Relevant location(s): JSONL lines 78 (plaintext thinking) and 80 (exact Write); 78 and :80; 80 (2026-07-17T16:05:36.388Z); lines 78
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-abd75f1f5fe6b3d3b.jsonl`

- [M02: KSUM-main-b5fea9c2.jsonl](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1485–1497.
  - Relevant location(s): 1491
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M03: DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
