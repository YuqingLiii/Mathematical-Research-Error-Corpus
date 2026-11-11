# Verdict

$$
\boxed{\text{\((E1_{\mathrm{gap}})\) remains OPEN WITH EARLIEST GAP.}}
$$

All five proposed new facts—realignment defect, centered alignment, low Choi rank, Hilbert–Schmidt contraction, and the unitary extension of Pure-\(Q\)—are valid, with two qualifications:

1. \((RD\text{-}PT2)\) is exactly the arithmetic-mean relaxation of the previously proved alignment bound, hence is **REDUNDANT**.
2. Low Choi rank plus \(C_{\rm up}\) excludes a thin region near exact \(PA\)-saturation, but the complete scalar necessary system remains feasible. An exact symbolic large-\(D\) family satisfying every scalar inequality is given below.

Moreover, even a stronger decoupled operator relaxation survives: one can construct

* a positive contraction \(S=P_0+P\) satisfying the exact coherent-state Pure-\(Q\) bound,
* a positive Choi matrix \(\widetilde J=rP_0+B\) with correct bistochastic marginals and an exact rank-\(m(m-1)\) unitary frame,
* matching traces, purities, \(\alpha,i,\tau\), and all symmetric-Bell endpoint inequalities,

but without imposing that \(\widetilde J\) is the realignment of that same \(S\), or that its frame elements are the pair differences of one \(m\)-tuple.

Thus the earliest missing implication is genuinely the **same-map realignment and pair-difference coupling**, not another scalar trace-purity estimate.

---

# 1. Common block notation

Let

$$
e=\frac{|I_D\rangle\rangle}{\sqrt D},
\qquad
P_0=|e\rangle\langle e|,
\qquad
P_\perp=I-P_0.
$$

Relative to

$$
\mathbb C e\oplus e^\perp,
$$

write

$$
S=
\begin{pmatrix}
1&0\\
0&P
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
r&z^*\\
z&B
\end{pmatrix},
\tag{1.1}
$$

where

$$
r=\frac{\alpha}{D},
\qquad
P\succeq0,
\qquad
B\succeq0.
$$

The normalized invariants are

$$
i=\frac{\mathsf I_U}{m^4}=\operatorname{Tr}S^2=\operatorname{Tr}J^2,
$$

$$
\tau=\frac{\mathsf T_U}{m^4}
=\langle\langle I|J^2|I\rangle\rangle.
$$

Since \(|I\rangle\rangle=\sqrt D\,e\),

$$
\langle e|J^2|e\rangle=\frac{\tau}{D}.
$$

The upper-left entry of \(J^2\) is \(r^2+\|z\|^2\), so

$$
\boxed{
h:=\|z\|^2=\frac{\tau}{D}-r^2.
}
\tag{1.2}
$$

Put

$$
u=\operatorname{Tr}P=\alpha-1,
\qquad
v=\operatorname{Tr}B=D-r,
\qquad
n=D^2-1.
$$

Also,

$$
b:=\operatorname{Tr}P^2=i-1.
\tag{1.3}
$$

Since

$$
\operatorname{Tr}J^2
=
r^2+2\|z\|^2+\operatorname{Tr}B^2,
$$

we obtain

$$
\boxed{
a:=\operatorname{Tr}B^2
=
i-\frac{2\tau}{D}+r^2.
}
\tag{1.4}
$$

Finally, Pair-energy gives

$$
\frac{\mathsf C_U}{m^4}
=
r+\frac{\Theta_Q}{m^2}.
$$

Because

$$
\Theta_Q=m^2\operatorname{Tr}(BP),
$$

define

$$
x:=\operatorname{Tr}(BP)\ge0.
$$

Then

$$
\boxed{
\frac{\mathsf C_U}{m^4}=r+x.
}
\tag{1.5}
$$

---

# 2. Audit of the realignment defect

Realignment is a permutation of matrix entries, so

$$
\|J\|_2=\|S\|_2.
$$

Moreover, \(S,J\succeq0\), so \(\operatorname{Tr}(SJ)\) is real and nonnegative. Therefore

$$
\begin{aligned}
\|S-J\|_2^2
&=
\operatorname{Tr}S^2+\operatorname{Tr}J^2
-2\operatorname{Tr}(SJ)\\
&=
2i-2\frac{\mathsf C_U}{m^4}.
\end{aligned}
$$

Multiplication by \(m^4/2\) gives

$$
\boxed{
\mathsf I_U-\mathsf C_U
=
\frac{m^4}{2}\|S-J\|_2^2.
}
\tag{RD}
$$

This identity is correct.

## 2.1 The proposed \(RD\text{-}PT2\) lower bound

From the blocks in (1.1),

$$
S-J=
\begin{pmatrix}
1-r&-z^*\\
-z&P-B
\end{pmatrix}.
$$

Hence

$$
\|S-J\|_2^2
=
(1-r)^2+2h+\|P-B\|_2^2.
$$

Dropping the last nonnegative term gives

$$
i-\frac{\mathsf C_U}{m^4}
\ge
\frac{(1-r)^2}{2}+h.
$$

Using \(h=\tau/D-r^2\),

$$
\boxed{
i-\frac{\mathsf C_U}{m^4}
\ge
\frac{\tau}{D}-r-\frac{r^2}{2}+\frac12.
}
\tag{2.1}
$$

