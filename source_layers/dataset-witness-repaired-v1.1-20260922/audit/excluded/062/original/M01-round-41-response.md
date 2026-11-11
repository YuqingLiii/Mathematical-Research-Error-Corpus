# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The frozen normalization is

$$
D=941541228773064677,\qquad
B^2=\frac1{D(D+2)},\qquad
A_{\rm sp}^2=(D+1)B^2,
$$

and the physical target remains the exact even, symplectic-Fourier \(+1\) baseline with spikes at \(\pm(1,0)\), together with the PW10 bound.  No exact baseline vector, frozen-edge vector, exclusion of \(x^{(10)}\), physical violator, or phase-uniform PW10 proof is currently available.  Any finite-slope Gauss-mixture exclusion remains an ansatz theorem, not a proof of the physical gate. 

The adjacent \(14\)-root matrix circuit and its convex dual are correct. However, the holomorphic Plücker relation does **not** directly control the required sesquilinear circuit. The exact outcome is a rigorous method limit:

$$
\boxed{
\begin{gathered}
\text{Any valid linear use of the adjacent holomorphic Plücker wedge is either}\\
\text{inadmissible for the physical sesquilinear circuit, or—when a constant}\\
\text{conjugation real structure makes it admissible—has identically zero target gain.}
\end{gathered}}
\tag{PlueckerLinearNoGo}
$$

This is proved for arbitrary adjacent \(k+2\)-root/\(k\)-slope circuits over any odd prime field. An explicit frozen-dimensional canonical-cofactor family attains the zero-target conclusion with a nonzero ordinary Plücker coefficient, so the result is not merely formal.

It does **not** rule out:

* a constant separator using the transpose-symmetric matrix directions;
* a constant separator combining those directions with the Plücker direction to reduce the ordinary denominator;
* a genuinely frequency-dependent matrix multiplier;
* the exact global shared-phase dual across all Fourier frequencies.

No separator satisfying

$$
\rho_\nu>\frac1{\sqrt{D+1}}
$$

is produced, and no thirteen-slope ansatz theorem follows.

---

# 1. The adjacent matrix circuit

Let \(V_-(c)\) be the full translated \(14\times12\) matrix. Let

$$
B(c)=\begin{pmatrix} b^{(0)}(c)&b^{(1)}(c)\end{pmatrix}\in\mathbb C^{14\times2},
$$

where:

* \(b^{(0)}\) is the padded cofactor null vector on \(I_0=\{0,\ldots,12\}\);
* \(b^{(1)}\) is the padded cofactor null vector on \(I_1=\{1,\ldots,13\}\).

Thus

$$
V_-(c)^{\mathsf T}B(c)=0.
$$

For the mirror translated-square circuit,

$$
V_+(c)=\overline{V_-(c)}.
$$

Every coefficient matrix in the paired-ruling span has the form

$$
F(c)=X(c)V_+(c)^{\mathsf T}+V_-(c)Y(c)^{\mathsf T}.
$$

Therefore

$$
\begin{aligned}
B(c)^{\mathsf T}F(c)\overline{B(c)}
={}&
B^{\mathsf T}X\,V_+^{\mathsf T}\overline B
+
B^{\mathsf T}V_-\,Y^{\mathsf T}\overline B\\
={}&0.
\end{aligned}
$$

Hence the exact pointwise matrix circuit is

$$
\boxed{
B(c)^{\mathsf T}F(c)\overline{B(c)}=0_{2\times2}.
}
\tag{1.1}
$$

---

# 2. Fourier extraction of the four matrix entries

Write

$$
b_i^{(q)}(c)
=
\sum_\ell A_i^{(q)}(\ell)\omega^{\ell c},
\qquad q\in\{0,1\},
$$

and define

$$
C_{ij}^{qs}(\delta)
=
\sum_\ell
A_i^{(q)}(\ell+\delta)
\overline{A_j^{(s)}(\ell)}.
$$

Then

$$
\boxed{
b_i^{(q)}(c)\overline{b_j^{(s)}(c)}
=
\sum_\delta
C_{ij}^{qs}(\delta)\omega^{\delta c}.
}
\tag{2.1}
$$

