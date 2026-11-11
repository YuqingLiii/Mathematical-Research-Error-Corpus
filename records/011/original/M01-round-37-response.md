# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The complete mirror formulas (37.1)–(37.6) are correct. I obtain exact grouped \(\ell_2\)-energy identities for the ordinary coefficients and a stronger simultaneous root-selection theorem: the \(13\) roots may be chosen with at most \(1000\) parent defects, with all ordered nonzero root differences distinct, and with

$$
\left|\sum_{i=0}^{12}\omega^{r_i}\right|^2\ge\frac{2431}{199}.
$$

However, the strongest Cauchy–Schwarz/Parseval estimate after grouping is provably incapable of reversing `MirrorResidual12`. The obstruction is already present in the zero-row ordinary energy:

$$
\boxed{
\mathcal E_{0,\mathrm{ord}}
\ge
\frac{D-26}{52}\,\mathcal E_T,
}
$$

where \(\mathcal E_T=\sum_\nu|T_\nu|^2\). Consequently, the support-based Cauchy upper estimate is itself strictly larger than the exceptional side for every possible cofactor field. This rigorously delimits that proof route.

A larger translated support with a positive-semidefinite nullspace weight is exactly a positive sum of rank-one mirror circuits. It returns to the same grouped residual and does not automatically improve the target-to-ordinary norm ratio.

Thus the audited ansatz theorem remains:

$$
\boxed{
\text{every quadratic-Gauss baseline mixture uses at least twelve paired ruling slopes}.
}
$$

No thirteen-slope lower bound is proved.

The fixed normalization and prior open status agree with the supplied source: \(D=941541228773064677\), \(B^2=[D(D+2)]^{-1}\), \(A_{\rm sp}^2=(D+1)B^2\), and no exact baseline or PW10 proof was previously available. 

---

# 1. Audit of the cross-correlations

Remove the common quadratic chirp and write

$$
p_i(c):=\sum_{\ell\in\mathbb F_D}A_i(\ell)\omega^{\ell c},
$$

so that

$$
a_i(c)=\omega^{-M_0c^2/8}p_i(c).
$$

Define

$$
C_{ij}(\delta)
=
\sum_\ell
A_i(\ell+\delta)\overline{A_j(\ell)}.
$$

Then

$$
\begin{aligned}
p_i(c)\overline{p_j(c)}
&=
\sum_{\ell,m}
A_i(\ell)\overline{A_j(m)}
\omega^{(\ell-m)c}\\
&=
\boxed{
\sum_{\delta}
C_{ij}(\delta)\omega^{\delta c}.
}
\end{aligned}
\tag{1.1}
$$

Thus the orientation in (37.1) is correct. It also gives

$$
\boxed{
C_{ji}(-\delta)=\overline{C_{ij}(\delta)}.
}
\tag{1.2}
$$

---

# 2. Re-derivation of the complete mirror coefficient equation

The physical square-coordinate reconstruction is

$$
F(S_i(c),S_j(c))
=
\frac1D
\sum_x
\Psi(x,y_{ij})
\omega^{(c+d_{ij})x},
$$

where

$$
y_{ij}=\frac{r_i-r_j}{2},
\qquad
d_{ij}=\frac{r_i+r_j}{2}.
$$

Substitute (1.1) into

$$
\sum_{i,j}
p_i(c)\overline{p_j(c)}
F(S_i(c),S_j(c))=0,
$$

and take the unnormalized Fourier coefficient

$$
\sum_c(\cdots)\omega^{-\nu c}.
$$

The exponent containing \(c\) is

$$
c(\delta+x-\nu).
$$

Character orthogonality forces

$$
x=\nu-\delta.
$$

The factor \(D\) from the character sum cancels the \(D^{-1}\) in the physical reconstruction. Hence

$$
\boxed{
0=
\sum_{i,j,\delta}
C_{ij}(\delta)
\omega^{d_{ij}(\nu-\delta)}
\Psi(\nu-\delta,y_{ij}).
}
\tag{2.1}
$$

This is exactly (37.2).