In the original variables, this is exactly

$$
\boxed{
\mathsf I_U-\mathsf C_U
\ge
\frac{\mathsf T_U-2m^4\alpha+m^4D}{D}
-
\frac{m^4(\alpha-D)^2}{2D^2}.
}
\tag{RD-PT2}
$$

Now use

$$
\frac{\mathsf C_U}{m^4}=r+x
$$

and

$$
a+b
=
2i-\frac{2\tau}{D}+r^2-1.
$$

Rearranging (2.1) gives

$$
\boxed{
r+x\le r+\frac{a+b}{2}.
}
\tag{2.2}
$$

Thus \(RD\text{-}PT2\) is exactly the estimate

$$
x\le\frac{a+b}{2}.
$$

The previous alignment bound gives \(x\le\sqrt{ab}\), and

$$
\sqrt{ab}\le\frac{a+b}{2}.
$$

Therefore

$$
\boxed{
RD\text{-}PT2\text{ is valid but REDUNDANT with Align.}
}
$$

---

# 3. Centered alignment

Both \(B\) and \(P\) act on the \(n\)-dimensional space \(e^\perp\). Write

$$
B=\frac vnP_\perp+B_0,
\qquad
P=\frac unP_\perp+P_1,
$$

with

$$
\operatorname{Tr}B_0=\operatorname{Tr}P_1=0.
$$

Then

$$
\operatorname{Tr}(BP)
=
\frac{uv}{n}+\operatorname{Tr}(B_0P_1).
$$

Furthermore,

$$
\|B_0\|_2^2=a-\frac{v^2}{n},
\qquad
\|P_1\|_2^2=b-\frac{u^2}{n}.
$$

Hilbert–Schmidt Cauchy–Schwarz yields

$$
\boxed{
x
\le
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
}
\tag{Centered-Align}
$$

The radicands are nonnegative by the trace-purity inequalities.

## 3.1 It is never weaker than uncentered Align

Set

$$
\xi=\frac{v}{\sqrt{na}},
\qquad
\zeta=\frac{u}{\sqrt{nb}}.
$$

Then \(0\le\xi,\zeta\le1\), and after division by \(\sqrt{ab}\), the centered upper bound becomes

$$
\xi\zeta+\sqrt{1-\xi^2}\sqrt{1-\zeta^2}.
$$

This is at most \(1\). Hence

$$
\boxed{
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}
\le\sqrt{ab}.
}
\tag{3.1}
$$

Equality in the scalar comparison requires \(\xi=\zeta\). Equality in the full centered bound additionally requires \(B_0\) and \(P_1\) to be positively proportional.

---

# 4. The trace-centered scalar escape

Suppose

$$
\tau=Dr^2,
\qquad
i=1+\frac{u^2}{n}.
\tag{4.1}
$$

Then \(z=0\), \(P\) is trace-purity minimal, and

$$
b=\frac{u^2}{n}.
$$

A direct calculation gives

$$
1+\frac{(Dr-1)^2}{D^2-1}-r^2
=
\frac{(D-r)^2}{D^2-1}.
$$

Thus

$$
a=\frac{v^2}{n}.
$$

Both centered variances vanish, and

$$
x\le\frac{uv}{n}.
$$

Let

$$
A_0=\frac{m(\alpha+D)}{D(D+1)},
$$

the value at equality in \(PA\). Substitution into the exact endpoint formulas gives

$$
\boxed{
\frac{\mathsf C_{\rm up}}{m^4}
=
r+\frac{uv}{n},
}
\tag{4.2}
$$

and

$$
\boxed{
\frac{\mathsf C_{\rm req}}{m^4}
-
\left(r+\frac{uv}{n}\right)
=
-\frac{(\alpha-D)(D+3)(D^2-\alpha)}
{2(D-1)}
\le0.
}
\tag{4.3}
$$

Since the feasible regime has \(D<\alpha<D^2\), the right side is strictly negative.

Therefore centered trace-purity alone has an exact escape. Low Choi rank is needed to move away from this trace-minimal point.

---

# 5. Low rank of \(B\)

The Choi matrix of \(\Phi\) is

$$
J=
\frac1{m^2}
\sum_{a,b}
|A_{ab}\rangle\rangle
\langle\langle A_{ab}|,
\qquad
A_{ab}=U_b^*U_a.
$$

Compression to \(e^\perp\) gives

$$
B=
\frac1{m^2}
\sum_{a,b}
|P_\perp A_{ab}\rangle\rangle
\langle\langle P_\perp A_{ab}|.
$$

For \(a=b\),

$$
A_{aa}=I_D,
\qquad
P_\perp|I_D\rangle\rangle=0.
$$

Hence

$$
\boxed{
B=
\frac1{m^2}
\sum_{a\ne b}
|P_\perp A_{ab}\rangle\rangle
\langle\langle P_\perp A_{ab}|.
}
\tag{5.1}
$$

There are \(m(m-1)\) summands, so

$$
\boxed{
\operatorname{rank}B\le k:=m(m-1).
}
\tag{5.2}
$$

For a positive operator of rank at most \(k\) and trace \(v\),

$$
\operatorname{Tr}B^2\ge\frac{v^2}{k}.
$$

