# Round 21 local audit

- Audit completed (UTC): `2026-09-13T05:48:42Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-21-response.md`
- Web-response SHA-256:
  `8b719f8fcebe3298849dcf6b64f25375ad1280e2383fb1dd17c39b4bc750ae7f`
- Browser completion indicator: `Worked for 12m 36s`
- Capture equality: the browser response-copy payload, the artifact copy, and
  the output copy are exactly equal. Each UTF-8 Markdown copy has `24,397`
  Unicode characters, `24,405` bytes, and `1,612` newline characters.

## Verdict

Round 21 does **not** close PW10. It correctly derives the complete
two-line average, the rank-two displacement identities, a global quartic
contraction, the anti-projector symmetry, three weighted coefficient
formulas, and the conditional frozen orbit bound

\[
\mathcal F_\Gamma<\frac{51}{4}.
\]

None constructs a physical phase lift of `x^(10)`, excludes every possible
lift, proves a phase-uniform residual gap, or proves PW10. The exact status is

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

The physical lift of `x^(10)` and the finite `r=2`, low-`A` gate remain open.

## Complete two-line average

The displayed `FullTwoLineAverage` formula is correct. Independent direct
matrix checks at `D=3,5,7` agree with the average of the entire plaquette,
including the covariance terms and the alternating four-cycle. The
nonzero-shift average is exactly `D^2/(D-1)^2` times the all-shift average.

The formula leaves explicit terms such as

\[
\operatorname{Tr}(P\overline X_L\overline X_M),\qquad
\operatorname{Tr}\bigl(P\mathcal K_L(\overline X_M)\bigr),
\]

which are expressed through cross-basis Kirkwood--Dirac and three-point
Bargmann amplitudes. This verifies the narrower statement that the complete
calculation still contains unresolved cross-basis data.

The response's stronger sentence that “no-cancellation is now fully derived”
is not accepted literally. Displaying the combined formula and naming its KD
terms does not prove that the complete expression cannot simplify further on
the physical compatibility locus, nor does it produce a phase obstruction.
No such cancellation theorem is needed for accepting the formula itself.

## Rank-two system and global contraction

For a physical projector `P`, all of the following are correct with the
stated Weyl convention and normalizations:

\[
\Delta_g^3=(1-x_g)\Delta_g,
\qquad
\Delta_g^4=(1-x_g)\Delta_g^2,
\]

the quadratic, cubic, and quartic trace moments, the Weyl expansion of
`Delta_g`, and the coefficientwise twisted-convolution identity. The
phase-free cross-displacement Gram entry

\[
1-x_g-x_h+x_{h-g}
\]

is also correct. For the self-Fourier nonnegative frozen magnitude, its PSD
condition is already inherited from the centered circulant Gram matrix.

Averaging the fourth displacement moment gives

\[
\boxed{
\operatorname{Tr}R^4
=1+\frac4D\bigl(\operatorname{Tr}R^3-1\bigr)
}
\]

and equivalently

\[
\operatorname{Tr}(R^2-R)^2
=2\left(1-\frac2D\right)
\bigl(1-\operatorname{Tr}R^3\bigr).
\]

The Weyl twirls, the alternating-term normalization `S_2/D^2`, and the final
algebra were independently checked on both the projector and anti-projector
branches at `D=3,5`.

## Exact anti-projector symmetry and its scope

The transformation

\[
P\longmapsto \widetilde P=\frac{2I}{D}-P
\]

has trace and purity one, negates every nonzero Weyl coefficient, preserves
all coefficient magnitudes, and sends every displacement to its negative.
The response's eigenvalues and cubic and quartic moments are exact. Hence the
rank-two family and any linear weighted contraction of it cannot serve as a
positivity or pure-versus-anti-pure branch selector.

This symmetry is **not** a no-go theorem for using the uncontracted rank-two
equations to reject this particular frozen magnitude. If those equations
were inconsistent for every phase field with magnitude `x^(10)`, they would
exclude both branches and therefore exclude a physical lift. Round 21 does
not establish either consistency or inconsistency.