---

# 3. Exceptional and ordinary coefficients

Because the roots are distinct,

$$
y_{ij}=0\iff i=j.
$$

For \(i=j\),

$$
d_{ii}=r_i.
$$

At \(x=1\), one has \(\delta=\nu-1\); at \(x=-1\), one has \(\delta=\nu+1\). Evenness gives

$$
\Psi(-1,0)=\Psi(1,0).
$$

Therefore the full exceptional coefficient is

$$
\boxed{
T_\nu
=
\sum_i
\left[
\omega^{r_i}C_{ii}(\nu-1)
+
\omega^{-r_i}C_{ii}(\nu+1)
\right].
}
\tag{3.1}
$$

This verifies (37.3), including both spike offsets.

For an arbitrary physical row \(y\), define

$$
I_y
=
\left\{
(i,j):
\frac{r_i-r_j}{2}=y
\right\}.
$$

The complete—exceptional included—coefficient at \((x,y)\) is

$$
\boxed{
\widetilde W_{\nu;x,y}
=
\sum_{(i,j)\in I_y}
C_{ij}(\nu-x)\omega^{d_{ij}x}.
}
\tag{3.2}
$$

The ordinary coefficient \(W_{\nu;x,y}\) equals this expression except that the two coordinates

$$
(x,y)=(1,0),\quad(-1,0)
$$

are removed and combined into \(T_\nu\).

Thus

$$
\boxed{
T_\nu\Psi(1,0)
+
\sum_{(x,y)\ne(\pm1,0)}
W_{\nu;x,y}\Psi(x,y)=0.
}
\tag{3.3}
$$

Taking absolute values and using

$$
\frac{A_{\rm sp}}B=\sqrt{D+1}
$$

gives exactly

$$
\boxed{
\sqrt{D+1}|T_\nu|
\le
\sum_{(x,y)\ne(\pm1,0)}
|W_{\nu;x,y}|.
}
\tag{3.4}
$$

---

# 4. Exceptional-side Parseval identity

Define

$$
G(c)
:=
\sum_i
\omega^{r_i+c}|p_i(c)|^2.
\tag{4.1}
$$

Let

$$
A_\nu=\sum_i\omega^{r_i}C_{ii}(\nu-1),
\qquad
B_\nu=\sum_i\omega^{-r_i}C_{ii}(\nu+1),
$$

so \(T_\nu=A_\nu+B_\nu\).

Using (1.1),

$$
\begin{aligned}
\sum_\nu A_\nu\omega^{\nu c}
&=
\sum_i\omega^{r_i+c}|p_i(c)|^2\\
&=G(c),
\end{aligned}
$$

while

$$
\sum_\nu B_\nu\omega^{\nu c}
=
\overline{G(c)}.
$$

Therefore

$$
\sum_\nu T_\nu\omega^{\nu c}
=
G(c)+\overline{G(c)}
=
2\sum_i
\cos\left(\frac{2\pi(r_i+c)}D\right)|p_i(c)|^2.
$$

Unnormalized Parseval gives

$$
\boxed{
\sum_\nu|T_\nu|^2
=
\frac1D
\sum_c
\left|
2\sum_i
\cos\left(\frac{2\pi(r_i+c)}D\right)|p_i(c)|^2
\right|^2.
}
\tag{4.2}
$$

Thus (37.6) is correct.

---

# 5. Exact grouped ordinary \(\ell_2\) energy

The load-bearing observation is that, within one difference row \(y\), the values \(d_{ij}\) are distinct.

Indeed,

$$
r_i=d_{ij}+y,\qquad
r_j=d_{ij}-y,
$$

so \(d_{ij}\) and \(y\) recover the ordered pair.

For fixed \(y\), expand

$$
\sum_{\nu,x}
|\widetilde W_{\nu;x,y}|^2.
$$

Using (3.2), put \(\delta=\nu-x\). Summation over \(x\) gives

$$
\sum_x
\omega^{(d_{ij}-d_{k\ell})x}
=
D\,\mathbf1_{\{(i,j)=(k,\ell)\}}.
$$