Therefore

$$
\boxed{
a\ge\frac{v^2}{m(m-1)}.
}
\tag{B-rank}
$$

Since

$$
a=i-\frac{2\tau}{D}+r^2
$$

and \(\tau\ge Dr^2\),

$$
a\le i-r^2.
$$

Consequently,

$$
\boxed{
i\ge
r^2+\frac{(D-r)^2}{m(m-1)}.
}
\tag{I-rank}
$$

Both proposed rank inequalities are correct.

---

# 6. Why low-\(A\) feasibility forces \(D>m\)

The pure-state Haar average from the preceding rounds gives

$$
m(\alpha+D)\le AD(D+1).
\tag{PA}
$$

Also,

$$
\alpha\ge\frac{D^2}{m}.
$$

Therefore

$$
D^2+mD\le AD(D+1),
$$

so

$$
\boxed{
D\ge\frac{m-A}{A-1}.
}
\tag{6.1}
$$

The Gap condition gives

$$
A<m^{1/(2m)}.
$$

For \(m>1\),

$$
\frac{\log m}{2m}
<
\frac{m-1}{2m}.
$$

Also, with \(x=(m-1)/(m+1)\),

$$
\log(1+x)\ge\frac{x}{1+x}=\frac{m-1}{2m}.
$$

Thus

$$
m^{1/(2m)}
<
\frac{2m}{m+1},
$$

and hence

$$
A<\frac{2m}{m+1}.
$$

This is equivalent to

$$
\frac{m-A}{A-1}>m.
$$

Therefore

$$
\boxed{D>m.}
\tag{6.2}
$$

In particular,

$$
m(m-1)<D^2-1=n,
$$

so the rank bound for \(B\) is genuinely stronger than the ambient trace-purity bound.

---

# 7. Hilbert–Schmidt contraction

For every \(X\),

$$
\begin{aligned}
\|L(X)\|_2
&=
\left\|
\frac1m\sum_vU_vXU_v^*
\right\|_2\\
&\le
\frac1m\sum_v\|U_vXU_v^*\|_2\\
&=\|X\|_2.
\end{aligned}
$$

Hence

$$
\|L\|_{2\to2}\le1.
$$

Since

$$
\Phi=L^*L,
$$

its Liouville matrix satisfies

$$
0\preceq S\preceq I.
$$

Moreover, \(L(I)=I\) and \(L^*(I)=I\), so

$$
Se=e.
$$

Consequently,

$$
\boxed{
0\preceq P\preceq P_\perp.
}
\tag{7.1}
$$

The eigenvalues of \(S\) lie in \([0,1]\), and

$$
\operatorname{Tr}S=\alpha.
$$

Therefore

$$
\boxed{
i=\operatorname{Tr}S^2\le\operatorname{Tr}S=\alpha.
}
\tag{Contract}
$$

Equivalently,

$$
b=i-1\le\alpha-1=u.
$$

The proposed contraction statement is correct.

---

# 8. Pointwise Pure-\(Q\) extension to unitaries

Let \(W\) be unitary and choose an orthonormal eigenbasis:

$$
W=\sum_{j=1}^D z_j\rho_j,
\qquad
|z_j|=1,
\qquad
\rho_j=|y_j\rangle\langle y_j|.
$$

Set

$$
q_j=Q(\rho_j).
$$

Since \(Q(I)=0\),

$$
\sum_jq_j=0.
$$

Let \(K\) be their Gram matrix:

$$
K_{jk}=\langle q_j,q_k\rangle_{\rm HS}.
$$

Then

$$
K\succeq0,
\qquad
K\mathbf1=0,
\qquad
K_{jj}\le\epsilon,
$$

where

$$
\epsilon=\frac Am-\frac1D.
$$

Therefore

$$
\operatorname{Tr}K\le D\epsilon
$$

and

$$
\lambda_{\max}(K)\le D\epsilon.
$$

Now

$$
\|Q(W)\|_2^2=z^*Kz.
$$

Because \(K\mathbf1=0\),

$$
z^*Kz
=
(P_{\mathbf1^\perp}z)^*K(P_{\mathbf1^\perp}z).
$$

Also,

$$
\|P_{\mathbf1^\perp}z\|^2
=
D-\frac{|\sum_jz_j|^2}{D}
=
D-\frac{|\operatorname{Tr}W|^2}{D}.
$$

Hence

$$
\boxed{
\|Q(W)\|_2^2
\le
\epsilon
\left(D^2-|\operatorname{Tr}W|^2\right).
}
\tag{8.1}
$$

Summing this over \(W=A_{ab}\),

$$
\begin{aligned}
\Theta_Q
&\le
\epsilon
\sum_{a,b}
\left(D^2-|\operatorname{Tr}A_{ab}|^2\right)\\
&=
m^2\epsilon(D^2-\alpha).
\end{aligned}
$$

Since \(x=\Theta_Q/m^2\),

$$
\boxed{
x\le\epsilon(D^2-\alpha).
}
\tag{Unitary-Q}
$$

The proposed unitary extension is correct.

---

# 9. Strongest direct scalar necessary system

Let

$$
q=m(A-1)=9(1+\eta)^2>9.
$$

Then

