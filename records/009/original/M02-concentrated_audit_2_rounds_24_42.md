已完成。下面的结论区分了“数学错误”和“包内无法独立复核的依赖”；后者不会被自动当作已证明。

# 1. Audit receipt

**Package:** `02_r024_r042_structured_ansatz`

**Attachments received**

* `02_r024_r042_structured_ansatz_CORE.md`
* `02_r024_r042_structured_ansatz_EVIDENCE.zip`

`CORE.md`明确把本包定位为 September 7 V7 baseline 之后的历史证据链，并从 Round 24 开始。

**Archive integrity checks actually performed**

* External `CORE.md` SHA-256:
  `1d7c095fcb902e32f40c3d9c70079659e0d468e24f9f74d85ed76606fc7af74a`
* ZIP SHA-256:
  `2bff4b8d2277a8caad4a4757592b788433effc66dd8849483ba674ab0240a4ae`
* External CORE is byte-identical to the CORE copy inside the ZIP.
* `MANIFEST.tsv`: 245 archived files checked; all 245 stored SHA-256 values reproduced.
* Round index: all 57 indexed prompt/response/audit size/hash records checked against archive contents.

**Files actually opened/read**

I did **not** read every one of the 246 ZIP entries line-by-line. Coverage was source-targeted around every load-bearing R24–R42 theorem and its verifier.

I opened/read:

* `02_r024_r042_structured_ansatz_CORE.md`
* `audit/MASTER_AUDIT_PROTOCOL.md`
* `audit/02_r024_r042_structured_ansatz_ROUND_INDEX.tsv`
* `MANIFEST.tsv`
* `evidence/outputs/round-23-local-audit.md`
* local audits for R31–R42
* source response sections for the R28 arithmetic correction, R29 ruling analysis, R31–33 rectangle/line-line/resultant chain, R34 three-slope circuits, R36 translated mirror circuit, R37 method-limit relaxation, and R41–42 Plücker/constant-real-structure chain
* independent derivations:

  * `round-31-independent-rectangle-rigidity.md`
  * `round-32-independent-line-line-reduction.md`
  * `round-32-independent-zero-dimension-exclusion.md`
  * `round-32-independent-cosine-kernel.md`
  * `round-33-independent-plane-resultant-nogo.md`
  * `round-33-independent-resultant-chiral-chord.md`
  * `round-35-independent-translated-aligned-circuit.md`
* representative verifier source, including R33, R35, and R42.

Rounds 24–30 were additionally read through the embedded prompt/response/local-audit stream in CORE.

**Code actually run**

I reran 27 historical verification scripts covering:
`PlusFrame`, the even witness, `RealRankTwo`, chirp spectrum, shear reduction, sparse CAZAC, MUB deformation, quadric rulings, ray uncertainty, rectangle rigidity, zero-dimensional cases, rectangular cosine minors, plane resultants, triple-chord checks, physical circuits, translated/aligned circuits, and every R33–R42 web-response checker.

All completed assertions passed.

I also wrote and ran an independent small-prime checker for:

* `PlusFrame` at \(D=3,5,7\);
* RowCAZAC/ruling formulas at \(D=5,7,11\);
* rectangle identities;
* chiral base loci/no-root-at-infinity checks;
* the \(S+tJ\) paired inequality/equality cases;
* frozen integer thresholds.

One initial failure in **my** custom `PlusFrame` checker was traced to my incorrectly using a conjugated projector factor in \(P\operatorname{Diag}(w)P\). After correcting that implementation, all tests passed. This was not a package failure.

**Coverage limits**

1. The package includes only `round-23-local-audit.md`, not the complete R23 prompt/response/source verifier set from the preceding package. Some R24 frozen-edge numerical estimates import those R23 bounds.
2. Small-prime scripts are sanity checks, not transfers to the frozen prime unless accompanied by a symbolic argument.
3. I did not line-by-line inspect every non-load-bearing README, browser receipt, or duplicate archival copy.
4. No external theorem was silently supplied from memory; where a needed predecessor proof was absent, I mark the dependency `NOT_CHECKED`.

---

# 2. Executive verdict

**No load-bearing mathematical error was found in the checked R24–R42 analytic chain.**
The earliest actual error found is the R28 dictionary-count typo \(970353651\), whose correct value is \(604842954373\); it was already locally corrected and is non-load-bearing.
The earliest package-level verification gap is R24's universal frozen-edge specialization, which imports exact R23 numerical bounds whose primary proof artifacts are not supplied here; that specialization is therefore `NOT_CHECKED` as a self-contained Package-02 claim.
R29 contains a false descriptive claim about rank-one cross-ruling differences; the discriminant formulas remain correct and R30 explicitly repairs the scope.
R37 contains an under-specified norm-data relaxation that should not be promoted beyond `CONJECTURED`/`NOT_CHECKED`.
The R33 arbitrary-rank **two-slope** no-go survives the checked degeneracies and is an ansatz theorem only.
The R36 **at least twelve paired ruling slopes** theorem survives, again only inside the quadratic-Gauss paired-ruling ansatz.
The R42 \(S+tJ\) theorem survives exactly under a **constant real structure and constant separator**; the symmetric \(S\) problem and global/frequency-dependent matrix dual remain open.
No result in R24–R42 proves PW10, the all-copy purity gate, a fixed-pair regularized defect, or the full-size Holevo/MOE theorem.

---

# 3. Claim ledger

