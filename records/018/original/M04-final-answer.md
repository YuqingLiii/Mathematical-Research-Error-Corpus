# Verdict: **OPEN WITH EARLIEST GAP**

I continued from the frozen Round-6 setup and the audited Round-5 identities in the supplied record. 

The five proposed Round-6 facts audit as follows:

$$
\boxed{\text{RD, Centered-Align, B-rank, Contract, and Unitary-Q are all valid.}}
$$

There are, however, two important changes to the proposed closure strategy.

First,

$$
\boxed{\text{Unitary-Q is actually REDUNDANT throughout the feasible low-\(A\) regime.}}
$$

Second, after adding a strictly stronger centered fourth-moment consequence of Pure-\(Q\), the complete scalar necessary system is still feasible. In fact it survives for an explicit symbolic family with

$$
D=D_{\rm PA}+1,
$$

one integer above the smallest dimension allowed by PA. Thus the proposed “B-rank near \(D_{\min}\), Centered-Align/Unitary-Q for large \(D\)” two-regime scalar closure fails.

The first genuinely unresolved ingredient is consequently the **physical realignment/pair-difference coupling**

$$
B=P_\perp J_\Phi P_\perp,\qquad
J_\Phi=\mathcal R^{-1}(P_0+P)\succeq0,
\qquad
A_{ab}=U_b^*U_a,
$$

not any remaining scalar inequality.

The Round-6 proposed facts and requested two-regime test are at .

---

## 1. Realignment defect

Put

$$
c:=\frac{\mathsf C_U}{m^4}=\operatorname{Tr}(JS),
\qquad
i=\operatorname{Tr}S^2=\operatorname{Tr}J^2.
$$

Because reshuffling preserves Hilbert–Schmidt norm,

$$
\|S\|_2=\|J\|_2.
$$

Hence

$$
\begin{aligned}
\frac12\|S-J\|_2^2
&=\frac12\left(\|S\|_2^2+\|J\|_2^2
-2\operatorname{Tr}(SJ)\right)\\
&=i-c.
\end{aligned}
$$

Multiplying by \(m^4\),

$$
\boxed{
\mathsf I_U-\mathsf C_U
=
\frac{m^4}{2}\|S-J\|_2^2 .
}
\tag{RD}
$$

So RD is correct.

### The proposed RD-PT2 inequality

Relative to

$$
\mathbb Ce\oplus e^\perp,\qquad e=|I\rangle\rangle/\sqrt D,
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
\end{pmatrix}.
$$

Since

$$
\langle e,J^2e\rangle=\frac{\tau}{D},
$$

we have

$$
\|z\|^2=\frac{\tau}{D}-r^2.
$$

Therefore

$$
\begin{aligned}
i-c
&=\frac12\|S-J\|_2^2\\
&=
\frac12(1-r)^2+
\left(\frac{\tau}{D}-r^2\right)
+\frac12\|P-B\|_2^2\\
&\ge
\frac{\tau}{D}-r+\frac{1-r^2}{2}.
\end{aligned}
$$

In unnormalized variables this is exactly the displayed RD-PT2 inequality.

Equivalently, with

$$
a:=\operatorname{Tr}B^2
=i-\frac{2\tau}{D}+r^2,\qquad
b:=\operatorname{Tr}P^2=i-1,
$$

and

$$
h:=\operatorname{Tr}(BP)=c-r,
$$

RD-PT2 is simply

$$
\boxed{h\le\frac{a+b}{2}.}
$$

It is therefore **redundant** once Centered-Align below is available.

---

# 2. Trace-centered alignment

Let

$$
u:=\operatorname{Tr}P=\alpha-1,\qquad
v:=\operatorname{Tr}B=D-r,\qquad
n:=D^2-1.
$$

Center

$$
P_c=P-\frac unP_\perp,\qquad
B_c=B-\frac vnP_\perp.
$$

Then

$$
\operatorname{Tr}P_c^2=b-\frac{u^2}{n},
\qquad
\operatorname{Tr}B_c^2=a-\frac{v^2}{n},
$$

and

$$
\operatorname{Tr}(BP)
=
\frac{uv}{n}+\operatorname{Tr}(B_cP_c).
$$

Hilbert–Schmidt Cauchy–Schwarz gives

