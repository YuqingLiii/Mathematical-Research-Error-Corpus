# Verdict

\[
\boxed{\texttt{GenericTheta300185Exclusion is proved within the present finite-slope audit context.}}
\]

For

\[
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300185)m_6,
\]

with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the exact low-fiber data imply

\[
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}>3254E.
}
\]

Consequently,

\[
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}>3254E,
\]

and the exact slack identity gives

\[
M_{\rm ord}<970330473E.
\]

This contradicts the inherited strict target estimate

\[
\sqrt{D+1}\,|T_1|>970330473E.
\]

Thus no exact baseline exists in this finite-slope ansatz.

The inherited Laurent coefficient formula and common phase variables are the previously audited ones. fileciteturn0file0L47-L135 The four-slack identity and its relation to the ordinary mass are likewise frozen from the prior audit. fileciteturn0file1L594-L675

The requested size-three census was completed, but the decisive correction is:

\[
\boxed{\text{No size-three packet is needed.}}
\]

The rowwise size-two matching fails, since \(M_i<B_i\) for every row. However, the phase variables \(Z,W\) are common to **all** cofactors. Matching equal exponent-difference keys across different deleted rows raises the exact opposite-sign packet count from

\[
605828
\]

rowwise matches to

\[
1290408
\]

global matches. After charging the one common bad-coordinate budget, exactly

\[
145464
\]

global size-two packets remain. Those packets alone close the \(3254E\) gap.

This is a finite-slope ansatz exclusion, not a proof of PW10. The frozen source explicitly separates the two. fileciteturn0file2L24-L38 Only an exact physical construction or a phase-uniform inequality for all admissible states would settle PW10. fileciteturn0file3L369-L374 That same scope restriction is retained throughout the attached audit material. fileciteturn0file4L369-L394 fileciteturn0file5L369-L394

---

# 1. Exact contradiction setup

Set

\[
H:=3254,\qquad K:=970333728.
\]

The formal support table is

\[
\boxed{
\begin{aligned}
(S_i)_{i=0}^{12}
={}&(
53624480,67257904,74299124,80378638,82205100,85479374,\\
&83844488,85479374,82205100,80378638,74299124,67257904,53624480).
\end{aligned}}
\tag{1.1}
\]

At a safe spacing,

\[
C_{ii}(0)=e_i^2,\qquad C_{ii}(2)=0,
\]

and

\[
(K-1)E-M_{\rm ord}
=
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}.
\tag{1.2}
\]

Assume for contradiction that

\[
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}<HE.
\tag{1.3}
\]

Since all four slacks are nonnegative,

\[
\Delta_{\rm ray}<HE,\qquad
\Delta_{\rm flat}<HE.
\tag{1.4}
\]

Put

\[
w_i=\sqrt{S_i},\qquad
\alpha=\frac{w\cdot e}{K}.
\]

Then

\[
\|e-\alpha w\|_2^2
=\frac{\Delta_{\rm ray}}K
<\frac{HE}{K},
\tag{1.5}
\]

and

\[
\alpha^2>\frac{K-H}{K^2}E.
\tag{1.6}
\]

---

# 2. Near-ray and support-loss budgets

From (1.5)–(1.6),

\[
\frac{|e_i-\alpha\sqrt{S_i}|}
{\alpha\sqrt{S_i}}
<
\sqrt{\frac{HK}{(K-H)S_i}}.
\]

The denominator \(128\) is valid because

\[
\boxed{
(K-H)S_{\min}-H\cdot128^2K
=
301544956661312>0,
}
\tag{2.1}
\]

where

\[
S_{\min}=53624480.
\]

Hence

\[
e_i>\frac{127}{128}\alpha\sqrt{S_i}
\qquad\forall i.
\tag{2.2}
\]

Let

\[
n_i=|\operatorname{supp}A_i|,
\qquad
m_i=S_i-n_i.
\]

For the padded coefficient array,

\[
D_i:=S_ie_i^2-L_i^2\ge m_ie_i^2.
\]

