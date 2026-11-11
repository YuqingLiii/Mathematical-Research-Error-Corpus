# Record 049 — Finite-dimensional Grothendieck bounds

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> \binom{600}{2}\,598=107281800

**Recorded location:** Triangle/hypermetric no-go note, lines114–123.

**Context (annotation, not a source quotation):** The proof note counts index choices with an unordered pair of two distinct vertices and a third distinct vertex.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The displayed integer product is incorrect.

### Argument or calculation

binom(600,2)=600*599/2=179700; multiplying by598 gives107460600, not107281800. The discrepancy is178800. This is a local arithmetic/count-reporting error; it does not by itself invalidate the checker loops or the associated nonnegativity result.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** triangle checker 的短标题不含组合计数算式，无法判定乘法错误的形成阶段。

- [2026-08-31T01:24:17.961Z — codex_reasoning_summary](original/M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.readable.md) — source line 320; recorded role: generation.

## Original materials

- [M01: d4-triangle-hypermetric-no-go-20260830.md](original/M01-d4-triangle-hypermetric-no-go-20260830.md "research-graph/grothendieck-d4/artifacts/d4-triangle-hypermetric-no-go-20260830.md")
  - Coverage: Full bundled file; source lines 1–210.
  - Relevant location(s): lines 114-123; Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.cut.triangle-no-go.yaml
  - Source: `research-graph/grothendieck-d4/artifacts/d4-triangle-hypermetric-no-go-20260830.md`

- [M02: GROTHD4.cut.triangle-no-go.yaml](original/M02-GROTHD4.cut.triangle-no-go.yaml "research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.cut.triangle-no-go.yaml")
  - Coverage: Full bundled file; source lines 1–43.
  - Source: `research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.cut.triangle-no-go.yaml`

- [M03: rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl](original/M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/30/rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl") · [event data](original/M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 309–326.
  - Relevant location(s): lines 320
  - Source: `local-session-archive/2026/08/30/rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl`

- [M04: h4_triangle_hypermetric_no_go_checker.py](original/M04-h4_triangle_hypermetric_no_go_checker.py "research-graph/grothendieck-d4/tools/h4_triangle_hypermetric_no_go_checker.py")
  - Coverage: Full bundled file; source lines 1–200.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/artifacts/d4-triangle-hypermetric-no-go-20260830.md; Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.cut.triangle-no-go.yaml
  - Source: `research-graph/grothendieck-d4/tools/h4_triangle_hypermetric_no_go_checker.py`
