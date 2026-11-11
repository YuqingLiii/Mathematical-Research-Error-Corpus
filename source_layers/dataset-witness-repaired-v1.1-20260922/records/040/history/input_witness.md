# Record 040 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> the relabeling is an input-independent unitary on the value register applied around each query, so one query to either oracle simulates one query to the other.

**Recorded location:** Manuscript Edit event, 2026-07-17T21:36:50.131Z, query-model paragraph.

**Context (annotation, not a source quotation):** The manuscript asserted exact one-query equivalence for arbitrary per-symbol bijections in the XOR oracle O_x|i,b>=|i,b XOR x_i>.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Arbitrary bijections of symbol labels need not respect XOR translations, so they cannot generally be implemented by the asserted fixed conjugation around a single oracle call.

### Argument or calculation

Take three-bit symbols and a bijection phi that swaps 1 and 2 and fixes 0,3,4,5,6,7. Fixed before/after value-register unitaries implementing every relabeled oracle, with phi(0)=0, would conjugate X_a to X_phi(a), where X_a|b>=|b XOR a>. Since X_a X_b=X_(a XOR b), this requires phi(a XOR b)=phi(a) XOR phi(b). But phi(1 XOR 4)=phi(5)=5, whereas phi(1) XOR phi(4)=2 XOR 4=6. Querying into an ancilla, applying phi, updating the response, and uncomputing uses two oracle calls; constant-factor asymptotic transfers may survive.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 先考虑 compute-copy-uncompute 的两次查询顾虑，随后明确否定该顾虑并采用一查询等价；错误不是仅在最后文本中出现。

- [2026-07-17T21:36:26.191Z — claude_visible_thinking](original/M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md) — source line 101; recorded role: generation.

## Original materials

- [M01: KSUM-agent-a9938705d211bef32.jsonl](original/M01-KSUM-agent-a9938705d211bef32.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-a9938705d211bef32.jsonl") · [event data](original/M01-KSUM-agent-a9938705d211bef32.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 95–118.
  - Relevant location(s): JSONL lines 101 (plaintext thinking) and 111 (exact Edit); 101 and :111; 111 (2026-07-17T21:36:50.131Z); lines 101; lines 111
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-a9938705d211bef32.jsonl`

- [M02: KSUM-main-b5fea9c2.jsonl](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 627–639.
  - Relevant location(s): 633
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M03: DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
