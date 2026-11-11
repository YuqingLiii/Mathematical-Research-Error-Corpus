Completed audit:

# 1. Audit receipt

**Package:** `04_r059_r081_global_certificates_I`.

**Attachments received:** `04_r059_r081_global_certificates_I_CORE(1).md` and `04_r059_r081_global_certificates_I_EVIDENCE(1).zip`.

**Integrity.** The uploaded CORE has SHA-256 `04727698b4afa469cac300f932dc18b4cb0227b61919dbe3f0acf1c00ff093b7`; the ZIP has SHA-256 `3a777186fa90e5016bd1f9d0dbeb9f0def8ca92afaf4d67144989ae0ef06cbcb`. `unzip -t` passed. All 301 `MANIFEST.tsv` entries exist and match their recorded SHA-256. The CORE embedded in the ZIP is byte-identical to the uploaded CORE.

**Files actually opened/inspected:** CORE; `MASTER_AUDIT_PROTOCOL.md`; `README.md`; round index; `MANIFEST.tsv`; selected response/audit sections for R59, R60, R66, R67, R75, R77, R80, R81; `explore_round59_global.cpp`, `explore_round66_global.cpp`, `explore_round67_global.cpp`, `explore_round81_global.cpp`; all 23 `explore_round59_global.cpp`–`explore_round81_global.cpp` were programmatically scanned for theta constants, temporary ranges, disabled expectation guards, and integer types; all `verify_round67_global_budget.py`–`verify_round81_global_budget.py` were run.

**Current computations actually run:** all 15 exact budget verifiers R67–R81 passed; independent integer recomputation of all R59–R81 final cleared margins passed; exact rearrangement range checks were independently recomputed for all 23 C++ sources; permutation-sign logic was exhaustively cross-checked on 5,904 independently generated small cases. A full R59 13-row run was attempted but exceeded the 300-second execution limit, so full contemporary census replication is `INCOMPLETE`. Audit-only full-row-0 runs for R59, R67, and R81 reproduced their saved row-0 low-fiber census and rowwise match; R59 additionally reproduced formal support `S_0=53,624,480`.

The CORE itself identifies the operative cutoff as the September 7 baseline.

---

# 2. Executive verdict

No fatal defect was found in the **new reusable packet-certificate mathematics** within the checked scope.
The earliest substantive correction is R59: its strict two-slack inequality is derived only inside a contradiction branch, but its response headline presents it as if unconditional.
The correct unconditional consequence is only that the **total four-slack sum is at least** `HE`; that is nevertheless sufficient for the baseline contradiction.
R60 also contains an off-by-one description of “sharp” support-loss ceilings; the larger supplied values are conservative, so the certificate survives.
The R66 row-subset refinement and R67 coupled weighted-support refinement are mathematically valid.
`B_coupled < M_global` alone proves only `N>0`; every coupled round also needs—and has—a separately positive Pell-cleared margin.
No stale target theta, unsafe `t` buffer, arithmetic overflow, nondeterministic merge dependence, or invalid pruning was found in the scanned final sources.
Full contemporary re-enumeration of the ≈206M size-two records was infeasible here, so those census totals remain `INCOMPLETE` rather than newly verified.
The imported full four-slack identity/strict baseline target is `NOT_CHECKED` from first principles in this package.
Therefore every named `GenericTheta...Exclusion` remains `CORRECT_BUT_CONDITIONAL` and `CONJECTURED`.

---

# 3. Claim ledger