$$
A=1+\frac qm,
\qquad
2m\log\left(1+\frac qm\right)<\log m.
\tag{9.1}
$$

Every admissible tuple must produce real variables

$$
D,\alpha,r,u,v,n,\tau,i,a,b,h,x
$$

satisfying the following.

## 9.1 Dimension and one-copy constraints

$$
D\in\mathbb N,
\qquad
D>m,
$$

$$
\boxed{
\frac{D^2}{m}
\le
\alpha
\le
\frac{AD(D+1)}{m}-D
<
D^2.
}
\tag{9.2}
$$

Also

$$
r=\frac{\alpha}{D},
\quad
u=\alpha-1,
\quad
v=D-r,
\quad
n=D^2-1.
$$

## 9.2 Mixing and block positivity

$$
\boxed{
Dr^2\le\tau\le\sqrt A\,Dr^2.
}
\tag{9.3}
$$

Define

$$
h=\frac{\tau}{D}-r^2\ge0.
$$

Positivity of

$$
J=
\begin{pmatrix}r&z^*\\z&B\end{pmatrix}
$$

implies

$$
B\succeq\frac{zz^*}{r}.
$$

Hence

$$
\boxed{
h\le rv,
\qquad
a\ge\frac{h^2}{r^2}.
}
\tag{9.4}
$$

## 9.3 Trace-purity and rank constraints

$$
b=i-1,
\qquad
a=i-\frac{2\tau}{D}+r^2.
$$

For \(P\),

$$
\boxed{
\frac{u^2}{n}\le b\le u.
}
\tag{9.5}
$$

For \(B\),

$$
\boxed{
\frac{v^2}{m(m-1)}
\le a\le v^2.
}
\tag{9.6}
$$

Contraction adds

$$
\boxed{i\le\alpha.}
\tag{9.7}
$$

## 9.4 Alignment bounds

Define

$$
H_{\rm cen}
=
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
\tag{9.8}
$$

Then

$$
\boxed{
0\le x
\le
\min\left\{
H_{\rm cen},
\epsilon(D^2-\alpha),
v,
i-r
\right\}.
}
\tag{9.9}
$$

Here:

* \(x\le v\) follows from \(0\le P\le I\);
* \(x\le i-r\) follows from \(r+x=\operatorname{Tr}(JS)\le i\).

## 9.5 Exact symmetric-Bell endpoints

Define

$$
\begin{aligned}
\gamma_{\rm req}(i,\tau)
={}&
(D+2)i+(D+1)\tau\\
&+\frac12B_0(D,\alpha)\\
&-
\frac{A}{2m}
\alpha D(D+1)(D+3),
\end{aligned}
\tag{9.10}
$$

and

$$
\begin{aligned}
\gamma_{\rm up}(i,\tau)
=\frac12\Bigg[
&\frac{A}{m}
(\alpha+D)(D+2)(D+3)\\
&-
\left(
D^2+4D+\alpha^2+2(D+4)\alpha
\right)\\
&-2i-4\tau
\Bigg].
\end{aligned}
\tag{9.11}
$$

Then

$$
\boxed{
\gamma_{\rm req}(i,\tau)
\le r+x
\le
\gamma_{\rm up}(i,\tau).
}
\tag{9.12}
$$

Equivalently, scalar feasibility requires

$$
\boxed{
\max\{0,\gamma_{\rm req}-r\}
\le x
\le
\min\{
H_{\rm cen},
\epsilon(D^2-\alpha),
v,
i-r,
\gamma_{\rm up}-r
\}.
}
\tag{9.13}
$$

No lower bound on \(i\) or \(\tau\) has been substituted inside a nonmonotone expression in this system.

---

# 10. Near-\(PA\)-saturation is partially excluded

Let the \(PA\) slack be

$$
s:=AD(D+1)-m(\alpha+D)\ge0.
\tag{10.1}
$$

The upper endpoint \(\gamma_{\rm up}\) is strictly decreasing in both \(i\) and \(\tau\).

From B-rank,

$$
i\ge
\frac{2\tau}{D}-r^2+\frac{v^2}{m(m-1)}.
$$

After substituting this lower bound, the resulting upper endpoint remains decreasing in \(\tau\), so it is maximized at

$$
\tau=Dr^2,
\qquad
i=r^2+\frac{v^2}{m(m-1)}.
\tag{10.2}
$$

A direct expansion gives

$$
\boxed{
\begin{aligned}
\gamma_{\rm up}^{\rm rank}-r
={}&
\frac{(D+2)(D+3)(D+\alpha)}
{2Dm(D+1)}\,s\\
&+
\frac{
(D^2-\alpha)
\left[
m(m-1)(D+\alpha)
-(D+1)(D^2-\alpha)
\right]
}{
D^2m(D+1)(m-1)
}.
\end{aligned}
}
\tag{10.3}
$$

Define

$$
\Xi:=
(D+1)(D^2-\alpha)-m(m-1)(D+\alpha).
$$

If \(\Xi>0\), feasibility requires

$$
\boxed{
s\ge
\frac{
2(D^2-\alpha)\Xi
}{
D(D+2)(D+3)(D+\alpha)(m-1)
}.
}
\tag{10.4}
$$

Thus exact \(PA\)-saturation \(s=0\) is impossible whenever \(\Xi>0\).

