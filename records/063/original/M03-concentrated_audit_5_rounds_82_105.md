Audit completed. The report below stays within the requested scope and word limit.

# 1. Audit receipt

**Package:** `05_r082_r105_global_certificates_II`.

**Attachments examined:** `05_r082_r105_global_certificates_II_CORE(1).md` and `05_r082_r105_global_certificates_II_EVIDENCE(1).zip`. The CORE identifies itself as historical proof-development evidence after the September 7 V7 cutoff.

**Files actually opened/parsed:** the complete CORE; `README.md`, `MASTER_AUDIT_PROTOCOL.md`, `PACKAGE_05_PROMPT.md`, `BASELINE.md`, `05_r082_r105_global_certificates_II_ROUND_INDEX.tsv`, and `MANIFEST.tsv`; every indexed Round 82–105 prompt/response/audit entry present in the ZIP; all 23 supplied `explore_round*_global.cpp` files for R82–102, R104, R105; all 23 `verify_round*_global_budget.py` files and saved arithmetic logs; R102/R103 dispatch and recovery records; R104 staging/pre-audit; and R105 pre-audit. Targeted source-level inspection was deepest for R82, R94, R98, R102/103, R104, and R105.

**Code/checks actually run:** all 352 manifest entries were independently SHA-256/size checked: **352/352 pass**. All 22 arithmetic-verifier scripts from R82–R104 for which the packaged verifier was directly runnable reproduced their saved stdout **byte-for-byte**. I independently recomputed the rearrangement range, denominator sign change, strict coupled rounding, survivors, and cleared margin for representative early/middle/late points R82/300219, R94/300232, R102/300240, R104/300241, and R105/300242; all five matched. I statically checked every supplied C++ source and Python budget verifier for target-theta drift.

**Coverage limit:** I did **not** complete a fresh exhaustive C++ determinant census. A fresh build/run of the self-checking R105 source exceeded the execution window. The packaged R105 budget verifier also requires a compiled binary that the ZIP does not contain. Those exhaustive-rerun claims are therefore `INCOMPLETE` in this audit, not silently accepted.

# 2. Executive verdict

No fatal mathematical defect was found in the load-bearing finite-slope certificate chain within the checks actually performed.

The earliest concrete source defect is Round 82: its C++ enumerator contains a stale active `SUPPORT` array summing to `970332140`, not the actual Round-82 `K=970337664`. The defect does **not** enter the load-bearing census/global merge or exact coupled-support-loss verifier, so it does not invalidate `GenericTheta300219Exclusion` at candidate strength.

Round 98 contains a genuine prompt copy/substitution error in two non-load-bearing size-four row counts; the public response detected and corrected it before using the certificate.

Round 102 is correctly an interruption, not a completed audit receipt. Round 103 supplies the captured public recovery for `theta=300240` while explicitly retaining `CONJECTURED`.

The corrected provenance frontier is therefore: **captured public reconstruction through 300240; local candidates through 300242; earliest missing public response at 300241.** The claimed R104 dispatch itself is `NOT_CHECKED` because the supplied ZIP contains no R104 dispatch-receipt file.

Extending this finite theta frontier by 300241 and 300242 is **not a conceptual advance toward the unrestricted/full-size theorem**.

# 3. Claim ledger

| Source / claim                                  | Dependency                                                                      | Audit action                                                            | Status                                                                                         | Consequence                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| R82–R103 finite-slope packet machinery          | Exact determinant enumeration; canonical `(d6,dr)` matching; support-loss lemma | Source correspondence inspected; range/arithmetic independently checked | `CORRECT_BUT_CONDITIONAL`                                                                      | Supports only displayed twelve-slope ansätze                    |
| R82 `theta=300219` certificate                  | `K,H,M_global`, coupled loss, strict target                                     | Fresh exact arithmetic/range reconstruction                             | `COMPUTATIONALLY_REPRODUCED`; named result `CONJECTURED`                                       | Candidate survives despite stale non-load-bearing C++ `SUPPORT` |
| R94 `theta=300232`                              | Same                                                                            | Fresh range/arithmetic reconstruction                                   | `COMPUTATIONALLY_REPRODUCED`; `CONJECTURED`                                                    | Middle-march representative survives                            |
| R98 raw-size-four vector                        | Prompt values                                                                   | Compared prompt, response, local audit                                  | Two entries `INCORRECT`, corrected result survives                                             | No effect on `K`, size-two stream, `M_global`, or packet bound  |
| R102 `theta=300240` public completion           | Browser final answer                                                            | Examined interruption record                                            | `INCOMPLETE`                                                                                   | R102 alone is not a public audit                                |
| R103 recovery of `theta=300240`                 | Fresh public response + local θ300240 evidence                                  | Receipt/provenance and arithmetic inspected                             | `PROVENANCE_ONLY` + `COMPUTATIONALLY_REPRODUCED`; theorem `CONJECTURED`                        | Restores captured-public frontier through 300240                |
| R104 `theta=300241` certificate                 | Local source/log/verifier                                                       | Fresh range/arithmetic reconstruction                                   | `COMPUTATIONALLY_REPRODUCED`; `CONJECTURED`                                                    | Local candidate only                                            |
| “R104 was dispatched”                           | Missing dispatch receipt                                                        | Manifest/archive search                                                 | `NOT_CHECKED`                                                                                  | Do not count as successful external/public audit                |
| R105 `theta=300242`                             | Local source/log/pre-audit                                                      | Static self-check review + independent arithmetic                       | arithmetic `COMPUTATIONALLY_REPRODUCED`; full binary rerun `INCOMPLETE`; theorem `CONJECTURED` | Local-only endpoint                                             |
| Finite-slope exclusion ⇒ PW10/full-size theorem | Complete reduction from unrestricted problem                                    | Searched package; none supplied                                         | `NOT_CHECKED` / global target `OPEN`                                                           | No global promotion                                             |