| Material claim                                                                    | Source locator          | Audit action                                                                       | Status                                   | Consequence                                                        |
| --------------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------ |
| Contrary branch gives `Δ_ray<HE`, `Δ_flat<HE`                                     | CORE R59 response §1    | Re-derived from nonnegative total slack                                            | `VERIFIED_IN_THIS_AUDIT`                 | Valid only under total-slack `<HE` assumption.                     |
| Full four-slack identity `(K-1)E-M_ord=ΣΔ` and nonnegativity of Young/group terms | inherited Wiener chain  | Package does not supply complete upstream derivation/definitions                   | `NOT_CHECKED`                            | All final ansatz exclusions remain conditional on it.              |
| Canonical key `(d6,dr)`, relative sign, cross-row matching                        | R59 §§4–6               | Sign/parity audit; code inspection; independent small permutation test             | `VERIFIED_IN_THIS_AUDIT`                 | Equal keys really share the same `Z,W` phase across cofactors.     |
| Coordinate-disjoint packet selection and deletion accounting                      | R59 §6; R66 refinement  | Direct combinatorial check                                                         | `VERIFIED_IN_THIS_AUDIT`                 | At most one chosen packet is destroyed per bad coordinate.         |
| Packet energy/Cauchy lemma                                                        | R59 §7                  | Algebraically re-derived                                                           | `VERIFIED_IN_THIS_AUDIT`                 | `Δ_ray+Δ_flat ≥ (6-4√2)GN/(G+4N)E`.                                |
| Pell clearing                                                                     | R59 §8 and reused later | Exact integer recomputation                                                        | `VERIFIED_IN_THIS_AUDIT`                 | `577²-2·408²=1` gives strict `35/102` lower bound.                 |
| Coupled weighted support-loss budget                                              | R67 §6, reused later    | Re-derived inequality and strict integer rounding; all R67–81 budget scripts rerun | `VERIFIED_IN_THIS_AUDIT`                 | Legitimately replaces the loose sum of per-row maxima.             |
| Exhaustive determinant/global-merge totals                                        | per-round C++ logs      | Hashes checked; row-0 tests at R59/R67/R81; full R59 run timed out                 | `INCOMPLETE`                             | Saved counts are evidence, not newly independently exhausted here. |
| Named finite-slope exclusions R59–R81                                             | each response           | Certificate logic checked conditional on census + upstream identity/target         | `CORRECT_BUT_CONDITIONAL`; `CONJECTURED` | No promotion to phase-uniform/general theorem.                     |

---

# 4. Detailed findings

### F-001 — Medium — contradiction-branch strictness is overstated in R59–R66

R59 first assumes

$$
\Delta_{\rm ray}+\Delta_{\rm flat}+\Delta_{\rm Young}+\Delta_{\rm group}<HE
$$

and only then derives the near-ray/support-loss bounds.

Consequently the later packet conclusion `Δ_ray+Δ_flat>HE` is **branch-local**. The public R59 headline nevertheless states the strict two-slack bound without that qualification. The same presentation pattern persists through R66.

The valid reductio is:

$$
\text{total}<HE
\Longrightarrow
\Delta_{\rm ray}+\Delta_{\rm flat}>HE,
$$

a contradiction. Therefore, unconditionally,

$$
\boxed{\text{total}\ge HE},
$$

not `total>HE`, and hence

$$
M_{\rm ord}\le(K-1-H)E.
$$

That non-strict bound is already sufficient because the inherited target inequality is strict.

**Minimal correction:** qualify every strict two-slack statement as “inside the contradiction branch” and use `≥HE` / `≤` in the unconditional conclusion. The finite-slope exclusions are not invalidated.

### F-002 — Low — R60 “sharp ceiling” off by one, already repaired

The strict inequality is `m_i < x_i`; therefore the maximum admissible integer is `ceil(x_i)-1`, not simply `ceil(x_i)`. R60 identifies that every supplied value was one too large.

Because the larger values were used as deletion upper bounds, they are conservative and make the packet lower bound weaker. The original positive margin therefore remains valid. No downstream invalidation.

### F-003 — Pass — canonical global matching is mathematically legitimate

Ordering the two Laurent monomials by `(Q6,Qr)` fixes orientation; multiplying an entire cofactor by `-1` changes both coefficients and leaves `σ=c0c1` unchanged. Since all deleted-row cofactors use the same physical `Z,W`, equal `(d6,dr)` keys really produce a common phase `ζ`.