This proves the anticipated near-boundary exclusion. It is not global: a modest positive \(PA\) slack can restore the upper endpoint.

---

# 11. Exact large-\(D\) scalar survivor

The full scalar system is not globally infeasible.

Choose

$$
q=10,
\qquad
\eta=\frac{\sqrt{10}}{3}-1,
\qquad
A=1+\frac{10}{m}.
$$

Let \(m\) be any sufficiently large multiple of \(5\), for example

$$
m>e^{20}.
$$

Then

$$
2m\log\left(1+\frac{10}{m}\right)<20<\log m,
$$

so Gap holds.

Set

$$
\boxed{
D=\frac{m^2}{5},
\qquad
\alpha=\frac{m^3}{25}.
}
\tag{11.1}
$$

Thus

$$
\alpha=\frac{D^2}{m},
\qquad
r=\frac m5.
$$

Choose

$$
\boxed{
\tau=Dr^2=\frac{m^4}{125},
}
\tag{11.2}
$$

and

$$
\boxed{
i=
r^2+\frac{(D-r)^2}{m(m-1)}
=
\frac{2m^2-m}{25}.
}
\tag{11.3}
$$

Then

$$
u=\frac{m^3}{25}-1,
\qquad
v=\frac{m(m-1)}5,
$$

$$
a=\frac{m(m-1)}{25},
\qquad
b=\frac{2m^2-m-25}{25}.
$$

Finally choose

$$
\boxed{x=0.}
\tag{11.4}
$$

This is only a scalar relaxation, not a tuple.

## 11.1 \(PA\), contraction, and rank

The exact \(PA\) slack is

$$
\boxed{
AD(D+1)-m(\alpha+D)
=
\frac{m(m^2+m+10)}5>0.
}
\tag{11.5}
$$

Also,

$$
\boxed{
\alpha-i=\frac{m(m-1)^2}{25}>0.
}
\tag{11.6}
$$

The B-rank inequality is saturated:

$$
a=\frac{v^2}{m(m-1)}.
$$

Moreover,

$$
v^2-a
=
\frac{m(m-1)(m^2-m-1)}{25}>0.
$$

## 11.2 Centered radicands

A direct calculation gives

$$
\boxed{
a-\frac{v^2}{n}
=
b-\frac{u^2}{n}
=
\frac{
m(m-1)
\left(m^4-25m^2+25m-25\right)
}{
25(m^2-5)(m^2+5)
}.
}
\tag{11.7}
$$

This is positive for all sufficiently large \(m\). Hence Centered-Align is well-defined, and \(x=0\) satisfies it.

Unitary-\(Q\), contraction, and \(x\le v\) are also automatic because all corresponding upper bounds are positive.

## 11.3 Exact endpoint check

For this family,

$$
\boxed{
\gamma_{\rm up}-r
=
\frac{
m^5+6m^4+35m^3+160m^2+410m+1500
}{250}
>0.
}
\tag{11.8}
$$

On the other hand,

$$
\boxed{
\begin{aligned}
\gamma_{\rm req}-r
={}&
-\frac{m}{1250}
\Big(
2m^6-5m^5+50m^4\\
&\qquad
-115m^3+360m^2-450m+350
\Big)
<0.
\end{aligned}
}
\tag{11.9}
$$

For \(m\ge3\), the polynomial in parentheses is positive; for example, group it as

$$
m^5(2m-5)
+
m^3(50m-115)
+
m(360m-450)
+
350.
$$

Thus

$$
\gamma_{\rm req}\le r+x\le\gamma_{\rm up}
$$

with \(x=0\).

Therefore:

$$
\boxed{
\text{Every scalar inequality listed in Section 9 survives exactly.}
}
$$

This disproves any attempted closure based only on that scalar system.

---

# 12. The exact realignment/coherent-state coupling omitted by the scalar system

For an actual tuple, \(J\) and \(S\) are not independent.

For every pure state \(\rho_y=|y\rangle\langle y|\),

$$
\begin{aligned}
\langle\langle\rho_y|S|\rho_y\rangle\rangle
&=
\operatorname{Tr}\bigl[\rho_y\Phi(\rho_y)\bigr]\\
&=
\|L(\rho_y)\|_2^2,
\end{aligned}
$$

while the Choi frame gives

$$
\begin{aligned}
\langle\langle\rho_y|J|\rho_y\rangle\rangle
&=
\frac1{m^2}
\sum_{a,b}
|\operatorname{Tr}(\rho_yA_{ab})|^2\\
&=
\|C(\rho_y)\|_2^2.
\end{aligned}
$$

For pure input, the two expressions are algebraically equal:

$$
\operatorname{Tr}
\left[
\rho_yA_{ab}\rho_yA_{ab}^*
\right]
=
|\langle y|A_{ab}|y\rangle|^2.
$$

Hence

$$
\boxed{
\langle\langle\rho_y|S|\rho_y\rangle\rangle
=
\langle\langle\rho_y|J|\rho_y\rangle\rangle
\quad
\forall y.
}
\tag{12.1}
$$

Write

$$
|\rho_y\rangle\rangle
=
\frac e{\sqrt D}+t_y,
\qquad
t_y\in e^\perp.
$$