| Source                                             | Exact material claim                                                                                      | Load-bearing dependency                                   | Audit action                                                       | Status           | Consequence                                                                             |   |                             |                           |                       |          |                                                              |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------ | ---------------- | --------------------------------------------------------------------------------------- | - | --------------------------- | ------------------------- | --------------------- | -------- | ------------------------------------------------------------ |
| R24 `PlusFrame`                                    | \(q_{\min}>1/(2D^2)\) gives an explicit \(+1\)-Fourier-supported PSD trace-one matrix with diagonal \(q\) | Fourier normalization only                                | Re-derived diagonal map; small-prime matrices                      | `PROVED`         | Mixed relaxation feasible under stated sufficient hypothesis; says nothing about purity |   |                             |                           |                       |          |                                                              |
| R24 `EvenPlusPSD`                                  | A pure even \(+1\)-Fourier edge produces a rank-one feasible `EvenPlusPSD` matrix                         | Rank-one lift                                             | Direct implication checked                                         | `NECESSARY-ONLY` | Mixed feasibility cannot be promoted to pure phase retrieval                            |   |                             |                           |                       |          |                                                              |
| R24 universal frozen-edge witness                  | Every nonzero frozen edge has the stated even-supported PSD witness and spectral floor                    | Imported R23 frozen \(q_h\)/Fourier bounds                | Algebra and frozen arithmetic rerun; predecessor proof unavailable | `NOT_CHECKED`    | Valid conditional on the R23 bounds; not independently promoted from Package 02         |   |                             |                           |                       |          |                                                              |
| R25 `RealRankTwo`                                  | Pure complex edge feasibility iff real supported PSD feasibility of rank \(\le2\)                         | Reality of \(\Pi\)                                        | Re-derived both directions                                         | `EQUIVALENT`     | Exact reformulation, not a relaxation                                                   |   |                             |                           |                       |          |                                                              |
| R25 `RankTwoNewton`                                | For PSD trace-one \(G\), rank \(\le2\) iff \(1-3\operatorname{Tr}G^2+2\operatorname{Tr}G^3=0\)            | PSD essential                                             | Eigenvalue derivation checked                                      | `EQUIVALENT`     | No rank-two existence follows without attaining zero defect                             |   |                             |                           |                       |          |                                                              |
| R26 chirp Jacobian                                 | Uniform chirp is a submersion with stated sharp singular value                                            | Odd-prime Fourier algebra                                 | Character decomposition + verifier                                 | `PROVED`         | Only local liftability                                                                  |   |                             |                           |                       |          |                                                              |
| R26 continuation ball                              | Every even probability inside the explicit \(\rho_D\) ball lifts                                          | Quantitative contraction estimate                         | Bounds rerun                                                       | `PROVED`         | Frozen/baseline targets are far outside the certified ball                              |   |                             |                           |                       |          |                                                              |
| R27 shear-invariant no-go                          | No baseline lift has a shear-invariant ray                                                                | Baseline amplitudes + Parseval                            | Re-derived                                                         | `PROVED`         | Closes only shear-fixed branch                                                          |   |                             |                           |                       |          |                                                              |
| R27 shear/RowCAZAC coordinates                     | Line magnitudes + orbit relations + all RowCAZAC equations exactly encode baseline lift                   | Full shear-isotypic decomposition                         | Fourier-coordinate derivation checked                              | `EQUIVALENT`     | Legitimate exact reformulation                                                          |   |                             |                           |                       |          |                                                              |
| R27 sparse-CAZAC                                   | Non-singleton perfect cyclic autocorrelation support \(s\) obeys \(p^2\le6^{s-1}\)                        | Integer relation determinant argument                     | Independent proof audit + exhaustive small primes                  | `PROVED`         | Frozen lift needs at least 47 nontrivial shear characters                               |   |                             |                           |                       |          |                                                              |
| R28 bordered Gauss                                 | One global symmetric quadratic core with arbitrary symmetric border cannot realize baseline               | \(p\ge7,\ a\ne0\)                                         | Gauss sum + circle argument                                        | `PROVED`         | Only this bordered class is closed                                                      |   |                             |                           |                       |          |                                                              |
| R28 sparse deformation                             | (2                                                                                                        | T                                                         |                                                                    | T-T              | +                                                                                       | T | \sqrt p<p\Rightarrow E_y=0) | Three selected MUB blocks | Gram estimate checked | `PROVED` | Frozen modified row must change at least 777716 coefficients |
| R28 dictionary count                               | Printed first-open dictionary bound \(970353651\)                                                         | Arithmetic only                                           | Exact integer recomputation                                        | `CORRECTED`      | Correct count \(604842954373\); theorem unaffected                                      |   |                             |                           |                       |          |                                                              |
| R29 bounded Gauss mixtures                         | No effective symmetric quadratic-Gauss baseline mixture with \(r\le31150\)                                | Restricted quadratic-phase independence                   | Recomputed Gram inequality                                         | `PROVED`         | Ansatz-specific rank obstruction                                                        |   |                             |                           |                       |          |                                                              |
| R29 one paired ruling slope                        | Arbitrary rank on \(L_{m,+}\cup L_{m,-}\) cannot realize baseline                                         | Ruling parameterization                                   | Re-derived factorization                                           | `PROVED`         | One-slope Gauss class closed                                                            |   |                             |                           |                       |          |                                                              |
| R29 “rank-one differences only on selected slopes” | Cross-ruling rank-one differences are confined to the two chosen slopes                                   | None                                                      | Explicit \(\mathbb F_7\) counterexample                            | `DISPROVED`      | Descriptive statement only; later discriminant treatment survives                       |   |                             |                           |                       |          |                                                              |
| R30 multi-slope tensor span                        | \(k\)-slope paired span has \(\dim=k(D+1-k)\) for \(k\le(D+1)/2\)                                         | Prime Fourier full spark                                  | Tensor intersection independently checked                          | `PROVED`         | A linear span theorem, not target existence                                             |   |                             |                           |                       |          |                                                              |
| R30 count threshold                                | Below \(k_{\rm count}\), restricted probability map cannot be a submersion                                | Dimension only                                            | Dimension arithmetic checked                                       | `NECESSARY-ONLY` | Does not exclude singular solutions                                                     |   |                             |                           |                       |          |                                                              |
| R31 target-ray/core bound                          | Gauss-mixture candidate needs at least 686127259 effective \(\kappa\)-values/cores                        | Target-ray uncertainty                                    | Fourier normalization checked                                      | `PROVED`         | Not a ruling-slope bound; not general baseline theorem                                  |   |                             |                           |                       |          |                                                              |
| R31 rectangle rigidity                             | Two-slope grid forces stated low affine dimensions                                                        | Oriented-area identities                                  | Polynomial identity re-derived                                     | `PROVED`         | Restricts but does not yet exclude two slopes                                           |   |                             |                           |                       |          |                                                              |
| R32 line-line/Schur reductions                     | Surviving two-slope classes reduce to low-dimensional \((1,1),(1,2),(2,1)\)-type cases and low Schur rank | Generic cosine full spark + exceptional cases             | Independent degeneracy audit                                       | `PROVED`         | Sets up R33; Hadamard full rank alone not used illegally                                |   |                             |                           |                       |          |                                                              |
| R33 `TwoSlopeNoGo`                                 | No arbitrary-rank two-paired-ruling-slope Gauss mixture realizes baseline                                 | R32 + binary/ternary resultants + finite chiral base loci | Degree/support counts, infinity cases, incidence argument checked  | `PROVED`         | **Ansatz only**; ≥3 slopes and non-Gauss remain                                         |   |                             |                           |                       |          |                                                              |
| R34 three-slope circuit                            | Exact tensor decomposition and complete 16-term annihilator circuit family for three slopes               | Fourier full spark                                        | Re-derived linear algebra                                          | `EQUIVALENT`     | No three-slope no-go                                                                    |   |                             |                           |                       |          |                                                              |
| R36 `TwelveSlopeLowerBound`                        | Every quadratic-Gauss paired-ruling baseline mixture uses at least 12 distinct slopes                     | Translated mirror circuit + finite-grid selection         | Exact hyperplane count and reverse triangle rerun                  | `PROVED`         | Closes \(k\le11\) ansatzes only                                                         |   |                             |                           |                       |          |                                                              |
| R37 Cauchy/Parseval route                          | Displayed scalar grouped-\(\ell_2\) route cannot yield required \(k=12\) bound                            | Its stated aggregation                                    | Algebra checked                                                    | `PROVED`         | Does not exclude weighted/matrix/coefficient-sensitive methods                          |   |                             |                           |                       |          |                                                              |
| R37 norm-data relaxation                           | Abstract data can be assigned to defeat a stronger method-limit claim                                     | Unwritten coefficient construction                        | Source does not verify all support/symmetry constraints            | `NOT_CHECKED`    | Must not be used as a theorem                                                           |   |                             |                           |                       |          |                                                              |
| R38 cofactor Wiener domination                     | Actual translated cofactors obey the stated diagonal/off-diagonal \(\ell_1\) domination                   | Shifted null equations                                    | Rechecked                                                          | `PROVED`         | Still numerically too weak                                                              |   |                             |                           |                       |          |                                                              |
| R39 `AllSlopeWienerOptimality`                     | Best translation-invariant linear-convolution recovery constant is exactly 1                              | Unrestricted sequence model                               | Wiener argument/checker                                            | `PROVED`         | Method-limit result, not maximal-minor completeness                                     |   |                             |                           |                       |          |                                                              |
| R40 `CofactorRelaxationNoGo`                       | Actual canonical cofactors can satisfy inherited qualitative conditions while giving huge \(\mathcal O\)  | Probabilistic existence                                   | Integer/probability estimates checked                              | `PROVED`         | Qualitative package alone cannot force desired small \(\mathcal O\)                     |   |                             |                           |                       |          |                                                              |
| R41 alternating Plücker                            | Under constant real structure, pure alternating holomorphic wedge has zero target gain                    | \(\bar B=BR\)                                             | Sesquilinear/holomorphic conversion checked                        | `PROVED`         | Pure \(J\) direction closed only in stated setting                                      |   |                             |                           |                       |          |                                                              |
| R41 “any valid linear use”                         | Broad wording appears to cover mixed/global uses                                                          | Same                                                      | Compared with actual derivation                                    | `CORRECTED`      | Only direct pointwise alternating conversion was proved                                 |   |                             |                           |                       |          |                                                              |
| R42 `MixedPlueckerNoCancellation`                  | For constant real structure, adding \(tJ\) cannot improve a fixed symmetric \(S\) separator               | \(y\leftrightarrow-y\) pairing                            | Pairing, zero row, equality cases independently checked            | `PROVED`         | Full constant \(S+tJ\) assistance closed; symmetric \(S\) optimum remains               |   |                             |                           |                       |          |                                                              |
| Any promotion to PW10/full-size                    | Structured no-go results imply global physical theorem                                                    | Would require unrestricted reduction + phase lift         | Searched throughout R24–42                                         | `DISPROVED`      | No such implication exists; globals remain `OPEN`                                       |   |                             |                           |                       |          |                                                              |

