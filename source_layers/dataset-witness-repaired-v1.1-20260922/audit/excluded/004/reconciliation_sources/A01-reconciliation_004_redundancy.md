# Record 004: the omitted lower endpoint is redundant in the stated system

This is a new algebraic reconciliation, not an assertion that the old audit was never performed.
The old audit correctly wrote the two-sided centered Cauchy inequality, but did not establish that omitting its lower side removes any feasible point from the full scalar system.

Use the source's notation, and write `k=m(m−1)` (this k is only the rank bound here).
The source imposes

    A=1+q/m, q>9, A<m^(1/(2m)),
    D²/m ≤ alpha ≤ A D(D+1)/m − D,
    r=alpha/D, u=Dr−1, v=D−r, n=D²−1,
    a≥v²/k, b=a+2 tau/D−r²−1, tau≥Dr², x≥0.

First m≥10: for an integer 1≤m≤9, A>1+9/m≥2 but m^(1/(2m))<2.
Since log(m)/m decreases for m≥10 and (5/4)^20>10, we have A<5/4.
Combining the two bounds on alpha gives

    D ≥ (m−A)/(A−1) > 4m−5 ≥ (7/2)m,
    0<r≤A(D+1)/m−1 < 5D/(4m).

In particular n>k and v>0. Put

    F=D²+D−k−r(D+k+1),
    G=D²−D−k+r(k+1−D).

For t=D/m≥7/2 and m≥10, the bounds above give

    F/m² > (7/8)t²−(101/80)t−1 > 0,
    G/m² > (7/8)t²−t/10−1 > 0.

Both quadratics are increasing for t≥7/2, and their values at 7/2 are positive.
Direct polynomial expansion gives the identity

    [(D−r)²/k+r²−1](n−k)−(Dr−1)² = FG/k > 0.

Consequently

    b ≥ a+r²−1 ≥ v²/k+r²−1 > u²/(n−k)
      ≥ u²/(n−v²/a).

Multiplication by the positive denominators yields

    (a−v²/n)(b−u²/n) > (uv/n)².

Thus the proposed missing lower endpoint

    uv/n − sqrt((a−v²/n)(b−u²/n))

is strictly negative throughout the source's scalar domain. It is already implied by x≥0.
This is not a counterexample to centered Cauchy; it shows that the old witness does not establish an error in the full displayed system. Its degenerate a=v²/n example also violates a≥v²/k because n>k and v>0.

Release decision: exclude this particular alleged mathematical error. Do not claim all other arguments in the source are correct.