$$
\boxed{
h
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

Both square-root factors are nonnegative by trace-purity.

It is never weaker than uncentered Align because

$$
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)}
\le\sqrt{ab},
$$

which is ordinary Cauchy–Schwarz applied to

$$
\left(
\frac v{\sqrt n},
\sqrt{a-\frac{v^2}{n}}
\right),\quad
\left(
\frac u{\sqrt n},
\sqrt{b-\frac{u^2}{n}}
\right).
$$

### Audit of the proposed scalar escape

At

$$
\tau=Dr^2,\qquad
i=1+\frac{u^2}{n},
$$

we have

$$
b-\frac{u^2}{n}=0.
$$

Moreover

$$
a=1+\frac{u^2}{n}-r^2
=\frac{v^2}{n},
$$

because

$$
n(1-r^2)+u^2=(D-r)^2=v^2.
$$

Thus both centered variances vanish, and

$$
h\le\frac{uv}{n}.
$$

At

$$
A=A_0:=\frac{m(r+1)}{D+1},
$$

direct substitution indeed gives

$$
c_{\rm up}=r+\frac{uv}{n},
$$

and

$$
\boxed{
c_{\rm req}
-\left(r+\frac{uv}{n}\right)
=
-\frac{(\alpha-D)(D+3)(D^2-\alpha)}
       {2(D-1)}
\le0.
}
$$

So the claimed scalar escape is correct.

---

# 3. Low rank of \(B\)

Since

$$
J=\frac1{m^2}\sum_{a,b}|A_{ab}\rangle\rangle
   \langle\langle A_{ab}|,
\qquad A_{ab}=U_b^*U_a,
$$

and \(A_{aa}=I\),

$$
P_\perp|A_{aa}\rangle\rangle=0.
$$

Hence

$$
\boxed{
B=
\frac1{m^2}
\sum_{a\ne b}
|P_\perp A_{ab}\rangle\rangle
\langle\langle P_\perp A_{ab}|
}
$$

and therefore

$$
\boxed{\operatorname{rank}B\le k:=m(m-1).}
$$

Since \(\operatorname{Tr}B=v\),

$$
a=\operatorname{Tr}B^2
\ge\frac{v^2}{k}.
$$

Using

$$
a=i-\frac{2\tau}{D}+r^2
$$

and

$$
\tau\ge Dr^2
$$

gives

$$
\boxed{
i\ge r^2+\frac{(D-r)^2}{m(m-1)}.
}
\tag{I-rank}
$$

### Why \(D>m\) follows rather than being assumed

PA and \(\alpha\ge D^2/m\) give

$$
D+m\le A(D+1),
$$

hence

$$
D\ge\frac{m-A}{A-1}.
\tag{3.1}
$$

Gap gives

$$
A<m^{1/(2m)}.
$$

Using \(\ln m<m-1\),

$$
\ln A
<
\frac{m-1}{2m}
\le
\ln\frac{2m}{m+1},
$$

so

$$
A<\frac{2m}{m+1}.
$$

Substitution into (3.1) gives

$$
\boxed{D>m.}
$$

Thus B-rank and I-rank are correct.

---

# 4. Hilbert–Schmidt contraction

For arbitrary \(X\),

$$
\begin{aligned}
\|L(X)\|_2
&=
\left\|
\frac1m\sum_aU_aXU_a^*
\right\|_2\\
&\le
\frac1m\sum_a\|U_aXU_a^*\|_2
=\|X\|_2.
\end{aligned}
$$

Thus

$$
\|L\|_{2\to2}\le1.
$$

Since

$$
S=L^*L,
$$

$$
0\preceq S\preceq I.
$$

The scalar direction \(e\) is a unit eigenvector, so

$$
S=P_0+P,\qquad
0\preceq P\preceq P_\perp.
$$

Consequently

$$
\boxed{i=\operatorname{Tr}S^2\le\operatorname{Tr}S=\alpha.}
\tag{Contract}
$$

Equivalently

$$
b=i-1\le u=\alpha-1.
$$

This audit is correct.

---

# 5. Unitary-\(Q\): correct, but redundant

Pure-\(Q\) says

$$
\|Q(\rho_y)\|_2^2\le\epsilon,
\qquad
\epsilon=\frac Am-\frac1D.
$$

Take an arbitrary unitary