The R24 source itself explicitly distinguishes mixed-state feasibility from pure phase retrieval and warns that a negative projected-frame weight would reject only that frame ansatz, not the full PSD problem.

---

# 4. Detailed findings

## F-001 — R24 universal frozen-edge specialization has an unverified predecessor dependency

**Severity:** Medium — verification/provenance gap, not a demonstrated false theorem.

**Locator:** R24, Sections 9–12; dependency originates in the R23 exact frozen edge-product bounds.

The algebraic projected-frame construction is self-contained. The universal frozen-edge conclusion, however, additionally uses quantitative statements such as the near-uniform lower floor for \(q_h\) and the small nonzero Fourier coefficients of the edge product. Those are imported from R23.

The archive contains `round-23-local-audit.md`, which reports those inequalities, but not the underlying R23 response/proof/checker archive needed to reconstruct the load-bearing Sidon-spectrum and perturbation estimates from their original source.

For example, the R24 domination step has the logical form

$$
D^2q_h(p)>L_0,\qquad
|D(Tq_h)(p)|<\Theta_0
$$

$$
\Longrightarrow
w_p>\frac{3.999997}{(D+3)(D+5)},\quad p\ne0,
$$

followed by domination of a possibly negative \(w_0\). I verified the implication and all displayed frozen arithmetic. What is not independently supplied in Package 02 is the full primary proof of the two antecedent uniform inequalities.

