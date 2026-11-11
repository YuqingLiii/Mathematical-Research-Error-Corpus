# Round 23 local audit

## Verdict

`PARTIAL ADVANCE — ONE CORRECTION — PW10 OPEN`

Round 23 produced a valid analytic witness showing that the rank-relaxed
two-basis marginal test is feasible for every frozen edge `h`. More
importantly, the edge identity strengthens to the exact eigenvector equation

\[
\mathscr F d_h=d_h.
\]

The response did not construct a pure edge vector for either requested
nonzero edge, did not assemble a common rank-one coefficient matrix, and did
not prove or disprove PW10. Its final open status is therefore correct.

There is one definite but non-central error: for the antisymmetric symplectic
Fourier kernel used here, `mathscr F^2=I`, not phase-space reflection.
Evenness of `d_h` follows from Hermiticity of `alpha`, not from squaring this
Fourier transform.

## Capture receipt

- Browser completion indicator: `Worked for 11m 26s`.
- Exact response copies:
  `artifacts/web-gpt56sol-pro/round-23-response.md` and
  `outputs/round-23-gpt56sol-pro-response.md`.
- Both response files are byte-identical to the browser `Copy response`
  payload.
- Response SHA-256:
  `a599b8aaf756c1aef06ce7f78582f59f9cf22d56c98a4f02e8794c1a1ff3688e`.
- Response size: 21,755 Unicode characters, 21,761 bytes, and 1,388 newline
  characters.
- Prompt source and archived sent copy are byte-identical, with SHA-256
  `d996deb7742792dde8266db941a061bf70122969ecd5a7ee66322d669b046fc0`.
- The browser-copied send payload equals the prompt with its single terminal
  newline removed; its SHA-256 is
  `580f65c1831025fef65340d79f7b64dd8242ae9299fb151fde56868370102eb4`.

## VERIFIED

### 1. Edge Fourier and the stronger eigenvector identity

The independently checked identity is

\[
\widehat d_h(k)
=D\alpha_{h/2+k}\alpha_{h/2-k}.
\]

Hermiticity gives

\[
\alpha_{h/2-k}=\overline{\alpha_{k-h/2}},
\]

so its right side is exactly `D d_h(k)`. With the normalized symplectic
Fourier transform

\[
(\mathscr Ff)(k)=D^{-1}\sum_p f(p)\omega^{[p,k]},
\]

this proves `mathscr F d_h=d_h`. The half-labels and signs were also
reproduced by direct random-projector checks at `D=3,5,7`.

The separate relations

\[
d_h(-p)=d_h(p),\qquad
d_{-h}(p)=\overline{d_h(p)}
\]

follow directly from `alpha_{-z}=conjugate(alpha_z)`.

### 2. Centering and autocorrelation

Removing the two endpoint terms `p=plus_or_minus h/2` gives the stated
`CenteredEdgeFourier` equation. At `k=h/2` its phase factor is one and it
reduces exactly to

\[
\sum_u\beta_u\beta_{h-u}\omega^{[u,h]/2}
=(D-2)\beta_h,
\]

the previously audited oriented centered-idempotence coefficient equation.
The `h=0` formula `widehat d_0^beta(k)=D x_k-1` is also correct.

Parseval with `D^2` phase-space points gives the stated exact
`EdgeAutocorrelation` identity, including the negative Fourier sign.

### 3. Frozen pointwise and energy bounds

Using the exact Sidon-spectrum bound `-m <= lambda_z <= M`, every nonzero
entry obeys

\[
\gamma\le x_z^{(10)}\le U,
\]

where

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)},
\qquad
U=\frac{11}{D+1}+\frac{10}{M}.
\]

Exact rational checks give

\[
U=5.4166514736151412\times10^{-17}<7\times10^{-17},
\]

\[
D\gamma=0.9999999793884637\ldots>1-3\times10^{-8}.
\]

The previously derived exact norm relation for `eta=x-b`, together with
`O_10<=M U`, yields

\[
\|\eta\|_2^2
\le \frac{200}{D+1}+\frac{200}{M}
<\frac{49}{4\cdot10^{16}}.
\]

Exact squaring, with no floating-point square-root inference, verifies

\[
2\|b\|_2\|\eta\|_2+\|\eta\|_2^2
<\frac{53}{5\cdot10^8}.
\]

Consequently, for every nonzero `h`,

\[
D^2\gamma^2\le E_h<1+1.06\times10^{-7},
\]

and the checked lower endpoint is

\[
D^2\gamma^2=0.9999999587769279\ldots.
\]

### 4. Phase-free one-edge tests

The two distributions are identical because `x` is even:

\[
q_h(p)=\widetilde q_h(p).
\]

The response's crude but rigorous collision bound is valid. Direct exact
rational evaluation of its stated envelope gives

