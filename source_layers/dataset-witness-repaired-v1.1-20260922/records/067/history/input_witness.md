# Record 067 — Optimal circuit distance of the Gross code

**Review status:** `source_or_fixture_check_pending`.

Explicit supports and fault counts are recovered, but final self-contained publication needs the corresponding Gross parity matrices and raw candidate schedule alongside this record to independently check logical nontriviality.

## Original statement and context

> * weight-≤10 configurations from the weight-12 pool: **0** in both sectors.
> 
> [Excerpt break]
> 
> 1. **`d_eff = 11` is not certified.** Only the weight-12-pool disqualifier is clean. Uncovered:
>    `|gamma| <= 10` arising from weight-14 logicals, or from overlapping residual configurations
>    (`Σ|E_i| = |V| + 2m`, `m >= 1`). Weight-13 is now **provably empty** (§2, even weight). Closing
>    this is exactly the campaign's 990-slot SAT machinery, per sector.

**Recorded location:** Candidate-search report dated 23 August 2026, section 6 audit and section 6.2(1), lines 177 and 185–188.

**Context (annotation, not a source quotation):** The model explicitly kept its proposed schedule as a candidate, not a proved distance-12 construction. The erroneous part is the zero-count audit and the assertion that all weight-12-pool distance-at-most-10 mechanisms had been excluded.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The filter tested only two of four gain-positive residual shapes. In particular, a four-suffix with one qubit outside the target logical support can still give a positive gain after cancellation by a singleton. Requiring each hook to fit entirely inside the target support misses such configurations.

### Argument or calculation

The same candidate admits target support V={1,3,7,11,12,14,72,73,74,77,78,80}. Use check 66's four-suffix {78,12,141,72}, check 2's two-suffix {77,80}, and eight singleton faults {1,3,7,11,14,73,74,141}. Their symmetric difference is exactly V; qubit 141 cancels. The total cost is 1+1+8=10, not more than 10. The raw order for check 66 is (68,67,78,12,141,72) at times (5,8,9,11,12,32); check 2's last two times are (12,32). The archived verifier checks V∈ker H_Z and V∉rowspace H_X and finds 72 such witnesses in each sector. The effective-distance audit is false; no false completed-root claim is attributed.

Scope: computation_false.


### Archived review excerpt

> `V ∈ ker H_Z`, `V ∉ rowspace(H_X)`, `|V| = 12`, `⊕(residual supports) = V`, and counts the faults
> one by one: **144 / 144 assertions pass.** The smallest witness, in full:
> 
> ```
> Z-memory, |V| = 12, 10 faults
>   V          = {1, 3, 7, 11, 12, 14, 72, 73, 74, 77, 78, 80}
>   hook       check 66, 4-suffix, qubits {78, 12, 141, 72}   times (9, 11, 12, 32)
>              (check 66 full CNOT order 68,67,78,12,141,72 at times 5,8,9,11,12,32)
>   hook       check  2, 2-suffix, qubits {77, 80}            times (12, 32)
>   singletons {1, 3, 7, 11, 14, 73, 74, 141}                 (8 of them)
> ```
> 
> `|V ∩ D| = 5`, `|D \ V| = 1`, so `cost = 2 + (12−5) + 1 = 10`. The X-memory witness has the same
> shape (check 18's 4-suffix + check 26's 2-suffix + 8 singletons).
> 
> ### 1.3 The witnesses are not an artefact of the residual presentation
> 
> The campaign's certified machinery uses the **360-column** extended code with [SBB26]'s three
> 
> [Excerpt break]
> 
> complete list of gain-positive shapes is:
> 
> | shape | residuals | gain | tested by wave 37? |
> |---|---|---|---|
> | `{i4,i5,i6} ⊆ V` (3-suffix) | 1 | 2 | **yes** |
> | `{i5,i6} ⊆ V` (2-suffix) | 1 | 1 | **yes** |
> | 4-suffix `{i3,i4,i5,i6}` with exactly 3 in `V` ≡ `{i1,i2} ⊆ V Δ supp(a)` (**2-prefix**) | 1 | 1 | **NO** |
> | `{i2,i3,i4} ⊆ V` (2-suffix ⊕ 5-suffix) | 2 | 1 | **NO** |
> 
> `d_eff <= 10` in this stratum iff some `V` carries total gain `>= 2`. Wave 37's `hunt.dext_le10`
> implemented only rows 1–2 — its own comment, *"no longer suffix can fit"*, is true but irrelevant:
> the missing shapes do not need the suffix to fit inside `V`. Measured on the candidate:
> 
> | sector | 3-suffix-in-`V` | 2-suffix-in-`V` | **2-prefix-in-`V`** | disjoint gain-1 pairs |
> |---|---|---|---|---|
> | Z-memory | 0 | 144 | **888** | **132** |
> | X-memory | 0 | 360 | **456** | **84** |
> | `M_cand` (either sector) | 0 | 360 | 360 | **0** |