**Correction:** split the status:

* projected-frame/even-map algebra: `PROVED`;
* universal frozen-edge spectral-floor specialization: `NOT_CHECKED` **within this package**, or `PROVED conditional on the R23 exact bounds`.

This does not make the later baseline ansatz no-go chain false.

---

## F-002 — R28 contains a concrete arithmetic error, but it is non-load-bearing

**Severity:** Low.

**Locator:** R28 first-undecided deformation dictionary.

The response printed

$$
777716^2+777716+1=970353651.
$$

Direct integer arithmetic gives

$$
777716^2=604842176656,
$$

so

$$
\boxed{
777716^2+777716+1=604842954373.
}
$$

The wrong value is instead

$$
31151\cdot31150+1=970353651.
$$

The local audit itself records this exact correction and states that no proof step used the erroneous printed count.

The MUB independence inequality, the \(777716\) threshold, and the near-Sidon difference-set bound recompute correctly.

**Minimal correction:** replace only the displayed dictionary count. No downstream theorem is invalidated.

---

## F-003 — R29's geometric description of rank-one cross-ruling differences is false

**Severity:** Low for the theorem chain; material as a scope correction.

**Locator:** R29 discussion of the two-slope dual system.

The response says that rank-one differences are confined to the two selected ruling directions.

Counterexample over \(\mathbb F_7\):

$$
\theta_{0,+}(1)=(1,1,0),\qquad
\theta_{1,+}(2)=(2,3,1).
$$

Their difference is

$$
(6,5,6).
$$

Its quadratic discriminant is

$$
4(6)(6)-5^2
=144-25
=119
\equiv0\pmod7.
$$

Moreover,

$$
(6,5,6)=6(1,2,1),
$$

so it is rank one in slope \(m=2\), neither of the selected slopes \(0,1\).

The package later explicitly supplies this correction.

**Consequence:** the prose description is `DISPROVED`; the actual Fourier formulas branch on the discriminant itself, not on the false confinement assertion. The R29/R30 no-go and span results therefore survive.

---

## F-004 — R37's abstract norm-data method-limit witness is not fully constructed

**Severity:** Medium for that one method-limit claim; no effect on later exact no-go theorems.

**Locator:** R37 Section 14.

The argument retains only exceptional data, ordinary magnitudes, a support allowance, symmetry, and aggregate \(\ell_2\) energy, then asserts that the required cancellation can be distributed among available slots.

The local audit correctly identifies the missing step: no explicit coefficient assignment is written that simultaneously verifies every per-frequency support restriction and central-symmetry constraint.

Thus the argument demonstrates a plausible scalar-energy obstruction to that proof method, but does not yet exhibit a complete feasible point of the claimed relaxed coefficient system.

**Minimal correction:** classify this particular Section-14 relaxation as `CONJECTURED` or `NOT_CHECKED`, not `PROVED`.

No later load-bearing theorem relies on it. R38–R40 provide separate, more concrete method-limit results.

---

## F-005 — `PlusFrame` is correct, but its logical strength is exactly mixed-state sufficiency

**Severity:** High if misused; no misuse survived in the audited package.

For

$$
\Pi_+=\frac{I+\mathscr F}{2},
$$

$$
\langle r|\Pi_+|p\rangle
=\frac12\left(\delta_{rp}+\frac1D\omega^{[p,r]}\right).
$$

Hence

$$
|\langle r|\Pi_+|p\rangle|^2
=
\begin{cases}
\dfrac{(D+1)^2}{4D^2},&p=r,\\[1mm]
\dfrac1{4D^2},&p\ne r.
\end{cases}
$$

With

$$
c=\frac1{2D(D+1)},\qquad
w_p=\frac{4D}{D+2}(q_p-c)
$$

and

$$
W=\sum_pw_p=\frac{2D}{D+1},
$$