With the translated physical coordinates

$$
y_{ij}=\frac{r_i-r_j}{2},
\qquad
d_{ij}=\frac{r_i+r_j}{2},
$$

Fourier extraction of (1.1) yields, for each \(\nu\),

$$
\boxed{
\mathbf T_\nu\Psi(1,0)
+
\sum_{\rm ordinary}
\mathbf W_{\nu;x,y}\Psi(x,y)
=0_{2\times2}.
}
\tag{2.2}
$$

The entries are exactly:

$$
(\mathbf T_\nu)_{qs}
=
\sum_{i\in I_q\cap I_s}
\left[
\omega^{r_i}C_{ii}^{qs}(\nu-1)
+
\omega^{-r_i}C_{ii}^{qs}(\nu+1)
\right],
\tag{2.3}
$$

and

$$
(\mathbf W_{\nu;x,y})_{qs}
=
\sum_{\substack{
i\in I_q,\ j\in I_s\\
(r_i-r_j)/2=y
}}
C_{ij}^{qs}(\nu-x)\,
\omega^{(r_i+r_j)x/2},
\tag{2.4}
$$

with \((x,y)=\pm(1,0)\) removed from the ordinary sum.

Thus (41.3)–(41.5) are correct, including the support intersections:

$$
I_0\cap I_0=I_0,\qquad
I_1\cap I_1=I_1,\qquad
I_0\cap I_1=\{1,\ldots,12\}.
$$

---

# 3. The physical coefficient is globally shared

Divide (2.2) by \(\Psi(1,0)\). Define

$$
z_{x,y}:=\frac{\Psi(x,y)}{\Psi(1,0)}.
$$

For every ordinary coordinate,

$$
|z_{x,y}|=\frac B{A_{\rm sp}}=\frac1{\sqrt{D+1}}.
$$

The exact matrix identity is

$$
\boxed{
\mathbf T_\nu
=
-\sum_{\rm ordinary}
z_{x,y}\mathbf W_{\nu;x,y}
\qquad\text{for every }\nu.
}
\tag{3.1}
$$

The same scalar \(z_{x,y}\):

* is shared by all four matrix entries;
* is shared by every Fourier frequency \(\nu\);
* obeys the evenness constraint

  $$
  z_{-x,-y}=z_{x,y}.
  $$

Therefore the per-\(\nu\) zonotope test is only a relaxation. It permits a different coefficient vector for each \(\nu\) and generally ignores the even-orbit sharing.

---

# 4. Exact per-frequency convex dual

Use the complex bilinear pairing

$$
\langle\Lambda,X\rangle
=
\operatorname{tr}(\Lambda^{\mathsf T}X)
=
\sum_{q,s}\Lambda_{qs}X_{qs}.
$$

For fixed \(\nu\), define

$$
\mathcal A_\nu(\Lambda)
=
\left(
\langle\Lambda,\mathbf W_{\nu;x,y}\rangle
\right)_{\rm ordinary}.
$$

Then

$$
\rho_\nu
=
\sup_{\Lambda:\,\|\mathcal A_\nu\Lambda\|_1>0}
\frac{
|\langle\Lambda,\mathbf T_\nu\rangle|
}{
\|\mathcal A_\nu\Lambda\|_1
}.
\tag{4.1}
$$

If there exists

$$
\Lambda\in\ker\mathcal A_\nu
$$

with

$$
\langle\Lambda,\mathbf T_\nu\rangle\ne0,
$$

then

$$
\rho_\nu=+\infty.
$$

Otherwise the target functional descends to \(\operatorname{im}\mathcal A_\nu\). Complex \(\ell _1/\ell _\infty\) duality gives

$$
\boxed{
\rho_\nu
=
\min\left\{
\|z\|_\infty:
\mathbf T_\nu
=
\sum_{\rm ordinary}
z_{x,y}\mathbf W_{\nu;x,y}
\right\}.
}
\tag{4.2}
$$