Because

\[
D_i\le\Delta_{\rm flat}<HE,
\]

we obtain

\[
m_i<
\frac{H\,128^2K^2}
{127^2(K-H)S_i}.
\]

The exact integer ceilings are

\[
\boxed{
\begin{aligned}
(m_i)=(&59812,47688,43168,39903,39016,37522,38254,\\
       &37522,39016,39903,43168,47688,59812).
\end{aligned}}
\tag{2.3}
\]

If a formal coefficient vanishes, or lies in a nontrivial actual-frequency collision group, call it bad. If \(z_i\) coefficients vanish and the collision-group sizes are \(r_{i,j}\ge2\), then

\[
m_i\ge z_i+\sum_j(r_{i,j}-1).
\]

The number of bad formal coordinates is therefore at most

\[
z_i+\sum_jr_{i,j}
\le2m_i.
\]

Thus

\[
\boxed{
\begin{aligned}
(B_i)=2(m_i)
={}&(
119624,95376,86336,79806,78032,75044,76508,\\
&75044,78032,79806,86336,95376,119624).
\end{aligned}}
\tag{2.4}
\]

Globally,

\[
\boxed{\sum_iB_i=1144944.}
\tag{2.5}
\]

---

# 3. Exact low-fiber census at \(\theta=300185\)

All counts below were regenerated with the special-column order

\[
(3,1,20,-20,490,-490,12090,-12090,300185,-300185).
\]

## 3.1 Raw-fiber populations

The singleton counts are

\[
\boxed{
\begin{aligned}
(U_i)=(&2611200,5487296,6765992,7099598,7596018,8124580,7618740,\\
       &8124580,7596018,7099598,6765992,5487296,2611200).
\end{aligned}}
\tag{3.1}
\]

The raw size-two counts are

\[
\boxed{
\begin{aligned}
(H_{2,i})=(&8170368,13221080,15472420,17578010,19216372,20092120,\\
&18913704,20092120,19216372,17578010,15472420,13221080,8170368).
\end{aligned}}
\tag{3.2}
\]

The raw size-three counts are

\[
\boxed{
\begin{aligned}
(H_{3,i})=(&2127360,3505232,4554436,4984486,5436016,5747266,\\
&6162284,5747266,5436016,4984486,4554436,3505232,2127360).
\end{aligned}}
\tag{3.3}
\]

The raw size-four counts are

\[
\boxed{
\begin{aligned}
(H_{4,i})=(&8437248,11517728,12835600,14926940,15308330,16650972,\\
&15684144,16650972,15308330,14926940,12835600,11517728,8437248).
\end{aligned}}
\tag{3.4}
\]

The global totals are

\[
\boxed{
\begin{aligned}
\sum_iU_i&=82988108,\\
\sum_iH_{2,i}&=206414444,\\
\sum_iH_{3,i}&=58871876,\\
\sum_iH_{4,i}&=175037780.
\end{aligned}}
\tag{3.5}
\]

Every raw size-two fiber is a genuine binomial:

\[
\boxed{
\begin{aligned}
\#\{\text{genuine binomials}\}&=206414444,\\
\#\{\text{collected }\pm2\text{ monomials}\}&=0,\\
\#\{\text{zero Laurent polynomials}\}&=0.
\end{aligned}}
\tag{3.6}
\]

The seven global size-two moment checksums are

\[
\boxed{
\begin{aligned}
\sum t&=4953946656,\\
\sum\Delta Q_6&=751437057188672,\\
\sum\Delta Q_r&=3332976,\\
\sum\sigma&=136796092,\\
\sum t^2&=879381258751814153744,\\
\sum(\Delta Q_6)^2&=7182685321895457821152,\\
\sum(\Delta Q_r)^2&=79580045136.
\end{aligned}}
\tag{3.7}
\]

---

## 3.2 Size-three collection

After equal Laurent monomials are collected, the exact size-three classification is