\[
2\sum_pq_h(p)^2
<1.5274468280089911\times10^{-29}
<5\times10^{-29}.
\]

For every nonzero shift, all edge-product lengths are positive and their
total is at least `D^2 gamma^2`, whereas twice the largest length is below
`2U`. Thus the reverse-triangle endpoint is zero. The frozen
autocorrelation target is bounded by

\[
\frac2{D+1}+\frac{53}{5\cdot10^8}
<1.07\times10^{-7}
<D^2\gamma^2,
\]

so each individual polygon test passes. These are only separate
autocorrelation tests; they do not ensure a single globally consistent phase
assignment.

The exact computations of `h_star` and the third Sidon label are correct:

\[
h_\star=(970330475,1940660948),
\]

\[
a_2=(1940660952,15525287596).
\]

### 5. Analytic two-basis PSD witness

Let `N=D^2`, and let `F` be the normalized symplectic Fourier matrix. The
proposed matrix

\[
K^{(h)}=\operatorname{Diag}(q_h)
+F^*\operatorname{Diag}(q_h)F-N^{-1}I
\]

has trace one and diagonal `q_h` in both bases. The exact frozen bounds imply

\[
q_{\min}\ge\frac{\gamma^2}{E_h}>rac1{2N}.
\]

Writing `q_h=q_min 1+r`, with `r>=0`, gives

\[
K^{(h)}=
(2q_{\min}-N^{-1})I
+\operatorname{Diag}(r)
+F^*\operatorname{Diag}(r)F\succeq0.
\]

This proof is exact and applies to every nonzero `h`. The matrix identities
and decomposition were also checked numerically at `D=3,5,7`.

### 6. Cross-edge rank-one consistency

The reconstruction

\[
Y_{a,b}=d_{a-b}((a+b)/2)
=D^{-1}\widehat d_{a-b}((a+b)/2)
=\alpha_a\overline{\alpha_b}
\]

is correct. It implies

\[
Y_{a,b}Y_{b,c}=x_bY_{a,c}
\]

and the three-label phase cycle. Its magnitude is automatic, so the
displayed triangle gives no magnitude-only contradiction for the frozen
pseudo-point. It is a genuine condition lost when the edge problems are
relaxed independently.

The response also correctly distinguishes this raw coefficient-matrix cycle
from the Weyl-cocycle-weighted orbit Bargmann moment. Summing a termwise
rank-one identity over triples in `A` does not create a new scalar
obstruction.

## CORRECTED

The sentence saying that the Fourier eigenvalue equation implies evenness
because `mathscr F^2` is reflection is false for the transform actually used.
Antisymmetry gives

\[
\begin{aligned}
(\mathscr F^2f)(\ell)
&=\frac1{D^2}\sum_{p,k}f(p)
  \omega^{[p,k]+[k,\ell]}\\
&=\frac1{D^2}\sum_{p,k}f(p)\omega^{[p-\ell,k]}\\
&=f(\ell).
\end{aligned}
\]

Thus

\[
\boxed{\mathscr F^2=I.}
\]

This does not invalidate `mathscr F d_h=d_h`, the PSD witness, or the direct
Hermiticity proof of `d_h(-p)=d_h(p)`.

## NECESSARY-ONLY / TOO WEAK

- The collision and individual polygon inequalities are necessary but far
  from excluding either requested nonzero edge.
- The analytic `K^(h)` is a mixed-state marginal witness. It need not have
  rank one and need not be supported in the `+1` Fourier eigenspace.
- Separate pure edge solutions, even if found, still have to assemble into
  one Hermitian rank-one matrix with the fixed diagonal `x`.
- The three-edge phase cycle is not numerically evaluable from magnitudes
  alone.

## OPEN / earliest gap

No exact violating vector, no exact exclusion of `x^(10)`, and no
phase-uniform proof of PW10 was produced. The earliest sharpened gap is:

1. for a selected nonzero `h`, does an even `+1` symplectic-Fourier
   eigenvector exist with squared magnitudes `r_h`;
2. if separate edge vectors exist, can they satisfy the common rank-one
   cross-edge cycles and centered idempotence simultaneously?

Therefore

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

## Local verification artifacts

- `work/verify_round23_pre_send.py`: prompt integrity and frozen arithmetic.
- `work/verify_round23_edge_fourier.py`: direct projector checks at
  `D=3,5,7`.
- `work/verify_round23_web_response.py`: exact capture, rational bounds,
  collision envelope, polygon margins, and the Fourier-square correction.
- `work/verify_round23_psd_witness.py`: Fourier involution, two-basis
  diagonals, trace, PSD decomposition, and small-prime quadratic-form checks.

All four scripts pass `py_compile` and their executable assertions.
