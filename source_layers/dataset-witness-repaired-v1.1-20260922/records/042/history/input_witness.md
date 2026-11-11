# Record 042 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> \Q\bigl(\kSum_{\Zq,t,N}\bigr)\;=\;\Omega_k\!\left(\sqrt N\, q^{1/6}\right)
> \qquad\text{for all } q\ \text{up to}\ \Theta_k(N).

**Recorded location:** Full-manuscript Write event, 2026-07-17T20:31:31.554Z; inherited-floor theorem.

**Context (annotation, not a source quotation):** The displayed 'in particular' conclusion ranges over all small q, although the preceding construction has a sufficiently-large-alphabet condition.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

### Argument or calculation

Set k=3, q=3, t=0, N>=7. Among N residues in Z3, some residue a occurs at least three times. Their sum is3a=0 mod3, so every input is a YES instance and Q=0. This contradicts a positive Omega(sqrt(N)*3^(1/6)) lower bound stated for all q up to a linear ceiling. The counterexample does not refute the preceding theorem restricted by q>=(k-1)(kK+k+2).

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理明确提到 q 的下界条件，正文较宽的参数窗口没有保留它。可以定位条件丢失，但无法据此证明整段推导正确或判定心理/实现层面的原因。

- [2026-07-17T20:02:43.380Z — claude_visible_thinking](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md) — source line 550; recorded role: generation.

## Original materials

- [M01: KSUM-main-b5fea9c2.jsonl](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M01-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 544–556, 563–576, 1485–1497.
  - Relevant location(s): JSONL line 569 (exact full-manuscript Write containing the overbroad every-q theorem sentence); 569; 569 (2026-07-17T20:31:31.554Z); 1491 (2026-07-19T17:17:00.237Z); lines 550; lines 569
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M02: DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