\[
\boxed{
\begin{aligned}
\#\{\text{genuine trinomials}\}&=58871844,\\
\#\{\text{collected binomials}\}&=32,\\
\#\{\text{collected monomials}\}&=0,\\
\#\{\text{zero polynomials}\}&=0.
\end{aligned}}
\tag{3.8}
\]

The 32 collected binomials occur as:

- 16 in deleted row \(4\);
- 16 in deleted row \(8\).

For genuine trinomials, normalize the leading sign to \(+\). The four sign-pattern totals are

\[
\boxed{
\begin{array}{c|r}
\text{pattern}&\text{count}\\ \hline
(+,+,+)&18596376\\
(+,-,+)&14083474\\
(+,+,-)&13075024\\
(+,-,-)&13116970
\end{array}}
\tag{3.9}
\]

and these sum to \(58871844\).

The same-support pattern census gives

\[
\boxed{
\begin{aligned}
\#\{\text{ordered exponent supports}\}&=19566221,\\
\#\{\text{supports carrying one sign pattern}\}&=19548948,\\
\#\{\text{supports carrying two sign patterns}\}&=17273,\\
\#\{\text{supports carrying three patterns}\}&=0,\\
\#\{\text{supports carrying all four patterns}\}&=0.
\end{aligned}}
\tag{3.10}
\]

Thus the literal common-support four-pattern Hadamard packet proposed in the prompt does not occur. This does **not** imply that every possible size-three construction fails; it only closes that precise packet form.

---

# 4. Rowwise size-two matching is insufficient

For each deleted row, canonicalize each size-two binomial as

\[
\epsilon Z^{A}W^{B}
\left(
1+\sigma Z^{d_6}W^{d_r}
\right),
\qquad \sigma\in\{\pm1\}.
\]

Let \(n_i^\sigma(d_6,d_r)\) be the multiplicity of a signed exponent-difference key in row \(i\), and define

\[
M_i=\sum_{d_6,d_r}\min\{n_i^+(d_6,d_r),n_i^-(d_6,d_r)\}.
\]

The exact rowwise counts are

\[
\boxed{
(M_i)=
(9084,39388,56644,58044,37500,69164,66180,
69164,37500,58044,56644,39388,9084).
}
\tag{4.1}
\]

Their total is

\[
\boxed{\sum_iM_i=605828.}
\tag{4.2}
\]

But

\[
M_i<B_i
\qquad\text{for every }i,
\]

so a row-by-row deletion-robust packet count certifies no surviving pair. This is precisely why the Round-57 rowwise argument does not extend directly.

The correction is to use the global identity

\[
\Delta_{\rm ray}+\Delta_{\rm flat}
=
KE-\left(\sum_iL_i\right)^2,
\tag{4.3}
\]

which couples all thirteen cofactors. The phase variables \(Z,W\) are also common globally, so equal exponent-difference keys may be matched across distinct deleted rows.

---

# 5. Exact global opposite-sign matching

For a canonical exponent-difference key

\[
\kappa=(d_6,d_r),
\]

let

\[
p_\kappa
=
\sum_i n_i^+(d_6,d_r),
\qquad
n_\kappa
=
\sum_i n_i^-(d_6,d_r).
\]

Globally,

\[
\boxed{
\begin{aligned}
\#\{\text{size-two records}\}&=206414444,\\
\#\{\text{distinct exponent-difference keys}\}&=7999142,\\
\sum_\kappa p_\kappa&=171605268,\\
\sum_\kappa n_\kappa&=34809176,\\
\#\{\kappa:p_\kappa n_\kappa>0\}&=177236.
\end{aligned}}
\tag{5.1}
\]

Choose, for each key, exactly

\[
\min(p_\kappa,n_\kappa)
\]

coordinate-disjoint \(+\)/\(-\) pairs. The total is

\[
\boxed{
M_{\rm global}
=
\sum_\kappa\min(p_\kappa,n_\kappa)
=
1290408.
}
\tag{5.2}
\]

The largest contribution from one key is

