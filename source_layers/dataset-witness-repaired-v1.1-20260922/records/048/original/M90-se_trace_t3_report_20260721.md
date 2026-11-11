# Route T3 proposer report: colored Johnson spectra and von Neumann pairing

Date: 2026-07-21  
Node: `SE.denom.Phi.legal.trace.t3`  
Role/status ceiling: proposer/execution; no completion-tier DAG status is licensed  
Repository scope: writes only in `artifacts/logs_se_trace_t3_20260721/`

## 0. Verdict

**T3: STILL BLOCKED.** Neither (T-a) nor (T-b) is proved uniformly.

The first premise of the advertised scalar Johnson-scheme reduction is false in the
mixed-color range. The colored state set is a transitive diagonal `S_(n-1)`-set, but
when `a,b,n-1-j>0` its orbital centralizer is noncommutative. Already the standard
representation occurs with multiplicity two. The actual fiber space carries an even
larger multiplicity-bearing induced module. Consequently `D_h=L_hL_h^*` is not, in
general, described by one Eberlein/dual-Hahn scalar for each two-colored intersection
type. It is a matrix-valued element of a Schurian coherent-configuration commutant.

There is nevertheless an exact replacement for the proposed scheme statement:
`D_h` and every `A_gamma=S_(h,gamma)^*S_(h,gamma)` are equivariant for the diagonal
`S_(n-1)` action and therefore split into finite multiplicity blocks. The fold/frame
construction makes every single-branch `A_gamma` block rank at most one and gives its
nonzero eigenvalue explicitly as `binom(j,a)` times a normalized character-projector
trace. `D_h`, however, contains genuine matrices `ell_mu ell_mu^*` on multiplicity
spaces. These matrices are the unresolved all-parameter objects.

Two exact hostile gates prove that simultaneous diagonalization cannot be assumed:

| sector | `rank([A_0,D_h])` | `||[A_0,D_h]||_HS^2` |
|---|---:|---:|
| `(4,8,2,(2);1,(1);1,(1))` | 4 | `9604/46875` |
| `(4,8,2,(1,1);1,(1);1,(1))` | 4 | `1024/11907` |

The valid von Neumann bound still passes both gates and all nine archived exact small
gates. What is missing is a uniform majorization inequality for the reduced
multiplicity matrices. The killer, secondary, and larger tame rows have exact/certified
scalar T-a checks but no archived `A,D` spectral construction, so they are not silently
counted as T3 spectral gates. The `c>=2` regime is also untested because the required
`23296 x 1120` multiplicity-resolved carrier embedding is absent.

Status recommendation: keep the T3 node **OPEN** (or at most proposer-level
`CONJECTURED` if the controller wishes to record the exact block reduction), with
`pending-review`. Do not mark it PROVED or REFUTED. The scalar commutative-Johnson
subroute is refuted by the exact mixed-color witness, but the broader matrix-valued
coherent-configuration route remains live.

## 1. Types and the exact symmetry object

Put

\[
 p=n-1,qquad
 \Omega_{a,b}=\{(I,J):I,J\subseteq[p],\ I\cap J=\varnothing,
 |I|=a,\ |J|=b\}.
\]

The matching identifies the first `p` points of `B` with `A^circ`. The diagonal group

\[
 G=S_p
\]

permutes matched coordinates simultaneously on both colors, fixes the query and the
unmatched `B` point, and acts transitively on `Omega_(a,b)`. A reference state has
stabilizer

\[
 H=S_a\times S_b\times S_{p-j},
 \qquad \Omega_{a,b}\simeq G/H. \tag{1.1}
\]

For `s=(I,J)` let `D_s=I union h(J)`. The fiber

\[
 \mathcal F_s=\operatorname{Ran}\Pi_{D_s},\qquad
 \dim\mathcal F_s=r=f^\theta,
\]

is a copy of `V_theta`. On the reference fiber, `H` acts as

\[
 \sigma_\theta=
 \operatorname{Res}^{S_j}_{S_a\times S_b}V_\theta
 \boxtimes \mathbf 1_{S_{p-j}}. \tag{1.2}
\]

Therefore the correctly typed physical fiber module is

\[
 \boxed{\mathscr X_h\simeq\operatorname{Ind}_H^G\sigma_\theta,}
 \qquad \dim\mathscr X_h=\binom pa\binom{p-a}b f^\theta. \tag{1.3}
\]