A positive and negative record therefore yield `|1+ζ|` and `|1-ζ|`. Matching `min(pκ,nκ)` records one-to-one is deterministic and probability-free. Record multiplicities are preserved; no assumption that a key occurs only once is made.

### F-004 — Pass — packet energy, Cauchy, and Pell comparison

For every packet,

$$
|1+\zeta|^2+|1-\zeta|^2=4,\qquad
|1+\zeta|+|1-\zeta|\le2\sqrt2.
$$

With `G` unit anchors and `N` disjoint packets this gives `Q=G+4N`, and Cauchy on the remaining coordinates gives exactly

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
\ge\frac{(6-4\sqrt2)GN}{G+4N}E.
$$

The Pell clearing has the correct inequality direction because `sqrt(2)<577/408`, hence `6-4sqrt(2)>35/102`. No division by an unproved-sign quantity occurs: `K-H>0`, `S_i>0`, and inside the contrary branch `α>0`.

### F-005 — Pass — R66 row-subset deletion refinement

Once packets are preselected using only rows `S`, only bad coordinates in those rows can destroy a selected packet. Singleton anchors may simultaneously be retained from all 13 rows, charging all-row bad budgets there. This is conservative, not double counting. The R66 prompt explicitly states this intended distinction.

Thus using all-row anchors together with a subset packet budget is valid.

### F-006 — Pass — R67 coupled weighted budget

Let `D_i=S_i e_i²-L_i²` and `m_i=S_i-|supp A_i|`. Rowwise Cauchy gives `D_i≥m_i e_i²`, while

$$
\Delta_{\rm flat}\ge\sum_iD_i
$$

because every cross term is nonnegative. Retaining the row weights before replacing `S_i` by `S_min` yields

$$
\sum_i m_iS_i
<
\frac{Hd^2K^2}{(d-1)^2(K-H)}.
$$

Strict integer rounding is therefore legitimate. The bad-coordinate count satisfies

$$
B_{\rm coupled}\le2\sum_i m_i.
$$

Important implication check: `B_coupled<M_global` establishes only positive surviving packet count `N`; it does **not** establish the required slack coefficient. R67–R81 all additionally perform the cleared comparison

$$
35GN-H\cdot102(G+4N)>0.
$$

I independently recomputed these final margins for every R67–R81 log; all agree exactly.

### F-007 — Low — source-evolution hazards exist but are non-load-bearing

All 23 final exploratory sources contain the correct target `theta`; my scan found no other stale `300xxx` literal. Every source still contains stale Round-58 `EXPECTED_*` arrays, but they are protected by `VERIFY_ROUND58_EXPECTATIONS=false`, so they cannot force a false pass.

All sources use `TMIN=-3,753,400`, `TMAX=3,753,450`. Independently derived exact ranges run from `[-3,727,167,3,727,215]` at R59 to `[-3,727,539,3,727,587]` at R81, so every buffer is adequate. R59 prose mentions a different wider buffer; that is a prose/source mismatch, not truncation.

No relevant overflow was found: `t`, `Q6`, `d6` fit signed 32-bit under an absolute `Q6` bound below `90,092,160`; `q`, `Qr`, `dr` fit their declared small integer widths; aggregate moments/checksums use 128-bit arithmetic. The thread workers write distinct result slots and all merges/sorts occur afterward, so merge output does not depend on scheduling.

---

# 5. Dependency/invalidation map

