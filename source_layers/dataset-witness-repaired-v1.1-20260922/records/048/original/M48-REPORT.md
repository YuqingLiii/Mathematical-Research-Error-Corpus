# Independent review: first tame `c=2` actual gate

Date: 2026-07-22  
Reviewed packet: `artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/`  
Prerequisites: the `n=18` reduced inventory and the independently **CONFIRMED** `R_out` review  
Write scope: this review directory only

## Verdict

**CONFIRMED.** The first tame `c=2` actual gate is complete and passes both
required caps. The corrected colored transport is semantically consistent,
the reduced `2 x 2` block recoupling has the asserted scalar Gram matrix, the
stored fold vector has the required `theta` and `S11` types, and a fresh
central-action Lanczos calculation recovers all eight rational input weights.

This verdict is limited to this one tame `c=2` gate. It does not claim the
whole T5 program, a second tame gate, or a uniform theorem for all `c>=2`.

## 1. Integrity and independent method

All archived manifests for the reviewed packet, the reduced inventory, the
`R_out` source packet, and the confirmed `R_out` review verify byte-for-byte.

The reviewer did not accept the archived rational `q_mu` values as inputs.
The review script independently:

- enumerates the `nu=(15,2,1)` and `(29,3,2,1)/(14,2,1)` tableau bases;
- rebuilds every seminormal adjacent-generator plan from tableau contents;
- exhaustively audits all 20 color permutations and the unmatched-`nu`
  convention;
- recomputes the raw and reduced block-shuffle dimensions by the Aitken
  determinant;
- acts on the archived `z` with the newly built diagonal-`S17` action;
- runs a fresh eight-step, twice-reorthogonalized Lanczos calculation;
- recovers rational spectral weights from the new floating weights, and only
  then compares them with the archived fractions;
- derives `||t_mu||^2`, `r_mu`, `T_a`, and `T_b` exactly.

## 2. Correct colored transport and disappearance of the unmatched bug

The old unmatched-label failure is absent.

The canonical internal `beta` block initially occupies `nu` labels `0,1,2`.
The base placement permutation is independently reconstructed as

`[4,5,6,0,1,2,3,7,8,9,10,11,12,13,14,15,16,17]`.

Thus the `beta` block is first moved to matched `nu` labels `4,5,6`; the
unmatched label `0` is in the spectator/Pieri block before any coloring acts.
For each of all 20 splits of six labels into two triples, the review checks

`k_images[x] = color_images[x]`,

`n_images[0] = 0`, and

`n_images[x+1] = color_images[x]+1` for every `x=0,...,5`.

Therefore the same `S6` coset representative acts diagonally on the matched
`kappa`/`nu` labels, while unmatched `nu` label 0 is fixed in every split.
The adjacent word sends canonical order to the color image; its reversal is
the inverse. Hence the carrier uses the inverse word and the `theta` pullback
uses the forward word, exactly as required.

This is also checked at representation level: after the base placement, the
two `S3` generators on `nu` labels `4,5,6` intertwine the internal `beta`
representation with residuals `1.87e-16` and `5.76e-16`. This rules out a
mere comment/indexing coincidence.

## 3. Inventory, query type, and reduced block shuffle

Fresh Young-lattice enumeration gives exactly 1,344 `nu` tableaux and 4,896
query-skew tableaux, in exact agreement with the inventory. Fresh seminormal
diagonal, target, and off-diagonal arrays agree entry-for-entry with the
inventory. The archived two query seeds have orthonormal Gram residual below
`1e-15`, and their independently evaluated JM-type residuals are below
`1e-13`.

The Aitken determinant independently gives the apparent unreduced dimension

`f^((29,3,2,1)/(2,1)) = 3,212,127`.

The last-row triviality leaves exactly eight horizontal endpoints. Their
dimensions are

| endpoint | dimension |
|---|---:|
| `(17,2,1)` | 272 |
| `(16,3,1)` | 2,023 |
| `(16,2,2)` | 1,360 |
| `(16,2,1,1)` | 2,040 |
| `(15,3,2)` | 11,765 |
| `(15,3,1,1)` | 14,144 |
| `(15,2,2,1)` | 11,900 |
| `(14,3,2,1)` | 97,664 |