$$
W=\sum_{j=1}^D\lambda_j\rho_j,
\qquad |\lambda_j|=1,
$$

in an eigenbasis, and put

$$
\bar\lambda=\frac1D\sum_j\lambda_j.
$$

Since \(Q(I)=0\),

$$
Q(W)=
\sum_j(\lambda_j-\bar\lambda)Q(\rho_j).
$$

Therefore

$$
\begin{aligned}
\|Q(W)\|_2^2
&\le
\left(\sum_j|\lambda_j-\bar\lambda|^2\right)
\left(\sum_j\|Q(\rho_j)\|_2^2\right)\\
&\le
D\epsilon
\left(D-\frac{|\operatorname{Tr}W|^2}{D}\right).
\end{aligned}
$$

Hence

$$
\boxed{
\|Q(W)\|_2^2
\le
\epsilon\bigl(D^2-|\operatorname{Tr}W|^2\bigr).
}
\tag{Unitary-Q}
$$

Summing over \(A_{ab}\) gives the proposed

$$
\boxed{
h=\operatorname{Tr}(BP)
\le
\epsilon(D^2-\alpha).
}
$$

### But this adds no information in the feasible regime

From Gap and \(\ln m>18\),

$$
A<\frac32.
$$

Indeed \(\ln A<\ln m/(2m)<1/4\), hence
\(A<e^{1/4}<3/2\).

Then (3.1) actually gives

$$
D>\frac{2m}{A},
$$

because

$$
\frac{m-A}{A-1}>\frac{2m}{A}
\iff
m(2-A)>A^2,
$$

and the right-hand inequality follows from
\(A<3/2\) and \(m>6\).

Therefore

$$
\epsilon D=\frac{AD}{m}-1>1.
$$

But \(0\le P\le P_\perp\) already gives, for every unitary \(W\),

$$
\begin{aligned}
\|Q(W)\|_2^2
&=\langle\langle W|P|W\rangle\rangle\\
&\le\|P_\perp W\|_2^2\\
&=
D-\frac{|\operatorname{Tr}W|^2}{D}.
\end{aligned}
$$

Since \(\epsilon D>1\), this is strictly stronger than Unitary-Q.

Thus

$$
\boxed{
\text{Unitary-Q is REDUNDANT for every feasible }(E1_{\rm gap})\text{ candidate.}
}
\tag{5.1}
$$

So it cannot supply the proposed “large-\(D\)” half of a two-regime proof.

---

# 6. A strictly stronger centered fourth-moment endpoint

There is one immediate Pure-\(Q\) consequence stronger than Round 5's \(C_{\rm up}\).

Set

$$
g(y):=\|Q(\rho_y)\|_2^2
=\langle\langle\rho_y|P|\rho_y\rangle\rangle.
$$

Then pointwise

$$
0\le g(y)\le\epsilon,
$$

so

$$
g(y)^2\le\epsilon g(y).
\tag{6.1}
$$

The Haar first moment is

$$
\mu:=\mathbb Eg(y)
=
\frac{\operatorname{Tr}P}{D(D+1)}
=
\frac{\alpha-1}{D(D+1)}.
\tag{6.2}
$$

The exact fourth-moment contraction gives

$$
\boxed{
\mathbb E g(y)^2
=
\frac{
D\alpha^2-2D\alpha+2Dc+2Di+4D\tau-D-12\alpha+6
}{
D^2(D+1)(D+2)(D+3)
}.
}
\tag{6.3}
$$

Equation (6.3) follows directly by expanding
\(f(y)=m^2(1/D+g(y))\) in the audited \(S_4\) moment formula; no probabilistic approximation is involved.

Averaging (6.1),

$$
\mathbb Eg^2\le\epsilon\mu.
$$

Solving (6.3) for \(c\) gives a new endpoint \(c\le c_\circ\).

It is most transparently expressed through the old normalized endpoint

$$
c_{\rm up}:=\frac{\mathcal C_{\rm up}}{m^4}.
$$

Define the PA slack

$$
s_{\rm PA}
:=
AD(D+1)-m(\alpha+D)\ge0.
$$

Since

$$
\epsilon-\mu
=
\frac{s_{\rm PA}}{mD(D+1)},
$$

one obtains

