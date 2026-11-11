# Round 18 local audit

- Audit completed (UTC): `2026-09-13T03:43:58Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-18-response.md`
- Web-response SHA-256:
  `b1fa58adab6a2b9007273febee95a33b57ec33629b339bf9817fde9bd0afe49d`
- Browser completion indicator: `Worked for 11m 53s`
- Capture equality: the browser response-copy payload, artifact, and output
  copy are text-identical; the two Markdown files are byte-identical, each
  `23,320` bytes, `23,320` Unicode characters, and `1,297` lines.

## Verdict

Round 18 makes one valid cross-line organizational advance, but it does not
settle the physical gate:

\[
\boxed{
\sum_{L,k}\delta_{L,k}^2
=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2,
\qquad
\delta_{L,k}=\operatorname{Tr}
\left[P_{L,k}(R_\alpha^2-R_\alpha)\right].
}
\]

Together with the complete stabilizer MUB, these residuals vanish exactly
when the reconstructed operator is a rank-one projector.  A designated
family of cross-basis `2 x 2` Cauchy inequalities is likewise equivalent to
physicality under the standing Hermiticity, trace-one, and purity-one
hypotheses.  These identities are verified below.

One advertised component does not survive audit.  The response's continuous
"line-shift Hessian" differentiates only `C_ind`, but the same-line cubic
`C_dep` is invariant only under the **discrete** field-character shifts.  It
varies under the continuous balanced-representative deformation used in the
response.  Equations (10.1)--(10.2) are therefore not established necessary
conditions as written.

No compatible phases with `C(alpha)=1` are constructed, and no positive
phase-uniform residual gap is proved.  Consequently `x^(10)` physicality,
PW10, and the finite `r=2` low-`A` gate remain open.

## Line theorem and line-shift Parseval

The response correctly rechecks the Round 17 line theorem.  The exact
half-excess is

\[
Z_L=\sum_{t\in H_L}\zeta_L(t)
=\frac{5(D-m)}{D(m-1)}+\frac{10\ell_L}{M},
\]

so `E_L=2Z_L`, with all factors of two correct.  Both probabilistic bounds
are valid:

\[
\frac{(1-\rho)^2}{4\mathcal E_L}
>\frac{m-1}{176}>60
\]

for one line, and

\[
Z_L<\frac{5m+20}{M}<\frac1{10000},
\qquad
\frac{(1-\rho)^2}{8Z_L}>312.5
\]

for a simultaneous union bound over
`(D+1)(D-1)=D^2-1<2^120` nonzero marginals.  The conditional-expectation
potential is the corresponding finite greedy derandomization.  Thus the
named line, all line factors, and complete stabilizer feasibility remain
closed and verified.

For every independent zero-sum triple on three distinct projective lines,
the six Weyl phases are three copies of `zeta` and three of its conjugate.
Distinct unordered triples give distinct product-shift characters; `T` and
`-T` are inverse distinct characters because `D` is odd.  Therefore both
Parseval formulas are correct:

\[
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=\frac{36}{D^4}\sum_T r_T^2x_ux_vx_w
\]

and

\[
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=\frac6{D^4}\sum_{u,v\ \mathrm{independent}}
r_{u,v}^2x_ux_vx_{-u-v}.
\]

The independent checker explicitly verifies the sixfold multiplicity and
character injectivity for `p=3,5`, and enumerates the full line-shift second
moment for `p=3`.

## Sharpened frozen RMS bound

Self-Fourier symmetry gives the exact convolution identity

\[
\sum_{u,v}x_ux_vx_{-u-v}=D\sum_zx_z^3.
\]

For the exact nonzero cap

\[
U=\frac{11}{D+1}+\frac{10}{M},
\]

the already audited integer comparison gives

\[
U<\frac1{135873434^2},
\qquad
(D-1)U^2<10^{-14}.
\]

Thus

