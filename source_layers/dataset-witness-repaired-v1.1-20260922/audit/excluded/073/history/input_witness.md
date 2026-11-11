# Record 073 — Group-orbit Bell matrices

**Review status:** `interpretation_check_pending`.

Original contextual proof is permutation-scoped. Establish that the unqualified node was asserted beyond that context before counting this as an error.

## Original statement and context

> Group averaging maps every feasible top-singular-space balance weight to an invariant feasible weight, and every invariant positive-semidefinite weight on a real isotypic component is represented by Hermitian positive-semidefinite multiplicity blocks over the division algebras R, C, and H.

**Recorded location:** Model clarification, RM-1: preserved previous claim; RM-2: broader orthogonal-action diagnostic.

**Context (annotation, not a source quotation):** The model clarification preserves this previous shorthand claim. Its referenced proof uses row/column permutations; the sentence alone omits that hypothesis.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Constant-diagonal feasibility is preserved by permutations, not by arbitrary orthogonal conjugation. Whether this is an actual scope error depends on which inherited assumptions governed the shorthand node.

### Argument or calculation

Set A=U=V=I_2, H=[[1,1/2],[1/2,1]], and R=(1/sqrt(2))*[[1,1],[1,-1]]. Then R^2=I and RA=AR, while RHR^T=diag(3/2,1/2). The group average (H+RHR^T)/2 has diagonal (5/4,3/4), not (1,1). This refutes an arbitrary-orthogonal-action extension, but does not refute the explicitly permutation-scoped source proof.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: rch-model-clarification-20260907.md](original/M01-rch-model-clarification-20260907.md "research-graph/grothendieck-group-orbit/artifacts/rch-model-clarification-20260907.md")
  - Coverage: Full bundled file; source lines 1–54.
  - Relevant location(s): RM-1 and RM-2, lines 7–37; #RM-1,RM-2; Referenced by research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/rch-model-clarification-20260907.md`

- [M02: rch-invariant-blocks-review-20260907.md](original/M02-rch-invariant-blocks-review-20260907.md "research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md")
  - Coverage: Full bundled file; source lines 1–237.
  - Relevant location(s): RM1 / Hadamard-reflection test; #L199-210
  - Source: `research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md`

- [M03: complete-extremizer-classification-20260829.md](original/M03-complete-extremizer-classification-20260829.md "research-graph/grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md")
  - Coverage: Full bundled file; source lines 1–232.
  - Relevant location(s): #GOC-T6; Referenced by research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md`

- [M04: GROTHORB.rch-reduction.yaml](original/M04-GROTHORB.rch-reduction.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.rch-reduction.yaml")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.rch-reduction.yaml`

- [M05: rch-invariant-blocks-20260907.md](original/M05-rch-invariant-blocks-20260907.md "research-graph/grothendieck-group-orbit/artifacts/rch-invariant-blocks-20260907.md")
  - Coverage: Full bundled file; source lines 1–361.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/rch-invariant-blocks-20260907.md`

- [M06: group-orbit-literature-positioning-20260907.md](original/M06-group-orbit-literature-positioning-20260907.md "research-graph/grothendieck-group-orbit/artifacts/group-orbit-literature-positioning-20260907.md")
  - Coverage: Full bundled file; source lines 1–147.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/reviews/rch-invariant-blocks-review-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/group-orbit-literature-positioning-20260907.md`