$$
\boxed{
c\le
c_\circ
:=
c_{\rm up}
-
\frac{s_{\rm PA}(D+2)(D+3)}
     {2mD}.
}
\tag{Centered-C-up}
$$

Therefore

$$
\boxed{c_\circ\le c_{\rm up},}
$$

with strict inequality whenever PA is strict.

This is a genuine strengthening of the Round-5 scalar system.

---

# 7. Strongest scalar necessary system obtained here

Put

$$
q=m(A-1)=9(1+\eta)^2>9,
$$

so Gap is exactly

$$
2m\ln\left(1+\frac qm\right)<\ln m.
$$

Every solution must admit numbers \(r,i,\tau,h\) satisfying

$$
\frac Dm\le r<D,
\qquad
m(r+1)\le A(D+1),
$$

and, with

$$
u=Dr-1,\quad v=D-r,\quad
n=D^2-1,\quad k=m(m-1),
$$

$$
Dr^2\le\tau\le\sqrt A\,Dr^2,
$$

$$
b:=i-1,\qquad
a:=i-\frac{2\tau}{D}+r^2,
$$

$$
\boxed{
\frac{u^2}{n}\le b\le u,
\qquad
\frac{v^2}{k}\le a\le v^2,
}
\tag{7.1}
$$

and

$$
h\ge0,\qquad
h\le v,
$$

$$
\boxed{
h\le
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
}
\tag{7.2}
$$

Pair-energy is simply

$$
c=r+h.
$$

Finally the symmetric-Bell constraints, including the new centered fourth moment, are

$$
\boxed{
c_{\rm req}\le r+h\le c_\circ.
}
\tag{7.3}
$$

Unitary-Q can be omitted from this strongest system because of (5.1). The old \(c_{\rm up}\) can likewise be omitted because \(c_\circ\le c_{\rm up}\).

---

# 8. What B-rank does at the PA boundary

Suppose both lower constraints saturate:

$$
r=\frac Dm,
\qquad
m(r+1)=A(D+1).
$$

Then

$$
D=D_0:=\frac{m-A}{A-1}.
$$

To maximize the allowed upper endpoint subject to B-rank, take

$$
\tau=Dr^2,
\qquad
i=r^2+\frac{(D-r)^2}{m(m-1)}.
$$

Direct simplification gives

$$
\boxed{
c_{\rm up}-r
=
\frac{
(m-A)(m-1)
\left(mA^2-mA+A-m\right)
}{
m^3(A-1)^2
}.
}
\tag{8.1}
$$

Because \(A<3/2\),

$$
mA^2-mA+A-m
=
m(A^2-A-1)+A
<
-\frac m4+\frac32<0.
$$

Hence

$$
c_{\rm up}<r.
$$

Since physical Pair-energy gives \(c=r+h\ge r\), the simultaneous PA/lower-\(\alpha\) corner is impossible.

So B-rank genuinely excludes the exact boundary.

But it does **not** exclude a useful near-boundary regime.

---

# 9. Explicit scalar survivor only one dimension above the boundary

Choose

$$
\boxed{q=10},
$$

hence

$$
A=1+\frac{10}{m},
\qquad
\eta=\frac{\sqrt{10}}3-1>0.
$$

Take \(m\) a sufficiently large multiple of \(10\), with

$$
\ln m>20.
$$

Then

$$
2m\ln\left(1+\frac{10}{m}\right)<20<\ln m,
$$

so Gap holds.

Set

$$
\boxed{
D=\frac{m(m-1)}{10},
\qquad
r=\frac{m-1}{10}.
}
\tag{9.1}
$$

For these parameters,

$$
D_0=\frac{m-A}{A-1}
=\frac{m(m-1)}{10}-1,
$$

so

$$
\boxed{D=D_0+1.}
$$

Also

$$
\alpha=Dr=\frac{m(m-1)^2}{100}
=\frac{D^2}{m}.
$$

Thus the lower \(\alpha\)-constraint is saturated.

Take

$$
\boxed{
\tau=Dr^2
=
\frac{m(m-1)^3}{1000},
}
$$

and

$$
\boxed{
i=
r^2+\frac{(D-r)^2}{m(m-1)}
=
\frac{(m-1)^2(2m-1)}{100m}.
}
\tag{9.2}
$$

Finally take