Using the blocks (1.1), equation (12.1) becomes

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
-
\frac{2}{\sqrt D}
\operatorname{Re}\langle z,t_y\rangle
=
\frac{r-1}{D}
\quad
\forall y.
}
\tag{12.2}
$$

This pointwise quartic identity is stronger than every scalar trace and purity relation used above.

When \(\tau=Dr^2\), one has \(z=0\), and it reduces to

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
=
\frac{r-1}{D}
\quad
\forall y.
}
\tag{12.3}
$$

The scalar relaxation does not retain this identity.

---

# 13. Exact counterexample inside a decoupled operator relaxation

The preceding scalar survivor can be upgraded to a genuine operator model satisfying all of the following separately:

* \(0\le P\le P_\perp\);
* the exact Pure-\(Q\) coherent-state bound;
* correct \(\operatorname{Tr}P\) and \(\operatorname{Tr}P^2\);
* a positive Choi matrix \(\widetilde J\) with correct unital and trace-preserving marginals;
* an exact rank-\(m(m-1)\) unitary frame for \(B\);
* matching \(\alpha,i,\tau\);
* all scalar and symmetric-Bell endpoint constraints.

What is not imposed is

$$
\widetilde J=\operatorname{realign}(P_0+P)
$$

or the existence of one tuple whose pair differences give that frame.

This precisely shows what remains missing.

## 13.1 Dimensions

Choose \(m\) to be a sufficiently large multiple of \(10\), and retain

$$
D=\frac{m^2}{5}.
$$

Then \(D=2d\) is even.

Decompose

$$
\mathbb C^D=\mathbb C^d\oplus\mathbb C^d.
$$

Inside the Hilbert–Schmidt space \(M_D\), let

* \(\mathcal H_\times\) be the cross-block matrices;
* \(\mathcal H_\parallel\) be the block-diagonal traceless matrices.

Their dimensions are

$$
R_\times=\frac{D^2}{2},
\qquad
R_\parallel=\frac{D^2}{2}-1,
$$

and

$$
R_\times+R_\parallel=n.
$$

Let \(\Pi_\times,\Pi_\parallel\) be their orthogonal projections.

## 13.2 Choosing the spectrum of \(P\)

Retain

$$
u=\frac{m^3}{25}-1,
\qquad
b=\frac{2m^2-m-25}{25}.
$$

Set

$$
\Delta=b-\frac{u^2}{n}.
$$

Explicitly,

$$
\boxed{
\Delta=
\frac{
m(m-1)(m^4-25m^2+25m-25)
}{
25(m^2-5)(m^2+5)
}>0.
}
\tag{13.1}
$$

Put

$$
\lambda_0=\frac un,
$$

and define

$$
\boxed{
\lambda_\times
=
\lambda_0+
\sqrt{
\frac{R_\parallel\Delta}
{R_\times n}
},
}
\tag{13.2}
$$

$$
\boxed{
\lambda_\parallel
=
\lambda_0-
\sqrt{
\frac{R_\times\Delta}
{R_\parallel n}
}.
}
\tag{13.3}
$$

Then

$$
R_\times\lambda_\times
+
R_\parallel\lambda_\parallel
=u,
$$

and

$$
R_\times\lambda_\times^2
+
R_\parallel\lambda_\parallel^2
=b.
$$

Define

$$
\boxed{
P=
\lambda_\times\Pi_\times
+
\lambda_\parallel\Pi_\parallel.
}
\tag{13.4}
$$

### Positivity

The exact expression

$$
\boxed{
\lambda_0^2
-
\frac{R_\times\Delta}{R_\parallel n}
=
\frac{
m^5+25m^4-100m^3+1250
}{
(m^2-5)(m^2+5)(m^4-50)
}
>0
}
\tag{13.5}
$$

shows that \(\lambda_\parallel>0\).

Also,

$$
\lambda_\times
\le\frac{u}{R_\times}
<\frac2m<1.
$$

Hence

$$
0\le P\le P_\perp.
$$

## 13.3 Exact coherent-state bound

Let

$$
y=y_1\oplus y_2,
\qquad
s=\|y_1\|^2.
$$

For \(\rho_y=|y\rangle\langle y|\),

$$
\|\Pi_\times\rho_y\|_2^2
=
2s(1-s)\le\frac12,
$$

and

$$
\|\Pi_\parallel\rho_y\|_2^2
=
1-\frac1D-2s(1-s).
$$

Therefore

$$
\begin{aligned}
\langle\langle\rho_y|P|\rho_y\rangle\rangle
={}&
\lambda_\parallel\left(1-\frac1D\right)\\
&+
(\lambda_\times-\lambda_\parallel)2s(1-s).
\end{aligned}
$$

Using \(2s(1-s)\le1/2\),

$$
\begin{aligned}
\langle\langle\rho_y|P|\rho_y\rangle\rangle
&\le
\frac{\lambda_\times+\lambda_\parallel}{2}
-\frac{\lambda_\parallel}{D}.
\end{aligned}
$$

Because \(R_\times>R_\parallel\),

$$
\lambda_\times+\lambda_\parallel\le2\lambda_0.
$$

Thus

$$
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\lambda_0.
$$

Finally,

$$
\boxed{
\epsilon-\lambda_0
=
\frac{
5(m^4+5m^2-5m-25)
}{
m^2(m^2-5)(m^2+5)
}
>0.
}
\tag{13.6}
$$