This is not merely the scalar permutation module on colored sets unless `f^theta=1`
and the stabilizer action is trivial.

With isometries `E_s:V_theta -> F_s`, the `(s,t)` block of the Gram is

\[
 \widehat D_{s,t}=E_s^*P_\xi E_t:V_\theta\to V_\theta. \tag{1.4}
\]

The quadruple

\[
 (u,v,w,x)=(|I\cap I'|,|I\cap J'|,|J\cap I'|,|J\cap J'|) \tag{1.5}
\]

classifies the `G`-orbit of an ordered pair. Thus (1.5) determines a block orbit, but
not generally a scalar block. Changing fiber gauges conjugates the matrices in (1.4).
This is the operator-valued version of the four-overlap formula proved for T2.

### 1.1 Why the orbital algebra is noncommutative

For the scalar state module `C[Omega]=Ind_H^G 1`, the multiplicity of the standard
representation `V_(p-1,1)` equals the dimension of its `H`-fixed subspace. If
`a,b,p-j>0`, `H` has exactly three point orbits (`I`, `J`, and the remainder). Vectors
constant on those three cells and having total sum zero form a two-dimensional space.
Hence

\[
 \operatorname{mult}_{(p-1,1)}\mathbb C[\Omega_{a,b}]=2,
 \qquad
 \operatorname{End}_G\mathbb C[\Omega_{a,b}]
 \supseteq \operatorname{Mat}_2(\mathbb C). \tag{1.6}
\]

So the mixed-color orbitals form a homogeneous Schurian coherent configuration with a
noncommutative adjacency/centralizer algebra, not a commutative association scheme.
When `a=0` or `b=0`, the scalar state space reduces to the ordinary Johnson scheme
`J(p,j)`; this boundary does not cover the full tame range.

For the actual fiber module, Frobenius reciprocity gives the exact multiplicity

\[
 m_\mu^{X}
 =\dim\operatorname{Hom}_H(\operatorname{Res}_H V_\mu,\sigma_\theta)
 =\sum_{\alpha',\beta'}
 c_{\alpha'\beta'}^\theta
 c_{\alpha',\beta',(p-j)}^\mu. \tag{1.7}
\]

The last coefficient is the iterated LR coefficient. This is the correct
representation-theoretic substitute for a scalar bi-Johnson eigenmatrix.

## 2. Exact spectrum of `D_h` in reduced form

The strict carrier has type

\[
 \mathcal C=P_\xi V_\lambda,qquad
 \dim\mathcal C=f^\kappa f^\nu c.
\]

Restricting from `S_p x S_n` to diagonal `G=S_p`, branching of `V_nu` over the
unmatched point gives

\[
 \mathcal C\downarrow_G
 \simeq\bigoplus_{\mu}V_\mu\otimes\mathbb C^{m_\mu^C},
 \qquad
 m_\mu^C=c\sum_{\zeta\nearrow\nu}g(\kappa,\zeta,\mu), \tag{2.1}
\]

where `zeta nearrow nu` means that `nu/zeta` is one removable box and `g` is a
Kronecker coefficient. The fiber module decomposes as

\[
 \mathscr X_h\simeq
 \bigoplus_\mu V_\mu\otimes\mathbb C^{m_\mu^X}. \tag{2.2}
\]

The analysis map `L_h:C->X_h` is `G`-equivariant, so Schur's lemma gives

\[
 L_h=\bigoplus_\mu I_{V_\mu}\otimes\ell_\mu,
 \qquad
 \ell_\mu:\mathbb C^{m_\mu^C}\to\mathbb C^{m_\mu^X}. \tag{2.3}
\]

Consequently

\[
 \boxed{D_h=L_hL_h^*
 =\bigoplus_\mu I_{V_\mu}\otimes(\ell_\mu\ell_\mu^*),} \tag{2.4}
\]

and its exact spectrum is

\[
 \boxed{\operatorname{Spec}(D_h)
 =\biguplus_\mu
 \operatorname{Spec}(\ell_\mu\ell_\mu^*)^{\times f^\mu}.} \tag{2.5}
\]

For orthonormal intertwiner bases `U_(mu,r)^X:V_mu->X_h` and
`U_(mu,s)^C:V_mu->C`, the reduced entries are explicitly