\[
\boxed{1152.}
\tag{5.3}
\]

Compared with the rowwise matching,

\[
\boxed{
M_{\rm global}-\sum_iM_i
=
1290408-605828
=
684580.
}
\tag{5.4}
\]

This is the exact cross-row matching gain.

For example, the key

\[
(d_6,d_r)=(2401604,0)
\]

has global multiplicities

\[
p_\kappa=1152,\qquad n_\kappa=1344,
\]

so it supplies \(1152\) opposite-sign packets. Its row distributions are

\[
(0,0,192,96,0,288,0,288,0,96,192,0,0)
\]

for \(+\), and

\[
(0,0,0,0,480,192,0,192,480,0,0,0,0)
\]

for \(-\). The matching is therefore intrinsically cross-cofactor.

---

# 6. Collision-robust surviving anchors and global packets

The raw singleton and raw size-two populations are disjoint formal-coordinate sets.

Using the one common bad set:

- at least
  \[
  G_i:=U_i-B_i
  \]
  singleton coordinates remain physical-frequency-isolated and have modulus exactly \(1\);
- at most \(\sum_iB_i\) of the globally preselected coordinate-disjoint packets can be destroyed.

The surviving singleton counts are

\[
\boxed{
\begin{aligned}
(G_i)=(&2491576,5391920,6679656,7019792,7517986,8049536,\\
&7542232,8049536,7517986,7019792,6679656,5391920,2491576).
\end{aligned}}
\tag{6.1}
\]

Thus

\[
\boxed{
G:=\sum_iG_i=81843164.
}
\tag{6.2}
\]

The total bad-coordinate budget is \(1144944\), so the number of surviving global packets is

\[
\boxed{
N
=
M_{\rm global}-\sum_iB_i
=
1290408-1144944
=
145464.
}
\tag{6.3}
\]

A bad coordinate destroys at most one selected packet because the packet matching is coordinate-disjoint. No packet is charged twice.

---

# 7. Global matched-packet inequality

For each surviving packet with key \((d_6,d_r)\), put

\[
\zeta=Z^{d_6}W^{d_r},
\qquad |\zeta|=1.
\]

After removing unit monomial factors, its two coefficient magnitudes are

\[
r_+=|1+\zeta|,
\qquad
r_-=|1-\zeta|.
\]

Exactly,

\[
\boxed{
r_+^2+r_-^2=4,
}
\tag{7.1}
\]

and

\[
\boxed{
r_++r_-\le2\sqrt2.
}
\tag{7.2}
\]

Concatenate all thirteen padded coefficient-magnitude arrays. Their total length is \(K\), total squared norm is \(E\), and total \(\ell_1\)-norm is

\[
L:=\sum_iL_i.
\]

Among their entries are, disjointly:

1. \(G\) unit anchors;
2. \(N\) complete opposite-sign packets.

The selected entries therefore have exact squared energy

\[
\boxed{
Q=G+4N=82425020.
}
\tag{7.3}
\]

The number of remaining padded coordinates is

\[
\boxed{
R=K-G-2N=888199636.
}
\tag{7.4}
\]

Their squared energy is \(E-Q\). Therefore

\[
L
\le
G+2\sqrt2\,N+\sqrt{R(E-Q)}.
\tag{7.5}
\]

Write

\[
A=G+2\sqrt2\,N.
\]

Then

\[
A+\sqrt{R(E-Q)}
=
\frac{A}{\sqrt Q}\sqrt Q
+
\sqrt R\,\sqrt{E-Q}.
\]

Cauchy–Schwarz in \(\mathbb R^2\) gives

\[
L^2
\le
\left(
R+\frac{A^2}{Q}
\right)E.
\tag{7.6}
\]

Since

\[
\Delta_{\rm ray}+\Delta_{\rm flat}
=
KE-L^2,
\]

we obtain

\[
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
\ge
\frac{(6-4\sqrt2)GN}{G+4N}\,E.
}
\tag{7.7}
\]