The minimum is attained because all spaces are finite-dimensional.

Thus

$$
\boxed{
\rho_\nu>\frac1{\sqrt{D+1}}
}
$$

would exclude a baseline.

The converse is false: \(\rho_\nu\le1/\sqrt{D+1}\) supplies only a per-frequency coefficient vector, not one global physical phase field.

---

# 5. The exact global shared-phase dual

The physical coefficients are shared across \(\nu\). Let \(\mathcal Q\) denote ordinary even-orbit representatives, and replace

$$
\mathbf W_{\nu;q}
$$

by the appropriately grouped coefficient

$$
\mathbf W_{\nu;q}+\mathbf W_{\nu;-q}
$$

when \(q\ne-q\).

Define

$$
\rho_{\rm glob}
=
\min\left\{
\|z\|_\infty:
\mathbf T_\nu
=
\sum_{q\in\mathcal Q}
z_q\widetilde{\mathbf W}_{\nu;q}
\quad\forall\nu
\right\}.
\tag{5.1}
$$

Its exact dual is

$$
\boxed{
\rho_{\rm glob}
=
\sup_{\{\Lambda_\nu\}}
\frac{
\left|
\sum_\nu
\langle\Lambda_\nu,\mathbf T_\nu\rangle
\right|
}{
\sum_{q\in\mathcal Q}
\left|
\sum_\nu
\langle\Lambda_\nu,\widetilde{\mathbf W}_{\nu;q}\rangle
\right|
}.
}
\tag{5.2}
$$

As before, the value is \(+\infty\) if the numerator does not annihilate the kernel of the ordinary map.

This is the exact matrix separator respecting cross-\(\nu\) coefficient sharing. The physical problem is stronger still because it requires

$$
|z_q|=\frac1{\sqrt{D+1}},
$$

not merely \(\|z\|_\infty\le1/\sqrt{D+1}\).

---

# 6. The four constant-matrix pairings

For a row \(i\), write

$$
b_i=(b_i^{(0)},b_i^{(1)}).
$$

The pointwise rank-one coefficient matrix for an ordered pair \((i,j)\) is

$$
b_i^{\mathsf T}\overline{b_j}.
$$

For the matrix basis

$$
E_{00},\qquad E_{11},\qquad
S:=E_{01}+E_{10},\qquad
J:=E_{01}-E_{10},
$$

the four scalar pairings are:

$$
\boxed{
\langle E_{00},b_i^{\mathsf T}\overline{b_j}\rangle
=
b_i^{(0)}\overline{b_j^{(0)}},
}
\tag{6.1}
$$

$$
\boxed{
\langle E_{11},b_i^{\mathsf T}\overline{b_j}\rangle
=
b_i^{(1)}\overline{b_j^{(1)}},
}
\tag{6.2}
$$

$$
\boxed{
\langle S,b_i^{\mathsf T}\overline{b_j}\rangle
=
b_i^{(0)}\overline{b_j^{(1)}}
+
b_i^{(1)}\overline{b_j^{(0)}},
}
\tag{6.3}
$$

and

$$
\boxed{
\langle J,b_i^{\mathsf T}\overline{b_j}\rangle
=
b_i^{(0)}\overline{b_j^{(1)}}
-
b_i^{(1)}\overline{b_j^{(0)}}.
}
\tag{6.4}
$$

The sign in (6.4) is correct because

$$
\operatorname{tr}(J^{\mathsf T}X)=X_{01}-X_{10}.
$$

This verifies (41.9).

---

# 7. Holomorphic Plücker versus sesquilinear wedge

The audited holomorphic Plücker identity is

$$
\boxed{
b_i^{(0)}b_j^{(1)}
-
b_j^{(0)}b_i^{(1)}
=
\Delta_{0,13}\Delta_{ij}.
}
\tag{7.1}
$$

But the physical \(J\)-pairing is

$$
b_i^{(0)}\overline{b_j^{(1)}}
-
b_i^{(1)}\overline{b_j^{(0)}}.
\tag{7.2}
$$