the projected diagonal is

$$
[K_+(q)]_{r,r}
=
\frac{D+2}{4D}w_r+\frac{W}{4D^2}
=q_r.
$$

The condition

$$
q_{\min}>\frac1{2D^2}
$$

is stronger than \(q_p>c\), hence \(w_p>0\). Therefore this genuinely gives a PSD, trace-one, \(+1\)-supported mixed witness.

What it does **not** give is a vector \(v\) with

$$
\mathscr Fv=v,\qquad |v_p|^2=q_p.
$$

Similarly, `EvenPlusPSD` is a necessary convex relaxation for such a vector, not an equivalent formulation unless rank one is restored. The package explicitly keeps pure one-edge phase retrieval open.

**Status:** `PROVED` for the mixed witness; `NECESSARY-ONLY` for its use as a pure-edge test.

---

## F-006 — R33 `TwoSlopeNoGo` survives the exceptional and zero-dimensional cases

**Severity:** Load-bearing positive audit result.

**Locator:** R32–R33 line-line/resultant chain.

The checked chain is:

1. Rectangle/line-line reduction leaves only the low-dimensional surviving branches.
2. Pairwise binary resultants are used only for pairwise consequences; the package correctly retracts the invalid implication “pairwise common roots imply one common triple root.”
3. Identically zero pencils and degree-drop cases are treated separately.
4. Roots at projective infinity are checked and absent for the relevant chiral base loci.
5. The genuine three-row step uses a separate ternary resultant.

The ternary resultant is of degree at most \(4\) in each of three cosine parameters, hence after the chosen separated substitutions has at most

$$
9^3=729
$$

Fourier frequencies.

On the physical side, the corresponding resultant function has support at most \(3\) in the common-phase branch and at most \(67\) in the mixed branch. For the frozen prime these supports are vastly below the prime-Fourier uncertainty threshold, forcing the resultant field function to vanish identically.

The subsequent finite-base-locus incidence argument is the step that yields a common projective base point. Since each chiral base locus consists of four reduced finite points and three distinct row parameters would yield three distinct collinear chiral points where that configuration allows none, the surviving branches are contradicted.

The resulting statement is exactly:

$$
\boxed{
\text{No arbitrary-rank two-slope Gauss mixture produces a baseline lift.}
}
$$

The response itself expressly restricts this to an ansatz theorem and leaves three or more ruling slopes and dense nonquadratic vectors untouched.

**Status:** `PROVED` **inside the arbitrary-rank two-paired-ruling-slope Gauss ansatz**.

---

## F-007 — R36 really closes \(k\le11\), but nothing beyond the quadratic-Gauss paired-ruling class

**Severity:** Load-bearing positive audit result.

The R36 translated mirror construction was independently reproducible.

For eleven slopes the proof chooses twelve roots while avoiding all required parent collisions, \(-8\)-offset collisions, and root equalities. The exact number of forbidden affine hyperplanes is

$$
H=28680315881817666,
$$

and the frozen arithmetic satisfies

$$
32H<D.
$$

The finite-grid union bound therefore supplies a root assignment with all prohibited equalities absent and with the required short-arc phase alignment.

Writing \(n=11!\), exactly

$$
12n
$$

raw terms contribute coherently to the exceptional coefficient. The complete raw family contains

$$
(12n)^2
$$

terms, so after removing the coherent exceptional contribution the ordinary raw count is

$$
12n(12n-1).
$$

Because forbidden parent equalities and offsets ensure every ordinary raw term has the baseline magnitude \(B\), while the target terms have \(A_{\rm sp}=\sqrt{D+1}\,B\), the reverse-triangle comparison forces an inequality incompatible with the certified short-arc lower bound.

Padding an ansatz using fewer than eleven slopes by unused distinct slopes then closes all \(k\le11\).

The package's own local audit correctly states the exact scope: the theorem is

$$
\boxed{
\text{every quadratic-Gauss baseline mixture uses at least twelve paired ruling slopes},
}
$$

not a general baseline theorem.

The same mechanism provably stops at \(k=12\); R36/R37 do not establish a thirteen-slope lower bound.

**Status:** `PROVED` ansatz theorem.

---

## F-008 — R41 is overbroad in wording; R42 gives the correct maximal constant-\(S+tJ\) statement

**Severity:** Medium scope correction; R42 itself survives.

R41 contains the broad sentence that “any valid linear use” of the adjacent Plücker wedge is either inadmissible or zero-target.

The local audit correctly narrows it: R41 directly closes only the pure holomorphic alternating direction after a constant real structure converts the physical sesquilinear circuit into a holomorphic one. It does not by itself eliminate mixed symmetric/alternating separators or frequency-dependent/global constructions.

R42 then legitimately treats the mixed **constant** problem.

Assume

$$
\overline{B(c)}=B(c)R,\qquad R\in GL_2(\mathbb C)
$$

with constant \(R\). For a constant physical separator \(\Lambda\), set

$$
A=\Lambda R^{\mathsf T}=S+tJ,
\qquad
S^{\mathsf T}=S,
\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Because the target matrix is transpose-symmetric,

$$
\langle J,T_\nu\rangle=0;
$$

the numerator depends only on \(S\).

The ordinary matrices obey

$$
W_{\nu;x,-y}=W_{\nu;x,y}^{\mathsf T}.
$$

Consequently, for

$$
a_{\nu;x,y}=\langle S,W_{\nu;x,y}\rangle,\qquad
p_{\nu;x,y}=\langle J,W_{\nu;x,y}\rangle,
$$