Hence

$$
\boxed{
\sum_{\nu,x}
|\widetilde W_{\nu;x,y}|^2
=
D\sum_{(i,j)\in I_y}
\sum_\delta|C_{ij}(\delta)|^2.
}
\tag{5.1}
$$

This identity already includes every multiplicity of equal root differences.

Summing over \(y\),

$$
\boxed{
\sum_{\nu,x,y}
|\widetilde W_{\nu;x,y}|^2
=
D\sum_{i,j,\delta}|C_{ij}(\delta)|^2.
}
\tag{5.2}
$$

---

## 5.1 Character-domain form

Put

$$
S(c)=\sum_i|p_i(c)|^2.
$$

From (1.1) and Parseval,

$$
\sum_\delta|C_{ij}(\delta)|^2
=
\frac1D
\sum_c
|p_i(c)|^2|p_j(c)|^2.
$$

Therefore

$$
\boxed{
D\sum_{i,j,\delta}|C_{ij}(\delta)|^2
=
\sum_cS(c)^2.
}
\tag{5.3}
$$

---

## 5.2 Removing the two exceptional coordinates

The two separately removed coefficient sequences are \(A_\nu\) and \(B_\nu\). Each has energy

$$
\sum_\nu|A_\nu|^2
=
\sum_\nu|B_\nu|^2
=
\frac1D\sum_c|G(c)|^2.
$$

Consequently, the exact total ordinary energy is

$$
\boxed{
\mathcal E_{\rm ord}
:=
\sum_{\nu}
\sum_{(x,y)\ne(\pm1,0)}
|W_{\nu;x,y}|^2
=
\sum_cS(c)^2
-
\frac2D\sum_c|G(c)|^2.
}
\tag{5.4}
$$

This is the strongest global grouped \(\ell_2\) identity.

---

# 6. Off-diagonal and zero-row energies

Separate

$$
\mathcal E_{\rm off}
=
D\sum_{i\ne j,\delta}|C_{ij}(\delta)|^2
$$

and

$$
\mathcal E_{0,\rm ord}
=
D\sum_{i,\delta}|C_{ii}(\delta)|^2
-
\sum_\nu(|A_\nu|^2+|B_\nu|^2).
$$

Then

$$
\mathcal E_{\rm ord}
=
\mathcal E_{\rm off}+\mathcal E_{0,\rm ord}.
$$

The character-domain forms are

$$
\boxed{
\mathcal E_{\rm off}
=
\sum_c
\left[
S(c)^2-\sum_i|p_i(c)|^4
\right],
}
\tag{6.1}
$$

and

$$
\boxed{
\mathcal E_{0,\rm ord}
=
\sum_c\sum_i|p_i(c)|^4
-
\frac2D\sum_c|G(c)|^2.
}
\tag{6.2}
$$

These are exact; no root genericity is used.

---

# 7. Exact symmetries

Equation (1.2) implies

$$
\boxed{
\widetilde W_{-\nu;-x,-y}
=
\overline{\widetilde W_{\nu;x,y}}.
}
\tag{7.1}
$$

It also gives

$$
\boxed{T_{-\nu}=\overline{T_\nu}.}
\tag{7.2}
$$

The physical coefficient symmetry

$$
H_{y,z}=H_{z,y}=H_{-y,-z}
$$

and baseline evenness imply

$$
\Psi(-x,-y)=\Psi(x,y).
$$

These relations pair the ordinary coefficient positions exactly. They do **not** make the corresponding physical phases independent or conjugate. In particular,

$$
\Psi(-x,-y)=\Psi(x,y)
$$

does not imply that \(\Psi(x,y)\) is real.

Thus the symmetry halves neither the absolute-value budget in (3.4) nor the \(\ell_2\) energy in (5.4). Any stronger use of \(H_{y,z}=H_{z,y}\) would reintroduce the full Fourier-\(+1\) phase compatibility problem.

---

# 8. Exact support factors

Each cofactor polynomial \(p_i\) is a sum of at most