## Weighted coefficient extraction

The master kernel `K_w`, right side `R_w`, and all three specializations

\[
w=\mathbf1_\Gamma,\qquad w=\lambda,\qquad
w(g)=\sum_{a\in A}\omega^{[a,g]}
\]

have the correct character signs and powers of `D`. Direct small-prime tests
at `D=3,5` verify the formulas coefficient by coefficient for all output
labels. The claims `z_star=(0,1) notin A` and `z_star notin Gamma` follow from
the strict integer separation of the first coordinates `t_j`.

Two limitations remain:

1. The requested frozen cyclotomic sums at `z_star` were not evaluated.
   They remain symbolic and are replaced by the coarse entrywise cap `U`.
   Thus this is an exact coefficient-specific reformulation, not an exact
   frozen obstruction.
2. The displayed strict simplification

   \[
   \sqrt8\,D\sqrt{\lambda_z^2+M^2+6M}<4DM
   \]

   does not follow from the stated bound `|lambda_z|<=M`. At that envelope,
   the coefficient is

   \[
   4DM\sqrt{1+3/M}>4DM.
   \]

   A sharper estimate for the chosen nonzero `lambda_(z_star)` could repair
   the constant, but none is supplied. This does not change the conclusion:
   either envelope is enormously larger than the fixed right side and gives
   no contradiction.

The lambda- and centered-exponential-sum Cauchy bounds and their frozen
comparisons are otherwise arithmetically correct.

## Orbit channel

`OrbitPurity` is exact. For a hypothetical lift of the frozen magnitude,

\[
x_g\le U=\frac{11}{D+1}+\frac{10}{M}
\]

gives

\[
\mathcal F_\Gamma\le MU
=10+\frac{11M}{D+1}<\frac{51}{4}.
\]

The integer receipt

\[
D+1-4M=161074851798>0
\]

is correct. The third-moment lower and upper bounds, `D>4m^2`, `D<5M`,
`DU<61`, and the strict all-distinct contribution below `60` also check.
After rearrangement they yield only

\[
\frac{\mathcal F_\Gamma^2}{m}-\mathcal F_\Gamma<60,
\]

which is automatic in the relevant range and supplies no improvement.

## Verification receipts

- `work/verify_round21_web_response.py` — SHA-256
  `7ed7f994e35e2e3150982c063a8b8636a9abfa32994b843efa1077a0d336da55`;
  capture, prompt receipt, frozen arithmetic, and unsupported `<4DM` step:
  `PASS` with the limitation detected.
- `work/verify_round21_global_contractions.py` — SHA-256
  `6a32da085811c839fa3485a60751850aa0bc964bc6b6fda9cdd291425a19b77a`;
  anti-projector, global quartic average, weighted master formulas at
  `D=3,5`, and exact frozen inequalities: `PASS`.
- `work/verify_round21_rank_two_displacement.py` — SHA-256
  `03a6dbae1894b5c24d91593fb67177500d9187eb9724efd5c4595f93365d62ad`;
  rank-two displacement identities at `D=3,5,7`: `PASS`.
- `work/verify_round21_two_line_average.py` — SHA-256
  `713a0750b0ebbb82386678420764d7d89498da004178841ec1c3b627063f38a2`;
  complete two-line average at `D=3,5,7`: `PASS`.
- Independent notes:
  `work/round-21-independent-rank-two-displacement.md` — SHA-256
  `e0892fca4b432375d8a5e73a31ab484222ba72cf3b6b16f44d1d97a1a585ecd2`;
  `work/round-21-independent-two-line-average.md` — SHA-256
  `8a91c06a11edb08ede7d32327c490b96923329e960aff187d6f0b474f9286d47`.

All four Python checkers pass `py_compile`.

The first genuinely new Round 21 claim accepted after independent checking
is `RT4-average`, together with the exact anti-projector symmetry. Both are
necessary-only. The earliest unresolved gate remains a physical phase lift
or a phase-uniform exclusion for `x^(10)`; even excluding that one
pseudo-point would still not prove PW10 for all physical magnitudes.