These are different objects. Equation (7.1) cannot be inserted into (7.2) without an independently proved relation converting the conjugated cofactor vector to the unconjugated one.

---

# 8. Exact conjugation audit

Let \(\mathcal M\) be the ordered slope list. The translated matrix is

$$
V_{\mathcal M}(c)_{i,s}
=
\omega^{-m_s(r_i+c)^2/8}.
$$

Complex conjugation gives

$$
\boxed{
\overline{V_{\mathcal M}(c)}
=
V_{-\mathcal M}(c).
}
\tag{8.1}
$$

Thus conjugation changes the slope set \(\mathcal M\) to \(-\mathcal M\) at the **same** translation parameter \(c\).

For the signed cofactor vectors,

$$
\boxed{
\overline{b_{\mathcal M}^{(q)}(c)}
=
\varepsilon_P\,b_{-\mathcal M}^{(q)}(c),
}
\tag{8.2}
$$

after reordering the negated columns by a permutation \(P\); here

$$
\varepsilon_P=\det P.
$$

There is no general conversion to

$$
b_{\mathcal M}^{(q)}(-c).
$$

---

## 8.1 Minimal counterexample to the proposed \(c\mapsto-c\) conversion

Take one slope \(m\) and two roots. After removing the common \(c^2\)-chirp, one cofactor component has the form

$$
\xi_r(c)
=
\omega^{-mr^2/8}\omega^{-mrc/4}.
$$

Then

$$
\overline{\xi_r(c)}
=
\omega^{mr^2/8}\omega^{mrc/4},
$$

whereas

$$
\xi_r(-c)
=
\omega^{-mr^2/8}\omega^{mrc/4}.
$$

Hence

$$
\boxed{
\frac{\overline{\xi_r(c)}}{\xi_r(-c)}
=
\omega^{mr^2/4}.
}
\tag{8.3}
$$

The ratio depends on the row root \(r\). For two roots with distinct squares there is no common scalar phase converting the whole vector.

Therefore:

$$
\boxed{
\text{Central conjugation does not, in general, turn (7.2) into (7.1), even
after replacing \(c\) by \(-c\).}
}
\tag{8.4}
$$

This is the first decisive obstruction to a direct Plücker separator.

---

# 9. The only admissible constant real-structure case

Suppose the slope multiset is invariant under negation:

$$
-\mathcal M=\mathcal M
$$

and let \(P\) be the corresponding column permutation. Then

$$
\overline{V(c)}=V(c)P.
$$

The same permutation acts on every maximal minor, so

$$
\boxed{
\overline{b^{(q)}(c)}
=
\varepsilon_P\,b^{(q)}(c)
\qquad(q=0,1).
}
\tag{9.1}
$$

After one common scalar phase, the two cofactor vectors may therefore be taken real.

More generally, if there exists a constant matrix \(R\in GL_2(\mathbb C)\) such that

$$
\boxed{
\overline{B(c)}=B(c)R
\quad\forall c,
}
\tag{9.2}
$$

then for a constant separator \(\Lambda\),

$$
b_i\Lambda\overline{b_j}^{\,\mathsf T}
=
b_i\bigl(\Lambda R^{\mathsf T}\bigr)b_j^{\mathsf T}.
\tag{9.3}
$$

Decompose

$$
\Lambda R^{\mathsf T}
=
S+tJ,
\qquad
S^{\mathsf T}=S.
\tag{9.4}
$$

The holomorphic Plücker identity controls exactly the alternating term

$$
b_iJb_j^{\mathsf T}.
$$

---

# 10. Plücker target orthogonality

At a physical target contribution, the row indices coincide:

$$
i=j.
$$

For every two-vector \(b_i\),

$$
\boxed{
b_iJb_i^{\mathsf T}=0.
}
\tag{10.1}
$$

Therefore the entire target sequence of the alternating Plücker component vanishes:

$$
\boxed{
\langle\Lambda_{\rm Pl},\mathbf T_\nu\rangle=0
\quad\forall\nu,
}
\tag{10.2}
$$

whenever