$$
\boxed{h=0.}
$$

### PA

One finds

$$
A(D+1)-m(r+1)=\frac{10}{m}>0.
$$

### B trace-purity

Here

$$
v=D-r=\frac{(m-1)^2}{10},
$$

and

$$
a=i-r^2
=
\frac{(m-1)^3}{100m}
=
\frac{v^2}{m(m-1)}.
$$

So B-rank is saturated exactly.

### P trace-purity

With \(u=\alpha-1\),

$$
b-\frac{u^2}{n}
=
\frac{
(m-1)^3
\left(
m^4-2m^3-99m^2+100m-100
\right)
}{
100m(m^2-m-10)(m^2-m+10)
}.
$$

This is positive for all sufficiently large \(m\).

Also

$$
\alpha-i
=
\frac{(m-1)^4}{100m}>0,
$$

so Contract holds.

### Symmetric-Bell lower endpoint

Direct substitution yields

$$
\boxed{
c_{\rm req}-r
=
-\frac{(m-1)^2}{20000m}
\left(
m^6-13m^5+73m^4-531m^3
+1190m^2-3120m+400
\right).
}
$$

The polynomial in parentheses is positive for \(m\ge14\). Hence

$$
c_{\rm req}<r.
\tag{9.3}
$$

### New centered fourth-moment upper endpoint

For this same family,

$$
\boxed{
c_\circ-r
=
\frac{
m^5-5m^4+69m^3-27m^2-38m-6000
}{
200m^2
}.
}
\tag{9.4}
$$

This is positive for all sufficiently large \(m\).

Thus with \(h=0\),

$$
c_{\rm req}<r=c<c_\circ.
$$

Every scalar inequality in §7 is satisfied.

Therefore

$$
\boxed{
\text{the complete scalar necessary system survives already at }D=D_0+1.
}
\tag{9.5}
$$

This disproves the proposed scalar two-regime closure.

In particular, no “large-\(D\)” use of Unitary-Q can rescue it, because Unitary-Q is already redundant.

---

# 10. A decoupled operator relaxation also survives

The preceding survivor is only scalar. One can go further and show that even **positive \(P\) plus a low-rank unitary frame \(B\), considered separately**, do not close the gap.

This is not a physical tuple; its purpose is to identify the coupling that remains indispensable.

Choose above \(m=10k\) with \(k\) odd. Then

$$
D=\frac{m(m-1)}{10}
$$

is odd, so

$$
n=D^2-1
$$

is even.

Keep the scalar values in §9 and define

$$
u=Dr-1,\qquad b=i-1,
$$

$$
t:=\frac un,
\qquad
s:=
\sqrt{
\frac{b-u^2/n}{n}
}.
$$

For sufficiently large \(m\),

$$
0<s<t.
$$

Indeed the lower inequality was proved above, while

$$
2\frac{u^2}{n}-b
=
\frac{
m^6+96m^5-594m^4+1096m^3
-899m^2+10400m-100
}{
100m(m^2-m-10)(m^2-m+10)
}>0.
$$

## 10.1 An invisible Hilbert-space direction

Regard the traceless Hermitian matrices as a real Hilbert space of even dimension \(n\). Choose an orthogonal complex structure

$$
\mathcal A^2=-I,\qquad
\mathcal A^{\mathsf T}=-\mathcal A,
$$

and extend it complex linearly to traceless \(M_D\).

Set

$$
K=i\mathcal A.
$$

Then

$$
K=K^*,\qquad
K^2=P_\perp,\qquad
\operatorname{Tr}K=0,
$$

while for every Hermitian \(X\),

$$
\langle\langle X|K|X\rangle\rangle
=
i\langle X,\mathcal A X\rangle_{\mathbb R}=0.
$$

Define

$$
\boxed{P=tP_\perp+sK.}
\tag{10.1}
$$

Its eigenvalues are \(t\pm s\), hence

$$
0\preceq P\preceq P_\perp.
$$

Moreover

$$
\operatorname{Tr}P=tn=u
$$

and

$$
\operatorname{Tr}P^2
=n(t^2+s^2)=b.
$$

For every pure \(\rho_y\),

$$
\begin{aligned}
\langle\langle\rho_y|P|\rho_y\rangle\rangle
&=
t\|P_\perp\rho_y\|_2^2\\
&=
t\left(1-\frac1D\right)\\
&=
\frac{u}{D(D+1)}
=\mu.
\end{aligned}
$$