$$
f=12!=479001600
$$

characters. Hence

$$
|\operatorname{supp}C_{ij}|\le f^2,
$$

where

$$
\boxed{f^2=229442532802560000.}
$$

Let

$$
m_y=|I_y|.
$$

For a fixed \(\nu\), the number of potentially nonzero \(x\)-positions in row \(y\ne0\) is at most

$$
\min\{D,m_yf^2\}.
$$

The zero row contributes at most \(D-2\) ordinary coordinates. Therefore the exact support-based Cauchy factor is

$$
\boxed{
P(R)
=
D-2+
\sum_{y\ne0}
\min\{D,m_yf^2\}.
}
\tag{8.1}
$$

Consequently,

$$
\boxed{
\sum_\nu
\left(
\sum_{\rm ordinary}|W_{\nu;x,y}|
\right)^2
\le
P(R)\,\mathcal E_{\rm ord}.
}
\tag{8.2}
$$

This tracks every root-difference multiplicity.

---

# 9. Simultaneous Sidon, low-defect, high-character-sum roots

The Round 36 parent-defect count is

$$
H_{\rm par}
=
4474129380309388800.
$$

Choose the thirteen roots independently and uniformly in \(\mathbb F_D\). Let \(X\) count parent-equality and parent-\((-8)\) defects. Then

$$
\mathbb E X=\frac{H_{\rm par}}D.
$$

There are \(13\cdot12=156\) ordered nonzero root differences. The number of unordered pairs of such ordered differences is

$$
\binom{156}{2}=12090.
$$

Every equality between two distinct ordered differences is a proper linear equation and has probability \(1/D\). Thus the probability that the ordered-difference map fails to be injective is at most \(12090/D\).

By Markov,

$$
\Pr(X\ge1001)
\le
\frac{H_{\rm par}}{1001D}.
$$

Hence the event

$$
\mathcal G=
\{
X\le1000
\text{ and all ordered nonzero root differences are distinct}
\}
$$

has probability at least

$$
1-\frac{H_{\rm par}}{1001D}-\frac{12090}{D}.
$$

The exact comparison

$$
\begin{aligned}
&1001D
-200H_{\rm par}
-200\cdot1001\cdot12090\\
&\qquad=
47656893937539563677>0
\end{aligned}
$$

gives

$$
\boxed{\Pr(\mathcal G)>\frac{199}{200}.}
\tag{9.1}
$$

Now put

$$
Z=\sum_{i=0}^{12}\omega^{r_i}.
$$

For independent uniform roots,

$$
\mathbb E|Z|^2=13,
$$

and always \(|Z|^2\le169\).

If every point in \(\mathcal G\) had

$$
|Z|^2<\frac{2431}{199},
$$

then

$$
\begin{aligned}
\mathbb E|Z|^2
&<
\frac{199}{200}\frac{2431}{199}
+\frac1{200}\,169\\
&=13,
\end{aligned}
$$

a contradiction.

Therefore:

$$
\boxed{
\begin{gathered}
\exists\text{ thirteen roots such that}\\
X\le1000,\quad
(r_i-r_j)_{i\ne j}\text{ are all distinct},\\
\left|\sum_i\omega^{r_i}\right|^2
\ge\frac{2431}{199}.
\end{gathered}
}
\tag{9.2}
$$

Thus the earlier low-collision selection can be strengthened to an exact Sidon root selection without weakening its character-sum lower bound.

---

# 10. The Sidon support factor

For the roots from (9.2),

$$
m_y=1
\qquad(y\ne0).
$$

There are \(156\) nonzero difference rows. Hence

$$
\boxed{
P_{\rm Sid}
=
D-2+156f^2
=
36734576345972424675.
}
\tag{10.1}
$$

The support Cauchy bound becomes

$$
\boxed{
\sum_\nu
\left(
\sum_{\rm ordinary}|W_{\nu;x,y}|
\right)^2
\le
P_{\rm Sid}\,\mathcal E_{\rm ord}.
}
\tag{10.2}
$$