$$
\Lambda_{\rm Pl}R^{\mathsf T}=tJ.
$$

By contrast, the ordinary coefficients are

$$
b_iJb_j^{\mathsf T}
=
\Delta_{0,13}\Delta_{ij},
\qquad i\ne j,
$$

and need not vanish.

This proves:

## Adjacent Plücker target-orthogonality theorem

$$
\boxed{
\begin{gathered}
\text{Whenever a constant conjugation real structure makes the holomorphic}\\
\text{Plücker wedge into a valid physical sesquilinear circuit, that wedge has}\\
\text{identically zero target coefficient at every Fourier frequency.}
\end{gathered}
}
\tag{10.3}
$$

Thus a purely Plücker-controlled constant separator has ratio

$$
\rho_\nu=0
$$

whenever its ordinary denominator is nonzero.

---

# 11. An exact canonical-cofactor equality family

Take the frozen field and choose the twelve slopes

$$
\mathcal M
=
\{\pm1,\pm2,\ldots,\pm6\}.
$$

Order them in six adjacent \(\pm\)-pairs. The negation permutation is a product of six transpositions, so

$$
\varepsilon_P=(-1)^6=1.
$$

Also,

$$
\sum_{m\in\mathcal M}m=0,
$$

so no residual common \(c^2\)-chirp complicates the normalization.

Hence

$$
\overline{b^{(q)}(c)}=b^{(q)}(c).
$$

Choose roots

$$
r_i=i,\qquad 0\le i\le13.
$$

At \(c=0\), the shared \(12\times12\) minor

$$
\Delta_{0,13}(0)
$$

uses row labels

$$
1^2,2^2,\ldots,12^2
$$

and the twelve distinct slope labels \(\pm1,\ldots,\pm6\). Because \(D\) is prime and all labels are distinct, prime-Fourier full spark gives

$$
\Delta_{0,13}(0)\ne0.
$$

For the endpoint ordered pair \((0,13)\),

$$
b_{0}^{(1)}=0,\qquad
b_{13}^{(0)}=0,
$$

so the alternating ordinary coefficient is, up to its fixed orientation sign,

$$
\boxed{
b_0^{(0)}(c)b_{13}^{(1)}(c)
=
\pm\Delta_{0,13}(c)^2.
}
\tag{11.1}
$$

It is not identically zero. Therefore at least one ordinary Fourier coefficient is nonzero.

On the other hand, every target coefficient of \(J\) is zero by (10.1). Hence this is an **actual canonical-cofactor family** with:

$$
\boxed{
\text{nonzero ordinary Plücker coefficient, but zero target gain.}
}
\tag{11.2}
$$

This is the required equality/counterexample family for the Plücker-linear separator class.

---

# 12. What Plücker controls in the complete constant-\(\Lambda\) family

Under a constant real structure (9.2), write

$$
A:=\Lambda R^{\mathsf T}=S+tJ,
\qquad S^{\mathsf T}=S.
$$

Then

$$
\langle\Lambda,\mathbf T_\nu\rangle
=
\langle S,\mathbf T_\nu^{\rm hol}\rangle,
$$

because the \(J\)-target vanishes.

For the ordinary coefficients,

$$
\langle\Lambda,\mathbf W_{\nu;q}\rangle
=
\langle S,\mathbf W_{\nu;q}^{\rm hol}\rangle
+
t\,\mathbf P_{\nu;q},
$$

where

$$
\mathbf P_{\nu;q}
$$

is the Fourier coefficient of the Plücker wedge

$$
\Delta_{0,13}\Delta_{ij}.
$$

Thus the full constant-separator problem reduces exactly to

$$
\boxed{
\sup_{\substack{S^{\mathsf T}=S\\t\in\mathbb C}}
\frac{
|\langle S,\mathbf T_\nu\rangle|
}{
\sum_{\rm ordinary}
\left|
\langle S,\mathbf W_{\nu;q}\rangle
+t\mathbf P_{\nu;q}
\right|
}.
}
\tag{12.1}
$$

This shows precisely what the Plücker direction can and cannot do:

