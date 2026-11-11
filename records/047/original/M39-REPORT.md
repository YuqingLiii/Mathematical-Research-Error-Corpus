# Tame c=2 `R_col_to_car` and `R_in`

## Verdict: COMPLETE

The unique entry-60 carrier gap has been constructed without an ambient `V_(30,3,2,1)` matrix, `G6`, n=7 transfer, or fitting. The source-normalized four-block recoupling is

`R_col_to_car^* R_col_to_car = (3640/4437) I_2`.

In the deterministic JM gauges used by the program,

`R_col_to_car = sqrt(3640/4437) I_2`

up to off-diagonal binary64 residual `3.6e-14`. A common `U(2)` rotation changes this displayed representative but not its Gram, the fold vector's central weights, or either physical trace.

## Reduced construction

The two bracketings are

- carrier: `alpha+row14 -> kappa`, `beta+row15 -> nu`, then `kappa x nu -> LONG` in its two JM copies;
- colored fold: `alpha x beta -> theta` in its two LR copies, then `theta+row29 -> LONG`.

Here `alpha=beta=(2,1)`, `theta=(3,2,1)`, `kappa=(14,2,1)`, `nu=(15,2,1)`, and `LONG=(29,3,2,1)`.

The stored 4,896-dimensional query-skew module is first reduced to its 34-dimensional `S15`-invariant subspace. Imposing the last three JM weights gives nullity two; all reference-weight residuals are below `9.5e-14`. The apparent 3,212,127-dimensional block-shuffle space is then reduced by the last-row triviality to eight endpoint skew modules of total dimension 141,168. The 42 adjacent swaps exchanging blocks of sizes 14 and 3 give the recoupling above.

For the raw fold, the unmatched `nu` label is first placed in the spectator block. The same `S6` coset representative then acts diagonally on `kappa` and `nu`; the carrier uses the inverse adjacent word and the `theta` pullback uses the forward word. The resulting `z=(FL)^*delta_(L,theta)` has all five reference `theta` JM residuals below `3e-15` and all ten `S11`-trivial generator residuals below `1e-15`.

## Eight exact weights

With `q_mu=||P_mu z||^2`, the exact reconstructed values and derived norms are:

| `mu` | `q_mu` | `||t_mu||^2` | `r_mu=||t_mu||^2/20` |
|---|---:|---:|---:|
| `(14,2,1)` | `41785/41743296` | `16714/93177` | `8357/931770` |
| `(13,3,1)` | `284075/19380816` | `51650/93177` | `5165/186354` |
| `(13,2,2)` | `28615/2608956` | `57230/93177` | `5723/186354` |
| `(13,2,1,1)` | `273545/8613696` | `109418/93177` | `54709/931770` |
| `(12,3,2)` | `39275/269178` | `6284/4437` | `1571/22185` |
| `(12,3,1,1)` | `10555/31059` | `84440/31059` | `4222/31059` |
| `(12,2,2,1)` | `150205/346086` | `54620/13311` | `2731/13311` |
| `(11,3,2,1)` | `4400/609` | `3200/261` | `160/261` |

The central Lanczos spectrum is `49,59,61,63,72,74,76,88` to at most `4e-14`, exactly the eight Pieri constituents. Its eighth-step breakdown is `2.11e-9`; all spurious continuation weights in the diagnostic 12-step run were below `1.3e-30`. Simultaneously,

`sum_mu q_mu = 254780/31059 = ||z||^2`,

with binary64 reconstruction residual below `9e-15`. The conversion is the exact Frobenius-reciprocity normalization

`||t_mu||^2 = C(17,6) f^theta/f^mu q_mu`, with `f^theta=16`.

## Actual gates using completed `R_out`

Combining these `r_mu` with the previously completed exact `8 x 4` `R_out` branch masses gives

- `T-a = 160582822829/1705200 = 94172.42718097584`;
- `T-b = 67576575391/445057200 = 151.8379556403087`.

The three tail contributions are `782051881/11126430`, `10709998/189225`, and `105757951/4238640`. Both gates pass their registered caps:

- `T-a <= 51396202/35` with margin `2343440138611/1705200`;
- `T-b <= 51396202/1015` with margin `22468630077569/445057200`.

## Reproducibility and scope

`construct_rcol.py` rebuilds the JM seeds, reduced 9j, literal 20-color fold vector, central weights, rational table, and actual gates. The NPZ persists the two JM seeds, the `2 x 2` recoupling, the source-normalized carrier vector of shape `(1105,2,1344)`, and exact numerator/denominator arrays.

No DAG, note, handoff, paper, or ksum file was edited, and no commit was created.