# 4. Detailed findings

### F-001 — Medium — stale active Round-82 `SUPPORT` array

**Locator:** `evidence/work/explore_round82_global.cpp:340–347`, used at approximately lines 458–461.

The source's `SUPPORT` array is

`(53624480,67257904,74298900,80378416,...,74298900,67257904,53624480)`

and sums to **970332140**. Round 82's actual formal-support vector sums to **970337664**. Thus the source contains a genuine stale constant.

It is not load-bearing here. The program computes and prints each real `row_support` from the histogram independently; the stale array is used only in `weighted_surviving`. In the archived R82 run every row's exploratory `surviving` value is zero, so `weighted_surviving=0` regardless of those stale multipliers. More importantly, the final coupled certificate comes from `verify_round82_global_budget.py`, using the correct `K`, support minimum, `M_global`, and singleton total. My independent calculation reproduces

`loss<=133183`, `B_coupled=266366`, `N=1012318`, `G=82725646`, margin `2867424128397140>0`.

**Minimal correction:** replace the stale R82 `SUPPORT` array with the actual R82 vector and do not call this source fully theta-self-checking.

### F-002 — Low/Medium — status rhetoric exceeds the retained governance status

Round 82 opens with “`GenericTheta300219Exclusion is proved within the present finite-slope audit context`” but later says the result remains **CONJECTURED**. Its local audit similarly says Round 82 “establishes” a strict lemma. R83–R84 repeat the “proved” formulation, and R82–R101 local audits repeatedly use “establishes”.

The explicit `CONJECTURED` sections prevent an actual status promotion, but “proved”, “establishes”, and unqualified “independently verified” are too strong under the master protocol.

**Minimal correction:** use “computationally reproduced/supports the finite-slope candidate”; reserve “independent theorem verification” for replication outside this proof-development context.

### F-003 — Medium — Round-98 textual substitution corrupted two row counts

The R98 prompt transmitted `H4` rows 3 and 9 as `14,928,318`; the exact value is `14,926,862`. The audit identifies the mechanism: replacing the substring `6862` by the new `8318` accidentally altered digits inside `14926862`.

The global H4 total was already correct, and H4 is not used by the size-two packet certificate. The corrected response retained the correct `K=970338792`, `M_global=1270316`, `B_coupled=308700`, and positive margin. Thus no downstream candidate is invalidated.

### F-004 — High provenance significance — Round 102 cannot count as completed review

The archive explicitly records three progress messages with `end_turn=false`, followed by the maximum-conversation-length interruption; there is no final Round-102 assistant answer. The local audit correctly preserves the local `theta=300240` calculation but does not promote the interrupted output.

Round 103 is a fresh-chat recovery and explicitly calls the result a finite-slope candidate with governance status `CONJECTURED`. Its retained local replication reports the same global counts and says nothing establishes the fixed-channel regularized defect or full-size rate gate.

### F-005 — Medium provenance defect — supplied archive does not contain the claimed R104 dispatch receipt

The CORE has a Round-104 prompt but says `RESPONSE — MISSING FROM LOCAL CORPUS`; its pre-audit still describes `300241` as discovery evidence. The later R105 pre-audit states that R104 had “one verified dispatch” but no response bytes were saved.

However, the ZIP manifest contains `round-104-staging.md` and `work/round-104-prompt.md`, **not** a `round-104-dispatch.md` or equivalent dispatch receipt. The package-specific audit prompt's assertion that a dispatch record is supplied is therefore unsupported by the supplied evidence.

**Minimal correction:** R104 dispatch = `NOT_CHECKED`; R104 public audit = absent. This does **not** move the earliest missing-public-audit frontier earlier than 300241.

### F-006 — Medium coverage/reproducibility gap — R105 verifier is not runnable as packaged