No scale estimate for \(E/K\), no size-three packet, and no rowwise decomposition is used.

---

# 8. Exact comparison with \(3254E\)

Use

\[
\sqrt2<\frac{577}{408},
\]

which follows from

\[
577^2-2\cdot408^2=1.
\]

Hence

\[
6-4\sqrt2
>
6-\frac{4\cdot577}{408}
=
\frac{35}{102}.
\tag{8.1}
\]

Therefore

\[
\Delta_{\rm ray}+\Delta_{\rm flat}
>
\frac{35GN}{102(G+4N)}E.
\tag{8.2}
\]

The exact cleared comparison is

\[
\boxed{
35GN-3254\cdot102(G+4N)
=
389325666745200>0.
}
\tag{8.3}
\]

Consequently,

\[
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}>3254E.
}
\tag{8.4}
\]

This already implies

\[
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}>3254E.
}
\tag{8.5}
\]

---

# 9. Consequence for the baseline

Using \(K=970333728\),

\[
\begin{aligned}
M_{\rm ord}
&=
(K-1)E-
\bigl(
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}
\bigr)\\
&<
(K-1-3254)E\\
&=
970330473E.
\end{aligned}
\tag{9.1}
\]

But the inherited target estimate is strict:

\[
\sqrt{D+1}|T_1|>970330473E.
\tag{9.2}
\]

This contradicts the physical baseline inequality

\[
\sqrt{D+1}|T_1|\le M_{\rm ord}.
\]

Hence:

\[
\boxed{
\begin{gathered}
\texttt{GenericTheta300185Exclusion:}\\
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300185)m_6,\\
\text{the fifth centered pair arbitrary and all twelve slopes distinct}\\
\Longrightarrow
\text{no exact baseline exists.}
\end{gathered}}
\tag{9.3}
\]

For \(\delta=-2m_6\), interchange the defect endpoints and reverse the common \(m_6\)-orientation. All magnitude counts and inequalities are unchanged.

This remains a finite-slope candidate theorem pending independent replication outside this proof-development context.

---

# 10. Reproducibility package

The complete reproducibility bundle contains:

- integer-only low-fiber enumerator;
- exact size-two key counter;
- thirteen-stream global key merger;
- detailed cross-row packet census;
- complete size-three census;
- exact summaries and arithmetic certificates;
- SHA-256 digests of all large raw streams;
- verbatim Markdown archive of the Round 57 public response.

The bundle SHA-256 is

```text
3e3afacd9ab544167b465a77d213bff76a2e0df16a3795800af410992e4e5405
```

The Round 57 response archive SHA-256 is

```text
4eacec0cde11e9c2dd0379989ccc56c9c082ab3b29acd1b61af1a68dbd093d41
```

Large intermediate binary streams are not duplicated inside the ZIP; their individual SHA-256 digests are included.

- [Complete Round 58 audit bundle](sandbox:/mnt/data/round58_theta300185_audit_bundle.zip)
- [Verbatim Round 57 response archive](sandbox:/mnt/data/round57_response.md)
- [Integer-only size-three/low-fiber reproducer](sandbox:/mnt/data/round58_size3_reproducer.cpp)
- [Global size-two key-count source](sandbox:/mnt/data/round58_size2_keycounts.cpp)
- [Global size-two merge source](sandbox:/mnt/data/round58_size2_merge.cpp)
- [Detailed global size-two merge source](sandbox:/mnt/data/round58_size2_merge_detail.cpp)
- [Low-fiber summary](sandbox:/mnt/data/round58_lowfiber_summary.csv)
- [Complete size-three summary](sandbox:/mnt/data/round58_size3_summary.csv)
- [Global size-two packet summary](sandbox:/mnt/data/round58_global_size2_summary.csv)
- [Global packet detail](sandbox:/mnt/data/round58_global_size2_detail.txt)
- [Exact arithmetic certificates](sandbox:/mnt/data/round58_exact_inequality_checks.txt)
- [All artifact digests](sandbox:/mnt/data/round58_digest.txt)