one has

$$
a_{\nu;x,-y}=a_{\nu;x,y},\qquad
p_{\nu;x,-y}=-p_{\nu;x,y}.
$$

The \(y=0\) terms have \(p=0\), so ordinary terms pair as

$$
|a+tp|+|a-tp|.
$$

Triangle inequality gives

$$
|a+tp|+|a-tp|
\ge |(a+tp)+(a-tp)|
=2|a|.
$$

Summing paired terms yields

$$
\boxed{
\inf_{t\in\mathbb C}
\sum_{\rm ordinary}|a_{\nu;x,y}+tp_{\nu;x,y}|
=
\sum_{\rm ordinary}|a_{\nu;x,y}|.
}
$$

The package's R42 statement is therefore correct.

The equality cases are also correct:

* if \(a\ne0\), equality requires \(tp/a\in[-1,1]\);
* if \(a=0,\ p\ne0\), equality requires \(t=0\);
* if \(p=0\), that pair imposes no restriction.

Thus adding an alternating constant \(tJ\) never helps a fixed symmetric \(S\).

But the theorem assumes both a **constant real structure** and a **constant \(2\times2\) separator**. The package itself correctly leaves frequency-dependent multipliers, general slopes lacking a constant real structure, the optimal symmetric \(S\), and rank-two component cancellation open.

**Status:** R41 broad wording `CORRECTED`; R42 `PROVED` in its exact domain.

---

## F-009 — No structured result supplies the missing physical phase lift

**Severity:** Critical boundary preservation.

Rounds 27–42 mostly work on a baseline two-spike pure-edge problem and then on increasingly structured coefficient/circuit classes. Even a complete baseline lift would still be only a **one-edge** result.

Nothing checked in this package establishes a common coefficient field

$$
Y_{a,b}=\alpha_a\overline{\alpha_b}
$$

simultaneously across all edge differences, nor centered idempotence

$$
P^2=P
$$

for the physical operator reconstructed from one common \(\alpha\).

Accordingly, the following implications remain invalid:

$$
\text{baseline ansatz no-go}
\not\Rightarrow \text{PW10},
$$

$$
\text{one-edge lift}
\not\Rightarrow \text{physical lift of }x^{(10)},
$$

$$
\text{finite-slope no-go}
\not\Rightarrow \text{phase-uniform theorem}.
$$

This is not merely an omitted caveat: it is an actual missing quantifier transition. The package generally respects it.

**Status:** physical lifting and all global consequences remain `OPEN`.

---

# 5. Dependency/invalidation map

| Finding                                 | Directly affected statements                                                | Downstream effect                                                                                                          |
| --------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| F-001 R23 predecessor gap               | R24 universal all-nonzero-frozen-edge spectral-floor/witness specialization | Mark conditional/`NOT_CHECKED`; does **not** invalidate the algebraic PlusFrame theorem or R27–R42 baseline ansatz results |
| F-002 R28 arithmetic typo               | Printed first-open dictionary column count                                  | None; R29 onward uses the corrected number                                                                                 |
| F-003 R29 third-ruling counterexample   | Sentence claiming rank-one differences stay in selected ruling directions   | None on the discriminant-based transforms; R30 explicitly corrects it                                                      |
| F-004 R37 incomplete relaxation witness | Only the Section-14 abstract norm-data method-limit claim                   | No R38–R42 theorem depends on it                                                                                           |
| F-005 mixed/pure distinction            | Any attempted promotion of R24 PSD feasibility to a pure edge               | Such promotion is invalid; package leaves rank-one problem open                                                            |
| F-006 R33 verification                  | R32 surviving two-slope branches                                            | Legitimately closes the whole **two-slope Gauss** class, but nothing with \(\ge3\) slopes/general vectors                  |
| F-007 R36 verification                  | All paired-ruling quadratic-Gauss classes with \(k\le11\)                   | Legitimately yields 12-slope lower bound; does not touch \(k\ge12\) or non-Gauss classes                                   |
| F-008 R41/R42 scope                     | Pure/mixed Plücker constant-separator claims                                | R42 closes \(tJ\)-assistance only under constant real structure; symmetric and global matrix dual remain                   |
| F-009 missing physical lift             | Any PW10/full-size promotion                                                | Blocks all such promotions                                                                                                 |

There is therefore **no load-bearing invalidation cascade** in the checked R24–R42 chain. The genuine errors are either already corrected before downstream use or confined to non-load-bearing scope/method-limit statements.

---

# 6. Computational audit

## 6.1 Reproducibility and receipts

The archive itself is internally reproducible at the byte level:

* 245/245 manifest hashes matched;
* every indexed prompt/response/audit hash and byte count checked against its archived file;
* all selected executable verifier assertions passed.

This verifies saved-output integrity. It does **not** by itself verify mathematical completeness.

## 6.2 Arithmetic, overflow, and range handling

The Python verifiers use arbitrary-precision Python integers for the frozen constants; I found no fixed-width overflow in the load-bearing frozen comparisons.

In particular I independently reproduced:

* \(6^{46}<D^2<6^{47}\);
* the R28 \(777715\) deformation threshold;
* the corrected \(604842954373\) dictionary count;
* the \(31150/31151\) Gauss-mixture thresholds;
* the R36 hyperplane count and \(32H<D\);
* the R42 paired absolute-value identities.

No stale use of the erroneous R28 count was found downstream.

## 6.3 Program/object correspondence

