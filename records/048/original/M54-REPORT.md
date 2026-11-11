# Second tame `c=2` actual gate

## Verdict

**COMPLETE: both exact gates PASS.**

The target is

`n=19, q=38, j=6, theta=(3,2,1), a=b=3, alpha=beta=(2,1), c=2`.

It is strictly tame (`19>3*6`).  This is one finite actual gate, not a
uniform `c>=2` theorem.

## Why this is the second gate

An exact partition/LR enumeration shows that `j=6` is the first size at which
an LR multiplicity two occurs in this family.  At the tame boundary `n=18`,
the already completed `(3,2,1);(2,1),(2,1)` gate is the only admissible
`c>=2` sector.  Holding the small partitions fixed and increasing to `n=19`
is therefore the unique computationally nearest second tame gate.

This choice also has the highest mechanism information gain: it preserves the
two LR copies, the eight diagonal common-line blocks, and the long plus three
tail branches, while moving one step from the boundary into the strict tame
interior.  It tests whether the reduced recoupling algorithm itself reuses;
no numerical stability law from `n=18` is assumed.

## Reuse versus new construction

Reused, after all three source manifests were verified:

- standard/skew tableau enumeration;
- sparse seminormal generator construction;
- exact trivial-line squared-coordinate propagation;
- matrix-free query embedding, block shuffle, colored fold, and central
  Lanczos algorithms.

Constructed anew for `n=19`:

- the `V_(16,2,1)` and `(31,3,2,1)/(15,2,1)` rowword inventories;
- all sparse generator plans;
- the `S^((32,3,2,1)/(3,2,1))` fixed-fibre vector;
- every one of the `8x4` exact `R_out` masses;
- the reduced `2x2` color-to-carrier recoupling;
- the literal coherent 20-color fold vector `z`;
- the diagonal-`S18` central spectrum and eight weights;
- all exact `q_mu`, `||t_mu||^2`, `r_mu`, branch values, `T_a`, and `T_b`.

No `n=18` numerical witness (`R`, `z`, `q`, or branch mass) is used as input.
The script records every mechanical source-code adaptation and aborts if an
expected adaptation token is absent.

## Matrix-free dimensions and checks

| object | dimension |
|---|---:|
| `V_(16,2,1)` tableau basis | 1,615 |
| query skew `(31,3,2,1)/(15,2,1)` | 5,814 |
| fixed-fibre skew `(32,3,2,1)/(3,2,1)` | 29,760 |

The largest generator involution residual is `2.23e-16`.  The exact `R_out`
construction has 20 supported and 12 forced-zero entries.  Its four aggregate
checks are

| branch | `sum_mu f^mu |d_(gamma,mu)|^2` |
|---|---:|
| long | `18897879/64` |
| tail 1 | `4641/8` |
| tail 2 | `41769/64` |
| tail 3 | `4095/8` |

All equal the independently prescribed fibre aggregates exactly.

The new reduced block satisfies

`R_color_to_carrier^* R_color_to_carrier = (2240/2697) I_2`

with off-diagonal residual `5.29e-14` and diagonal mismatch `1.60e-13`.

## Eight input weights

The fresh diagonal-`S18` spectrum is

`60, 71, 73, 75, 85, 87, 89, 102`.

| `mu` | `q_mu` | `||t_mu||^2` | `r_mu` |
|---|---:|---:|---:|
| `(15,2,1)` | `6308/8940555` | `6308/40455` | `1577/202275` |
| `(14,3,1)` | `1061/90272` | `2122/4185` | `1061/41850` |
| `(14,2,2)` | `3733/431520` | `7466/13485` | `3733/134850` |
| `(14,2,1,1)` | `21395/855848` | `8558/8091` | `4279/80910` |
| `(13,3,2)` | `19547/151032` | `3554/2697` | `1777/26970` |
| `(13,3,1,1)` | `112277/373984` | `20414/8091` | `10207/80910` |
| `(13,2,2,1)` | `76863/201376` | `51242/13485` | `25621/134850` |
| `(12,3,2,1)` | `87040/11687` | `10880/899` | `544/899` |

Their exact sum is `67196/8091`.  The maximum discrepancy between the fresh
Lanczos weight and its recovered fraction is `6.83e-15`.

## Exact actual gates

The exact branch contraction gives

`T_a = 204466088827/1438400 = 142148.2819987486...`,

below

`B_theta(38)^2 T = 137582445/64 = 2149725.703125`,

with exact margin `721924840637/359600`.

The three tails give

`T_b = 8391760923/44590400 = 188.1965831883...`,

below

`137582445/1984 = 69345.990423...`,

with exact margin `770943422613/11147600`.

Thus both required caps pass.

## Scope

This artifact proves only this second tame `c=2` actual gate.  It demonstrates
that the matrix-free/reduced-block mechanism can be reused at the adjacent
strict-tame parameter, but it does not prove stability of the numerical
weights, a uniform theorem in `n`, all `c=2` sectors, or any `c>2` statement.

