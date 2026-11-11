# Physical tame `c=2` output recoupling `R_out`

**Verdict: COMPLETE** for the requested `R_out` subproblem.

The physical Pieri-to-completion/query reduced transform is constructed without an ambient `V_(30,3,2,1)` basis, and all `8 x 4` values `|d_(gamma,mu)|^2` are obtained exactly. Twelve entries vanish by Pieri support; the other twenty are positive rational numbers.

This result does not construct `R_in`, the eight `t_mu` norms, or the final tame gate contractions.

## 1. Reduced recoupling space

Fix one unit reference tableau of `theta=(3,2,1)`. The fixed-six-set fiber inside `V_lambda`, `lambda=(30,3,2,1)`, is controlled by the skew Specht module

```text
S^(lambda/theta),  dim = 24360.
```

Because `lambda/theta` is a horizontal 30-strip in the LR sense, this skew module contains one `S30`-trivial line. Let `w` be its unit vector. It is the reduced fixed-fiber vector appearing in the physical synthesis map.

For every branch child `tau_gamma` and active `mu`, the alternate subgroup chain is

```text
theta --add horizontal 11-strip--> mu
      --add horizontal 18-strip--> tau_gamma
      --add the query corner------> lambda.
```

When both Pieri coefficients are one, this defines a unit `S11 x S18`-trivial chain vector `v_(gamma,mu)`. When `tau_gamma/mu` is not a horizontal 18-strip, the chain is absent and the corresponding `d` is exactly zero.

The twenty supported chain spaces have disjoint tableau supports and exhaust the reduced space:

```text
sum_(gamma,mu) support_dimension = 24360 = dim S^(lambda/theta).
```

Thus they give the complete reduced `R_out` decomposition.

## 2. Exact seminormal construction

No eigenspace rationalization is used. For a seminormal adjacent-generator block with axial distance `d`, the simultaneous `+1` equation gives the exact squared-coordinate ratio

```text
weight(swapped tableau) / weight(tableau) = (d-1)/(d+1).
```

The code propagates these ratios as `Fraction` objects over each tableau graph and normalizes their exact sum. It constructs:

- the unique `S30`-trivial squared weights of `w` in all 24,360 coordinates;
- the unique `S11`-trivial weights from the previously built eight Pieri seeds;
- the unique `S18`-trivial weights for every supported `tau_gamma/mu`.

On each supported chain component, the exact ratio

```text
weight_w(T) / (weight_left(T_left) weight_right(T_right))
```

is constant over every tableau `T` in that component. Therefore

```text
|c_(gamma,mu)|^2 = |<v_(gamma,mu),w>|^2
```

is exactly this rational constant. This is an identity in the seminormal representation, not a fit to aggregate data. The floating vector retained for convenient replay has worst `S30` `+1` residual `8.76e-17`.

## 3. Physical normalization

Let

```text
Y = Ind_(S6 x S11)^S17(V_theta tensor 1),
N = C(17,6) = 12376,
f^theta = 16.
```

For a reference fiber coordinate, the multiplicity-free `mu` Fourier projector has diagonal weight

```text
f^mu / (N f^theta).
```

Frobenius reciprocity between this induced normalization and the unit chain vector gives

```text
|c_(gamma,mu)|^2
  = f^mu/(N f^theta) |d_(gamma,mu)|^2,
```

or equivalently

```text
|d_(gamma,mu)|^2
  = C(17,6) f^theta/f^mu |c_(gamma,mu)|^2.
```

The raw color fold has `||phi_mu||^2=C(6,3)=20`, so the corresponding branch mass is

```text
a_(gamma,mu) = 20 |d_(gamma,mu)|^2.
```

## 4. Exact `8 x 4` result

Columns are the long branch followed by the three tails of weights `29,31,33`.

| `mu` | `|d_long,mu|^2` | `|d_tail1,mu|^2` | `|d_tail2,mu|^2` | `|d_tail3,mu|^2` |
|---|---:|---:|---:|---:|
| `(14,2,1)` | `17391/78400` | `459/45472` | `51/11600` | `153/64960` |
| `(13,3,1)` | `17391/44800` | `0` | `39/2800` | `9/1792` |
| `(13,2,2)` | `52173/125440` | `1023/90944` | `0` | `837/103936` |
| `(13,2,1,1)` | `17391/39200` | `3267/227360` | `429/81200` | `0` |
| `(12,3,2)` | `3069/4480` | `0` | `0` | `31/1920` |
| `(12,3,1,1)` | `1023/1400` | `0` | `11/700` | `0` |
| `(12,2,2,1)` | `3069/3920` | `341/22736` | `0` | `0` |
| `(11,3,2,1)` | `341/280` | `0` | `0` | `0` |

The exact `a_gamma,mu=20|d_gamma,mu|^2` values and exact overlap squares are included row-by-row in the JSON and as numerator/denominator arrays in the NPZ.

## 5. Independent normalization checks

The aggregate constraints were not used to fit or solve the individual values. They were evaluated only after the exact skew recoupling table was complete.

The exact branch overlap sums are

```text
sum_mu |c_(long,mu)|^2  = 89001/89600 = eta_long/16,
sum_mu |c_(tail1,mu)|^2 = 1/448       = eta_tail1/16,
sum_mu |c_(tail2,mu)|^2 = 1/400       = eta_tail2/16,
sum_mu |c_(tail3,mu)|^2 = 1/512       = eta_tail3/16.
```

They sum to one exactly. After physical Fourier normalization, the four previously derived mass constraints are also reproduced exactly:

```text
sum_mu f^mu |d_(long,mu)|^2  = 19669221/100,
sum_mu f^mu |d_(tail1,mu)|^2 = 442,
sum_mu f^mu |d_(tail2,mu)|^2 = 12376/25,
sum_mu f^mu |d_(tail3,mu)|^2 = 1547/4.
```

Further checks:

- 20 supported entries and 12 Pieri-forced zeros;
- exact constant squared-coordinate ratio on all twenty supports;
- chain support dimensions sum to 24,360;
- total exact overlap square equals one;
- two consecutive runs produced byte-identical NPZ, JSON, and log outputs;
- the complete source-packet SHA manifest passes.

## 6. Resource and scope audit

The largest representation vector has length 24,360. Each generator is applied from one/two-sparse seminormal plans. No square matrix of that size is formed. In particular, the computation does not construct:

- the 25,589,760-dimensional ambient `V_lambda` basis;
- an ambient square operator;
- a dense carrier embedding;
- the `4896 x 2688` query-skew embedding.

No old `G6` value, non-tame `n=7` value, aggregate fit, or stability guess is used.

Files:

- `construct_rout.py`: exact reduced recoupling and verification;
- `tame_c2_rout.json`: all 32 exact entries, derivation metadata, and checks;
- `tame_c2_rout.npz`: reusable fixed-fiber vector and exact numerator/denominator tables;
- `tame_c2_rout.log`: concise full table and checks.

No DAG, note, handoff, paper, `ksum` file, or git history was modified, and no commit was made.