\[
\boxed{
\mathbb E_\kappa|C_{\rm ind}|^2
\le\frac6{D^3}\left[1+(D-1)U^2\right],
\qquad
\operatorname{RMS}(C_{\rm ind})<2.682\times10^{-27}.
}
\]

This is a correct average statement and not a uniform upper bound.  The
response's three-coordinate example

\[
F(\kappa_1,\kappa_2,\kappa_3)
=\frac{h(\kappa_1)h(\kappa_2)h(\kappa_3)}{(1-1/D)^3},
\qquad
h(s)=\mathbf1_{\{0\}}(s)-1/D,
\]

has supremum one but squared `L2` norm `1/(D-1)^3`.  It correctly proves
that support on three line coordinates plus a `D^(-3/2)` RMS scale alone
cannot control the supremum.  It is not itself the frozen cubic or a physical
counterexample.

## Verified MUB residual SOS

For the complete set of `D(D+1)` stabilizer projectors,

\[
\sum_{L,k}P_{L,k}\otimes P_{L,k}=I+F.
\]

Pairing this identity with
`H tensor H`, where `H=R_alpha^2-R_alpha` and `Tr H=0`, proves

\[
\sum_{L,k}\delta_{L,k}^2=\operatorname{Tr}H^2.
\]

The stabilizer projectors span all Hermitian matrices because Fourier
inversion within each basis recovers the Weyl labels on that line and the
projective lines partition the nonzero labels.  Hence all residuals vanish
if and only if `H=0`, equivalently `R_alpha` is a rank-one projector.

This is a valid structured SOS with `D(D+1)` scalar residuals.  It is also a
repackaging of the full global idempotence condition, not a phase-free
certificate that excludes the frozen magnitude profile.

## Verified cross-basis characterization

For rank-one projectors `P,Q`, positivity of `R` implies

\[
\operatorname{Tr}(PRQR)
=|\langle\phi|R|\chi\rangle|^2
\le\operatorname{Tr}(PR)\operatorname{Tr}(QR).
\]

Choose one distinct partner basis `tau(L)` for every stabilizer basis.  If
the inequality holds for all `P_(L,k),P_(tau(L),j)`, summing over `j` gives
`delta_(L,k)<=0`.  The `D` residuals on each line sum to zero, so all vanish;
the spanning argument then gives `R^2=R`.  Conversely a rank-one projector
makes every inequality an equality.  The equivalence is correct under the
standing assumptions.  The indexed system contains exactly

\[
D^2(D+1)
=834676191481542500102529837710713256761115423061571062
\]

inequalities.  Stabilizer positivity is physically necessary but is not
actually used in this sufficiency implication.

## Verified quantitative detection of the known field

For eigenvalues `mu_j` of a Hermitian trace-one, purity-one `R`,

\[
1-C
=\sum_j\mu_j^2(1-\mu_j)
\le\sqrt{\sum_j\mu_j^2}
\sqrt{\sum_j\mu_j^2(1-\mu_j)^2}
=\sqrt{\operatorname{Tr}(R^2-R)^2}.
\]

Combining this with the known field's

\[
C\le c_0=2\sqrt{3/D}-1/D
\]

proves total residual mass at least `(1-c_0)^2`.  The response's zero-sum
residual argument and averaging over a partner basis then yield an
existential cross-basis violation of at least

\[
\frac{1-c_0}{D\sqrt{D(D^2-1)}}
>1.1625\times10^{-45}.
\]

The direction, powers of `D`, exact indexed count, and decimal enclosure all
check.  This detects the already known nonphysical phase field; it does not
detect every phase assignment with the same magnitudes.

## Rejected continuous Hessian step

The line shifts preserving `C_dep` are the finite transformations

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}\omega^{\kappa_Lt},
\qquad \kappa_L\in\mathbb F_D.
\]

The response differentiates instead through

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}e^{i\bar t\theta_L}
\]

