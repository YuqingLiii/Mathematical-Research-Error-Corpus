# Verdict

$$
\boxed{\texttt{GenericTheta300187Exclusion is proved within the present finite-slope audit context.}}
$$

For

$$
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300187)m_6,
$$

with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census gives

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
}
$$

Therefore

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}\ge3318E,
$$

and the exact slack identity implies

$$
M_{\rm ord}\le970330473E.
$$

This contradicts the inherited strict target estimate

$$
\sqrt{D+1}\,|T_1|>970330473E.
$$

Thus no exact baseline exists in this finite-slope ansatz.

The frozen normalization and PW10 boundary are unchanged:

$$
D=941541228773064677=970330474^2+1,\qquad
B^2=\frac1{D(D+2)},\qquad
A_{\rm sp}^2=(D+1)B^2.
$$

A conclusion confined to this slope ansatz remains logically weaker than PW10.  The Laurent coefficient convention used below is the audited determinant convention in which all cofactor rows share the same physical variables \(Z,W\). 

The load-bearing new result is the independently reproduced global merge:

$$
\boxed{
M_{\rm global}=1326892,\qquad
N=159282,
}
$$

together with

$$
\boxed{
35GN-3318\cdot102(G+4N)
=428232492324252>0.
}
$$

No size-three packet is needed.

---

# 1. Exact contradiction setup

Set

$$
H:=3318,\qquad K:=970333792.
$$

The formal-support table is

$$
\boxed{
\begin{aligned}
(S_i)_{i=0}^{12}
={}&(
53624480,67257904,74299068,80378606,82205096,85479434,\\
&83844616,85479434,82205096,80378606,74299068,67257904,53624480).
\end{aligned}}
\tag{1.1}
$$

At a safe spacing,

$$
C_{ii}(0)=e_i^2,\qquad C_{ii}(2)=0.
$$

The exact Wiener-chain identity is

$$
(K-1)E-M_{\rm ord}
=
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}.
\tag{1.2}
$$

The four slacks are nonnegative; this identity follows by successively accounting for support Cauchy, convolution Young, physical-row grouping, and deletion of the target coefficient. 

Assume for contradiction that

$$
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}<HE.
\tag{1.3}
$$

Then, individually,

$$
\Delta_{\rm ray}<HE,\qquad
\Delta_{\rm flat}<HE.
\tag{1.4}
$$

Put

$$
w_i=\sqrt{S_i},\qquad
\alpha=\frac{w\cdot e}{K}.
$$

Since

$$
\Delta_{\rm ray}=KE-(w\cdot e)^2,
$$

we have

$$
\|e-\alpha w\|_2^2
=\frac{\Delta_{\rm ray}}K
<\frac{HE}{K},
\tag{1.5}
$$

and

$$
\alpha^2
=\frac{(w\cdot e)^2}{K^2}
>
\frac{K-H}{K^2}E.
\tag{1.6}
$$

---

# 2. Near-ray and support-loss budgets

Equations (1.5)–(1.6) imply

$$
\frac{|e_i-\alpha\sqrt{S_i}|}
{\alpha\sqrt{S_i}}
<
\sqrt{\frac{HK}{(K-H)S_i}}.
\tag{2.1}
$$

The maximal convenient integer denominator is \(127\):

$$
\boxed{
(K-H)S_{\min}-H\cdot127^2K
=
105062536388096>0,
}
\tag{2.2}
$$

whereas

$$
(K-H)S_{\min}-H\cdot128^2K
=
-715927181685184<0.
\tag{2.3}
$$

Hence

$$
e_i>\frac{126}{127}\alpha\sqrt{S_i}
\qquad\forall i.
\tag{2.4}
$$

Let

$$
n_i=|\operatorname{supp}A_i|,\qquad
m_i=S_i-n_i.
$$

For the coefficient-magnitude array padded with zeros to length \(S_i\),

$$
D_i:=S_ie_i^2-L_i^2\ge m_ie_i^2.
\tag{2.5}
$$

Since \(D_i\le\Delta_{\rm flat}<HE\), equations (1.6) and (2.4) give

$$
m_i<
\frac{H\,127^2K^2}
{126^2(K-H)S_i}.
$$

The exact strict-integer ceilings are