---

# VERIFIED

- The support table (58.1) and
  \[
  K=970333728.
  \]
- The \(1/128\) near-ray certificate.
- The support-loss ceilings \(m_i\).
- The common bad-coordinate budgets \(B_i\).
- The complete singleton, size-two, size-three, and size-four census.
- The exact total of \(206414444\) raw size-two fibers.
- Every raw size-two fiber is a genuine binomial.
- Zero collected \(\pm2\) size-two monomials.
- Zero collected size-two Laurent cancellations.
- The complete size-three classification.
- The absence of a common-support three- or four-pattern Hadamard packet.
- The exact global exponent-difference-key count \(7999142\).
- The global opposite-sign match count
  \[
  M_{\rm global}=1290408.
  \]
- The cross-row gain
  \[
  684580.
  \]
- The deletion-robust packet count
  \[
  N=145464.
  \]
- The exact global packet inequality (7.7).
- The cleared positive margin
  \[
  389325666745200.
  \]
- `GenericTheta300185Exclusion` within this finite-slope ansatz.

# CORRECTED

- The failure \(M_i<B_i\) in every individual row does **not** imply that size-two packets are exhausted.
- Equal exponent-difference keys may be paired across deleted rows because the same physical \(Z,W\) govern all cofactors.
- The correct globally matched count is \(1290408\), rather than the rowwise total \(605828\).
- The intended same-support four-pattern size-three packet does not occur.
- Size-three fibers were fully audited but are not needed for the exclusion.
- No bound on \(E/K\) is required.

# DISPROVED

- The claim that a size-three packet is necessary at \(\theta=300185\).
- The claim that rowwise packet failure implies global packet failure.
- The possibility that the complete collision-robust globally matched size-two relaxation lies below \(3254E\).
- The status “generic \(\theta=300185\) remains open” within this exact finite-slope ansatz.

# NECESSARY-ONLY

- Independent replication of the new cross-row matching census is still required before broader promotion.
- The theorem covers only the stated finite-slope ansatz.
- The size-three census is an exact audit result but is not load-bearing.
- No statement here settles the physical liftability of \(x^{(10)}\).
- No statement here proves PW10.

# EQUIVALENT

Within the audited Wiener chain,

\[
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}\ge3254E
\]

is equivalent to

\[
M_{\rm ord}\le970330473E.
\]

For every globally matched exponent-difference key, the selected coefficient magnitudes are exactly

\[
|1+\zeta|,\qquad |1-\zeta|.
\]

The globally coupled packet coefficient is exactly

\[
\frac{(6-4\sqrt2)GN}{G+4N}.
\]

# NUMERICAL-ONLY

- No floating-point phase sampling was used.
- No heuristic phase minimization was used.
- No interval branch-and-bound was needed.
- All low-fiber and key-merging computations are integer-only.
- The radical comparison was reduced to exact integer arithmetic.

# CONJECTURED

- Independent external replication of `GenericTheta300185Exclusion`.
- Extension of the global packet method to subsequent unresolved four-ratio values.
- A general thirteen-slope ansatz theorem.
- Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

- The full ratio-two and arbitrary one-defect classes.
- Non-centrally-symmetric twelve-slope families outside the candidate exclusions.
- A general thirteen-slope theorem.
- Dense nonquadratic baseline solutions.
- Existence of an exact baseline vector outside the excluded finite-slope ansätze.
- Frozen named-edge retrieval.
- Physical liftability of \(x^{(10)}\).
- An exact physical vector above \(10\).
- PW10.
- The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the global cross-cofactor opposite-sign matching census

\[
\boxed{
M_{\rm global}=1290408,\qquad
N=145464,
}
\]

together with its determinant-specific implication

\[
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
>
3254E.
}
\]

No exact baseline vector, exact frozen-edge vector, exclusion of \(x^{(10)}\), exact physical vector above \(10\), or phase-uniform PW10 proof was produced.

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]
