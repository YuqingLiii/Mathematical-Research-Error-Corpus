# Record 057 — Group-orbit Bell matrices

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> For every r>=3 and 0<=lambda<=1/2, the full D_r root projection A_r=WW^T/[4(r-1)], n=2r(r-1), satisfies
>   beta_cl(A_r-lambda I)=2r(2r-1)/3-n*lambda.

**Recorded location:** Registered shift-linear candidate, claim lines1–4; exact D3 envelope dossier, D3-1 and D3-3–D3-4.

**Context (annotation, not a source quotation):** The universal affine formula was registered as a candidate and later retained as refuted. beta_cl(B)=max_{s,t in {−1,+1}^n} s^T B t.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

A competing sign pair outperforms the extrapolated affine branch beyond lambda=1/4.

### Argument or calculation

For r=3 let W have rows(-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),(-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),(0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1), and A=WW^T/8. Take s=(1,1,1,1,-1,1,-1,1,-1,1,-1,1) and t=(-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1). Then s^TAt=8 and s^Tt=4. At lambda=1/2 their value is8-2=6, whereas the claimed formula gives10-12/2=4. One allowed pair already refutes the universal equality; no exhaustive upper-bound enumeration is needed.

Scope: tentative_candidate_refuted.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: GROTHORB.shift-linear-candidate.yaml](original/M01-GROTHORB.shift-linear-candidate.yaml "research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml")
  - Coverage: Full bundled file; source lines 1–57.
  - Relevant location(s): lines 1-4 and 47-53
  - Source: `research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml`

- [M02: d3-classical-envelope-20260907.md](original/M02-d3-classical-envelope-20260907.md "research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-20260907.md")
  - Coverage: Full bundled file; source lines 1–163.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml
  - Source: `research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-20260907.md`

- [M03: d3-envelope-review-20260907.md](original/M03-d3-envelope-review-20260907.md "research-graph/grothendieck-group-orbit/reviews/d3-envelope-review-20260907.md")
  - Coverage: Full bundled file; source lines 1–186.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml
  - Source: `research-graph/grothendieck-group-orbit/reviews/d3-envelope-review-20260907.md`

- [M04: d3-classical-envelope-certificate-20260907.json](original/M04-d3-classical-envelope-certificate-20260907.json "research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-certificate-20260907.json")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml; Referenced by research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-certificate-20260907.json`

- [M05: classical-exploration-summary-20260907.md](original/M05-classical-exploration-summary-20260907.md "research-graph/grothendieck-group-orbit/artifacts/classical-exploration-summary-20260907.md")
  - Coverage: Full bundled file; source lines 1–200.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml
  - Source: `research-graph/grothendieck-group-orbit/artifacts/classical-exploration-summary-20260907.md`

- [M06: classical-family-registration-20260907.md](original/M06-classical-family-registration-20260907.md "research-graph/grothendieck-group-orbit/artifacts/classical-family-registration-20260907.md")
  - Coverage: Full bundled file; source lines 1–142.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml
  - Source: `research-graph/grothendieck-group-orbit/artifacts/classical-family-registration-20260907.md`

- [M07: check_d3_classical_envelope.py](original/M07-check_d3_classical_envelope.py "research-graph/grothendieck-group-orbit/tools/check_d3_classical_envelope.py")
  - Coverage: Full bundled file; source lines 1–177.
  - Relevant location(s): Referenced by research-graph/grothendieck-group-orbit/artifacts/d3-classical-envelope-20260907.md
  - Source: `research-graph/grothendieck-group-orbit/tools/check_d3_classical_envelope.py`