R105 claims a frozen compiled-binary hash and says its verifier binds source, binary, log, and three-run record. The ZIP omits that executable. Running `verify_round105_global_budget.py` therefore stops at `FileNotFoundError` before its internal assertions.

I separately recomputed its exact range, denominator transition, support-loss rounding, survivor tuple and margin, obtaining exactly the archived values `B_coupled=383858`, `(N,G)=(919546,82611594)`, and `2568001366001556>0`.

**Minimal correction:** distinguish “archived hash claim” from “rerunnable packaged binary verification”; the latter is `INCOMPLETE`.

# 5. Dependency/invalidation map

* **F-001 → R82 exploratory weighted/subset diagnostics only.** It does not invalidate the R82 determinant histogram, canonical-key merge, `M_global`, separately computed support-loss arithmetic, or R83–R105.
* **F-002 → wording/status ledger R82–R101.** Replace theorem-sounding prose; mathematical numerical records remain unchanged.
* **F-003 → R98 prompt H4 rows 3 and 9 only.** The response repaired them before the certificate; R99 explicitly inherits the corrected values. No later load-bearing result depends on the erroneous pair.
* **F-004 → R102 provenance only.** R102 is not a completed public audit. R103 independently supplies the public θ300240 recovery, so the completed-public frontier remains 300240.
* **F-005 → R104 provenance.** `GenericTheta300241Exclusion` remains local/`CONJECTURED`; no R104 public response can be claimed.
* **F-006 → R105 fresh reproducibility strength.** Exact arithmetic survives, but a fresh exhaustive/self-checking execution is `INCOMPLETE`.
* **Common inherited dependency:** every `GenericTheta...Exclusion` still depends on the inherited strict-baseline target/four-slack framework. Package 05 does not supply a complete unrestricted reduction; therefore none affects PW10, a fixed-channel regularized defect, or the full-size theorem.

# 6. Computational audit

**Code/object correspondence.** For each deleted row, the C++ program ranges over every nonzero `q=x-y` in `[-12,12]`; for each admissible ordered `(x,y)` it permutes the ten special slope columns over the ten remaining row labels. This corresponds to the claimed determinant assignments. Canonicalization orders the two Laurent monomials and keys them by `(ΔQ6,ΔQr)` plus relative sign, which is sufficient for the physical magnitudes `|1±ζ|`.

**Theta drift.** Every one of the 23 supplied C++ sources contains only its intended current theta literal: 300219, 300221,…,300240,300241,300242. Every corresponding Python budget verifier also contains the intended theta/H pair. R103 correctly has no new local enumerator—it recovers R102's θ300240 result. No forbidden old theta was found in executable theta constants. The exception is F-001's stale R82 `SUPPORT` vector, not its slope constant.

**Ranges/buffers.** I independently exhausted all 286 ten-row subsets for every supplied theta. Every saved `t_min/t_max` matched. The tightest case is θ300242: `[-3727827,3727875]`, still at least **25,573** inside `[-3753400,3753450]`. No range truncation was found.

**Arithmetic/overflow.** Observed `|ΔQr|<=72`, `ΔQ6<=22,479,788`, maximum fiber size `480`, and `|t|<3.73×10^6`; the chosen `int16/int32` fields are safe. Fiber counts use `uint16_t` with an explicit pre-increment overflow guard. Global sums/checksums use 64/128-bit integers. The only floating computation found is in an auxiliary balancing heuristic, not in the load-bearing global match or exact coupled certificate.

**Representative fresh calculations:**

|   Round |      θ | Fresh exact result                                                       |
| ------: | -----: | ------------------------------------------------------------------------ |
|      82 | 300219 | range `-3727551..3727599`; `d=86`; `B=266366`; margin `2867424128397140` |
|      94 | 300232 | range `-3727707..3727755`; `d=91`; `B=237754`; margin `3230300529289204` |
| 102/103 | 300240 | range `-3727803..3727851`; `d=74`; `B=357236`; margin `2727807044033952` |
|     104 | 300241 | range `-3727815..3727863`; `d=98`; `B=203244`; margin `3053715195721792` |
|     105 | 300242 | range `-3727827..3727875`; `d=72`; `B=383858`; margin `2568001366001556` |

The θ300240 prompt itself records the same coupled bound and positive margin.

**Round-by-round status**