* it carries no numerator;
* it may still reduce the denominator by interfering with the symmetric directions;
* the holomorphic Plücker identity alone does not control that interference.

No exact bound for (12.1) is obtained.

Consequently, I do **not** claim that the entire constant-\(\Lambda\) class is closed. The closed class is the linear Plücker-controlled direction itself.

---

# 13. Endpoint rows do not rescue the Plücker target

The endpoint rows appear in only one null vector:

$$
b_{13}^{(0)}=0,\qquad b_0^{(1)}=0.
$$

Their Plücker contribution is entirely ordinary. For example,

$$
b_0^{(0)}b_{13}^{(1)}
$$

corresponds to the nonzero physical difference row

$$
y=\frac{r_0-r_{13}}2\ne0.
$$

No endpoint row contributes to the cross-circuit target because the target requires the same physical index in both supports:

$$
i\in I_0\cap I_1=\{1,\ldots,12\}.
$$

At each shared target index, the alternating wedge is zero.

Thus:

$$
\boxed{
\text{Endpoint rows supply ordinary Plücker mass but no coherent Plücker target gain.}
}
\tag{13.1}
$$

There is no endpoint telescope that changes the conclusion (10.3).

---

# 14. Frequency-dependent matrix multipliers

A frequency-dependent multiplier is legitimate if it is fixed by the circuit data and not chosen using the unknown physical phase field.

Let

$$
\Lambda(c)
=
\sum_\eta\widehat\Lambda(\eta)\omega^{\eta c}.
$$

Since

$$
B(c)^{\mathsf T}F(c)\overline{B(c)}=0
$$

pointwise,

$$
\left\langle
\Lambda(c),
B(c)^{\mathsf T}F(c)\overline{B(c)}
\right\rangle=0
$$

is also a valid pointwise circuit.

If

$$
\mathbf M_\nu
=
\mathbf T_\nu\Psi(1,0)
+
\sum_q\mathbf W_{\nu;q}\Psi(q)
$$

denotes the matrix Fourier coefficient, the scalar coefficient becomes

$$
\boxed{
0=
\sum_\eta
\left\langle
\widehat\Lambda(\eta),
\mathbf M_{\nu-\eta}
\right\rangle.
}
\tag{14.1}
$$

Thus frequency-dependent multiplication is convolution in \(\nu\).

It is illegitimate only if \(\Lambda(c)\) is allowed to depend on:

* the unknown values \(\Psi(x,y)\);
* the unknown physical phases \(z_{x,y}\);
* the unknown coefficient matrix \(F\).

The global dual (5.2) is exactly the admissible frequency-dependent separator problem with shared physical coefficients.

---

## 14.1 Frequency dependence does not remove the conjugation obstruction

Suppose one seeks a matrix \(\Lambda(c)\) satisfying

$$
u^{\mathsf T}\Lambda(c)\overline v
=
u^{\mathsf T}Jv
$$

for all \(u,v\in\mathbb C^2\).

Replacing \(v\) by \(iv\), the left side changes by \(-i\), while the right side changes by \(+i\). Therefore both sides would have to vanish identically.

Hence no complex-linear \(2\times2\) matrix, constant or frequency-dependent, can universally turn the sesquilinear pairing into the holomorphic wedge.

A conversion is possible only after imposing an additional real structure such as (9.2); in that case the target-orthogonality theorem applies.

---

# 15. Exact all-\(k\) adjacent Plücker theorem

The preceding argument is not special to \(k=12\).

Let \(p\) be any odd prime. Take:

* \(k\) paired-ruling slopes;
* \(k+2\) translated roots;
* adjacent \((k+1)\times k\) submatrices

  $$
  I_0=\{0,\ldots,k\},\qquad
  I_1=\{1,\ldots,k+1\};
  $$
* padded signed-cofactor null vectors \(b^{(0)},b^{(1)}\).

Let \(\Delta_{ab}\) be the complementary \(k\times k\) minors of the full \((k+2)\times k\) matrix. For shared rows \(i,j\),