$$
\boxed{
\begin{aligned}
(m_i)=(&60996,48631,44023,40693,39789,38265,39011,\\
       &38265,39789,40693,44023,48631,60996).
\end{aligned}}
\tag{2.6}
$$

A formal coordinate is called bad if its coefficient vanishes or it belongs to a nontrivial actual-frequency collision group. If \(z_i\) coordinates vanish and the collision groups have sizes \(r_{i,j}\ge2\), then

$$
m_i\ge z_i+\sum_j(r_{i,j}-1),
$$

while the number of affected formal coordinates is at most

$$
z_i+\sum_jr_{i,j}
\le2m_i.
$$

Thus the common bad-coordinate budgets are

$$
\boxed{
\begin{aligned}
(B_i)=2(m_i)
={}&(
121992,97262,88046,81386,79578,76530,78022,\\
&76530,79578,81386,88046,97262,121992).
\end{aligned}}
\tag{2.7}
$$

Globally,

$$
\boxed{\sum_iB_i=1167610.}
\tag{2.8}
$$

---

# 3. Independent low-fiber regeneration

The \(\theta=300187\) streams were regenerated from the determinant assignments themselves using the special-column order

$$
(3,1,20,-20,490,-490,12090,-12090,300187,-300187).
$$

An implementation-only issue was detected during the audit: the dense temporary \(t\)-array inherited from \(\theta=300185\) ended at \(3727200\), while one \(\theta=300187\) intermediate value is \(3727213\). The array range was widened to \([-3800000,3800000]\). This changes no determinant formula or completed output.

The principal per-row census is:

| \(i\) |    \(S_i\) | singleton \(U_i\) | raw size 2 | rowwise \(M_i\) | \(B_i\) | \(G_i=U_i-B_i\) |
| ----: | ---------: | ----------------: | ---------: | --------------: | ------: | --------------: |
|     0 | 53,624,480 |         2,611,200 |  8,170,368 |           9,164 | 121,992 |       2,489,208 |
|     1 | 67,257,904 |         5,487,296 | 13,221,080 |          39,604 |  97,262 |       5,390,034 |
|     2 | 74,299,068 |         6,765,980 | 15,472,392 |          57,134 |  88,046 |       6,677,934 |
|     3 | 80,378,606 |         7,099,590 | 17,577,938 |          59,130 |  81,386 |       7,018,204 |
|     4 | 82,205,096 |         7,595,966 | 19,216,428 |          39,164 |  79,578 |       7,516,388 |
|     5 | 85,479,434 |         8,124,592 | 20,092,252 |          69,782 |  76,530 |       8,048,062 |
|     6 | 83,844,616 |         7,618,952 | 18,913,724 |          67,092 |  78,022 |       7,540,930 |
|     7 | 85,479,434 |         8,124,592 | 20,092,252 |          69,782 |  76,530 |       8,048,062 |
|     8 | 82,205,096 |         7,595,966 | 19,216,428 |          39,164 |  79,578 |       7,516,388 |
|     9 | 80,378,606 |         7,099,590 | 17,577,938 |          59,130 |  81,386 |       7,018,204 |
|    10 | 74,299,068 |         6,765,980 | 15,472,392 |          57,134 |  88,046 |       6,677,934 |
|    11 | 67,257,904 |         5,487,296 | 13,221,080 |          39,604 |  97,262 |       5,390,034 |
|    12 | 53,624,480 |         2,611,200 |  8,170,368 |           9,164 | 121,992 |       2,489,208 |

The exact global totals are

$$
\boxed{
\sum_iU_i=82988200,
\qquad
\sum_iH_{2,i}=206414640.
}
\tag{3.1}
$$

Every raw size-two fiber is a genuine binomial:

$$
\boxed{
\#\{\text{genuine binomials}\}=206414640,
}
$$

with

$$
\boxed{
\#\{\text{collected }\pm2\text{ monomials}\}=0,
\qquad
\#\{\text{zero size-two Laurent polynomials}\}=0.
}
\tag{3.2}
$$

The recomputed raw size-three counts are

$$
\boxed{
\begin{aligned}
(H_{3,i})=(&2127360,3505232,4554368,4984524,5436034,5747218,\\
&6162128,5747218,5436034,4984524,4554368,3505232,2127360).
\end{aligned}}
\tag{3.3}
$$

