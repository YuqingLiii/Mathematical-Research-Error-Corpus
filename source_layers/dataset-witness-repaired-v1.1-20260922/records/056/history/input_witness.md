# Record 056 — Group-orbit Bell matrices

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> The proof also gives explicit extremizing vectors: the normalized rows of any
> paired top left/right singular bases.

**Recorded location:** Original balanced-rank theorem draft, GO-T4, lines 66–85.

**Context (annotation, not a source quotation):** The theorem applies to real rectangular matrices with transitive row and column permutation actions and does not exclude the zero matrix.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

### Argument or calculation

Let A be the 1-by-2 zero matrix. The two-element group acts trivially on its one row and swaps the two columns, so both actions are transitive and equivariance holds. The full top left space is R and the full top right space is R^2. Bases spanning these spaces have one and two columns, respectively; there is no pair with a common column count. Every feasible strategy still has the correct optimum value zero, so only the unconditional construction clause fails.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: balanced-rank-theorem-draft-20260829.md](original/M01-balanced-rank-theorem-draft-20260829.md "research-graph/grothendieck-group-orbit/artifacts/balanced-rank-theorem-draft-20260829.md")
  - Coverage: Full bundled file; source lines 1–155.
  - Relevant location(s): GO-T4, lines 66–85; Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/balanced-rank-theorem-draft-20260829.md`

- [M02: spectral-classification-review-20260907.md](original/M02-spectral-classification-review-20260907.md "research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md")
  - Coverage: Full bundled file; source lines 1–364.
  - Relevant location(s): Finding F5
  - Source: `research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md`

- [M03: proof_dag_schema.py](original/M03-proof_dag_schema.py "research-graph/tools/proof_dag_schema.py")
  - Coverage: Full bundled file; source lines 1–910.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/tools/proof_dag_schema.py`

- [M04: complete-extremizer-classification-20260829.md](original/M04-complete-extremizer-classification-20260829.md "research-graph/grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md")
  - Coverage: Full bundled file; source lines 1–232.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md`

- [M05: GROTHORB.spectral-upper.yaml](original/M05-GROTHORB.spectral-upper.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.spectral-upper.yaml")
  - Coverage: Full bundled file; source lines 1–42.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.spectral-upper.yaml`

- [M06: GROTHORB.balanced-criterion.yaml](original/M06-GROTHORB.balanced-criterion.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.balanced-criterion.yaml")
  - Coverage: Full bundled file; source lines 1–43.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.balanced-criterion.yaml`

- [M07: GROTHORB.invariant-projector.yaml](original/M07-GROTHORB.invariant-projector.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.invariant-projector.yaml")
  - Coverage: Full bundled file; source lines 1–42.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.invariant-projector.yaml`

- [M08: GROTHORB.equality-characterization.yaml](original/M08-GROTHORB.equality-characterization.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.equality-characterization.yaml")
  - Coverage: Full bundled file; source lines 1–59.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.equality-characterization.yaml`

- [M09: GROTHORB.transitive-optimum.yaml](original/M09-GROTHORB.transitive-optimum.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.transitive-optimum.yaml")
  - Coverage: Full bundled file; source lines 1–127.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.transitive-optimum.yaml`

- [M10: GROTHORB.extremizer-classification.yaml](original/M10-GROTHORB.extremizer-classification.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.extremizer-classification.yaml")
  - Coverage: Full bundled file; source lines 1–157.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.extremizer-classification.yaml`

- [M11: GROTHORB.counterexample.yaml](original/M11-GROTHORB.counterexample.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.counterexample.yaml")
  - Coverage: Full bundled file; source lines 1–42.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.counterexample.yaml`

- [M12: GROTHORB.noninvariant-extremizer.yaml](original/M12-GROTHORB.noninvariant-extremizer.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.noninvariant-extremizer.yaml")
  - Coverage: Full bundled file; source lines 1–44.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.noninvariant-extremizer.yaml`