Hence

$$
\boxed{
\sup_y
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\epsilon.
}
\tag{13.7}
$$

This is exactly the coherent-state Pure-\(Q\) constraint.

---

## 13.4 A rank-\(m(m-1)\) unitary frame

Let \(\{V_\ell\}_{\ell=1}^{d^2}\) be an orthogonal unitary error basis of \(M_d\).

The \(2d^2=D^2/2\) matrices

$$
W_{\ell,+}
=
\begin{pmatrix}
0&V_\ell\\
V_\ell&0
\end{pmatrix},
\qquad
W_{\ell,-}
=
\begin{pmatrix}
0&V_\ell\\
-V_\ell&0
\end{pmatrix}
\tag{13.8}
$$

are unitary, traceless, pairwise Hilbert–Schmidt orthogonal, and span \(\mathcal H_\times\).

Similarly, the matrices

$$
\begin{pmatrix}
V_\ell&0\\
0&V_\ell
\end{pmatrix},
\qquad
\begin{pmatrix}
V_\ell&0\\
0&-V_\ell
\end{pmatrix}
\tag{13.9}
$$

form an orthogonal unitary basis of the block-diagonal space; after removing the identity, they span \(\mathcal H_\parallel\).

Let

$$
k=m(m-1).
$$

Since \(D\gg m\),

$$
k<R_\times,\qquad k<R_\parallel.
$$

Choose any \(k\) orthogonal traceless unitaries \(W_1,\ldots,W_k\) from either subspace and define

$$
\boxed{
B=
\frac1{m^2}
\sum_{j=1}^k
|W_j\rangle\rangle\langle\langle W_j|.
}
\tag{13.10}
$$

Because \(\|W_j\|_2^2=D\),

$$
\operatorname{rank}B=k,
$$

$$
\operatorname{Tr}B
=
\frac{kD}{m^2}
=
\frac{D(m-1)}m
=
v,
$$

and

$$
\operatorname{Tr}B^2
=
\frac{kD^2}{m^4}
=
\frac{v^2}{k}
=
a.
$$

Thus B-rank is saturated.

Define

$$
\boxed{
\widetilde J
=
rP_0+B.
}
\tag{13.11}
$$

Equivalently,

$$
\widetilde J
=
\frac1{m^2}
\left[
m|I\rangle\rangle\langle\langle I|
+
\sum_{j=1}^k
|W_j\rangle\rangle\langle\langle W_j|
\right].
\tag{13.12}
$$

There are exactly

$$
m+k=m^2
$$

unitary frame elements, counting the \(m\) identity copies.

Every frame element is unitary, so

$$
\operatorname{Tr}_1\widetilde J
=
\operatorname{Tr}_2\widetilde J
=
I_D.
$$

Also,

$$
\langle\langle I|\widetilde J|I\rangle\rangle
=
\frac{D^2}{m}
=
\alpha,
$$

$$
\langle\langle I|\widetilde J^2|I\rangle\rangle
=
Dr^2
=
\tau,
$$

and

$$
\operatorname{Tr}\widetilde J^2
=
r^2+a
=
i.
$$

Meanwhile, with

$$
\widetilde S=P_0+P,
$$

one has

$$
\operatorname{Tr}\widetilde S=\alpha,
\qquad
\operatorname{Tr}\widetilde S^2=i.
$$

Thus all scalar traces and purities match exactly.

## 13.5 Alignment can be placed in either spectral sector

If the selected frame lies in \(\mathcal H_\times\),

$$
\operatorname{Tr}(BP)=v\lambda_\times.
$$

If it lies in \(\mathcal H_\parallel\),

$$
\operatorname{Tr}(BP)=v\lambda_\parallel.
$$

As \(m\to\infty\),

$$
\lambda_\times
=
\frac2m-\frac1{2m^2}+O(m^{-3}),
$$

$$
\lambda_\parallel
=
\frac1{2m^2}+O(m^{-3}).
$$

Thus the same separate spectral data permit alignments ranging from

$$
v\lambda_\parallel=\frac1{10}+O(m^{-1})
$$

to

$$
v\lambda_\times=\frac{2m}{5}+O(1).
$$

Both are compatible with the exact symmetric-Bell endpoints because

$$
\gamma_{\rm req}-r<0
$$

and

$$
\gamma_{\rm up}-r-D
=
\frac{
m^5+6m^4+35m^3+110m^2+410m+1500
}{250}
>0.
$$

Since \(v\lambda_\times<v<D\), both choices satisfy

$$
\gamma_{\rm req}\le r+x\le\gamma_{\rm up}.
$$

---

# 14. What the relaxed construction proves—and does not prove

The construction in Section 13 is not an admissible tuple for \((E1_{\rm gap})\). It deliberately does not establish

$$
\widetilde J=\operatorname{realign}(\widetilde S),
$$

and the \(m^2\) unitary frame elements are not shown to have the cocycle form

$$
W_{ab}=U_b^*U_a
$$

for one \(m\)-tuple.

It does prove the following exact negative result:

> Low rank of \(B\), a unitary frame for \(B\), positivity and contraction of \(P\), the uniform coherent-state Pure-\(Q\) bound, matching traces and purities, Choi marginal constraints, MM, PA, Centered-Align, Unitary-\(Q\), and the symmetric-Bell endpoints do not jointly imply a contradiction when the same-map realignment and pair-difference cocycle are omitted.

Thus no completion based only on those separate properties can settle \((E1_{\rm gap})\).

---

# 15. Earliest exact operator gap

For an actual tuple, one must simultaneously impose

$$
\boxed{
J=\operatorname{realign}(P_0+P)
=
\frac1{m^2}
\sum_{a,b}
|U_b^*U_a\rangle\rangle
\langle\langle U_b^*U_a|,
}
\tag{15.1}
$$

together with

$$
0\le P\le P_\perp,
\qquad
\sup_y
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\epsilon,
\tag{15.2}
$$

and the pointwise coupling

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
-
\frac{2}{\sqrt D}\operatorname{Re}\langle z,t_y\rangle
=
\frac{r-1}{D}
\quad\forall y.
}
\tag{15.3}
$$

The first missing implication is:

> **Realignment–pair-frame implication, OPEN.**
> Prove that every \(P,B,z\) arising from one frozen pair-difference tuple and satisfying (15.1)–(15.3), Gap, PA, and Pure-\(Q\), obeys an additional inequality that makes the interval (9.13) empty; or construct one tuple for which the full pointwise ratio bound holds.

No such inequality is proved here. The exact large-\(D\) scalar and decoupled-operator constructions show that it must use the actual realignment/cocycle coupling, not merely ranks, traces, purities, marginals, or coherent-state bounds considered separately.

---

# Audit ledger

| Status           | Statement                                                                                                                                            |                                                           |       |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----- |
| **PROVED**       | \(\mathsf I_U-\mathsf C_U=\frac{m^4}{2}\|S-J\|_2^2\).                                                                                                |                                                           |       |
| **PROVED**       | The proposed \(RD\text{-}PT2\) formula.                                                                                                              |                                                           |       |
| **REDUNDANT**    | \(RD\text{-}PT2\), because it is exactly \(x\le(a+b)/2\), weaker than Align.                                                                         |                                                           |       |
| **PROVED**       | Centered-Align, including all trace corrections and radicands.                                                                                       |                                                           |       |
| **PROVED**       | Centered-Align is never weaker than uncentered Align.                                                                                                |                                                           |       |
| **PROVED**       | The trace-centered escape and its exact factorization (4.3).                                                                                         |                                                           |       |
| **PROVED**       | (B=m^{-2}\sum_{a\ne b}                                                                                                                               | P_\perp A_{ab}\rangle\rangle\langle\langle P_\perp A_{ab} | ).    |
| **PROVED**       | \(\operatorname{rank}B\le m(m-1)\).                                                                                                                  |                                                           |       |
| **PROVED**       | B-rank and I-rank.                                                                                                                                   |                                                           |       |
| **PROVED**       | Gap, PA, and \(\alpha\ge D^2/m\) imply \(D>m\).                                                                                                      |                                                           |       |
| **PROVED**       | \(0\le S\le I\), \(0\le P\le P_\perp\), and \(i\le\alpha\).                                                                                          |                                                           |       |
| **PROVED**       | Unitary-\(Q\): (|Q(W)|_2^2\le\epsilon(D^2-                                                                                                           | \operatorname{Tr}W                                        | ^2)). |
| **PROVED**       | The complete direct scalar necessary system (9.1)–(9.13).                                                                                            |                                                           |       |
| **PROVED**       | Exact near-\(PA\)-saturation exclusion (10.3)–(10.4).                                                                                                |                                                           |       |
| **DISPROVED**    | Global infeasibility of the scalar system.                                                                                                           |                                                           |       |
| **PROVED**       | Exact large-\(D\) scalar survivor (11.1)–(11.9).                                                                                                     |                                                           |       |
| **DISPROVED**    | The claim that B-rank plus \(C_{\rm up}\), Centered-Align, and Unitary-\(Q\) close the two dimension regimes.                                        |                                                           |       |
| **PROVED**       | The pointwise same-map identity (12.2).                                                                                                              |                                                           |       |
| **PROVED — new** | Exact decoupled operator model with positive \(P\), uniform Pure-\(Q\), positive bistochastic \(\widetilde J\), and a rank-\(m(m-1)\) unitary frame. |                                                           |       |
| **DISPROVED**    | Sufficiency of the separate low-rank, frame, coherent-state, contraction, marginal, and endpoint constraints without realignment/cocycle coupling.   |                                                           |       |
| **OPEN**         | The realignment–pair-frame implication (15.1)–(15.3).                                                                                                |                                                           |       |
| **OPEN**         | Existence or nonexistence of one actual tuple satisfying \((E1_{\rm gap})\).                                                                         |                                                           |       |
| **OPEN**         | \((E1_{\rm gap})\).                                                                                                                                  |                                                           |       |
| **CONJECTURED**  | None promoted.                                                                                                                                       |                                                           |       |

The first new statement requiring independent verification is the exact decoupled operator construction in Section 13, especially the simultaneous coherent-state estimate (13.7) and unitary-frame realization (13.10)–(13.12).

The full-size theorem remains open because the finite \(r=2\) gate remains open, independently of the separate all-copy gate.