\[
 (\ell_\mu)_{rs}
 ={1\over f^\mu}\operatorname{Tr}_{V_\mu}
 \left((U_{\mu,r}^{X})^*L_hU_{\mu,s}^{C}\right). \tag{2.6}
\]

Expanding `L_h`, `P_xi`, and `Pi_D` turns (2.6) into a finite symmetric-group
character/subduction sum with the same `p!`, `n!`, and `(q-j)!` normalizations audited
in T2. Equations (2.4)-(2.6) are exact, but they are matrix-valued Hahn/Racah data when
either multiplicity exceeds one. Ordinary Eberlein polynomials apply only to the
multiplicity-free boundary.

The irrational `sqrt(13)` eigenpairs at the two rational hostile gates are a concrete
witness of the `2 x 2` multiplicity blocks, not a numerical accident.

## 3. Exact spectrum of one comparison branch

Let

\[
 \mathcal O_\gamma=\operatorname{Ran}(P_{\rm comp}Q_\gamma).
\]

The query-stabilizer branch is the irreducible `S_(q-1)` module `V_(tau_gamma)`.
Taking `S_n`-invariants on `B` gives, as a `G=S_p` module,

\[
 \mathcal O_\gamma\simeq
 \bigoplus_{\mu:\ c_{\mu,(n)}^{\tau_\gamma}=1}V_\mu. \tag{3.1}
\]

Pieri's rule makes each coefficient in (3.1) zero or one, so the output branch is
multiplicity-free even though `X_h` is not.

Put `m=binom(j,a)`, `N=binom(p,j)`. The exact fold identity is

\[
 S_{h,\gamma}S_{h,\gamma}^*
 =mK_\gamma,
 \qquad
 K_\gamma=
 \sum_{|L|=j}P_{\rm comp}Q_\gamma\Pi_LQ_\gamma P_{\rm comp}. \tag{3.2}
\]

For an active `mu` in (3.1), define the rank-`f^mu` projector

\[
 P_{\gamma\mu}=P_{\rm comp}Q_\gamma
 \left({f^\mu\over p!}\sum_{g\in G}\chi_\mu(g^{-1})\rho(g)\right) \tag{3.3}
\]

and choose one fixed `j`-set `L_0 subset A^circ`. Symmetry and (3.2) give

\[
 k_{\gamma\mu}
 ={1\over f^\mu}\operatorname{Tr}(P_{\gamma\mu}K_\gamma)
 ={N\over f^\mu}\operatorname{Tr}(P_{\gamma\mu}\Pi_{L_0}). \tag{3.4}
\]

All normalizations in (3.4) are visible: the fold `m`, the uncolored orbit count `N`,
the central-idempotent factor `f^mu/p!`, and the normalized subgroup averages inside
`P_comp`, `Q_gamma`, and `Pi_(L_0)`. Since `A_gamma=S_gamma^*S_gamma` and
`S_gamma S_gamma^*` have the same nonzero spectrum,

\[
 \boxed{\operatorname{Spec}_{>0}(A_\gamma)
 =\biguplus_{\mu:\ c_{\mu,(n)}^{\tau_\gamma}=1}
 \{m k_{\gamma\mu}\}^{\times f^\mu}.} \tag{3.5}
\]

Equivalently, on the `mu` multiplicity space of `X_h`, `A_gamma` is a positive
rank-at-most-one matrix. Formula (3.4) is the exact character-theoretic substitute for
the desired Eberlein/Hahn eigenvalue. It does not imply that different branches, or
`A_gamma` and `D_h`, commute.

For a tail sum `A_tail=sum_z A_z`, the `mu` block is a sum of these rank-one matrices.
Its spectrum depends also on their mutual multiplicity-space angles; individual scalar
values `k_(z,mu)` alone do not determine (T-b).

## 4. The valid von Neumann reduction and exact residual inequality

No simultaneous diagonalization is needed. Let `Lambda_D` be the multiset in (2.5),
let `Lambda_0` be (3.5), and let `Lambda_tail` be the eigenvalue multiset of
`A_tail=sum_z A_z`. Sort each decreasingly and pad with zeros. Von Neumann gives

\[
 \operatorname{Tr}(A_0D_h)
 \le V_0:=\sum_i\Lambda_{0,i}^{\downarrow}
                    \Lambda_{D,i}^{\downarrow}, \tag{4.1}
\]