For the §9 family,

$$
\boxed{
\epsilon-\mu
=
\frac{100}{m^2(m^2-m+10)}>0.
}
$$

Thus the full coherent-state Pure-\(Q\) bound is obeyed.

## 10.2 A low-rank unitary frame with the exact \(B\) trace and purity

A generalized Weyl basis supplies \(D^2-1\) pairwise Hilbert–Schmidt orthogonal traceless unitaries. Because \(D\) is odd they can be partitioned into adjoint pairs.

Since

$$
m(m-1)<\frac{D^2-1}{2}
$$

for sufficiently large \(m\), choose

$$
K_0:=m(m-1)
$$

such unitaries \(W_j\), no two belonging to the same adjoint pair.

Choose the complex structure \(\mathcal A\) above so that

$$
KW_j=-W_j
$$

for every selected \(j\); this is done by prescribing the \(90^\circ\) rotation on each real plane generated by
\(\Re W_j,\Im W_j\), then extending orthogonally.

Define

$$
\boxed{
B=
\frac1{m^2}
\sum_{j=1}^{K_0}
|W_j\rangle\rangle\langle\langle W_j|.
}
\tag{10.2}
$$

Because \(\|W_j\|_2^2=D\),

$$
\operatorname{Tr}B
=
\frac{m(m-1)D}{m^2}
=
\frac{D(m-1)}m
=D-r=v.
$$

Orthogonality gives

$$
\operatorname{Tr}B^2
=
\frac{m(m-1)D^2}{m^4}
=
\frac{v^2}{m(m-1)}
=a.
$$

Thus B-rank is saturated.

Finally,

$$
\boxed{
\operatorname{Tr}(BP)
=(t-s)v.
}
\tag{10.3}
$$

All trace, purity, rank, contraction, and coherent-state constraints are therefore simultaneously realizable in this **decoupled relaxation**. For sufficiently large \(m\),

$$
0\le(t-s)v\le v<c_\circ-r,
$$

while (9.3) gives \(c_{\rm req}<r\); hence even the scalar endpoint inequalities remain satisfied.

### What this construction deliberately does not satisfy

It is not a channel construction. In particular it does **not** impose

$$
B=P_\perp J P_\perp,\qquad
J=\mathcal R^{-1}(P_0+P)\succeq0,
$$

and the \(W_j\) are not required to be one common pair-difference system

$$
W_j=U_b^*U_a
$$

with the multiplicative consistency

$$
A_{ab}A_{bc}=A_{ac}.
$$

Indeed the invisible \(K=i\mathcal A\) is generally not \(*\)-preserving.

Therefore this is not a counterexample to \((E1_{\rm gap})\). It proves the narrower statement

$$
\boxed{
\begin{array}{c}
\text{Pure-Q + }0\le P\le P_\perp
+\text{ the exact traces/purities}\\
+\text{ a low-rank unitary-frame }B
\end{array}
\quad
\text{do not by themselves force the missing inequality.}
}
\tag{10.4}
$$

The common realignment/pair-difference origin is load-bearing.

---

# 11. Why the symmetric-Bell alignment route cannot close the survivor

For the explicit scalar family,

$$
c_{\rm req}<r.
$$

But Pair-energy always gives

$$
c=r+h\ge r.
$$

Therefore the symmetric-Bell necessary condition

$$
c\ge c_{\rm req}
$$

is **automatic** in that regime.

This has an important consequence: even a perfect new upper bound on

$$
h=\operatorname{Tr}(BP)
$$

cannot produce a contradiction there, unless some other physical condition first raises \(c_{\rm req}\) or excludes the scalar regime.

Thus the earliest open obligation is no longer merely “improve Align.” One must exploit the coupled physical structure to obtain either:

$$
\boxed{
\text{a different physical }T
\text{ with }R_U(T)>A-1
}
$$

for every admissible tuple, or an inequality from the common realignment/pair-difference structure that eliminates the surviving scalar/operator relaxation.

Concretely, the missing implication has the quantifiers