They are audit data only; they are not load-bearing below.

---

## 3.1 Moment checksums

The complete concatenated size-two stream has

$$
\boxed{206414640}
$$

records and satisfies

$$
\boxed{
\begin{aligned}
\sum t&=4953951360,\\
\sum\Delta Q_6&=751440452952096,\\
\sum\Delta Q_r&=3332784,\\
\sum\sigma&=136796544,\\
\sum t^2&=879392485546644366000,\\
\sum(\Delta Q_6)^2&=7182766542873529070944,\\
\sum(\Delta Q_r)^2&=79579947536.
\end{aligned}}
\tag{3.4}
$$

An additional custom index-weighted checksum is

$$
232752790813324275701672,
$$

and the stream FNV-1a-64 checksum is

```text
cc556cf4c6ca8f17
```

---

# 4. Canonical signs and cross-cofactor matching

After collecting a raw size-two fiber, order its two monomials lexicographically by

$$
(Q_6,Q_r).
$$

Write the coefficient as

$$
c_0Z^{A}W^{B}
+
c_1Z^{A+d_6}W^{B+d_r},
\qquad c_0,c_1\in\{\pm1\}.
$$

Define

$$
\sigma=c_0c_1\in\{\pm1\}.
$$

Multiplication by the leading unit sign and monomial gives

$$
1+\sigma Z^{d_6}W^{d_r}.
\tag{4.1}
$$

Changing the overall signed-minor convention of one cofactor multiplies both \(c_0,c_1\) by the same sign and leaves \(\sigma\) unchanged.

The canonical key is

$$
\kappa=(d_6,d_r).
$$

Because monomials are ordered lexicographically,

* \(d_6\ge0\);
* if \(d_6=0\), then \(d_r>0\).

Most importantly, the physical variables

$$
Z=\omega^{-m_6h^2/8},\qquad
W=\omega^{-m_rh^2/8}
$$

are common to every deleted-row cofactor. Thus equal canonical keys in different cofactors determine the same phase

$$
\zeta_\kappa=Z^{d_6}W^{d_r}.
$$

Different cofactor indices and different leading monomials contribute only unit prefactors and do not change coefficient magnitudes. Therefore a \(+\) record and a \(-\) record with the same key have magnitudes

$$
|1+\zeta_\kappa|,
\qquad
|1-\zeta_\kappa|,
$$

even when they lie in different deleted rows.

This justifies exact cross-cofactor matching.

---

# 5. Independent global merge

The thirteen per-row key files were generated independently from their raw streams and merged in sorted canonical-key order.

The result is

$$
\boxed{
\begin{aligned}
\#\{\text{global keys}\}&=7977021,\\
\#\{\sigma=+1\text{ records}\}&=171605592,\\
\#\{\sigma=-1\text{ records}\}&=34809048,\\
\#\{\text{keys carrying both signs}\}&=187548,\\
\max_\kappa\min(p_\kappa,n_\kappa)&=1152.
\end{aligned}}
\tag{5.1}
$$

The global opposite-sign match count is

$$
\boxed{
M_{\rm global}
=
\sum_\kappa\min(p_\kappa,n_\kappa)
=
1326892.
}
\tag{5.2}
$$

The sum of the thirteen rowwise match counts is only

$$
\sum_iM_i=615048,
$$

so the exact cross-row gain is

$$
\boxed{
1326892-615048=711844.
}
\tag{5.3}
$$

For example, the canonical key

$$
\kappa=(96916,0)
$$

has

$$
p_\kappa=1152,\qquad n_\kappa=1344,
$$

with row distributions

$$
(0,0,192,96,0,288,0,288,0,96,192,0,0)
$$

for \(+\), and

$$
(0,0,0,0,480,192,0,192,480,0,0,0,0)
$$

for \(-\). Its \(1152\) packets are intrinsically cross-cofactor.

---

## 5.1 Independent weighted checksums

Let the sorted global keys be \(\kappa_j=(d_{6,j},d_{r,j})\), indexed from \(j=1\), and define

$$
\operatorname{base}(\kappa_j)
=
(d_{6,j}\ll16)
+
\operatorname{uint16}(d_{r,j}+32768).
$$