| Finding                                       | Downstream effect                                                                                                                                                                               |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F-001                                         | R59–R66 strict subsidiary statements require correction. Final ansatz exclusions survive with non-strict unconditional total-slack bound. R67 onward explicitly records the branch distinction. |
| F-002                                         | Only R60's description of the supplied ceilings. Conservative certificate and downstream rounds unaffected.                                                                                     |
| F-003/F-004                                   | Reusable global packet lemma survives R59–R81.                                                                                                                                                  |
| F-005                                         | Validates R66's subset transition; later rounds do not numerically depend on R66's particular subset counts.                                                                                    |
| F-006                                         | Load-bearing for R67–R76, R78, R80; stronger cross-check at R77, R79, R81. No invalidation found.                                                                                               |
| F-007                                         | No mathematical invalidation; stale disabled arrays should nevertheless be deleted or regenerated to reduce future audit risk.                                                                  |
| Upstream `NOT_CHECKED` identity/strict target | Affects **every R59–R81 named exclusion**. They remain `CORRECT_BUT_CONDITIONAL`/`CONJECTURED`, regardless of local census margins.                                                             |
| Full census rerun `INCOMPLETE`                | Prevents this audit from upgrading any exact `M_global` census to `VERIFIED_IN_THIS_AUDIT`.                                                                                                     |

There is therefore no earliest round with a demonstrated fatal internal certificate defect. The earliest round that cannot be promoted to an unconditional theorem in this audit is **R59**, because the upstream Wiener-chain/strict-target dependency is `NOT_CHECKED` and the full contemporary census replay is `INCOMPLETE`.

---

# 6. Computational audit

The uploaded ZIP and all manifest hashes validate. Saved C++ sources consistently enumerate `(deleted,q,t)` fibers, collect genuine size-two Laurent binomials, canonically orient exponent differences, retain multiplicities, then perform deterministic row/global merges.

A complete current R59 run was attempted and exceeded the execution limit. The permitted small-instance fallback was therefore used:

* **R59:** complete deleted-row `0` reproduction: `U_0=2,611,200`, `H2_0=8,170,368`, `H3_0=2,127,360`, `H4_0=8,437,248`, `S_0=53,624,480`, row match `9,164`.
* **R67 transition to coupled budget:** complete row `0`: same first four low-fiber counts; row match `9,180`; coupled exact arithmetic independently reproduces `B=206,540`, `N=1,098,612`, margin `3,133,446,005,826,720`.
* **R81:** complete row `0`: `S_0=53,624,480`, row match `9,020`; exact rowwise and coupled budget verifier passes, and independent arithmetic reproduces both margins.

An independent parity implementation matched the C++ determinant-sign construction in all 5,904 tested reduced configurations.

### Round-by-round receipt/status table

`U` = upstream four-slack/strict-target dependency `NOT_CHECKED`; `E` = full current exhaustive census `INCOMPLETE`.

|  R |      θ | Historical receipt                       | Current reproduction      | Mathematical status / inherited dependency                       |
| -: | -----: | ---------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| 59 | 300187 | response+bundle local                    | row0 + arithmetic         | `CORRECT_BUT_CONDITIONAL`; U+E, all-row                          |
| 60 | 300189 | response+bundle local                    | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E, conservative ceiling             |
| 61 | 300191 | response+bundle local                    | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E                                   |
| 62 | 300193 | bundle hash unverified                   | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E                                   |
| 63 | 300194 | bundle hash unverified                   | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E                                   |
| 64 | 300196 | bundle hash unverified                   | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E                                   |
| 65 | 300198 | bundle hash unverified                   | arithmetic/static         | `CORRECT_BUT_CONDITIONAL`; U+E                                   |
| 66 | 300200 | bundle hash unverified                   | subset arithmetic/static  | `CORRECT_BUT_CONDITIONAL`; U+E+row-subset                        |
| 67 | 300202 | bundle hash unverified                   | row0 + coupled arithmetic | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 68 | 300204 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 69 | 300206 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 70 | 300207 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 71 | 300208 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 72 | 300209 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 73 | 300210 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 74 | 300211 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 75 | 300212 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 76 | 300213 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 77 | 300214 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E, separate primary + coupled check |
| 78 | 300215 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 79 | 300216 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E, separate primary + coupled check |
| 80 | 300217 | bundle hash unverified                   | budget rerun              | `CORRECT_BUT_CONDITIONAL`; U+E+coupled                           |
| 81 | 300218 | recovery response; ZIP hashes unverified | row0 + both budget routes | `CORRECT_BUT_CONDITIONAL`; U+E, separate primary + coupled check |