The strongest distinction is:

**R24.** Small-\(D\) matrix tests really instantiate the advertised Fourier/projector matrices. They verify the map identities, but the frozen “all edges” theorem additionally depends on analytic R23 input.

**R27.** Small-prime exhaustive tests of sparse supports demonstrate the lonely-difference phenomenon, but the frozen theorem rests on the determinant/Hadamard proof rather than extrapolation.

**R28.** The MUB scripts test selected finite-field matrices and exact frozen threshold arithmetic. The mathematical theorem uses a sufficient Gram positive-definiteness criterion; the program does not falsely enumerate “all deformations.”

**R31–32.** Rectangle and rectangular-cosine scripts exhaust the advertised small-prime grid/minor classes. They are supporting checks for symbolic identities, not a claim of exhaustive frozen enumeration.

**R33.** `verify_round33_plane_resultant.py` checks frequency counts, substitutions, and base-locus geometry. It is not by itself a computer proof of the complete ternary-resultant theorem. The accompanying source derivation and incidence argument are therefore load-bearing and were checked separately.

**R36.** The frozen proof does not enumerate a grid of \(H\) points. It uses an exact union-bound existence argument on a finite grid plus deterministic term counting. The verifier correctly checks the counts rather than pretending to enumerate \(D^{12}\)-scale objects.

**R42.** The \(p=17\) canonical-cofactor script verifies the pairing mechanism in a genuine finite analogue. It does not show that the frozen problem possesses the required constant real structure. R42 is correctly a theorem **conditional on that structure**.

## 6.4 Numerical versus exact computations

Floating/complex small-prime checks were not used as theorem promotion where an exact proof is required. In particular:

* small-prime baseline lifts remain `NUMERICAL-ONLY`;
* numerical full-character occupancy remains `NUMERICAL-ONLY`;
* no frozen-dimensional existence is inferred from those experiments.

## 6.5 Code defects

I found no load-bearing range, parsing, overflow, or pruning bug in the selected historical scripts.

My own first custom `PlusFrame` implementation had a projector-multiplication mistake; I corrected it before drawing any audit conclusion. No historical result depended on that code.

---

# 7. Corrected status ledger

## `PROVED`

Within their stated domains:

* `PlusFrame` mixed-state construction.
* Fourier/reflection projector algebra.
* Uniform-chirp local submersion and quantitative local ball.
* Shear-invariant baseline no-go and shear-breaking estimate.
* Sparse-CAZAC determinant lemma.
* Bordered single quadratic-Gauss core no-go.
* Sparse Gauss-deformation lower bound \(777716\).
* Exact two-core collapse.
* Restricted Gauss-mixture bounds.
* Parameter-quadric and ruling classifications.
* Target-ray/core-frequency lower bounds.
* Rectangle rigidity and line-line reductions.
* R33 `TwoSlopeNoGo`.
* Exact three-slope tensor/circuit linear algebra.
* R36 `TwelveSlopeLowerBound`:

  $$
  \text{quadratic-Gauss paired-ruling baseline}\Rightarrow k\ge12.
  $$
* R38 translated-cofactor Wiener domination.
* R39 `AllSlopeWienerOptimality` for its unrestricted linear-convolution model.
* R40 canonical-cofactor qualitative method-limit construction.
* R41 pure alternating Plücker zero-target theorem under a constant real structure.
* R42 `MixedPlueckerNoCancellation` under a constant real structure and constant separator.

The final CORE summary itself records the correct R39–R42 domains rather than treating them as global theorems.

### Routes genuinely closed by Rounds 24–42

1. Using the \(+1\)- or even-\(+1\)-supported **mixed PSD relaxation** as a rank-one obstruction.
2. A shear-invariant baseline ray.
3. Baseline lifts with at most 46 occupied nontrivial shear characters.
4. A bordered single symmetric quadratic Gauss core.
5. Per-row deformations of one Gauss core below the certified \(777716\) support threshold.
6. Genuine two-core Gauss mixtures.
7. Arbitrary-rank mixtures on one paired ruling slope.
8. Arbitrary-rank mixtures on exactly two paired ruling slopes.
9. Every quadratic-Gauss paired-ruling baseline ansatz using at most eleven slopes.
10. The specific unweighted scalar Cauchy/Parseval route audited in R37.
11. Translation-invariant linear-convolution improvements beyond constant \(1\) in R39's model.
12. Pure alternating Plücker assistance under a constant real structure.
13. Any constant alternating \(tJ\) improvement to a fixed symmetric constant separator under a constant real structure.

None of those is an exhaustive class of all physical solutions.

## `EQUIVALENT`

* R25 `RealRankTwo`.
* PSD trace-one `RankTwoNewton`.
* Shear-coordinate line/orbit/RowCAZAC formulation of the baseline problem.
* Fixed-\(k\)-slope tensor annihilator conditions.
* Three-slope complete circuit family for linear span membership.
* R33's stated resultant/common-base-point equivalences under its finite-base-locus and nondegeneracy hypotheses.

## `NECESSARY-ONLY`

* `EvenPlusPSD` without rank one.
* Collision and polygon tests.
* Purity/trace lower bounds that are not attained.
* Shear-breaking norm.
* 47-character lower bound.
* Target-ray/core-count lower bounds.
* Multi-slope dimension/submersion counts.
* The R31/R32 affine-dimension and low-Schur-rank conditions before R33.
* \(k\ge12\) inside the Gauss paired-ruling ansatz.
* R42's surviving symmetric-separator optimization conditions.