|   R |      θ | Evidence                               | Rerun in this audit                                               | Mathematical status |
| --: | -----: | -------------------------------------- | ----------------------------------------------------------------- | ------------------- |
|  82 | 300219 | public + local                         | arithmetic PASS; F-001                                            | `CONJECTURED`       |
|  83 | 300221 | public + local; 300220 support-covered | arithmetic PASS                                                   | `CONJECTURED`       |
|  84 | 300222 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  85 | 300223 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  86 | 300224 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  87 | 300225 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  88 | 300226 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  89 | 300227 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  90 | 300228 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  91 | 300229 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  92 | 300230 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  93 | 300231 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  94 | 300232 | public + local                         | PASS + fresh representative                                       | `CONJECTURED`       |
|  95 | 300233 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  96 | 300234 | public + local                         | PASS; historical verifier constants corrected in response runtime | `CONJECTURED`       |
|  97 | 300235 | public + local                         | PASS                                                              | `CONJECTURED`       |
|  98 | 300236 | public + local                         | PASS; F-003 corrected                                             | `CONJECTURED`       |
|  99 | 300237 | public + local                         | PASS                                                              | `CONJECTURED`       |
| 100 | 300238 | public + local                         | PASS                                                              | `CONJECTURED`       |
| 101 | 300239 | public + local                         | PASS                                                              | `CONJECTURED`       |
| 102 | 300240 | interrupted public + local             | arithmetic PASS; public `INCOMPLETE`                              | `CONJECTURED`       |
| 103 | 300240 | fresh public recovery + local          | θ300240 arithmetic reproduced                                     | `CONJECTURED`       |
| 104 | 300241 | local/pre-audit; response absent       | arithmetic PASS; dispatch `NOT_CHECKED`                           | `CONJECTURED`       |
| 105 | 300242 | local only                             | fresh arithmetic PASS; exhaustive binary rerun `INCOMPLETE`       | `CONJECTURED`       |

# 7. Corrected status ledger

**`VERIFIED_IN_THIS_AUDIT`:** archive manifest integrity; intended theta literals; all exact rearrangement ranges/buffer adequacy; no load-bearing integer-width overflow found; representative certificate arithmetic; R102's lack of final response; R104/R105 lack of captured public responses.

**`COMPUTATIONALLY_REPRODUCED`:** all available R82–R104 exact budget logs; representative R82/R94/R102/R104/R105 range/support-loss/margin calculations.

**`CORRECT_BUT_CONDITIONAL`:** packet-certificate ⇒ ansatz baseline contradiction, conditional on the inherited frozen strict-target/four-slack framework.

**`INCORRECT`:** R82 stale active `SUPPORT` constants; R98 prompt rows 3 and 9 H4 values; theorem-sounding “proved/establishes” language when governance remains `CONJECTURED`.

**`INCOMPLETE`:** fresh exhaustive C++ rerun; packaged R105 binary-bound verifier; R102 public answer.

**`NOT_CHECKED`:** the asserted R104 dispatch, because its receipt is absent from the supplied archive; any complete reduction from these ansätze to PW10/full-size.

**`PROVENANCE_ONLY`:** historical browser/model labels, hash receipts, three-run records, and runtime-bundle claims when their underlying response-side files were not captured.

**`CONJECTURED`:** every `GenericTheta...Exclusion` in this package, including θ300219–300242. Public reconstruction through θ300240 does not convert these to `PROVED`.

**`OPEN`:** PW10, the arbitrary one-defect/full ratio-two classes, positive regularized defect for one fixed finite pair, the all-copy physical-output gate, and the Hayden–Penington full-size extensive Holevo/MOE theorem. R105 explicitly preserves this boundary.

# 8. First remaining unknown

At the **operational theta-march provenance frontier**, the first missing public audit is exactly:

$$
\texttt{GenericTheta300241Exclusion}.
$$

Its local arithmetic is internally consistent: `K=970335976`, `B_coupled=203244`, `(N,G,Q,R)=(1070768,82786480,87069552,885407960)`, with positive cleared margin `3053715195721792`. But the CORE explicitly has no Round-104 response, so it remains a local `CONJECTURED` candidate.

At the stronger theorem-status level, even θ300219–300240 remain `CONJECTURED`; the captured public chain is an audit/provenance frontier, not a sequence of promoted theorems.

# 9. Final audit verdict

## `NO MATERIAL ERROR FOUND IN CHECKED SCOPE`

Concrete source/provenance defects were found—most notably the stale Round-82 `SUPPORT` array, the corrected Round-98 copy/substitution error, the unsupported R104-dispatch-record assertion, and incomplete packaged R105 binary reproducibility—but none was shown to invalidate the load-bearing finite-slope certificates through the checks actually performed.

The corrected boundary is: **captured public finite-slope reconstruction through θ=300240; local candidate evidence through θ=300242; earliest missing public audit at θ=300241.** No earlier checked mathematical defect forces that frontier backward.

Advancing the finite theta frontier from 300240 to local candidates 300241 and 300242 is not a conceptual advance toward the unrestricted problem: it adds two more members of the same restricted centrally symmetric twelve-slope ansatz family and supplies no completeness reduction.

**The Hayden–Penington full-size theorem remains OPEN.** No complete line-by-line proof of every required unrestricted/global step was supplied or established in this audit.