The saved/local prior exhaustive-run statements are `PROVENANCE_ONLY`; current exact budget arithmetic is `COMPUTATIONALLY_REPRODUCED`.

---

# 7. Corrected status ledger

**`VERIFIED_IN_THIS_AUDIT`:** contradiction-branch near-ray implication; canonical orientation and relative-sign invariance; deterministic global matching; coordinate-disjoint packet construction; packet-energy/Cauchy inequality; R66 selected-row deletion logic; R67 coupled weighted support-loss derivation; Pell-cleared comparison method.

**`COMPUTATIONALLY_REPRODUCED`:** ZIP/manifest integrity; exact final arithmetic for all R59–R81; all packaged coupled-budget verifiers R67–R81; row-0 determinant census at R59/R67/R81; all 23 assignment-range bounds.

**`CORRECT_BUT_CONDITIONAL`:** every R59–R81 finite-slope exclusion, conditional on the exact stored census and the imported four-slack/strict-target chain.

**`INCORRECT`:** treating branch-local `Δ_ray+Δ_flat>HE`, total `>HE`, or `M_ord<threshold` as unconditional in R59–R66; R60's original assertion that its one-larger values were the sharp strict maxima. Neither error invalidates the weaker sufficient conclusion.

**`INCOMPLETE`:** fresh full ≈206M-record census/merge replication.

**`NOT_CHECKED`:** complete upstream proof of the Young/group portions of the four-slack identity, the inherited strict target estimate, and the physical baseline inequality under all exact hypotheses.

**`PROVENANCE_ONLY`:** historical “independently audited/verified/proved” labels, prior full-run reports, and uncaptured per-round ZIP hashes from R62 onward.

**`CONJECTURED`:** all `GenericTheta...Exclusion` named candidates remain at that status.

Global targets—phase-uniform result, PW10, fixed regularized defect, all-copy gate, and full-size theorem—remain **OPEN**. R59 itself explicitly warns that the finite-slope result is weaker than PW10.

---

# 8. First remaining unknown

At the logical package boundary, the earliest exact unresolved dependency is the **complete four-slack Wiener-chain identity/nonnegativity together with the strict baseline target under the exact frozen hypotheses**. It is imported rather than reconstructed in this R59–R81 evidence archive and is therefore `NOT_CHECKED`.

Within the newly developed certificate machinery itself, the earliest current-audit unknown is the complete R59 13-row determinant/global-key census—especially `M_global=1,326,892`—because the full contemporary run did not finish. The source/object mapping, row-0 census, packet lemma, and final arithmetic all survived the checks actually performed.

---

# 9. Final audit verdict

$$
\boxed{\texttt{NO MATERIAL ERROR FOUND IN CHECKED SCOPE}}
$$

The audit found two real but nonfatal corrections: contradiction-branch strict inequalities were overstated as unconditional in early responses, and R60 initially mislabeled conservative one-larger ceilings as sharp. Neither destroys the corrected finite-slope certificates. The reusable global-key packet lemma, R66 row-subset refinement, and R67 coupled weighted support-loss refinement survived the mathematical checks performed.

This verdict does **not** upgrade any `GenericTheta...Exclusion` beyond `CONJECTURED`, because full exhaustive current replication is `INCOMPLETE` and the inherited Wiener-chain/strict-target dependency is `NOT_CHECKED`.

**The Hayden–Penington full-size theorem remains OPEN; no complete line-by-line proof of every required unrestricted global step has been supplied here. PW10 likewise remains OPEN.**