$$
\boxed{
b_i^{(0)}b_j^{(1)}
-
b_j^{(0)}b_i^{(1)}
=
\pm\Delta_{0,k+1}\Delta_{ij}.
}
\tag{15.1}
$$

Then:

1. For generic slope sets, complex conjugation replaces the slopes by their negatives, so (15.1) is not a valid physical sesquilinear circuit identity.

2. If the slope set admits a constant conjugation real structure, the alternating form in (15.1) becomes admissible, but every target diagonal satisfies

   $$
   b_i^{(0)}b_i^{(1)}
   -
   b_i^{(1)}b_i^{(0)}
   =0.
   $$

Therefore:

$$
\boxed{
\text{For every odd prime and every adjacent cofactor circuit, the linear
Plücker wedge alone cannot produce a nonzero target separator.}
}
\tag{AdjacentPlueckerLinearNoGo}
$$

This is the complete smaller-analogue theorem requested in the prompt.

---

# 16. The first exact remaining matrix obstruction

The Plücker-linear direction is closed. The first unresolved adjacent matrix problem is one of the following equivalent forms.

## 16.1 Constant separator

For general slopes, determine whether there exist \(\nu\) and \(\Lambda\) such that

$$
\boxed{
\frac{
|\langle\Lambda,\mathbf T_\nu\rangle|
}{
\sum_{\rm ordinary}
|\langle\Lambda,\mathbf W_{\nu;x,y}\rangle|
}
>
\frac1{\sqrt{D+1}}.
}
\tag{16.1}
$$

The Plücker relation does not evaluate the conjugated off-diagonal entries.

## 16.2 Real-structure residual

For conjugation-stable slopes, determine whether the denominator minimization in (12.1) satisfies

$$
\boxed{
\inf_{t\in\mathbb C}
\sum_{\rm ordinary}
\left|
\langle S,\mathbf W_{\nu;q}\rangle
+t\mathbf P_{\nu;q}
\right|
<
\sqrt{D+1}\,
|\langle S,\mathbf T_\nu\rangle|
}
\tag{16.2}
$$

for some transpose-symmetric \(S\).

This is a one-complex-parameter cancellation problem for each \(S\), but no exact inequality controls it.

## 16.3 Global shared-phase separator

Determine whether

$$
\boxed{
\rho_{\rm glob}>
\frac1{\sqrt{D+1}}
}
\tag{16.3}
$$

in the global dual (5.2).

This allows admissible frequency-dependent multipliers and enforces the same relaxed coefficient vector across all \(\nu\).

No one of (16.1)–(16.3) is settled.

---

# Explicit outcome discipline

This round produced:

1. **No exact baseline vector.**
2. **No exact frozen-edge vector.**
3. **No exact exclusion of \(x^{(10)}\).**
4. **No exact physical vector with \(\mathcal F_\Gamma>10\).**
5. **No phase-uniform proof of PW10.**
6. **No thirteen-slope ansatz theorem.**

Therefore, as required by the source’s verdict discipline, the status remains: 

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

# VERIFIED

* The adjacent matrix circuit

  $$
  B^{\mathsf T}F\overline B=0.
  $$
* The exact target and ordinary matrices (41.3)–(41.4).
* Padding and support intersections.
* Both spike shifts.
* The per-frequency convex dual (41.6), including the \(+\infty\) case.
* The fact that physical coefficients are shared:

  * across all four matrix entries;
  * across all \(\nu\);
  * across even coordinate pairs.
* The exact global shared-phase dual.
* All four scalar pairings \(E_{00},E_{11},S,J\).
* The sign in the \(J\)-pairing.
* The holomorphic Plücker identity and its distinction from the sesquilinear wedge.
* The exact conjugation law

  $$
  \overline{V_{\mathcal M}(c)}=V_{-\mathcal M}(c).
  $$
* The failure of a generic \(c\mapsto-c\) cofactor conversion.
* `PlueckerTargetOrthogonality`.
* The explicit negation-symmetric canonical-cofactor family with:

  * zero Plücker target;
  * nonzero ordinary Plücker coefficient.