## Original materials

- [M01: circdist_dstar_hunt1_20260823.md](original/M01-circdist_dstar_hunt1_20260823.md "research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md")
  - Coverage: Full bundled file; source lines 1–247.
  - Relevant location(s): lines 177, 185–188; hunt1 §0、§6 审计行、§6.2 第 1 项；hunt2 §0、§1.4；hunt3 §3.2；Workflow circdist-c5-wave37-serial（会话 9cc32a4a，2026-08-26T00:29:09Z）; #5,6,6.2; #0,#6,#6.2; ; Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md`

- [M02: circdist_dstar_hunt2_20260823.md](original/M02-circdist_dstar_hunt2_20260823.md "research-graph/circdist/artifacts/circdist_dstar_hunt2_20260823.md")
  - Coverage: Full bundled file; source lines 1–372.
  - Relevant location(s): lines 103–120, 131–148; #1.4; #0,#1.4; ; Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt2_20260823.md`

- [M03: circdist_dstar_hunt3_20260828.md](original/M03-circdist_dstar_hunt3_20260828.md "research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md")
  - Coverage: Full bundled file; source lines 1–678.
  - Relevant location(s): #3.2; Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md`

- [M04: circdist_sbbcert_review_20260820.md](original/M04-circdist_sbbcert_review_20260820.md "artifacts/circdist_sbbcert_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–580.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md
  - Source: `artifacts/circdist_sbbcert_review_20260820.md`

- [M05: tiled_gapcand_32.json](original/M05-tiled_gapcand_32.json "research-graph/artifacts/logs_circdist_dstar_hunt1_20260823/tiled_gapcand_32.json")
  - Coverage: Full bundled file; source lines 1.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md
  - Source: `research-graph/artifacts/logs_circdist_dstar_hunt1_20260823/tiled_gapcand_32.json`

- [M06: circdist_dstar_hunt1_20260823.md](original/M06-circdist_dstar_hunt1_20260823.md "research-graph/artifacts/circdist_dstar_hunt1_20260823.md")
  - Coverage: Full bundled file; source lines 1–247.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt2_20260823.md
  - Source: `research-graph/artifacts/circdist_dstar_hunt1_20260823.md`

- [M07: SCHEDULER.yaml](original/M07-SCHEDULER.yaml "research-graph/operations/circdist/SCHEDULER.yaml")
  - Coverage: Full bundled file; source lines 1–5252.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/operations/circdist/SCHEDULER.yaml`

- [M08: CIRCDIST_PROBLEMS.md](original/M08-CIRCDIST_PROBLEMS.md "research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`

- [M09: CIRCDIST.gross.yaml](original/M09-CIRCDIST.gross.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml")
  - Coverage: Full bundled file; source lines 1–1882.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml`

- [M10: CIRCDIST.gross.dext-cap.yaml](original/M10-CIRCDIST.gross.dext-cap.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.dext-cap.yaml")
  - Coverage: Full bundled file; source lines 1–82.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.dext-cap.yaml`

- [M11: CIRCDIST.lift.iff.yaml](original/M11-CIRCDIST.lift.iff.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`

- [M12: proof_dag_check.py](original/M12-proof_dag_check.py "tools/proof_dag_check.py")
  - Coverage: Full bundled file; source lines 1–930.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `tools/proof_dag_check.py`

- [M13: evidence_closure_check.py](original/M13-evidence_closure_check.py "research-graph/tools/evidence_closure_check.py")
  - Coverage: Full bundled file; source lines 1–75.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md
  - Source: `research-graph/tools/evidence_closure_check.py`