The independently reproduced checksums are

$$
\boxed{
\sum_jj\,\operatorname{base}(\kappa_j)
=
19507901400370362360168362,
}
\tag{5.4}
$$

and

$$
\boxed{
\sum_jj(3p_j+5n_j)
=
1648619144832160.
}
\tag{5.5}
$$

A second verifier, implemented independently in Python over the merged binary, reproduces all of (5.1)–(5.5).

---

# 6. Coordinate-disjoint packet family

For each canonical key \(\kappa\), list its \(p_\kappa\) positive-sign records and \(n_\kappa\) negative-sign records. Pair the first

$$
\min(p_\kappa,n_\kappa)
$$

records one-to-one.

Each size-two formal coordinate:

* has exactly one canonical key;
* has exactly one relative sign;
* is used in at most one selected packet.

Packets belonging to different keys are therefore coordinate-disjoint as well. This constructs exactly \(M_{\rm global}\) coordinate-disjoint opposite-sign packets.

The singleton formal fibers and size-two formal fibers are disjoint populations.

Now apply the one common bad set. In row \(i\), at most \(B_i\) formal coordinates can be bad. Hence:

* at least \(U_i-B_i\) singleton anchors remain isolated and nonzero;
* at most \(B_i\) selected packet coordinates are bad;
* because the packet family is coordinate-disjoint, at most \(B_i\) packets are destroyed in that row.

These two conclusions hold simultaneously. They do not allocate the budget twice; each is a conservative lower bound against the same bad set.

Thus the surviving singleton count is

$$
\boxed{
G
=
\sum_i(U_i-B_i)
=
82988200-1167610
=
81820590.
}
\tag{6.1}
$$

The surviving packet count is

$$
\boxed{
N
=
M_{\rm global}-\sum_iB_i
=
1326892-1167610
=
159282.
}
\tag{6.2}
$$

---

# 7. Global matched-packet inequality

Concatenate the thirteen padded coefficient-magnitude arrays. Their total length is \(K\), total squared norm is \(E\), and total \(\ell_1\)-norm is

$$
L=\sum_iL_i.
$$

Among the \(K\) entries are, disjointly:

1. \(G\) surviving unit-modulus singleton anchors;
2. \(N\) surviving opposite-sign packets.

For a packet with phase

$$
\zeta=Z^{d_6}W^{d_r},\qquad|\zeta|=1,
$$

the two magnitudes are

$$
r_+=|1+\zeta|,
\qquad
r_-=|1-\zeta|.
$$

Exactly,

$$
r_+^2+r_-^2=4,
\tag{7.1}
$$

and

$$
r_++r_-\le2\sqrt2.
\tag{7.2}
$$

Therefore the selected coordinates have exact squared energy

$$
\boxed{
Q=G+4N=82457718.
}
\tag{7.3}
$$

The number of remaining padded coordinates is

$$
\boxed{
R=K-G-2N=888194638.
}
\tag{7.4}
$$

Their squared energy is \(E-Q\). Hence

$$
L
\le
G+2\sqrt2\,N+\sqrt{R(E-Q)}.
\tag{7.5}
$$

Put

$$
A=G+2\sqrt2\,N.
$$

Then

$$
A+\sqrt{R(E-Q)}
=
\frac{A}{\sqrt Q}\sqrt Q
+\sqrt R\,\sqrt{E-Q}.
$$

Cauchy–Schwarz in \(\mathbb R^2\) yields

$$
L^2
\le
\left(
R+\frac{A^2}{Q}
\right)E.
\tag{7.6}
$$

But

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
=
KE-L^2.
$$

Since \(K-R=G+2N\), direct simplification gives

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
\ge
\frac{(6-4\sqrt2)GN}{G+4N}\,E.
}
\tag{7.7}
$$

This is the same abstract packet lemma as in Round 58, now independently certified with a new determinant census and new global key merge.

---

# 8. Exact arithmetic at \(\theta=300187\)

The regenerated quantities are

$$
\boxed{
\begin{aligned}
K&=970333792,\\
H&=3318,\\
G&=81820590,\\
N&=159282,\\
Q&=82457718,\\
R&=888194638.
\end{aligned}}
\tag{8.1}
$$

Use the exact rational estimate

