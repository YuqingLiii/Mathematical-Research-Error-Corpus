# Round 2 local audit

Date: 2026-09-12

Status: equation-level local audit completed. This is not an independent external review.

## Verdict

The response's literal verdict is correct:

    (E1) as written is PROVED.

However, this is a prompt-specification loophole, not progress that closes the intended
full-size gate. Round 2's displayed definition of (E1) omitted the positive-gap
condition inherited from Round 1. By taking eta large enough that A=m, the
one-copy and ratio bounds become vacuous. The physically relevant strengthened
statement

    ln m > 18,
    A^2 < m^(1/m),
    p_1(C) <= A/m,
    kappa_1(U) <= A-1

for one finite deterministic complex tuple remains **OPEN / CONJECTURED**.
Nothing in this response proves the full-size MOE or Holevo theorem.

## Status ledger

| Item | Local status | Meaning |
|---|---|---|
| Literal (E1) | VERIFIED | The explicit D=1, A=m witness satisfies every quantifier in the statement actually sent. |
| Relevance of literal (E1) to the main theorem | NEGATIVE | It violates the required positive-gap inequality by a maximal margin. |
| (OB) and (OB2) | VERIFIED | The transpose, block indices, and all factors of m are correct. |
| Product-input lower bound (LB) | VERIFIED | kappa_1(U) >= m p_1(C)-1 follows exactly from rank-one T. |
| Pointwise formulas (M2) and (6) | VERIFIED | They keep the actual marginal purity d_T; no illicit replacement by p_1 occurs. |
| (OL1) => (OB2) | VERIFIED | Uses d_T<=A/m. |
| Multiplicativity => (OB2) | VERIFIED | Uses p_1<=A/m. |
| Full implication/non-implication ledger | PARTIAL | The Weyl example proves multiplicativity and (OB2) do not imply (OL1). The answer only shows that (OL1) does not algebraically yield multiplicativity when p_1<A/m; it does not give a counterexample establishing the converse non-implication. |
| Frame identities (FR) and (RQ) | VERIFIED | Exact restricted Rayleigh quotient over the physical family F_T; the same tuple occurs in both left and right orbits. |
| Universal bound 0<=kappa_1<=m-1 | VERIFIED | Hilbert--Schmidt Cauchy--Schwarz on the positive equal-norm frame operators. |
| Equality condition for the universal bound | VERIFIED | Equality requires and is implied by F_(T,1)=...=F_(T,m). |
| Weyl tuple calculation | VERIFIED | p_1=1/D, self-multiplicativity holds, while kappa_1=D^2-1=m-1. |
| Weyl separation of (OL1) from (OB2) | VERIFIED | With A=D, maximally entangled T violates (OL1) but saturates (OB2). |
| Low-A gate (E1_gap) | OPEN / CONJECTURED | No tuple, obstruction, or uniform all-T estimate is supplied. |

## Direct check of the literal witness

Choose any integer m>exp(18) and

    eta = sqrt(m(m-1))/3 - 1.

Then eta>0 and

    A = 1 + 9(1+eta)^2/m = m.

For any channel with m-dimensional output, output purity is at most one, so

    p_1(C) <= 1 = A/m.

The response's frame estimate gives, for every tuple,

    kappa_1(U) <= m-1 = A-1.

For the fully explicit choice D=1 and U_1=...=U_m=1, the only input is
the scalar density operator 1, and

    C(1) = J_m/m,
    p_1(C)=1,
    R_U(T)=m-1

for every scalar Hilbert--Schmidt unit T. Thus both inequalities hold with
equality. All objects are finite and deterministic, so the quantifier order is
correct.

The same witness fails the needed gap:

    A^2 = m^2 > m^(1/m).

It therefore gives no positive regularized entropy defect.

## Check of the frame/Rayleigh reduction

With

    z_(a,v)(T)=U_a T U_v^T,
    F_(T,v)=sum_a |z_(a,v)>><<z_(a,v)|,
    F_T=sum_a |U_a T>><<U_a T|,

right multiplication R_v:Z->Z U_v^T is Hilbert--Schmidt unitary and

    F_(T,v)=R_v F_T R_v^*.

Directly,

    C(X_vw(T))_(a,b)
      = m^(-1) <z_(b,w)(T),z_(a,v)(T)>_HS,

so

    ||C(X_vw(T))||_2^2
      = m^(-2) Tr(F_(T,v) F_(T,w)).

All F_(T,v) have the same squared Hilbert--Schmidt norm
Q_T=Tr(F_T^2), and the diagonal case gives

    ||C(TT^*)||_2^2 = Q_T/m^2.

Consequently,

    1+R_U(T)
      = Tr[(sum_v F_(T,v))^2]/(m Tr(F_T^2))
      = m ||mathfrak R_U(F_T)||_2^2/||F_T||_2^2,

where

    mathfrak R_U(F)=m^(-1) sum_v R_v F R_v^*.

This is an exact reformulation, not a bound. Its domain is the nonconvex
physical family

    {F_T=sum_a |U_a T>><<U_a T| : ||T||_2=1},

not the full positive cone. That restriction is load-bearing.

For positive F_(T,v) of equal Hilbert--Schmidt norm,

    0 <= Tr(F_(T,v)F_(T,w)) <= Q_T.

Summing the m(m-1) off-diagonal pairs proves

    0 <= R_U(T) <= m-1.

This is sharp but far too weak when the positive-gap condition forces
A-1 < m^(1/(2m))-1 = O((ln m)/m).

## Check of the Weyl example

For the full D^2 Weyl tuple, m=D^2 and the associated random-unitary
channel is completely depolarizing:

    L(X)=Tr(X) I_D/D.

In the normalized Weyl operator basis, its complement is, up to transpose,

    C(rho)=D^(-1) W^* R_rho W,

where R_rho:Y->Y rho. The Hilbert--Schmidt singular values of R_rho
are the eigenvalues of rho, each repeated D times. Therefore

    ||C(rho)||_2^2 = Tr(rho^2)/D,
    p_1(C)=1/D=1/sqrt(m).

For every pure two-input state, L tensor L outputs I_(D^2)/D^2.
Complementarity therefore gives two-copy purity 1/D^2=1/m; convexity then
gives exact maximum-output 2-norm multiplicativity.

Combining this with (OB) yields

    R_U(T)=D/Tr[(TT^*)^2]-1.

The minimum possible input purity is 1/D, attained by T=I/sqrt(D), so

    kappa_1(U)=D^2-1=m-1.

With A=D (realized by the stated finite positive eta), one has
p_1=A/m; nevertheless (OL1) fails while (OB2) is saturated. This
validly separates the stronger conditional ratio gate from both
multiplicativity and the global two-copy target. It is outside the low-A
regime and does not refute (E1_gap).

## Corrected next gate

The next query must freeze the missing condition in the statement itself:

    (E1_gap)
    There exist finite m,D,eta>0 and U in U(D)^m such that
      ln m>18,
      A=1+9(1+eta)^2/m,
      A^2<m^(1/m),
      p_1(C)<=A/m,
      kappa_1(U)<=A-1.

Equivalently, after independently rechecking (FR), it asks for

    m ||mathfrak R_U(F_T)||_2^2 <= A ||F_T||_2^2

uniformly over every Hilbert--Schmidt unit T in the physical family. Literal
large-eta witnesses, full Weyl tuples, unrestricted cone norms, and ordinary
maximum-output multiplicativity do not settle this corrected statement.