* Legitimacy and sequence-domain form of frequency-dependent multipliers.
* `AdjacentPlueckerLinearNoGo` for arbitrary adjacent \(k+2\)-root circuits over odd prime fields.

# CORRECTED

* Complex conjugation sends the slope set to \(-\mathcal M\) at the same \(c\); it does not generally send a cofactor to the same-slope cofactor at \(-c\).
* The Plücker relation is holomorphic and cannot be substituted into the physical sesquilinear circuit without a separately proved real structure.
* The per-\(\nu\) zonotope dual is weaker than the physical problem because it does not enforce cross-\(\nu\), even-orbit, or exact-modulus sharing.
* A frequency-dependent multiplier is legitimate when fixed from circuit data, but it acts by convolution and cannot be optimized independently at each point without changing the circuit.
* Endpoint rows contribute ordinary Plücker mass, not target gain.
* The Plücker direction may still alter the denominator of a separator carrying symmetric target gain; that mixed problem remains open.

# DISPROVED

* Direct use of (41.8) inside the generic \(J\)-pairing.
* Any universal claim that conjugation converts the cofactors to the same system at \(-c\).
* Existence of a Plücker-only linear separator with nonzero target gain.
* Any claim that the endpoint rows create a Plücker target telescope.
* Any claim that frequency dependence alone removes the holomorphic/sesquilinear mismatch.

# NECESSARY-ONLY

* The per-\(\nu\) condition

  $$
  \rho_\nu\le\frac1{\sqrt{D+1}}
  $$

  for a baseline.
* The stronger global shared-phase condition

  $$
  \rho_{\rm glob}\le\frac1{\sqrt{D+1}}.
  $$
* The residual symmetric-plus-Plücker minimization (12.1).
* At least twelve paired ruling slopes for a surviving quadratic-Gauss ansatz.

# EQUIVALENT

For fixed \(\nu\),

$$
\rho_\nu
=
\min\left\{
\|z\|_\infty:
\mathbf T_\nu=\sum z_q\mathbf W_{\nu;q}
\right\},
$$

with \(+\infty\) exactly when the target does not annihilate the kernel of the ordinary coefficient map.

Across all frequencies,

$$
\rho_{\rm glob}
=
\min\left\{
\|z\|_\infty:
\mathbf T_\nu=\sum_qz_q\widetilde{\mathbf W}_{\nu;q}
\quad\forall\nu
\right\}
$$

and is dual to (5.2).

Under a constant real structure \(\overline B=BR\), the valid sesquilinear circuit is equivalent to a holomorphic bilinear circuit with matrix \(\Lambda R^{\mathsf T}\).

# NUMERICAL-ONLY

* No numerical optimization is used.
* No empirical matrix-dual value is used.
* Any numerical evaluation of (16.1)–(16.3) remains noncertifying.

# CONJECTURED

* A constant transpose-symmetric separator satisfying (16.1).
* A mixed symmetric-plus-Plücker cancellation satisfying (16.2).
* A frequency-dependent global separator satisfying (16.3).
* A thirteen-slope ansatz theorem.
* Eventual exclusion of every finite-slope quadratic-Gauss baseline.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* The complete constant-\(\Lambda\) adjacent matrix dual.
* The one-complex-parameter Plücker denominator cancellation in real-structure families.
* The global shared-phase matrix dual.
* Quadratic-Gauss mixtures on twelve or more slopes.
* Dense nonquadratic baseline solutions.
* Existence of an exact baseline pure-edge vector.
* Frozen named-edge retrieval.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the **adjacent Plücker target-orthogonality theorem**

$$
\boxed{
\text{Whenever the holomorphic adjacent Plücker wedge is made into a valid
sesquilinear circuit by a constant conjugation real structure, its target
coefficient vanishes identically at every Fourier frequency.}
$$

Its exact canonical family

$$
\mathcal M=\{\pm1,\ldots,\pm6\},
\qquad
r_i=i,
$$

shows that the Plücker direction can have nonzero ordinary mass while its target remains exactly zero.