$$
\sqrt2<\frac{577}{408},
$$

certified by

$$
577^2-2\cdot408^2=1.
$$

Thus

$$
6-4\sqrt2
>
6-\frac{4\cdot577}{408}
=
\frac{35}{102}.
\tag{8.2}
$$

Equation (7.7) therefore gives

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
>
\frac{35GN}{102(G+4N)}E.
\tag{8.3}
$$

The exact cleared comparison is

$$
\boxed{
35GN-3318\cdot102(G+4N)
=
428232492324252>0.
}
\tag{8.4}
$$

Consequently,

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
}
\tag{8.5}
$$

Since the remaining slacks are nonnegative,

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}\ge3318E.
}
\tag{8.6}
$$

---

# 9. Baseline contradiction

Using the exact slack identity and

$$
K-1-3318=970330473,
$$

we obtain

$$
\begin{aligned}
M_{\rm ord}
&=(K-1)E-
\bigl(
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}
\bigr)\\
&\le970330473E.
\end{aligned}
\tag{9.1}
$$

But the inherited target estimate is strict:

$$
\sqrt{D+1}|T_1|>970330473E.
\tag{9.2}
$$

This contradicts the physical baseline inequality

$$
\sqrt{D+1}|T_1|\le M_{\rm ord}.
$$

Hence:

$$
\boxed{
\begin{gathered}
\texttt{GenericTheta300187Exclusion:}\\
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300187)m_6,\\
\text{the fifth centered pair arbitrary and all twelve slopes distinct}\\
\Longrightarrow
\text{no exact baseline exists.}
\end{gathered}}
\tag{9.3}
$$

For \(\delta=-2m_6\), exchange the defect endpoints and reverse the common \(m_6\)-orientation. The magnitude census and inequalities are unchanged.

This remains a finite-slope candidate theorem pending review outside this proof-development context. It does not settle the exact baseline problem in general, produce a frozen-edge vector, or prove PW10. An ansatz exclusion is not a phase-uniform proof of PW10. 

---

# 10. Reproducibility package

The audit package contains:

* the widened-range integer-only determinant enumerator;
* per-row key aggregation;
* thirteen-way global merge;
* an independent merged-binary Python verifier;
* exact low-fiber and size-three summaries;
* all raw-stream and key-file SHA-256 digests;
* the two weighted global-key checksums;
* exact arithmetic certificates;
* the complete regeneration log;
* a Markdown archive of the public Round 58 response.

The bundle SHA-256 is

```text
fd5cc196b7568316942e49fc3a3e30725c6e3ab6444c96d8445f15c2558bf046
```

The merged global-key binary SHA-256 is

```text
2084ec640bcd501442574a9a88174e18c3755f97bcb1f4655bf8d62cfd2d4b05
```

The Round 58 Markdown archive has SHA-256

```text
e48d04426d22a998ea3d21baced3f1075e9b615e17059764bda1cdfb9288137d
```

That hash identifies the provided Markdown serialization; it is not asserted to equal the browser-copy byte serialization.

* [Complete Round 59 audit bundle](sandbox:/mnt/data/round59_theta300187_audit_bundle.zip)
* [Round 58 public-response Markdown archive](sandbox:/mnt/data/round58_response.md)
* [Integer-only low-fiber reproducer](sandbox:/mnt/data/round59_size3_reproducer.cpp)
* [Per-row key-count source](sandbox:/mnt/data/round59_size2_keycounts.cpp)
* [Audited global merge source](sandbox:/mnt/data/round59_size2_merge_audit.cpp)
* [Independent global-binary verifier](sandbox:/mnt/data/round59_verify_global.py)
* [Low-fiber summary](sandbox:/mnt/data/round59_lowfiber_summary.csv)
* [Size-three summary](sandbox:/mnt/data/round59_size3_summary.csv)
* [Global packet summary](sandbox:/mnt/data/round59_global_size2_summary.csv)
* [Detailed global-key census](sandbox:/mnt/data/round59_global_size2_detail.txt)
* [Raw-stream checksums](sandbox:/mnt/data/round59_size2_checks.txt)
* [Raw-stream SHA-256 manifest](sandbox:/mnt/data/round59_stream_sha256.txt)
* [Exact arithmetic certificates](sandbox:/mnt/data/round59_exact_inequality_checks.txt)
* [All artifact digests](sandbox:/mnt/data/round59_digest.txt)