This is substantially sharper than using all \(157D-2\) coordinate slots, but it remains far too weak.

---

# 11. Stronger rowwise Cauchy–Parseval bound

With Sidon roots, every nonzero difference row contains one ordered pair. Therefore, for every \(\nu\),

$$
\sum_{\rm ordinary}|W_{\nu;x,y}|
=
\mathcal O+Z_\nu,
$$

where

$$
\mathcal O
=
\sum_{i\ne j}\|C_{ij}\|_1
$$

is independent of \(\nu\), and

$$
Z_\nu
=
\sum_{x\ne\pm1}
\left|
\sum_i
C_{ii}(\nu-x)\omega^{r_ix}
\right|.
$$

Because \(|\operatorname{supp}C_{ij}|\le f^2\),

$$
\|C_{ij}\|_1
\le
f\|C_{ij}\|_2.
$$

There are \(156\) off-diagonal ordered pairs, so

$$
\mathcal O^2
\le
156f^2
\sum_{i\ne j,\delta}|C_{ij}(\delta)|^2
=
\frac{156f^2}{D}\mathcal E_{\rm off}.
\tag{11.1}
$$

For \(Z_\nu\), Cauchy in the \(D-2\) ordinary zero-row coordinates gives

$$
\sum_\nu Z_\nu^2
\le
(D-2)\mathcal E_{0,\rm ord}.
\tag{11.2}
$$

Minkowski in \(\ell_2(\nu)\) now gives the strongest support/Parseval estimate obtained here:

$$
\boxed{
\begin{aligned}
\sum_\nu
\left(
\sum_{\rm ordinary}|W_{\nu;x,y}|
\right)^2
\le
\left[
\sqrt{156f^2\,\mathcal E_{\rm off}}
+
\sqrt{(D-2)\mathcal E_{0,\rm ord}}
\right]^2.
\end{aligned}
}
\tag{11.3}
$$

Every support and multiplicity factor is explicit.

---

# 12. Exact Cauchy–Parseval barrier

Define

$$
\mathcal H_4
=
\sum_c\sum_i|p_i(c)|^4,
\qquad
\mathcal G_2
=
\sum_c|G(c)|^2.
$$

Equation (6.2) says

$$
\mathcal E_{0,\rm ord}
=
\mathcal H_4-\frac2D\mathcal G_2.
\tag{12.1}
$$

Pointwise,

$$
|G(c)|^2
=
\left|
\sum_i
\omega^{r_i+c}|p_i(c)|^2
\right|^2
\le
13\sum_i|p_i(c)|^4.
$$

Thus

$$
\mathcal G_2\le13\mathcal H_4.
\tag{12.2}
$$

The exceptional energy is

$$
\mathcal E_T
:=
\sum_\nu|T_\nu|^2
=
\frac4D
\sum_c(\operatorname{Re}G(c))^2
\le
\frac4D\mathcal G_2
\le
\frac{52}{D}\mathcal H_4.
\tag{12.3}
$$

Meanwhile,

$$
\mathcal E_{0,\rm ord}
\ge
\left(1-\frac{26}{D}\right)\mathcal H_4.
$$

Combining with (12.3),

$$
\boxed{
\mathcal E_{0,\rm ord}
\ge
\frac{D-26}{52}\,\mathcal E_T.
}
\tag{12.4}
$$

Now the second term in the upper bound (11.3) already satisfies

$$
(D-2)\mathcal E_{0,\rm ord}
\ge
\frac{(D-2)(D-26)}{52}\mathcal E_T.
$$

But

$$
(D-2)(D-26)-52(D+1)
=
D(D-80)>0.
$$

Therefore

$$
\boxed{
(D-2)\mathcal E_{0,\rm ord}
>
(D+1)\mathcal E_T.
}
\tag{12.5}
$$

The left side of `MirrorResidual12` is exactly

$$
(D+1)\mathcal E_T.
$$

Hence the Cauchy–Parseval upper estimate (11.3) is **always numerically larger** than the exceptional side, even before including any off-diagonal ordinary rows.

This proves:

