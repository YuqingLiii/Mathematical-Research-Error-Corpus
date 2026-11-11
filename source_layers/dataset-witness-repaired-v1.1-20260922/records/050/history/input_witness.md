# Record 050 — Finite-dimensional Grothendieck bounds

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 等号面支撑核至少为 28 维，而非此前的 12 维，因此算子秩上界严格改进为 746,797。

**Recorded location:** Assistant message, 2026-08-29T02:46:52.613Z; transcript lines2965–2970.

**Context (annotation, not a source quotation):** The assistant promoted a pre-projection equality-space dimension to a bound on the retained746825 coordinates.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Projection can kill directions; independence before projection does not imply independence afterward.

### Argument or calculation

Of the28 old directions,16 degree-3/4 Walsh directions are individually zero on all retained coordinates. The surviving image has rank12: a retained12-by-12 minor has determinant -120231596497305600, and the16 zero directions give the matching upper bound. Therefore the supported kernel bound is at least12, giving rank<=746825-12=746813; the claimed746825-28=746797 does not follow.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: 01a04050-2c65-7022-8844-6319c2da0799.md](original/M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md "research-graph/audit-bundles/2026-09-18/process-audit-v2/transcripts/01a04050-2c65-7022-8844-6319c2da0799.md")
  - Coverage: Selected text ranges; source lines 2907–3010, 5997–6098.
  - Relevant location(s): lines 2947-2970 and 6037-6058
  - Source: `research-graph/audit-bundles/2026-09-18/process-audit-v2/transcripts/01a04050-2c65-7022-8844-6319c2da0799.md`

- [M02: h4_degree4_equality_restriction_rank.py](original/M02-h4_degree4_equality_restriction_rank.py "research-graph/grothendieck-d4/tools/h4_degree4_equality_restriction_rank.py")
  - Coverage: Full bundled file; source lines 1–127.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/tools/h4_degree4_equality_restriction_rank.py`

- [M03: h4_effective_equality_rank_checker.py](original/M03-h4_effective_equality_rank_checker.py "research-graph/grothendieck-d4/tools/h4_effective_equality_rank_checker.py")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/tools/h4_effective_equality_rank_checker.py`

- [M04: d4-effective-equality-rank-certificate-20260830.json](original/M04-d4-effective-equality-rank-certificate-20260830.json "research-graph/grothendieck-d4/artifacts/certificates/d4-effective-equality-rank-certificate-20260830.json")
  - Coverage: Full bundled file; source lines 1–52.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/artifacts/certificates/d4-effective-equality-rank-certificate-20260830.json`

- [M05: d4-effective-equality-rank-checker-output-20260830.json](original/M05-d4-effective-equality-rank-checker-output-20260830.json "research-graph/grothendieck-d4/artifacts/d4-effective-equality-rank-checker-output-20260830.json")
  - Coverage: Full bundled file; source lines 1–30.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/artifacts/d4-effective-equality-rank-checker-output-20260830.json`

- [M06: GROTHD4.degree4.equality-rank.yaml](original/M06-GROTHD4.degree4.equality-rank.yaml "research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml")
  - Coverage: Full bundled file; source lines 1–63.
  - Source: `research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml`

- [M07: d4_n1_300x300.mat.degree4_equality_restriction_rank.json](original/M07-d4_n1_300x300.mat.degree4_equality_restriction_rank.json "research-graph/grothendieck-d4/artifacts/replay/h4_fd4_next_stage_bundle/d4_n1_300x300.mat.degree4_equality_restriction_rank.json")
  - Coverage: Full bundled file; source lines 1.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/artifacts/replay/h4_fd4_next_stage_bundle/d4_n1_300x300.mat.degree4_equality_restriction_rank.json`

- [M08: d4-sos-symmetry-20260830.md](original/M08-d4-sos-symmetry-20260830.md "research-graph/grothendieck-d4/artifacts/d4-sos-symmetry-20260830.md")
  - Coverage: Full bundled file; source lines 1–653.
  - Relevant location(s): Referenced by research-graph/grothendieck-d4/proof-dag/nodes/GROTHD4.degree4.equality-rank.yaml
  - Source: `research-graph/grothendieck-d4/artifacts/d4-sos-symmetry-20260830.md`
