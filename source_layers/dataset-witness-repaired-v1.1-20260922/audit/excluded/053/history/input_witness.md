# Record 053 — Finite-dimensional Grothendieck bounds

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> "natural rank-4 Gram point is an extreme non-cut elliptope "
> "point and therefore does not itself extend to the degree-4 "
> "generalized elliptope"

**Recorded location:** Original complete-isotypic export script, lines2617–2628.

**Context (annotation, not a source quotation):** The exported block is named elliptope_lemma_external_input but labels the claim PROVED_BY_USER_EXACT_MINOR.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The retained exact-minor checker establishes a rank condition, while the non-extension conclusion additionally requires an external theorem that the export does not prove or bind.

### Argument or calculation

The supplied minor det=327892164673536-146637833895936*sqrt(5) is nonzero, establishing rank(P o P)=10 for the relevant Gram matrix. The checker ends at that rank result. The subsequent implication from an extreme non-cut elliptope point to non-extension to the degree-four generalized elliptope is serialized as an external input, without a bound proof or citation in this artifact. Thus the artifact is not a self-contained proof of the claimed non-extension. No counterexample to the non-extension theorem is asserted.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: h4_complete_K_isotypic.py](original/M01-h4_complete_K_isotypic.py "research-graph/grothendieck-d4/tools/bootstrap/h4_complete_K_isotypic.py")
  - Coverage: Full bundled file; source lines 1–2773.
  - Relevant location(s): lines 2617-2628
  - Source: `research-graph/grothendieck-d4/tools/bootstrap/h4_complete_K_isotypic.py`

- [M02: h4_hadamard_square_rank.py](original/M02-h4_hadamard_square_rank.py "research-graph/grothendieck-d4/tools/bootstrap/h4_hadamard_square_rank.py")
  - Coverage: Full bundled file; source lines 1–61.
  - Source: `research-graph/grothendieck-d4/tools/bootstrap/h4_hadamard_square_rank.py`