$$
\boxed{
\begin{gathered}
\text{No argument consisting only of}\\
\text{row-support Cauchy--Schwarz plus the exact Parseval energies}\\
\text{can reverse `MirrorResidual12'.}
\end{gathered}
}
\tag{CauchyParsevalNoGo}
$$

This is a rigorous limitation of that specified method—not a statement that the true ordinary \(\ell_1\) side is large.

---

# 13. A fully evaluated universal upper bound

Since every \(p_i(c)\) is a sum of at most \(f\) unit characters,

$$
|p_i(c)|\le f.
$$

Consequently,

$$
\mathcal E_{\rm off}
\le
169Df^4,
$$

and

$$
\mathcal E_{0,\rm ord}
\le
13Df^4.
$$

Substitution into (11.3) gives

$$
\boxed{
\begin{aligned}
\sum_\nu
\left(
\sum_{\rm ordinary}|W_{\nu;x,y}|
\right)^2
\le
\left[
f^3\sqrt{26364\,D}
+
f^2\sqrt{13D(D-2)}
\right]^2.
\end{aligned}
}
\tag{13.1}
$$

This is an exact numerical-factor bound, but it is much weaker than the already insufficient coefficient-dependent bound (11.3).

---

# 14. Norm-data relaxation showing why coefficient structure is essential

There is a complementary method-limit statement.

Retain only:

1. the exceptional sequence \(T_\nu\);
2. ordinary coordinate magnitudes \(B\);
3. central evenness;
4. an ordinary support allowance of \(P_{\rm Sid}\) slots per \(\nu\);
5. total ordinary \(\ell_2\) energy \(\mathcal E_{\rm ord}\).

For each \(\nu\), distribute the required cancellation equally over the available ordinary slots. The minimum ordinary coefficient energy needed to cancel the exceptional term is

$$
\frac{D+1}{P_{\rm Sid}}|T_\nu|^2.
$$

Summed over \(\nu\),

$$
\mathcal E_{\min}
=
\frac{D+1}{P_{\rm Sid}}\mathcal E_T.
$$

But from (5.4) and \(|G|\le S\),

$$
\mathcal E_{\rm ord}
\ge
\left(1-\frac2D\right)\sum_cS(c)^2,
$$

while

$$
\mathcal E_T
\le
\frac4D\sum_cS(c)^2.
$$

Hence

$$
\mathcal E_{\rm ord}
\ge
\frac{D-2}{4}\mathcal E_T
>
\frac{D+1}{P_{\rm Sid}}\mathcal E_T.
$$

The remaining ordinary energy can be added in coefficient pairs whose physical contributions cancel identically.

Thus there is an abstract magnitude-compatible, centrally even coefficient relaxation satisfying:

* every scalar mirror equation;
* the exact exceptional energy;
* the exact ordinary total \(\ell_2\) energy;
* the same support allowance.

It need not come from cofactor cross-correlations and need not satisfy the global Fourier-\(+1\) phase equations. Therefore:

$$
\boxed{
\text{The data }
(\mathcal E_T,\mathcal E_{\rm ord},P_{\rm Sid})
\text{ and central symmetry alone cannot exclude a baseline.}
}
\tag{14.1}
$$

The remaining load-bearing structure is the nonlinear cross-correlation realization

$$
C_{ij}=A_i\star\widetilde{\overline{A_j}}
$$

together with the global physical phase compatibility.

---

# 15. Larger translated supports reduce to the same residual

Suppose \(t>k+1\) translated square rows are selected, so the left nullspace has dimension

$$
s=t-k.
$$

Let \(A(c)\) be a \(t\times s\) matrix whose columns span that nullspace:

$$
A(c)^{\mathsf T}V_-(c)=0.
$$

For a positive-semidefinite matrix \(\Lambda\succeq0\), set

$$
M(c)=A(c)\Lambda A(c)^*.
$$

Then

$$
\sum_{i,j}M_{ij}(c)F(S_i(c),S_j(c))=0.
\tag{15.1}
$$

Factor

$$
\Lambda=UU^*.
$$

If \(u_q\) denotes a column of \(U\), put

$$
b_q(c)=A(c)u_q.
$$

Then

$$
M(c)=\sum_q b_q(c)b_q(c)^*,
$$

and (15.1) is exactly

$$
\boxed{
\sum_q
b_q(c)^{\mathsf T}F(c)\overline{b_q(c)}=0.
}
\tag{15.2}
$$

Thus every positive-semidefinite larger-support circuit is a positive sum of rank-one mirror circuits.

After Fourier extraction, its exceptional and ordinary grouped coefficients are just the corresponding positive sums:

$$
T_\nu^{\rm tot}=\sum_qT_\nu^{(q)},
\qquad
W_{\nu;x,y}^{\rm tot}=\sum_qW_{\nu;x,y}^{(q)}.
$$

It therefore obeys the same residual inequality

$$
\sqrt{D+1}|T_\nu^{\rm tot}|
\le
\sum_{\rm ordinary}|W_{\nu;x,y}^{\rm tot}|.
$$

No dimension-only or positivity-only improvement appears.

A larger translated support may still help if one proves a new correlation theorem for the combined grouped coefficients. Merely replacing a rank-one null vector by

$$
M=A\Lambda A^*
$$

reduces to the same mirror residual and does not supply a thirteen-slope lower bound.

---

# 16. Exact remaining frontier

For the strengthened Sidon/low-defect roots, define

$$
\mathfrak R_{\rm mir}
=
\sum_\nu
\left(
\sum_{\rm ordinary}|W_{\nu;x,y}|
\right)^2
-
(D+1)\sum_\nu|T_\nu|^2.
\tag{16.1}
$$

Every baseline must satisfy

$$
\boxed{\mathfrak R_{\rm mir}\ge0.}
\tag{16.2}
$$

A thirteen-slope lower bound would follow from one exact translated circuit with

$$
\mathfrak R_{\rm mir}<0.
$$

The exact \(\ell_2\) identities show that neither:

* total ordinary energy,
* difference-row multiplicities,
* support cardinality,
* central symmetry,
* nor a positive-semidefinite enlargement of the nullspace circuit

is sufficient to force this strict reverse.

The first unresolved coefficient-specific task is therefore:

$$
\boxed{
\text{control the grouped ordinary }\ell_1\text{ norm using the actual
cross-correlation phases of the cofactors.}
}
$$

Equivalently, one needs a bound genuinely sharper than

$$
\|C_{ij}\|_1\le f\|C_{ij}\|_2
$$

and sharper than zero-row Cauchy over \(D-2\) coordinates, using simultaneous algebraic relations among all \(C_{ij}\).

---

# Explicit outcome discipline

This round produced:

1. **No exact baseline vector.**
2. **No exact frozen-edge vector.**
3. **No exact exclusion of \(x^{(10)}\).**
4. **No exact physical vector with \(\mathcal F_\Gamma>10\).**
5. **No phase-uniform proof of PW10.**
6. **No thirteen-slope ansatz lower bound.**

Therefore

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

# VERIFIED

* Cross-correlation orientation (37.1).
* The complete Fourier coefficient equation (37.2).
* Both exceptional spike offsets and (37.3).
* The grouping leading to (37.4)–(37.5).
* The exceptional Parseval identity (37.6).
* The exact rowwise grouped ordinary-energy identity (5.1).
* The total ordinary-energy identity (5.4).
* The exact off-diagonal and zero-row decompositions.
* The coefficient symmetries

  $$
  C_{ji}(-\delta)=\overline{C_{ij}(\delta)},
  \qquad
  W_{-\nu;-x,-y}=\overline{W_{\nu;x,y}}.
  $$
* The multiplicity-sensitive support factor \(P(R)\).
* Existence of roots that are simultaneously:

  * ordered-difference Sidon;
  * low-parent-defect;
  * high-character-sum.
* The exact Sidon support factor

  $$
  P_{\rm Sid}=36734576345972424675.
  $$
* The stronger rowwise Cauchy–Parseval upper bound (11.3).
* The zero-row barrier

  $$
  \mathcal E_{0,\rm ord}
  \ge\frac{D-26}{52}\mathcal E_T.
  $$
* `CauchyParsevalNoGo`.
* Reduction of positive-semidefinite larger-support circuits to sums of rank-one mirror circuits.

# CORRECTED

* The low-collision root selection can be strengthened to full ordered-difference Sidonicity without weakening the bound \(2431/199\).
* Equal difference rows must be grouped before Parseval; treating all ordered pairs as separate physical rows overcounts the support.
* The exact ordinary \(\ell_2\) energy is not \(D\sum|C_{ij}|^2\) after exceptional removal; the two separate spike energies must be subtracted as in (5.4).
* The symmetries \(H_{y,z}=H_{z,y}=H_{-y,-z}\) provide exact pairing relations but do not make ordinary phases independent or real.
* A larger nullspace and a positive-semidefinite circuit weight do not, by themselves, improve the target-to-ordinary norm ratio.

# DISPROVED

* Sufficiency of support-count Cauchy–Schwarz plus Parseval for reversing `MirrorResidual12`.
* Sufficiency of rowwise Cauchy–Schwarz plus Parseval for proving a thirteen-slope lower bound.
* Sufficiency of the data

  $$
  (\mathcal E_T,\mathcal E_{\rm ord},P_{\rm Sid})
  $$

  together with central symmetry.
* Any automatic improvement obtained solely by replacing one mirror cofactor vector with a positive-semidefinite larger-support nullspace weight.

# NECESSARY-ONLY

* `MirrorResidual12`.
* The exact residual \(\mathfrak R_{\rm mir}\ge0\).
* The multiplicity-sensitive support factor.
* The stronger Sidon-row upper bound (11.3).
* The cofactor cross-correlation realization of all \(C_{ij}\).

# EQUIVALENT

For the translated mirror circuit:

$$
a(c)^{\mathsf T}F(c)\overline{a(c)}=0
\quad\forall c
$$

is equivalent, by additive Fourier inversion, to the complete family (2.1).

The exceptional coefficient sequence \(T_\nu\) is equivalently represented by the character-domain formula (4.2).

For a positive-semidefinite enlarged nullspace circuit,

$$
M=A\Lambda A^*
$$

is equivalent to a positive sum of rank-one mirror circuits after factoring \(\Lambda\).

# NUMERICAL-ONLY

* No numerical estimate is used in the proof.
* Any empirical value of the grouped ordinary \(\ell_1\) norm remains numerical-only.
* Any numerical \(k=12\) phase optimization remains noncertifying.

# CONJECTURED

* A coefficient-specific inequality strong enough to make

  $$
  \mathfrak R_{\rm mir}<0
  $$

  for a suitable translated circuit.
* A thirteen-slope lower bound for quadratic-Gauss mixtures.
* Eventual nonexistence of every finite-slope quadratic-Gauss baseline.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* A sharp grouped-\(\ell_1\) estimate using the simultaneous cofactor correlations.
* The sign of \(\mathfrak R_{\rm mir}\) for an optimized \(k=12\) circuit.
* Quadratic-Gauss mixtures on twelve or more paired ruling slopes.
* Dense nonquadratic baseline solutions.
* Existence of an exact baseline pure-edge vector.
* Pure retrieval for the frozen named edges.
* Physical liftability of \(x^{(10)}\).
* Existence of an exact physical vector above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the exact grouped-energy theorem

$$
\boxed{
\mathcal E_{\rm ord}
=
\sum_c
\left(\sum_i|p_i(c)|^2\right)^2
-
\frac2D
\sum_c
\left|
\sum_i\omega^{r_i+c}|p_i(c)|^2
\right|^2,
}
$$

together with the resulting method-limit inequality

$$
\boxed{
\mathcal E_{0,\rm ord}
\ge
\frac{D-26}{52}\mathcal E_T,
}
$$

which proves that support-based Cauchy–Schwarz and Parseval alone cannot close the exact \(k=12\) mirror residual.