$$
\boxed{
\begin{gathered}
\forall\,m,D,\eta,U\text{ satisfying Gap and }p\le A/m,\\
\exists\,T,\quad \|T\|_2=1,\qquad
R_U(T)>A-1,
\end{gathered}
}
\tag{11.1}
$$

if \((E1_{\rm gap})\) is false.

No proof of (11.1) is obtained here.

Conversely, no explicit frozen tuple satisfying

$$
R_U(T)\le A-1
\qquad\forall\,T
$$

is constructed.

Hence \((E1_{\rm gap})\) remains open.

---

# Audit ledger

| Status                              | Statement                                                                                                                                                     |                                                           |                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| **PROVED**                          | RD: \(\mathsf I_U-\mathsf C_U=(m^4/2)\|S-J\|_2^2\).                                                                                                           |                                                           |                                           |
| **PROVED**                          | RD-PT2, equivalently \(h\le(a+b)/2\).                                                                                                                         |                                                           |                                           |
| **REDUNDANT**                       | RD-PT2 once Centered-Align is retained.                                                                                                                       |                                                           |                                           |
| **PROVED**                          | Centered-Align with the exact trace-centered variances.                                                                                                       |                                                           |                                           |
| **PROVED**                          | The proposed \(A=A_0,\tau=Dr^2,i=1+u^2/n\) escape factorization.                                                                                              |                                                           |                                           |
| **PROVED**                          | (B=m^{-2}\sum_{a\ne b}                                                                                                                                        | P_\perp A_{ab}\rangle\rangle\langle\langle P_\perp A_{ab} | ) and \(\operatorname{rank}B\le m(m-1)\). |
| **PROVED**                          | \(i\ge r^2+(D-r)^2/[m(m-1)]\).                                                                                                                                |                                                           |                                           |
| **PROVED**                          | Gap + PA + \(\alpha\ge D^2/m\) imply \(D>m\).                                                                                                                 |                                                           |                                           |
| **PROVED**                          | \(0\le P\le P_\perp\) and \(i\le\alpha\).                                                                                                                     |                                                           |                                           |
| **PROVED**                          | Unitary-Q as stated.                                                                                                                                          |                                                           |                                           |
| **REDUNDANT**                       | Unitary-Q throughout the feasible low-\(A\) regime, because \(\epsilon D>1\) and Contract is stronger.                                                        |                                                           |                                           |
| **PROVED — new**                    | Centered fourth-moment endpoint \(c\le c_\circ<c_{\rm up}\) when PA has slack.                                                                                |                                                           |                                           |
| **PROVED**                          | B-rank plus \(C_{\rm up}\) excludes the exact PA/lower-\(\alpha\) boundary.                                                                                   |                                                           |                                           |
| **DISPROVED as a closure strategy** | The proposed scalar two-regime closure: the full strengthened scalar system survives already at \(D=D_0+1\).                                                  |                                                           |                                           |
| **PROVED — new**                    | Explicit \(q=10,\ D=D_0+1\) symbolic family satisfying every scalar necessary inequality, including Centered-C-up.                                            |                                                           |                                           |
| **PROVED — new**                    | A decoupled operator relaxation satisfying the exact \(P/B\) traces, purities, contraction, coherent-state bound, and a low-rank unitary frame also survives. |                                                           |                                           |
| **OPEN**                            | Whether realignment positivity and the common pair-difference identities exclude that relaxation.                                                             |                                                           |                                           |
| **OPEN**                            | Existence of a deterministic physical \(T\) violating the ratio gate for every admissible tuple.                                                              |                                                           |                                           |
| **OPEN**                            | \((E1_{\rm gap})\).                                                                                                                                           |                                                           |                                           |
| **CONJECTURED**                     | None promoted.                                                                                                                                                |                                                           |                                           |

The first new formula I would ask an independent referee to recheck is

$$
\boxed{
c_\circ
=
c_{\rm up}
-
\frac{
\bigl[AD(D+1)-m(\alpha+D)\bigr](D+2)(D+3)
}{
2mD
},
}
$$

obtained from the genuinely centered pointwise inequality
\(g(y)^2\le\epsilon g(y)\).

The earliest remaining mathematical gap is the conversion of the **common physical realignment and pair-difference structure** into information not captured by the surviving scalar/decoupled relaxation. Until that is done, the finite \(r=2\) gate—and therefore separately the earlier all-copy problem—remains open.