using balanced integer representatives.  That continuous path preserves
magnitudes and Hermiticity, but not the dependent cubic.  Set
`t=(D-1)/2`.  The same-line zero-sum triple with coordinates `t,t,1` has
balanced integer sum `D`, so its monomial acquires `e^(iD theta_L)` rather
than remaining fixed.  Its inverse triple supplies the conjugate term.  For
all-positive compatible phases the frequency-`D` coefficient is strictly
positive, making the variation explicit.

Consequently a maximum of total `C=C_dep+C_ind` does not imply the response's
stationarity or Hessian condition for `C_ind` alone.  The valid discrete
replacement, if the unshifted field is physical, is

\[
C_{\rm ind}(\kappa)\le C_{\rm ind}(0)
\quad\text{for every discrete line shift }\kappa.
\]

This yields finite-difference constraints, not the claimed continuous
Hessian.

## Verification receipts

- `work/verify_round18_web_response.py` checks the captured response hash,
  frozen rational and integer bounds, RMS enclosure, MUB two-design and SOS
  normalizations at `p=3`, the rank-one cross-basis equalities, the defect
  inequality, the quantitative violation, and a small-prime counterexample
  to continuous invariance of the same-line cubic.  Result: `PASS (with
  Hessian flaw detected)`.
- Web-response checker SHA-256:
  `685604d170436a6739e347a13bb91caf421bcb498b68ef83226ad901fa2943da`
- `work/verify_round18_line_shift_parseval.py` independently checks the
  six-permutation and Parseval convention, explicit character injectivity at
  `p=3,5`, the normalized self-Fourier convolution factor, and frozen caps.
  Result: `PASS`.
- Parseval checker SHA-256:
  `b69a40003e886b1adc3c231c30b296421a9ba3f92377b3b7e4133312e34ec110`
- Independent Parseval derivation:
  `work/round-18-independent-line-shift-parseval.md`
- Parseval derivation SHA-256:
  `5eb04e96f15fdf421d44ad74a8683db0259b02dfdbabe296da5b76ed8272fa5c`
- Independent cross-line audit:
  `work/round-18-independent-cross-line-sos-audit.md`
- Independent cross-line audit SHA-256:
  `0519ef16fea441fc65e9c2c3f5c04083578635e30f7fa4cbc4b8af6a6a539920`

Both Python files pass `py_compile`.

## Corrected status ledger

### VERIFIED

- The Round 17 line-factor theorem, both union bounds, and greedy rule.
- Feasibility and insufficiency of the complete stabilizer layer.
- `SixPerm` and both `ShiftParseval` identities.
- The exact self-Fourier convolution identity and RMS bound below
  `2.682e-27`.
- The degree-three spike showing why RMS scale alone is not uniform.
- The complete-MUB two-design and residual SOS identities.
- The designated cross-basis `2 x 2` characterization under the standing
  hypotheses.
- The existential `1.1625e-45` violation bound for the already constructed
  nonphysical field.

### CORRECTED / REJECTED

- The response's continuous line-shift Hessian conditions are invalid as
  written because they omit the varying same-line cubic.
- The exact replacement currently available is a family of discrete
  maximum/finite-difference inequalities.
- The residual SOS and cross-basis system characterize the full physicality
  gate but do not provide a phase-free lower bound for `x^(10)`.

### DISPROVED

- Any inference from the tiny shift RMS to a uniform cubic gap.
- Sufficiency of linewise/stabilizer positivity for physicality.
- Validity of the response's `C_ind`-only continuous Hessian argument as a
  necessary condition.

### OPEN

- Whether `x^(10)` admits compatible phases with `C(alpha)=1`.
- Whether all compatible phases for `x^(10)` have a uniform positive MUB
  residual SOS.
- Whether the exact cross-basis system is feasible for `x^(10)`.
- Whether a different objective-above-10 magnitude profile has a physical
  lift.
- PW10 for the exact frozen tuple.
- The finite `r=2` low-`A` gate and all downstream conclusions.

Even excluding `x^(10)` would not prove PW10 for every physical magnitude
profile.  No quantifier promotion is made.