---

# VERIFIED

* The support table (59.2) and

  $$
  K=970333792.
  $$
* The \(1/127\) near-ray certificate.
* The failure of denominator \(128\).
* The support-loss ceilings \(m_i\).
* The common bad-coordinate budgets \(B_i\).
* All thirteen singleton, size-two, size-three, and size-four histograms.
* The exact total

  $$
  206414640
  $$

  of raw size-two fibers.
* Every raw size-two fiber is a genuine binomial.
* Zero collected \(\pm2\) size-two monomials.
* Zero collected size-two Laurent cancellations.
* The seven global moment checksums.
* Every per-row sign total and rowwise match count.
* The canonical orientation and relative-sign convention.
* The exact global key count

  $$
  7977021.
  $$
* The two weighted merge checksums (5.4)–(5.5).
* The global opposite-sign count

  $$
  M_{\rm global}=1326892.
  $$
* The cross-row gain

  $$
  711844.
  $$
* The deletion-robust packet count

  $$
  N=159282.
  $$
* The independent Python verification of the merged binary.
* The global packet inequality (7.7).
* The cleared margin

  $$
  428232492324252.
  $$
* `GenericTheta300187Exclusion` within this finite-slope ansatz.

# CORRECTED

* The inherited temporary \(t\)-array bound for \(\theta=300185\) is too narrow at \(\theta=300187\); the audit source uses \([-3800000,3800000]\).
* The storage-range issue is an implementation correction, not a determinant or counting correction.
* Rowwise matching gives only

  $$
  615048
  $$

  pairs and is not the correct load-bearing count.
* Equal canonical keys may be matched across deleted rows because \(Z,W\) are common globally.
* The correct global match count is

  $$
  1326892.
  $$
* No size-three packet or \(E/K\) estimate is required.

# DISPROVED

* The possibility that the independently regenerated global size-two packet relaxation lies below \(3318E\).
* The claim that rowwise packet matching exhausts the usable size-two structure.
* The need for a size-three argument at \(\theta=300187\).
* The status “generic \(\theta=300187\) remains open” within this precise finite-slope ansatz.

# NECESSARY-ONLYP

* Independent replication outside this proof-development context is still required before broader promotion of the candidate ansatz theorem.
* This theorem covers only the stated twelve-slope family.
* It does not prove the existence or nonexistence of a general baseline.
* It does not exclude \(x^{(10)}\).
* It does not produce a physical vector above \(10\).
* It does not prove PW10.

# EQUIVALENT

Within the audited Wiener route,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}\ge3318E
$$

is equivalent to

$$
M_{\rm ord}\le970330473E.
$$

For each globally matched key, the packet magnitudes are exactly

$$
|1+\zeta|,\qquad |1-\zeta|.
$$

The globally coupled packet coefficient is exactly

$$
\frac{(6-4\sqrt2)GN}{G+4N}.
$$

# NUMERICAL-ONLY

* No floating-point phase sampling was used.
* No heuristic phase minimization was used.
* No interval branch-and-bound was needed.
* The determinant enumeration, per-row aggregation, and global merge are integer-only.
* The radical bound is reduced to the exact Pell-type identity

  $$
  577^2-2\cdot408^2=1.
  $$

# CONJECTURED

* External replication of `GenericTheta300187Exclusion`.
* Extension of the global packet method to later unresolved four-ratio values.
* A general thirteen-slope ansatz theorem.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* The full ratio-two and arbitrary one-defect classes.
* Non-centrally-symmetric twelve-slope families outside the candidate exclusions.
* A general thirteen-slope theorem.
* Dense nonquadratic baseline solutions.
* Existence of an exact baseline vector outside the excluded finite-slope ansätze.
* Frozen named-edge retrieval.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the \(\theta=300187\) global cross-cofactor census

$$
\boxed{
M_{\rm global}=1326892,\qquad
N=159282,
}
$$

together with

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
}
$$

No exact baseline vector, exact frozen-edge vector, exclusion of \(x^{(10)}\), exact physical vector above \(10\), or phase-uniform PW10 proof was produced.

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIES GAP.}}
$$
