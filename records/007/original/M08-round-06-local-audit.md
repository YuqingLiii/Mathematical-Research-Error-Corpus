# Round 06 independent local audit

## Capture integrity

- Conversation: `Audit quantum construction`
- Mode/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator: `Worked for 20m 30s`
- Captured response: 31,934 bytes; 31,898 Unicode characters
- SHA-256: `9fb8abbde279c6c61c9294fa24f57a84ed140e921eeacb056c83cf88f885e55d`
- The artifact and output copies are byte-identical.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 6 does not prove or disprove `(E1_gap)`. Its main negative result survives audit: the full scalar relaxation, and even a substantially stronger relaxation in which the Liouville and Choi sides are built separately, remain feasible. The first unresolved implication in this proof route must use the fact that the same map supplies both sides through exact realignment together with the pair-difference/autocorrelation structure.

No conclusion about the separate all-copy gate changes.

## Claims independently verified

1. **Realignment defect.** Equal Hilbert--Schmidt norms of the Liouville and Choi reshufflings give

   ```text
   I_U - C_U = (m^4/2) ||S-J||_2^2.
   ```

   In the block decomposition, dropping `||P-B||_2^2` yields the advertised `RD-PT2`. After substituting `C_U/m^4=r+x`, it is exactly `x <= (a+b)/2`, and is weaker than `x <= sqrt(ab)` by AM--GM.

2. **Centered alignment.** Centering `B` and `P` on the `n=D^2-1` dimensional traceless space gives the stated upper bound. Both radicands are nonnegative trace-purity defects. The comparison with uncentered alignment reduces to the cosine inequality

   ```text
   xi*zeta + sqrt(1-xi^2)*sqrt(1-zeta^2) <= 1.
   ```

   The response's equality conditions are correct.

3. **Low Choi rank and `D>m`.** The `m` diagonal pair differences are identities and vanish after traceless compression, leaving at most `m(m-1)` rank-one terms. The purity bound `a >= v^2/[m(m-1)]` and the derived `I-rank` inequality follow. Combining PA with `alpha >= D^2/m` gives `D >= (m-A)/(A-1)`; Gap implies `A < 2m/(m+1)`, hence `D>m`.

4. **Contraction.** A convex average of unitary conjugations is a Hilbert--Schmidt contraction. Thus `0 <= S=L^*L <= I`, `Se=e`, `0 <= P <= P_perp`, and `i<=alpha`.

5. **Unitary-Q.** Diagonalizing a unitary `W`, forming the Gram matrix of the `Q(rho_j)`, using its zero-sum vector, and applying `lambda_max(K)<=Tr(K)<=D epsilon` gives

   ```text
   ||Q(W)||_2^2 <= epsilon (D^2-|Tr W|^2).
   ```

   Summing over all pair differences gives `x <= epsilon(D^2-alpha)` with the stated normalization.

6. **Same-map pure-state identity.** For every pure projector `rho_y`, both `Tr[rho_y Phi(rho_y)]` and the Choi-frame quadratic form equal the same average of `|<y|U_b^*U_a|y>|^2`. Expanding `|rho_y>>=e/sqrt(D)+t_y` yields equation (12.2) with the displayed sign and factor `2/sqrt(D)`.

## Exact symbolic checks

The response formulas were re-expanded with exact rational symbolic algebra, not floating-point sampling.

| Formula | Result |
| --- | --- |
| Near-PA factorization (10.3) | Exact identity |
| PA slack (11.5) | `m(m^2+m+10)/5` |
| Contraction slack (11.6) | `m(m-1)^2/25` |
| Both centered radicands (11.7) | Exact and equal |
| Endpoint formulas (11.8), (11.9) | Exact identities |
| Spectral defect `Delta` (13.1) | Exact identity |
| Positivity certificate (13.5) | Exact identity |
| Coherent-state slack (13.6) | Exact identity |

The asymptotics also agree:

```text
lambda_cross    = 2/m - 1/(2m^2) - 101/(8m^3) + O(m^-4),
lambda_parallel = 1/(2m^2) + 101/(8m^3) + O(m^-4).
```

Therefore the weaker `O(m^-3)` statements in the response are valid.

## Scalar-survivor audit

For `q=10`, sufficiently large `m` divisible by `5`,

```text
D=m^2/5,  alpha=m^3/25,  r=m/5,
tau=m^4/125,
i=m(2m-1)/25,
x=0,
```

satisfy Gap, PA, `alpha>=D^2/m`, strict `alpha<D^2`, MM, both trace-purity conditions, B-rank, contraction, block positivity, Unitary-Q, Centered-Align, Pair-energy, and both symmetric-Bell endpoints. Thus a purely scalar contradiction is impossible from the displayed system.

One correction is needed: Section 9 is not literally the *strongest* scalar system obtainable from centered Cauchy--Schwarz, because it omits the companion lower bound

```text
x >= uv/n - sqrt[(a-v^2/n)(b-u^2/n)].
```

Together with `x>=0`, this should be included as a maximum. It does not damage the survivor. For the family above its omitted lower endpoint is exactly

```text
-m(m-1)(m^2-5m-20) / [25(m^2+5)] < 0,
```

so `x=0` still satisfies the corrected two-sided centered inequality.

Section 10 also does not give a full analytic partition of every near-minimal dimension. It proves the narrower, exact statement that when `Xi>0`, feasibility forces the PA slack to exceed (10.4). That is useful but should not be described as a complete dimension-regime exclusion.

## Decoupled operator construction audit

Subject to its explicit relaxation boundary, Section 13 is algebraically sound.

- The two traceless Hilbert--Schmidt sectors have dimensions `D^2/2` and `D^2/2-1`.
- Equations (13.2)--(13.4) give exactly the required trace and purity for `P`.
- Equation (13.5) makes `lambda_parallel>0`; positivity then gives `lambda_cross<u/R_cross<2/m<1`.
- The cross/block projection calculation for a pure state is correct, and (13.6) verifies the uniform coherent-state bound.
- A unitary error basis containing the identity supplies the stated orthogonal cross and block-diagonal traceless unitaries. With `k=m(m-1)`, the frame in (13.10) has trace `v`, purity `a`, rank `k`, and correct Choi marginals.
- `J_tilde=rP_0+B` has the advertised `alpha`, `tau`, and `i`; placing `B` in either spectral sector gives the stated alignment range, and both choices lie inside the very wide endpoint interval.

This is **not** an admissible counterexample to `(E1_gap)`: `J_tilde` is not shown to be the realignment of the chosen `S_tilde=P_0+P`, and its off-diagonal unitary frame is not shown to be the pair-difference frame of one `m`-tuple. The response states those limitations correctly. It proves only that the listed properties, when imposed separately, are insufficient.

The Markdown audit ledger has two malformed rows because vertical bars inside ket/norm notation were not escaped. This is a presentation defect only; it does not change the mathematical claims.

## Earliest remaining gate

Within this chain, the earliest unresolved step is to exploit simultaneously

```text
J = realign(P_0+P)
  = m^-2 sum_(a,b) |U_b^*U_a>><<U_b^*U_a|,
```

the uniform coherent-state bound on `P`, and the fact that the frame is an autocorrelation/pair-difference frame of one frozen tuple. Neither the scalar survivor nor the decoupled model resolves that coupled condition.

Status: **COMPLETED — LOCALLY AUDITED; `(E1_gap)` AND THE FULL-SIZE THEOREM REMAIN OPEN.**