They total 141,168. The independently reconstructed adjacent word has length
42 and moves the final three labels ahead of the first fourteen:

`[14,15,16,0,1,...,13]`.

For the archived reduced `2 x 2` matrix, the fresh Gram calculation gives

`||R^*R-(3640/4437)I_2||_inf = 1.2121e-13`,

with largest off-diagonal entry of `R` equal to `3.5901e-14`. Thus

`R_col_to_car^* R_col_to_car = (3640/4437) I_2`

to the construction precision, with the claimed exact scalar normalization.

## 4. Fold-vector type

Using only the archived `z` and the independently rebuilt carrier actions,
the five reference-`theta` JM residuals are

`9.01e-16, 1.86e-15, 1.78e-15, 2.02e-15, 2.77e-15`.

The ten `S11` generator-fixed residuals range from `2.01e-16` to `5.43e-16`.
Thus `z` lies in the required `theta` JM line and is `S11`-trivial to
floating precision. Its shape is `(1105,2,1344)`.

## 5. Independent central spectrum and rational `q_mu`

The new diagonal-`S17` action uses `s_i` on `kappa` together with `s_(i+1)`
on `nu`, reflecting the fixed unmatched `nu` label. An eight-step Lanczos run
closes with residual `2.10e-9` and returns exactly eight Ritz values:

`49, 59, 61, 63, 72, 74, 76, 88`.

These equal the independently computed content sums of the eight active
partitions. In active-`mu` order, rational recovery from the fresh numerical
weights gives

| `mu` | `q_mu` |
|---|---:|
| `(14,2,1)` | `41785/41743296` |
| `(13,3,1)` | `284075/19380816` |
| `(13,2,2)` | `28615/2608956` |
| `(13,2,1,1)` | `273545/8613696` |
| `(12,3,2)` | `39275/269178` |
| `(12,3,1,1)` | `10555/31059` |
| `(12,2,2,1)` | `150205/346086` |
| `(11,3,2,1)` | `4400/609` |

The maximum numerical discrepancy from the recovered fractions is
`1.42e-14`. Only after this recovery were the archived numerator and
denominator arrays read; all eight agree exactly. Also

`sum_mu q_mu = 254780/31059 = ||z||^2`.

## 6. Exact normalization and actual caps

The normalization was recomputed from

`||t_mu||^2 = C(17,6) * 16/f^mu * q_mu`,

and `r_mu=||t_mu||^2/20`. The results are

| `mu` | `||t_mu||^2` | `r_mu` |
|---|---:|---:|
| `(14,2,1)` | `16714/93177` | `8357/931770` |
| `(13,3,1)` | `51650/93177` | `5165/186354` |
| `(13,2,2)` | `57230/93177` | `5723/186354` |
| `(13,2,1,1)` | `109418/93177` | `54709/931770` |
| `(12,3,2)` | `6284/4437` | `1571/22185` |
| `(12,3,1,1)` | `84440/31059` | `4222/31059` |
| `(12,2,2,1)` | `54620/13311` | `2731/13311` |
| `(11,3,2,1)` | `3200/261` | `160/261` |

Combining these with the 20 positive and 12 exact-zero `|d_(gamma,mu)|^2`
entries from the independently confirmed `R_out` review gives

`long = 160582822829/1705200`,

`tail_1 = 782051881/11126430`,

`tail_2 = 10709998/189225`,

`tail_3 = 105757951/4238640`.

Therefore

`T_a = 160582822829/1705200 = 94172.42718...`

is below `51396202/35 = 1468462.91429...`, and

`T_b = 67576575391/445057200 = 151.837956...`

is below `51396202/1015 = 50636.65222...`.

## Final adjudication

**CONFIRMED: the first tame `c=2` actual gate passes.** No transport mismatch,
unmatched-`nu` leakage, central-spectrum discrepancy, rational-weight error,
normalization error, or cap failure was found.

No DAG, node, note, handoff, paper, `research/ksum`, or git-history file was
modified, and no commit was created.