\[
 \operatorname{Tr}(A_{\rm tail}D_h)
 \le V_{\rm tail}:=\sum_i\Lambda_{{\rm tail},i}^{\downarrow}
                    \Lambda_{D,i}^{\downarrow}. \tag{4.2}
\]

Thus T3 reduces exactly to the two scalar inequalities

\[
 \boxed{V_0\le B_\theta(q)^2T,} \tag{4.3}
\]

\[
 \boxed{V_{\rm tail}\le
 {B_\theta(q)^2T\over\delta_{\min}+1}.} \tag{4.4}
\]

Equations (4.3)-(4.4), with (2.5) and (3.5), are the exact residual. The first
unresolved data are the singular values of all `ell_mu` and, for multiple tails, the
Gram matrices of the tail rank-one vectors. No known monotonicity of scalar dual-Hahn
polynomials controls these multiplicity matrices. Replacing them by commuting scalars
would contradict the exact commutator gates below.

## 5. Exact hostile spectra and noncommutation gates

The new script rebuilds the literal rational `L`, `S_0`, and `S_z` matrices from the
archived permutation-module constructors. It does not infer spectra from target values.

### 5.1 `theta=(2)`, mixed color

\[
 \operatorname{Spec}(D_h)=
 \left\{
 {7\over5},
 \left({7\over12}+{7\sqrt{13}\over60}\right)^{\times2},
 {7\over15},
 \left({7\over12}-{7\sqrt{13}\over60}\right)^{\times2}
 \right\}.
\]

\[
 \operatorname{Spec}(A_0)=
 \{(56/25)^{\times2},28/25,0^{\times3}\},
\]

\[
 \operatorname{Spec}(A_z)=
 \{16/75,(7/75)^{\times2},0^{\times3}\},
\]

\[
 \operatorname{Spec}(A_0+7A_z)=
 \{(14/5)^{\times2},12/5,0^{\times3}\}.
\]

The exact von Neumann values/caps are

\[
 {637+49\sqrt{13}\over125}\le {294\over25},\qquad
 {917+49\sqrt{13}\over2250}\le {49\over25},
\]

\[
 {1043+91\sqrt{13}\over150}\le {294\over25}.
\]

The actual long/tail/weighted traces are respectively
`1862/375`, `427/1500`, and `1001/150`.

### 5.2 `theta=(1,1)`, mixed color

\[
 \operatorname{Spec}(D_h)=
 \left\{
 {4\over3},
 \left({5+\sqrt{13}\over9}\right)^{\times2},
 {4\over9},
 \left({5-\sqrt{13}\over9}\right)^{\times2}
 \right\}.
\]

\[
 \operatorname{Spec}(A_0)=
 \{8/3,(32/21)^{\times2},0^{\times3}\},
\]

\[
 \operatorname{Spec}(A_z)=
 \{(1/7)^{\times2},0^{\times4}\},
\]

\[
 \operatorname{Spec}(A_0+7A_z)=
 \{(8/3)^{\times3},0^{\times3}\}.
\]

The exact von Neumann values/caps are

\[
 {992+64\sqrt{13}\over189}\le {32\over3},\qquad
 {17+\sqrt{13}\over63}\le {4\over3},
\]

\[
 {176+16\sqrt{13}\over27}\le {32\over3}.
\]

The actual long/tail/weighted traces are `256/63`, `1/21`, and `40/9`.

Both commutators are nonzero with the exact ranks/norms in Section 0. This is an
identity-level failure of simultaneous diagonalization, while the valid eigenvalue
pairing still passes.

## 6. Gate ledger and value/formula separation

| regime | identity/spectrum gate | scalar value gate | result |
|---|---|---|---|
| archived nine small `c=1` rows | exact `A,D` spectra and H2 long/tail/weighted | actual traces | `9/9` for each H2 label |
| two hostile mixed rows | fresh exact matrices, spectra, commutators | fresh actual and H2 values | PASS; commutation FAIL |
| killer `(9,18,3,(2,1);2,(2);1,(1))` | no archived T3 `A,D` spectra | exact T-a `408935/2744`, cap ratio `1415/2352` | scalar PASS; spectral UNTESTED |
| secondary `(9,18,3,(3);2,(2);1,(1))` | no archived T3 `A,D` spectra | certified interval below cap; printed rational is recognition only | scalar PASS; spectral UNTESTED |
| larger tame `(10,20,1,(1);1,(1);0,())` | no archived T3 `A,D` spectra | exact T-a `3200/361`, cap ratio `8/9` | scalar PASS; spectral UNTESTED |
| `c=2` `(7,14,6,(3,2,1);3,(2,1);3,(2,1))` | missing `23296 x 1120` carrier | none | UNTESTED |