## `CORRECTED`

* R28 dictionary count:

  $$
  970353651\ \to\ 604842954373.
  $$
* R29 rank-one cross-ruling differences may lie on a third ruling.
* R33 does not infer a triple common root from pairwise common roots.
* Projective roots at infinity and identically-zero pencil cases require explicit treatment.
* R41 “any valid linear use” is too broad; only its direct alternating pointwise class was established there.

## `NOT_CHECKED`

* Package-02-independent proof of the R23 quantitative edge bounds imported into the universal R24 frozen-edge spectral-floor theorem.
* R37 Section-14 abstract norm-data relaxation as a fully feasible coefficient construction.

## `NUMERICAL-ONLY`

* Machine-precision baseline lifts at small primes.
* Observed slope thresholds/full-character occupancy at those primes.
* Numerical conditioning/singular-value reconnaissance not accompanied by an exact transfer argument.

## `CONJECTURED`

* A dense full-character frozen-prime baseline lift.
* Any continuation of the small-prime solution branch to the frozen prime.
* A twelve-slope Gauss baseline existence/nonexistence theorem beyond the proven \(k\le11\) exclusion.
* Any stronger conclusion from the incomplete R37 norm-data construction.

## `OPEN` — structured/one-edge level

* Quadratic-Gauss baseline mixtures with \(k\ge12\).
* Dense genuinely nonquadratic baseline solutions.
* The unrestricted baseline two-spike pure-edge problem.
* Pure retrieval for \(z_\star\).
* Pure retrieval for \(h_\star\).
* General nonzero-edge pure retrieval.
* Cross-edge rank-one consistency.
* Symmetric constant-separator optimum in R42.
* General-slope constant matrix separators without a constant real structure.
* Frequency-dependent/global cross-\(\nu\) matrix separators.

CORE explicitly retains the symmetric \(S\) problem and the genuinely complex/rank-two/global branches after R42.

## `OPEN` — global targets, kept separate

* Physical liftability of \(x^{(10)}\).
* An exact physical vector with \(\mathcal F_\Gamma>10\).
* PW10.
* The all-copy physical-output purity gate.
* A positive regularized defect for one fixed finite pair.
* The Hayden–Penington full-size extensive Holevo/MOE theorem.

No ansatz result above changes any of these statuses.

---

# 8. First remaining unknown

There are two useful ways to state the first unresolved boundary.

### Earliest exact frozen-edge unknown

Already after R24–R25, for

$$
z_\star=(0,1),
$$

the first unresolved pure question is

$$
\boxed{
\exists v:\quad
\Pi_{+,\mathrm{ev}}v=v,\qquad
|v_p|^2=q_{z_\star}(p)\quad\forall p?
}
$$

Equivalently, with

$$
\mathcal K_{z_\star}
=
\{G\succeq0:
\operatorname{diag}G=q_{z_\star},
\ \Pi G=G\Pi=G\},
$$

is

$$
\boxed{
\inf_{G\in\mathcal K_{z_\star}}
\left(
1-3\operatorname{Tr}G^2+2\operatorname{Tr}G^3
\right)=0?
}
$$

No R24–R42 result answers that question. The mixed-state witnesses do not, and the later baseline structured ansatzes do not constitute an unrestricted reduction from \(q_{z_\star}\).

### First unrestricted case left after the R27–R42 structured baseline campaign

After sending the two exceptional baseline points to \(\pm e_1\), the still-open statement is simply:

$$
\boxed{
\exists v:\quad
\Pi_{+,\mathrm{ev}}v=v,
}
$$

with

$$
|v(\pm e_1)|^2
=
\frac{D+1}{D(D+2)},
\qquad
|v(p)|^2
=
\frac1{D(D+2)}
\quad(p\ne\pm e_1)?
$$

Rounds 27–42 exclude many **representations** of such a vector—sparse shear, bordered/Gauss, one/two slopes, up to eleven paired Gauss slopes, and several separator methods—but do not exhaust the ambient even \(+1\)-Fourier space.

That unrestricted baseline existence question is therefore still `OPEN`.

---

# 9. Final audit verdict

$$
\boxed{\texttt{NO MATERIAL ERROR FOUND IN CHECKED SCOPE}}
$$

This verdict is deliberately narrower than “the package is proved.” The checked load-bearing R24–R42 reductions and ansatz no-go theorems survive, subject to the explicit `NOT_CHECKED` predecessor dependency and the corrections above. The actual errors found—R28's dictionary arithmetic, R29's ruling-direction wording, and R41's overbroad wording—do not invalidate a downstream load-bearing theorem. R37's under-specified relaxation is not promoted.

The corrected endpoint is:

$$
\boxed{
\begin{gathered}
\text{R33 arbitrary-rank two-slope Gauss no-go: PROVED, ansatz only;}\\
\text{R36 at-least-12-slope result: PROVED, ansatz only;}\\
\text{R42 constant }S+tJ\text{ no-cancellation: PROVED under constant real structure;}\\
\text{unrestricted baseline/pure frozen edges/physical phase lift: OPEN.}
\end{gathered}
}
$$

**PW10 remains OPEN. The all-copy physical-output purity gate remains OPEN. The fixed finite-pair regularized-defect target remains OPEN. The Hayden–Penington full-size extensive Holevo/MOE theorem remains OPEN.**

In particular, the **full-size theorem remains OPEN**: this audit supplies no complete line-by-line proof of every required unrestricted global step.
