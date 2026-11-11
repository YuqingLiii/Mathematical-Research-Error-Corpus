# Round 20 local audit

- Audit completed (UTC): `2026-09-13T04:45:34Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-20-response.md`
- Web-response SHA-256:
  `1bf725e86a5e33c84e8c7cc72d42447d8baa3398546e28ccf507cdc27710f5f9`
- Browser completion indicator: `Worked for 11m 37s`
- Capture equality: the browser response-copy payload, the TextEdit plain-text
  capture, the artifact copy, and the output copy are exactly equal.  Each
  UTF-8 Markdown copy has `20,157` Unicode characters, `20,169` bytes, and
  `1,138` newline characters.

## Verdict

Round 20 does **not** close PW10.  It establishes a useful conditional
single-line residual gap, gives a correct universal two-line plaquette
expansion, identifies exact quotient symmetries, and verifies the product-
vector difference-frame identity.  None of these results constructs phases
for the frozen magnitudes or excludes every such phase choice.

The exact current status is therefore

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

The physical lift of `x^(10)` and the finite `r=2`, low-`A` gate remain open.
In particular, `x^(10)` is a pseudo-candidate of **unresolved physical
liftability**; it has not been proved nonphysical.

## Exact single-line slice

Assume conditionally that the unshifted reconstruction is a rank-one
projector `P`.  Shifting one stabilizer line gives `R_s=P+Delta_s`, where in
that line's eigenbasis

\[
q_k=p_{k-s},\qquad d_k=q_k-p_k.
\]

The independently checked exact sum of squares is

\[
\boxed{
f_L(s)=
\sum_kd_k^2(1-p_k-q_k)^2
+\sum_{k\ne j}p_kp_j(d_k+d_j)^2.
}
\]

Using the frozen line-purity bound and the exact coefficient floor

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)},
\]

every nonzero one-line shift obeys

\[
\boxed{
f_L(s)\ge
2\gamma\left(1-2\sqrt{3/D}\right)^2
=2.1241767045114586038878\ldots\times10^{-18}>0.
}
\]

This is pointwise and phase-free, but conditional on the existence of the
unshifted physical lift.  It constrains the Hamming-one boundary of the zero
set; it does not contradict the `D^2` globally displaced physical copies.

## Two-line plaquette

For perturbations `X` and `Y` supported on two distinct stabilizer lines,

\[
R^2-R=H_X+H_Y+XY+YX.
\]

The exact cross term is

\[
\begin{aligned}
 f(X+Y)-f(X)-f(Y)
={}&4\operatorname{Tr}(PX)\operatorname{Tr}(PY)
 -4\operatorname{Re}\operatorname{Tr}(PXY)\\
&+8\operatorname{Re}\operatorname{Tr}(PX^2Y+PXY^2)\\
&+4\operatorname{Tr}(PXYX+PYXY)
 +4\operatorname{Tr}(X^2Y^2)+2\operatorname{Tr}(XYXY).
\end{aligned}
\]

Mutual unbiasedness gives

\[
\operatorname{Tr}(X^2Y^2)
=\frac1D\operatorname{Tr}(X^2)\operatorname{Tr}(Y^2),
\]

but it does not similarly remove the alternating word
`Tr(XYXY)` or the terms containing `P`.  Those retain cross-basis
Kirkwood--Dirac and Bargmann phase data.

The response correctly displays these unresolved terms.  Its later claim
that the **full uniform average over both cyclic shifts** still retains phase
dependence is not established: it explicitly averages only one component
and says the higher terms behave similarly, without calculating the full
plaquette sum or excluding cancellation among all terms.  That no-go claim
is therefore **underived**, not accepted.

## Quotient zero set and the model limitation

For global character shifts

\[
\kappa(g)_L=[g,v_L],
\]

Weyl conjugation gives

\[
R_{\kappa+\kappa(g)}=W_gR_\kappa W_g^*,
\qquad
f(\kappa+\kappa(g))=f(\kappa).
\]

The subgroup `H` has exactly `D^2` elements.  Conditional on a physical
lift, the residual vanishes on `H`, while every nontrivial Hamming-one coset
has the same explicit `SingleLineGap` lower bound.

The response's generic quotient polynomial

\[
F_{\rm model}(\kappa)
=\frac2{D-1}\sum_{a\ne0}{\bf1}\{r_a\ne0\},
\qquad
r_a=\kappa_a-\kappa_0-a\kappa_\infty,
\]

does have zero set exactly `H`, Hamming-one boundary at least `2/(D-1)`,
range at most `2`, and three-line Fourier support.  Exhaustive checks at
`D=3,5` confirm these properties.  It shows that this **coarse package of
properties alone** cannot force a larger residual.  It does not use or test
the actual frozen coefficients, so it does not prove that every quotient-
Fourier route for the frozen instance must fail.

## Difference frame

With `U_a=W_a tensor conjugate(W_a)` and `S_A=sum_(a in A) U_a`, the Sidon
difference property gives the exact identity

\[
\boxed{K_\Gamma=S_AS_A^*-mI.}
\]

For `zeta=psi tensor conjugate(psi)`,

\[
\mathcal F_\Gamma(\psi)
=\|S_A^*\zeta\|^2-m.
\]

Thus PW10 is the product-vector estimate

\[
\|S_A^*(\psi\otimes\bar\psi)\|^2\le m+10.
\]

This reformulation is correct.  An unrestricted operator-norm bound loses
the rank-one vectorization constraint and supplies no closure by itself.

## Independent verification record

- `work/round-20-independent-single-line-slice.md` — SHA-256
  `8c6ccfd55ed5462cc7343d31f4f0850eac94f4f721ffa72306649c3c38660cd6`
- `work/verify_round20_single_line_slice.py` — SHA-256
  `f58d18f5ade1b5279bc16dd66e37a345a9dd7ae14815e41f248b30f016ae6971`;
  exact frozen arithmetic and small-prime checks at `D=3,5,7`: `PASS`
- `work/round-20-independent-two-line-plaquette.md` — SHA-256
  `68b961dfc3172777fc8ca0eeb8488c23ad50560c97eeac494b46f46ba9303164`
- `work/verify_round20_two_line_plaquette.py` — SHA-256
  `e27e922b2486d4e58501a32b7ab9726169e474e283a96a29d0b75dd59554c88c`;
  matrix checks at `D=3,5,7`: `PASS`
- `work/round-20-independent-quotient-frame.md` — SHA-256
  `f12d7e55c3922a5d98561a7f1668365bfe3ad72d4e232340d73f1b691d59d479`
- `work/verify_round20_quotient_and_frame.py` — SHA-256
  `802058c3dea004ba4080aff8b28a56e8cecacf5c87cbe957ba749eb3e279be88`;
  exact quotient and difference-frame checks at `D=3,5`: `PASS`
- `work/verify_round20_web_response.py` — SHA-256
  `eccecac9feeb5ccce9301a23a38db4820aef606b96d4759cf20f1afff59b51f7`;
  capture, frozen-gap, and quotient-model checks: `PASS`
- All four Python checkers pass `py_compile`.

The first genuinely new Round 20 claim accepted after independent checking
is `SingleLineSOS`, together with its exact conditional frozen gap.  The
full-average no-go and the word `nonphysical` are explicitly rejected at
the current evidence level.