The exact T2/local signed kernels remain signed. In particular, the mixed wedge row has
`-1/9` with ordered-pair multiplicity two per `L`, and the killer has
`-85/10584` with multiplicity six per `L`. The fresh matrix construction retains these
cross terms automatically; no absolute-value or positivity substitution is made.

The new code exercises the printed matrix definitions for the two hostile rows. The
archived nine-row record is hash-checked and used as prior exact spectrum evidence. The
killer/secondary/larger statements are explicitly only scalar T2 gates; agreement of
values does not verify the T3 spectral formulas in those rows.

## 7. `c>=2` boundary

For

\[
 (n,q,j,\theta,\alpha,\beta,c)
 =(7,14,6,(3,2,1),(2,1),(2,1),2),
\]

the Specht dimension is `23296` and the carrier dimension is
`f^(3,2,1) f^(4,2,1) c = 16*35*2 = 1120`. The absent object is a
multiplicity-resolved orthonormal embedding

\[
 \mathbb C^{1120}\hookrightarrow V_{(8,3,2,1)}\cong\mathbb C^{23296}
\]

together with its LR/subduction gauge and residual certificates for every map that does
not normalize `S_p x S_n`. Without it, neither the matrices `ell_mu` nor the `A,D`
identity/spectrum gates can be checked at `c=2`. No extrapolation from `c=1` is made.

## 8. Exact next missing object

The next proof object is a **uniform reduced-block theorem** supplying, for every
admissible tame sector:

1. orthonormal diagonal-`S_p` intertwiners for (1.7) and (2.1);
2. the fully normalized matrices `ell_mu` of (2.6), including LR and Kronecker
   multiplicity gauges;
3. the rank-one tail vectors and their cross-Gram matrices on each `mu` multiplicity
   space;
4. a proof of the majorization inequalities (4.3)-(4.4).

For Rule-7(b) testing, the first concrete missing instance is the `23296 x 1120`
embedding above. Scalar Hahn/Eberlein tables alone are insufficient because the exact
mixed-color gates already contain `Mat_2` blocks and nonzero commutators.

## 9. Reproduction and provenance

Command from the repository root:

```powershell
& 'C:[USER_HOME]/miniconda3/envs/AI_HW/python.exe' -u `
  artifacts/logs_se_trace_t3_20260721/se_trace_t3_exact_gates.py `
  --json artifacts/logs_se_trace_t3_20260721/se_trace_t3_exact_gates.json `
  --log artifacts/logs_se_trace_t3_20260721/log.txt
```

The script hash-checks/records the exact constructors and archived gate JSON/log inputs.
`log.txt` is the compact preview; the JSON records spectra, multiplicities, exact
commutator certificates, values, caps, and all dependency hashes. `SHA256SUMS.txt`
contains the final hashes of every delivered file. No node, DAG, index, handoff, note,
or paper file was edited.

## 10. Rule-7 audit

- **7a types:** PASS for every displayed operator. `L_h:C->X_h`,
  `D_h:X_h->X_h`, `S_gamma:X_h->O_gamma`, and `A_gamma:X_h->X_h`; all dimensions and
  all `c` dependence are explicit.
- **7b regime completeness:** PARTIAL. Exact small `c=1` identity/spectrum gates pass;
  expanded scalar gates pass; expanded spectral gates and `c>=2` are UNTESTED.
- **7c anchoring:** this is a proposer derivation, not an independent clean-room review.
  The module decomposition was derived from the typed group action; archived values were
  used only afterward as gates.
- **7d frozen inputs:** no c=1 result is extended to `c>=2`; scalar T2 values are not
  relabeled as T3 spectral checks.
- **7e failure modes:** checked noncommutativity, multiplicity, dimensions, fold `m`,
  orbit count `N`, subgroup normalizations, signed cross terms, value/formula separation,
  and simultaneous-diagonalization failure.
- **7f value versus formula:** the fresh hostile code constructs matrices and checks the
  formulas; expanded large rows remain scalar-only evidence.
- **7g quantifiers:** admissible means the canonical strict-sector conditions already
  used by TRACE; tame means `n>=3j`; the report separately states every boundary and
  untested regime.

