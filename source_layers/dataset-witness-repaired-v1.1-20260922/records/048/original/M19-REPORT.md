# Independent review: uniform Pieri effective-rank carrier theorem

Date: 2026-07-22  
Reviewed source: `artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_20260722/`

## Verdict

**CONFIRMED.** For every admissible tame physical sector and every positive
Littlewood--Richardson multiplicity `c`,

\[
 \mathcal R_h=\|\widetilde F L_h\|_{HS}^2
 \le B_\theta(q)\dim\mathscr Y
 \le B_\theta(q)T/c
 \le B_\theta(q)T.
\]

Combined with the already independently confirmed common-line identity and
output-frame inequality, this **closes uniform physical `T-b`** over that
entire scope.  It proves neither `T-a` nor T5 as a whole.

## Independent operator audit

Put `m=C(j,a)`.  The physical colour fold has type

`F: direct_sum_D fibre(D) -> Y`

and, for each uncoloured fibre, is the block row `[U_1 ... U_m]` with every
`U_i` unitary.  Hence

`F F^*=m I_Y`,

so `F~=F/sqrt(m)` is a **coisometry from the coloured intermediate space to
the uncoloured Pieri space**.  The direction matters: `F~F~^* = I_Y`, while
`F~^*F~` is only a projection.  Thus `||F~||op=1` and the reviewed fixed-set
frame gives

`||F~L_h||op^2 <= ||L_h||op^2 <= B_theta(q)`.

The common-line review identifies the full coherent quantity, without colour
pinching or deletion of LR columns,

`R_h=||F~L_h||HS^2`.

The composite has type `carrier -> Y`; therefore its rank is bounded in the
correct direction by the codomain dimension.  Pieri gives

`dim(Y)=C(n-1,j) f^theta`.

The elementary singular-value estimate

`||A||HS^2 <= rank(A)||A||op^2`

then yields `R_h<=B dim(Y)`.

## LR dimension and multiplicities

The LR decomposition is a genuine direct-sum decomposition:

`Ind(V_alpha x V_beta)=direct_sum_theta c_(alpha,beta)^theta V_theta`.

Consequently every positive summand satisfies

`c f^theta <= C(j,a) f^alpha f^beta`.

After multiplying by `C(n-1,j)`, this is exactly `dim(Y)<=T/c`.  Larger LR
multiplicity only strengthens the comparison; it does not create another
copy of `Y`, because the `c` copies live in the carrier domain of `L_h`, while
the physical colour fold still lands in the same uncoloured Pieri module.

An independent LR tableau enumeration and Frobenius-dimension calculation
checks all products through `j=10`, including every positive multiplicity and
the full induced-dimension identity.  Independent Pieri dimension sums are
checked at the zero-width boundary and at two tame values.  Both extreme
colour faces have exactly one LR constituent with multiplicity one.  Thus
`a=0`, `b=0`, higher `c`, and the harmless `j=0` boundary expose no missing
factor or zero-dimensional exception.

## Physical `T-b` implication

The independently reviewed common-line/output-frame chain is

`T_b=sum_mu f^mu r_mu h_mu`,

`(delta_min+1)h_mu <= w_mu <= B_theta(q)`.

If tails are present this gives

`T_b <= B_theta(q) R_h/(delta_min+1) <= B_theta(q)^2 T/(delta_min+1)`.

If there is no tail branch, `T_b=0` directly.  All coherent carrier and LR
directions remain inside `F~L_h`; the proof bounds its image rank and performs
no conditional expectation, maximum-over-branches step, or colour-diagonal
replacement.  Tameness is not used in the algebra beyond ensuring that the
registered modules and physical branches are admissible.

## Exact gates and active falsification

Both independently confirmed tame `c=2` packets were reloaded only after
their manifests passed.  The review independently recomputes `T`, `dim(Y)`,
all eight `f^mu r_mu` normalization identities per gate, the complete carrier
trace, all output-frame inequalities, and the physical tail sum.

| `n` | true rank cap `dim(Y)/T` | `c dim(Y)/T` | `R_h/(BT)` | physical `T-b` |
|---:|---:|---:|---:|---:|
| 18 | `1/5` | `2/5` | `101912/1513017` | PASS |
| 19 | `1/5` | `2/5` | `1075136/15575175` | PASS |

The source report labels `2/5` as the new rank cap.  Strictly, `2/5` is the
more conservative quantity `c dim(Y)/T`; the operator rank cap actually used
by the theorem is `dim(Y)/T=1/5`.  This is a presentation correction that
strengthens, rather than invalidates, the result.

Exact signed-permutation block folds independently check the coisometry
orientation and projection identity.  The LR/Pieri enumeration reaches
multiplicity greater than one.  No counterexample or boundary failure is
found.

## Strict adjudication

| claim | independent verdict |
|---|---|
| `R_h=||F~L_h||HS^2` and `||F~L_h||op^2<=B` | **CONFIRMED from reviewed dependencies and exact type audit** |
| `rank(F~L_h)<=dim(Y)=C(n-1,j)f^theta` | **CONFIRMED** |
| `c f^theta<=C(j,a)f^alpha f^beta` | **CONFIRMED, all positive LR `c`** |
| `R_h<=BT/c<=BT` | **CONFIRMED uniformly** |
| uniform physical `T-b` on all admissible tame sectors/all `c` | **CONFIRMED** |
| uniform `T-a` or completion of T5 | **NOT CLAIMED / NOT INFERRED** |

No DAG, notes, handoff, paper, `research/ksum`, or git-history file was
modified.  No commit was created.
