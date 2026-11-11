# CIRCDIST.cplx — Island V general case: code-realizable line sections are hard

Session continuation from the supplied historical visible-context record. Fresh isolated workspace, 2026-09-19.
Target: Island-V frontier (`w_X <= 4`, `d_X >= 4`, `k >= 2`) for the fixed-`d` complexity route.

**Protocol labels.** Nothing in this report is labelled PROVED. Written mathematical arguments are **CONJECTURED**. Exact finite computations produced by the self-contained verifier in Appendix A are **NUMERICAL**. No proof-DAG or historical repository file was accessed or modified.

## 0. Verdict

**Reading (a) fires, at the Island-V / X-sector level.** The realizability conditions do **not** collapse the general weight-4 CSP to matching. The right local object is stronger than the old `(S1)+(S2)` bookkeeping but still expressive enough for NP-hardness:

> a nondegenerate weight-4 check is a binary projective line `U <= N` together with a linear label map `phi : U -> Log`; its three list values are the graph of `phi` on `U \ {0}`.

A constant-size family of such line constraints implements Boolean XOR, constants, and a 3-SAT clause. More importantly, there is a linear-size **block-and-glue CSS compiler** taking any finite line-map instance to a code with every measured X-check of weight exactly 4, `d_X = 4`, and `k >= 2`, while preserving the designated list-section conflict relation exactly. Auxiliary equality/glue checks have a private syndrome value and can always be scheduled harmlessly. This is the nonlocal wiring mechanism that escapes the old `K4`/Hall obstruction.

The compiler also gives `d_Z >= 4`. Direct-summing a fixed `HGP(rep_3,rep_4)` spectator gives the full static promise `d_X=4`, `d_Z=3`, hence `d=3` exactly. The remaining wall before claiming full two-sector `Eff-Preserve` NP-completeness is **not** Island-V realizability: it is neutralising/certifying the schedule of the compiler's generally high-weight Z-check generators. Thus the fixed-`d` node moves to “essentially landed” in the pre-committed sense, but this report does **not** claim a complete two-sector NP-completeness theorem.

For the literal Island-V scope (X-check weight `<=4`, no opposite-sector weight bound), the weight-6 set-disjointness route is **moot as a source of hardness**: weight 4 already carries NP-hard list-section structure. For the stronger requirement that *both* X- and Z-generators be bounded by 4 or 6, the present compiler does not settle the issue; its Z rows can have growing weight.

---

## 1. Exact local characterization

Fix the historical notation

`Q = F_2^n / S_X`, `Log = ker(H_Z)/S_X <= Q`, and `m : Q -> Q/Log =: N`.

Choose any linear complement and write `Q = N \oplus Log`. For a weight-4 X-check `c`, its three `2|2` split values form

`L_c = {x_1,x_2,x_3}` with `x_1+x_2+x_3=0`.

### Lemma 1 — line-graph form — CONJECTURED

If `c` is nondegenerate, then

1. `W_c := {0,x_1,x_2,x_3}` is a 2-dimensional subspace of `Q`;
2. `W_c \cap Log = {0}`;
3. `U_c := m(W_c)` is a 2-dimensional subspace of `N`;
4. `m|_{W_c}:W_c -> U_c` is an isomorphism; hence there is a unique linear map
   `phi_c : U_c -> Log` such that

   `L_c = { (u,phi_c(u)) : u in U_c \ {0} }`.

**Argument.** The first statement is exactly `x_1+x_2+x_3=0`, with three distinct nonzero values in the nondegenerate case. Every `x_i` has reduced weight at most 2. If nonzero `w in W_c` lay in `Log`, then `rho(w) <= 2 < d_X`, contradicting the static-distance lower bound for a nonzero logical class. Hence `W_c \cap Log=0`; the rest is linear algebra. Degenerate checks are harmless by the already-reviewed observation “two equal values imply the third is zero”, so they can be deleted from a hardness instance.

Thus the exact hard object is:

> **LINE-SECTION.** Each constraint is a binary line `U={u,v,u+v}` and a linear map `phi:U->L`; choose a partial function `g:N ⇀ L` so that each constraint has a nonzero `w in U` with `g(w)=phi(w)`.

A partial solution may be totalised arbitrarily on unused points, so finite gadget analysis may treat `g` as total on the points of a gadget.

### Why the old clique obstruction is not global

The old `!=_3` wiring identified **entire** 2-dimensional value/syndrome subspaces. Equality of those subspaces is transitive, hence it installed clique closure. LINE-SECTION permits a different operation: two checks can share **one exact atom** `(u,b)` while their other four atoms are unrelated. Distinct binary lines meet in at most one nonzero point, and distinct linear maps on the same binary line agree on at most one nonzero point. This single-atom sharing is the escape hatch.

---

## 2. A conflict-faithful CSS compiler

This section is the realizability result.

### Theorem 2 — block-and-glue compilation — CONJECTURED

Let `I` be a finite LINE-SECTION instance over `N_0` and a finite binary label space `L_0`. Remove duplicate identical constraints. Write each constraint as

`c = ((u_{c1},b_{c1}), (u_{c2},b_{c2}), (u_{c3},b_{c3}))`

with

`u_{c1}+u_{c2}+u_{c3}=0`, `b_{c1}+b_{c2}+b_{c3}=0`,

and the three `u`'s nonzero and distinct.

There is a polynomial-size CSS code with designated weight-4 X-checks, plus auxiliary weight-4 X-checks, such that:

* every designated check has exactly the three intended atoms as its three split values;
* two designated values conflict iff they have the same `u` and different `b`;
* every auxiliary check has a globally private split syndrome, so all auxiliaries can be assigned harmlessly;
* every measured X-check has weight 4;
* `d_X >= 4` always;
* after adding the fixed seed of §2.5, `d_X=4` and `k>=2`.

The construction may have extra logical dimensions: it is **conflict-faithful**, which is all the reduction needs.

### 2.1 Four-qubit block for each abstract constraint

For each abstract constraint `c`, create four fresh physical qubits

`q_{c0}, q_{c1}, q_{c2}, q_{c3}`

and the local X-check

`R_c = q_{c0}+q_{c1}+q_{c2}+q_{c3}`.

Use the three star pairs

`P_{c1}=q_{c0}+q_{c1}`, `P_{c2}=q_{c0}+q_{c2}`, `P_{c3}=q_{c0}+q_{c3}`.

Modulo `R_c`, they satisfy `P_{c1}+P_{c2}+P_{c3}=0`, exactly matching the line relation.

### 2.2 Exact-atom gluing

For each atom `a=(u,b)` occurring in several abstract constraints, connect its occurrences by a tree. For an edge joining occurrence `(c,i)` to `(d,j)`, add the weight-4 X-stabilizer

`G_a(c,d) = P_{ci}+P_{dj}`.

This identifies the two pair values *exactly* in `Q`.

Start with all local rows `R_c`; scan the candidate glue rows and keep a glue row only if it increases the GF(2) row rank. Any discarded glue is already in the final rowspace, so the intended equality still holds. The resulting `H_X` is independent and every row has weight exactly 4.

Because duplicate constraints were removed, two distinct blocks share at most one atom. Hence there is at most one candidate glue between any unordered block pair.

### 2.3 Syndrome matrix

Let `E_c` be a fresh marker basis vector for block `c`. Define the four H_Z column syndromes by

`h_{c0}=E_c`,

`h_{ci}=E_c+u_{ci}` for `i=1,2,3`.

Take `H_Z` to be the coordinate matrix of these columns in `span{E_c} \oplus N_0`.

Every local row is orthogonal to `H_Z` because

`h_{c0}+h_{c1}+h_{c2}+h_{c3}=u_{c1}+u_{c2}+u_{c3}=0`.

Every glue row is orthogonal because each occurrence pair has syndrome `u`:

`(h_{c0}+h_{ci})+(h_{d0}+h_{dj})=u+u=0`.

So `H_X H_Z^T=0` exactly.

### 2.4 Conflict fidelity

Define an auxiliary linear certificate `beta` on physical columns by

`beta(q_{c0})=0`, `beta(q_{ci})=b_{ci}`.

It annihilates all local rows because `b_{c1}+b_{c2}+b_{c3}=0`, and it annihilates every glue row because a glue joins equal atoms. Hence `beta` descends to `Q`.

For a designated split value `x_{ci}=[P_{ci}]`:

`m(x_{ci})=u_{ci}`, `beta(x_{ci})=b_{ci}`.

* Same `(u,b)`: the occurrence-tree glues make the values exactly equal in `Q`.
* Same `u`, different `b`: their difference lies in `Log` (equal syndrome) but has nonzero `beta`, so it is not in `S_X`; therefore it is a nonzero logical difference and the pair is forbidden.
* Different `u`: the syndromes differ, so the pair is not forbidden.

Thus the code's designated-check CSP is **exactly** the abstract LINE-SECTION CSP.

### 2.5 Auxiliary checks have a private option

A retained glue joining `(c,i)` and `(d,j)` has support

`{q_{c0},q_{ci},q_{d0},q_{dj}}`.

Its three split syndromes are

`u`, `E_c+E_d`, `E_c+E_d+u`.

Choose the split represented by `q_{c0}+q_{d0}`, whose syndrome is `E_c+E_d`.

This syndrome cannot equal a designated value's syndrome, because designated values have marker part zero. It cannot equal the private choice of another retained glue, because no two retained glues use the same unordered block pair. Therefore all auxiliary checks can be assigned these private values simultaneously, with zero added conflicts.

This is the missing composition/padding lemma: **wire one exact atom, not one whole `!=_3` subspace.** The wiring is linear-size and does not install a transitive closure of unwanted constraints.

### 2.6 Static X distance

Every physical H_Z column contains exactly one marker `E_c`. Therefore:

* no weight-1 set has zero H_Z syndrome;
* a weight-2 set can have zero marker part only inside one block, but the four columns of a block are distinct because the three `u_{ci}` are distinct and nonzero;
* an odd number of columns can never have zero marker parity block-by-block, so in particular no weight-3 set has zero syndrome.

Hence `ker(H_Z)` contains no nonzero vector of weight `<4`: **`d_X >=4`** even before quotienting by X stabilizers.

Add once, on fresh abstract points, the satisfiable `CONST0` seed from §3.2. Its second point occurs with labels `0,1,2`. The differences between the exact values `(u,0)` and `(u,1)`, and between `(u,0)` and `(u,2)`, have physical representatives of weight 4, lie in `ker(H_Z)`, and have `beta` values `1` and `2`. They are nonzero independent logical classes. Therefore the compiled family has

`d_X=4` and `k>=2`.

### 2.7 Z-distance lower bound for the reduction family

For the specific gadgets below, every local block has at least two of its three atoms occurring elsewhere. For each such repeated atom the corresponding candidate glue row lies in `S_X`, whether or not it was retained as an independent generator.

Every `z in ker(H_X)` must have even parity inside every four-qubit block because of `R_c`, so no odd-weight Z centralizer element exists. A weight-2 centralizer element would have to use two qubits in one block. Two distinct repeated atom-pair stabilizers in the rowspace distinguish all four columns of that block, so no such pair is orthogonal to all of `S_X`. Hence

`d_Z >=4`

for the compiled reduction block.

---

## 3. NP-hard LINE-SECTION at `dim label = 2`

Use `L_0=F_2^2`, written as `{0,1,2,3}` with XOR addition. A line map is specified by its values `(a,b,a+b)` on ordered points `(x,y,x+y)`.

The following finite truth tables are exhaustively checked over all `4^3=64` total assignments by Appendix A.

### 3.1 BOOL/XOR line — NUMERICAL certificate, structural use CONJECTURED

Place four constraints on one line:

`B = {(0,0,0), (0,1,1), (1,0,1), (1,1,0)}`.

The simultaneous satisfying assignments are **exactly**

`(0,0,0), (0,1,1), (1,0,1), (1,1,0)`.

Thus the gadget forces

`x,y,z in {0,1}` and `z=x XOR y`.

Every atom in every one of the four checks appears in another check of the gadget; in fact every check has all three positions repeated.

### 3.2 Constants — NUMERICAL certificate, structural use CONJECTURED

For `CONST0(x)` use

`C0 = {(0,0,0), (0,1,1), (0,2,2), (1,0,1), (1,2,3)}`.

Its simultaneous satisfying assignments are exactly

`(0,0,3), (0,2,1)`.

So its first point is forced to `0`.

For `CONST1(x)` use

`C1 = {(0,0,0), (0,2,2), (1,0,1), (1,1,0), (1,2,3)}`.

Its simultaneous satisfying assignments are exactly

`(1,0,2), (1,2,0)`.

So its first point is forced to `1`.

For every check in either constant gadget, at least two of its three atoms are repeated elsewhere inside the gadget; Appendix A checks the exact counts.

### 3.3 Equality / negation wire

For two Boolean points `p,q`, put a BOOL/XOR gadget on the line

`{p,q,h}` with `h=p+q`.

Then add `CONST0(h)` to enforce `p=q`, or `CONST1(h)` to enforce `p!=q`.

All maps used are linear line maps; no arbitrary 3-list is being smuggled in.

### 3.4 Reduction from 3-SAT — CONJECTURED

Given a 3-CNF formula, give clause `t` two fresh basis vectors `a_t,b_t` and use the three occurrence points

`p_{t1}=a_t`, `p_{t2}=b_t`, `p_{t3}=a_t+b_t`.

They are a binary line by construction.

For every literal occurrence point `p`, attach a private BOOL gadget on `{p,r_p,p+r_p}` with fresh `r_p`; hence `g(p) in {0,1}`.

For each Boolean variable, choose one occurrence as reference. Wire every other occurrence to the reference:

* same literal polarity -> equality wire;
* opposite polarity -> negation wire.

Interpret occurrence value `0` as “this literal is true”.

Finally, for each clause add the single zero-map constraint

`(0,0,0)`

on its occurrence line. It is hit iff at least one of the three occurrence bits is zero, exactly the OR condition for the clause.

All auxiliary points use fresh basis coordinates, so unintended line coincidences are avoided. The number of points and constraints is linear in the formula size.

**Correctness.** A Boolean satisfying assignment sets every literal occurrence to `0` iff that literal is true; the wires and clause check are then satisfied, and all private helpers can be filled from the finite gadget tables. Conversely any section solution can be totalised. The private BOOL gadgets make every occurrence Boolean, the wires give a consistent truth value per variable, and every zero-map clause has a zero occurrence, hence a true literal.

Therefore LINE-SECTION is NP-hard already with `dim L_0=2`. Combining with Theorem 2 gives NP-hardness for **code-realizable** Island-V X-sector instances with weight-4 X checks, `d_X=4`, and `k>=2`.

---

## 4. Exact static `d=3` wrapper

The compiled reduction block has `d_X=4`, `d_Z>=4`. To meet the historical static promise `d=3`, direct-sum one fixed asymmetric HGP block:

`HGP(rep_3, rep_4)`.

Using the standard path repetition parity checks, its exact finite certificate in Appendix A is:

* `n=18`;
* `rank(H_X)=8`, `rank(H_Z)=9`, hence `k=1`;
* every X- and Z-check has weight at most 4;
* no X logical has weight `<4`, and `{0,1,2,3}` is an X logical of weight 4;
* no Z logical has weight `<3`, and `{0,4,8}` is a Z logical of weight 3.

So the spectator has `(d_X,d_Z)=(4,3)`. Direct sum gives the whole static code

`d_X=4`, `d_Z=3`, `d=3` exactly.

A separate exact d=3 hook-CSP check on the spectator finds safe schedules in both sectors; in fact all local orders survive unary filtering for that block. Disjoint composition creates no cross-sector/list coupling with the compiled reduction block.

**Scope wall.** The compiler's H_Z coordinate rows can be high weight (see §5), and this report does not certify the Z-check scheduling sector of that main block. Therefore this is a complete static-distance wrapper and an NP-hard X-sector restriction, but not yet a complete many-one reduction to the full two-sector `Eff-Preserve` problem.

---

## 5. Exact finite verification — NUMERICAL

Running Appendix A produced:

| item | exact output |
|---|---|
| BOOL gadget | exactly 4 solutions: `000,011,101,110` |
| CONST0 | exactly `(0,0,3)`, `(0,2,1)` |
| CONST1 | exactly `(1,0,2)`, `(1,2,0)` |
| satisfiable toy | abstract section = YES |
| satisfiable compiled code | `n=72`, 18 designated checks, 24 retained glues, `rank H_X=42`, `rank H_Z=25`, `k=5` |
| same code | max X-check weight `4`, `d_X=4`, `d_Z>=4`, designated conflict mismatches `0` |
| unsatisfiable toy `(x∨x∨x) ∧ (¬x∨¬x∨¬x)` | abstract section = NO |
| unsatisfiable compiled code | `n=304`, 76 designated checks, 127 retained glues, `rank H_X=203`, `rank H_Z=93`, `k=8` |
| same code | max X-check weight `4`, `d_X=4`, `d_Z>=4`, designated conflict mismatches `0` |
| HGP spectator | `[[18,1]]`, `(d_X,d_Z)=(4,3)`, max check weight 4 |

The compiler deliberately does **not** bound the opposite-sector generator weight: the SAT toy has max H_Z row weight 18; the UNSAT toy has max H_Z row weight 98. This is not a hidden defect; it is the exact remaining boundary for the stronger “both sectors bounded” version.

Verifier SHA-256:

`0fd00074ecaa533a21a7aa2096969a5c3b001953ecf46e610fe42a6462147be9`

---

## 6. Consequence for `CIRCDIST.cplx.fixed-d` and weight-6 repricing

### Fixed-d consequence — CONJECTURED

The Island-V open question is no longer “matching or hard?”: **hard**. Realizability adds the binary-line/local-linearity condition, but no further global Hall/exchange collapse survives. The block-and-glue compiler is the missing realizability/composition mechanism.

What this buys immediately:

1. fixed `d=3` **X-sector** NP-hardness with every X-check of weight 4, exact static `d_X=4`, and `k>=2`;
2. a fixed direct-sum wrapper giving exact whole-code static distance `d=3`;
3. a polynomial, edge-local wiring lemma with no clique closure.

What is still missing for the full node is one orthogonal-sector statement: choose/engineer the compiler's Z-check generating set and schedules so that its Z-sector is always YES. That is now the only barrier in this route; the list-realizability question itself is closed by the construction above.

Under the pre-committed pricing this is the **(a) reading** and supports moving the fixed-`d` NP-completeness route to roughly `P -> 0.7`, while not labelling the final theorem complete.

### Weight-6

* **Moot for Island-V hardness / the pre-committed route.** Weight-4 X checks already realize NP-hard section structure; there is no need to go to weight 6 merely to get a hard relation or nonlocal wiring.
* **Not moot for a stronger two-sided bounded-weight theorem.** The present H_Z rows grow with the incidence multiplicity. If the intended final restriction is “every X and every Z stabilizer generator has weight <=4 (or <=6)”, then a bounded-opposite-sector compiler remains open. Weight-6 set-disjointness is therefore best repriced as an optional route to *two-sided boundedness*, not as the primary source of hardness.

---

## 7. Precise frontier after this session

**Closed at argument level (CONJECTURED):**

* nondegenerate realizable lists are graphs of linear maps on binary lines;
* `dim Log >=2` is enough for a genuine hard fragment;
* arbitrary finite line-map conflict patterns are conflict-faithfully compilable to weight-4-X CSS codes using exact-atom glues;
* the glues have private choices and preserve `d_X>=4`;
* the explicit 3-SAT gadget family has `d_X=4`, `d_Z>=4`, `k>=2`;
* direct sum gives exact static `d=3`.

**Still open:**

* a uniform proof that the compiler's **Z-check scheduling sector** is always YES, or a modified compiler making that sector trivially safe;
* the stronger theorem with **both** X- and Z-generator weights bounded by 4 (or 6).

That is the exact wall. It is no longer a realizability-vs-matching wall.

---

## Appendix A — self-contained exact verifier

The following is the complete verifier used for every NUMERICAL statement above.

```python
#!/usr/bin/env python3
"""Exact finite checks for the Island-V line-section hardness construction.

Only Python stdlib is used.  Labels are F_2^2 elements encoded as 0..3.
Vectors/rows are Python integers (bitsets), so all arithmetic is exact GF(2).
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product, combinations, permutations
from collections import defaultdict, Counter

BOOL = [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
CONST0 = [(0,0,0),(0,1,1),(0,2,2),(1,0,1),(1,2,3)]
CONST1 = [(0,0,0),(0,2,2),(1,0,1),(1,1,0),(1,2,3)]


def gf2_basis(rows):
    b = {}
    for r in rows:
        x = r
        while x:
            p = x.bit_length()-1
            if p in b:
                x ^= b[p]
            else:
                b[p] = x
                for q in list(b):
                    if q != p and ((b[q] >> p) & 1):
                        b[q] ^= x
                break
    return b


def gf2_rank(rows):
    return len(gf2_basis(rows))


def in_span(x, basis_or_rows):
    b = basis_or_rows if isinstance(basis_or_rows, dict) else gf2_basis(basis_or_rows)
    while x:
        p = x.bit_length()-1
        if p not in b:
            return False
        x ^= b[p]
    return True


def gadget_solutions(maps):
    return [a for a in product(range(4), repeat=3)
            if all(any(a[i] == phi[i] for i in range(3)) for phi in maps)]


def shared_positions(maps):
    out = []
    for i, phi in enumerate(maps):
        s = set()
        for p in range(3):
            if any(j != i and maps[j][p] == phi[p] for j in range(len(maps))):
                s.add(p)
        out.append(s)
    return out


@dataclass(frozen=True)
class Check:
    name: str
    u: tuple[int,int,int]   # nonzero points, u1+u2=u3
    b: tuple[int,int,int]   # labels, b1+b2=b3
    kind: str


class Builder:
    def __init__(self):
        self.dim = 0
        self.checks: list[Check] = []
        self.occ = []

    def fresh(self):
        v = 1 << self.dim
        self.dim += 1
        return v

    def add_check(self, name, u, b, kind):
        assert u[0] ^ u[1] == u[2]
        assert all(u) and len(set(u)) == 3
        assert b[0] ^ b[1] == b[2]
        self.checks.append(Check(name, tuple(u), tuple(b), kind))

    def add_maps(self, p, q, maps, name, kind):
        r = p ^ q
        assert p and q and r and len({p,q,r}) == 3
        for i, phi in enumerate(maps):
            self.add_check(f"{name}:{i}", (p,q,r), phi, kind)

    def add_bool(self, p, name):
        r = self.fresh()
        self.add_maps(p, r, BOOL, name, "BOOL")

    def add_const(self, p, value, name):
        r = self.fresh()
        self.add_maps(p, r, CONST0 if value == 0 else CONST1, name, f"CONST{value}")

    def add_wire(self, p, q, flip, name):
        h = p ^ q
        self.add_maps(p, q, BOOL, name+":xor", "WIRE_BOOL")
        self.add_const(h, 1 if flip else 0, name+":const")

    def add_seed(self):
        # Satisfiable fixed component.  Its second point occurs with labels 0,1,2,
        # certifying two independent logical directions after compilation.
        x, y = self.fresh(), self.fresh()
        self.add_maps(x, y, CONST0, "seed", "SEED_CONST0")


def build_formula(clauses):
    """clauses: 3-tuples of (variable_name, positive_bool)."""
    B = Builder()
    by_var = defaultdict(list)
    for t, clause in enumerate(clauses):
        a, b = B.fresh(), B.fresh()
        pts = (a, b, a ^ b)
        for j, (var, positive) in enumerate(clause):
            by_var[var].append((pts[j], positive, t, j))
            B.occ.append((var, positive, t, j, pts[j]))
            B.add_bool(pts[j], f"bool_{t}_{j}")
        B.add_check(f"clause_{t}", pts, (0,0,0), "CLAUSE")
    for var, occs in by_var.items():
        ref = occs[0]
        for j, oc in enumerate(occs[1:], 1):
            B.add_wire(ref[0], oc[0], ref[1] != oc[1], f"wire_{var}_{j}")
    B.add_seed()
    return B


def abstract_solution(checks):
    """Exact backtracking for partial-section hitting."""
    cover = defaultdict(set)
    cand = []
    for i,c in enumerate(checks):
        opts = list(zip(c.u, c.b))
        cand.append(opts)
        for a in opts:
            cover[a].add(i)
    all_i = set(range(len(checks)))

    def rec(covered, assign):
        if len(covered) == len(checks):
            return dict(assign)
        best_opts = None
        for i in all_i - covered:
            opts = [a for a in cand[i] if a[0] not in assign or assign[a[0]] == a[1]]
            if not opts:
                return None
            if best_opts is None or len(opts) < len(best_opts):
                best_opts = opts
                if len(opts) == 1:
                    break
        best_opts.sort(key=lambda a: -len(cover[a] - covered))
        for u,b in best_opts:
            new = u not in assign
            if new:
                assign[u] = b
            ans = rec(covered | cover[(u,b)], assign)
            if ans is not None:
                return ans
            if new:
                del assign[u]
        return None
    return rec(set(), {})


@dataclass
class Code:
    n: int
    HX: list[int]
    HZ: list[int]
    local: list[int]
    glue: list[int]
    all_glues: list[tuple]
    glue_edges: list[tuple]
    hz_cols: list[int]
    beta_cols: list[int]
    atom_occ: dict
    M: int
    domain_dim: int


def compile_code(B: Builder):
    """Block-and-glue compiler.  H_X is returned independent, all rows weight 4."""
    M = len(B.checks)
    n = 4*M
    local = []
    atom_occ = defaultdict(list)
    beta_cols = [0]*n

    for cidx,c in enumerate(B.checks):
        q0 = 4*cidx
        local.append(sum(1 << (q0+j) for j in range(4)))
        for pos,(u,b) in enumerate(zip(c.u,c.b), start=1):
            atom_occ[(u,b)].append((cidx,pos))
            beta_cols[q0+pos] = b

    HX = list(local)
    basis = gf2_basis(HX)
    glue = []
    glue_edges = []
    all_glues = []
    used_block_pairs = set()

    for atom, occs in atom_occ.items():
        if len(occs) <= 1:
            continue
        root = occs[0]
        for other in occs[1:]:
            c,p = root
            d,q = other
            assert c != d
            block_pair = tuple(sorted((c,d)))
            # Distinct line maps share at most one atom; exact duplicate constraints are absent.
            assert block_pair not in used_block_pairs
            used_block_pairs.add(block_pair)
            row = (1 << (4*c)) | (1 << (4*c+p)) | (1 << (4*d)) | (1 << (4*d+q))
            assert row.bit_count() == 4
            e = (atom, root, other, row)
            all_glues.append(e)
            if not in_span(row, basis):
                HX.append(row)
                glue.append(row)
                glue_edges.append(e)
                basis = gf2_basis(HX)

    # Every omitted glue is already a stabilizer consequence, so equal atoms stay equal in Q.
    assert all(in_span(e[3], basis) for e in all_glues)
    assert gf2_rank(HX) == len(HX)

    # Syndrome columns h_{c,0}=e_c, h_{c,i}=e_c+u_{c,i} in F_2^M \oplus N.
    hz_cols = [0]*n
    for cidx,c in enumerate(B.checks):
        marker = 1 << (B.dim+cidx)
        q0 = 4*cidx
        hz_cols[q0] = marker
        for pos,u in enumerate(c.u, start=1):
            hz_cols[q0+pos] = marker | u

    HZ = []
    for bit in range(B.dim+M):
        row = 0
        for q,h in enumerate(hz_cols):
            if (h >> bit) & 1:
                row |= 1 << q
        if row:
            HZ.append(row)

    return Code(n,HX,HZ,local,glue,all_glues,glue_edges,hz_cols,beta_cols,dict(atom_occ),M,B.dim)


def beta(v, beta_cols):
    out = 0
    while v:
        l = v & -v
        q = l.bit_length()-1
        out ^= beta_cols[q]
        v ^= l
    return out


def verify_local_conflicts(P: Code, B: Builder):
    sx = gf2_basis(P.HX)
    vals = []
    for cidx,c in enumerate(B.checks):
        for pos,(u,b) in enumerate(zip(c.u,c.b), start=1):
            v = (1 << (4*cidx)) | (1 << (4*cidx+pos))
            s = P.hz_cols[4*cidx] ^ P.hz_cols[4*cidx+pos]
            vals.append((cidx,pos,u,b,v,s))
    mismatch = 0
    for i in range(len(vals)):
        c,p,u,b,v,s = vals[i]
        for j in range(i+1,len(vals)):
            d,q,u2,b2,v2,s2 = vals[j]
            if c == d:
                continue
            actual = (s == s2 and not in_span(v ^ v2, sx))
            expected = (u == u2 and b != b2)
            mismatch += (actual != expected)
    return mismatch


def find_beta_witness(P: Code, target):
    by_u = defaultdict(dict)
    for (u,b), occs in P.atom_occ.items():
        by_u[u][b] = occs
    sx = gf2_basis(P.HX)
    for u, lab in by_u.items():
        for b1,b2 in combinations(lab, 2):
            if (b1 ^ b2) != target:
                continue
            c,p = lab[b1][0]
            d,q = lab[b2][0]
            v = (1 << (4*c)) | (1 << (4*c+p)) | (1 << (4*d)) | (1 << (4*d+q))
            if v.bit_count() == 4:
                assert all(((v & z).bit_count() & 1) == 0 for z in P.HZ)
                assert not in_span(v, sx)
                assert beta(v, P.beta_cols) == target
                return v
    return None


def main_code_certificate(P: Code, B: Builder):
    # CSS and weights.
    css = all(((x & z).bit_count() & 1) == 0 for x in P.HX for z in P.HZ)
    assert css and max(r.bit_count() for r in P.HX) == 4

    # d_X >= 4: every syndrome column has exactly one block marker; within a block
    # all four columns are distinct.  So no 1/2/3 columns sum to zero.
    marker_mask = ((1 << P.M)-1) << P.domain_dim
    assert all((h & marker_mask).bit_count() == 1 for h in P.hz_cols)
    for c in range(P.M):
        assert len(set(P.hz_cols[4*c:4*c+4])) == 4

    # Seed supplies two independent weight-4 logicals, hence d_X=4 and k>=2.
    w1 = find_beta_witness(P,1)
    w2 = find_beta_witness(P,2)
    assert w1 is not None and w2 is not None

    # d_Z >= 4.  Local row forces even weight in each block, excluding odd weights.
    # Weight 2 would lie in one block; columns of H_X must then coincide.  They do not.
    hx_cols = []
    for q in range(P.n):
        col = 0
        for i,row in enumerate(P.HX):
            if (row >> q) & 1:
                col |= 1 << i
        hx_cols.append(col)
    assert all(col != 0 for col in hx_cols)
    for c in range(P.M):
        assert len(set(hx_cols[4*c:4*c+4])) == 4

    # Conflict table on designated local checks is exactly the abstract atom rule.
    mism = verify_local_conflicts(P,B)
    assert mism == 0

    # Each retained glue has a private selected split syndrome e_c+e_d.
    priv = []
    for atom,(c,p),(d,q),row in P.glue_edges:
        s = P.hz_cols[4*c] ^ P.hz_cols[4*d]
        priv.append(s)
        assert (s & marker_mask).bit_count() == 2
    assert len(priv) == len(set(priv))

    k = P.n - gf2_rank(P.HX) - gf2_rank(P.HZ)
    assert k >= 2
    return {
        "n": P.n,
        "local_checks": P.M,
        "retained_glues": len(P.glue),
        "all_atom_equalities": len(P.all_glues),
        "rank_HX": gf2_rank(P.HX),
        "rank_HZ": gf2_rank(P.HZ),
        "k": k,
        "max_w_HX": max(r.bit_count() for r in P.HX),
        "max_w_HZ": max(r.bit_count() for r in P.HZ),
        "dX": 4,
        "dZ_lower": 4,
        "local_conflict_mismatches": mism,
        "private_glue_syndromes": len(priv),
        "private_glue_unique": len(set(priv)),
    }


def path_rep(n):
    return [(1 << i) | (1 << (i+1)) for i in range(n-1)]


def hgp_rep(n1,n2):
    H1, H2 = path_rep(n1), path_rep(n2)
    r1, r2 = n1-1, n2-1
    left = n1*n2
    N = left + r1*r2
    HX=[]
    for a in range(r1):
        for j in range(n2):
            row=0
            for i in range(n1):
                if (H1[a]>>i)&1:
                    row |= 1 << (i*n2+j)
            for b in range(r2):
                if (H2[b]>>j)&1:
                    row |= 1 << (left+a*r2+b)
            HX.append(row)
    HZ=[]
    for i in range(n1):
        for b in range(r2):
            row=0
            for j in range(n2):
                if (H2[b]>>j)&1:
                    row |= 1 << (i*n2+j)
            for a in range(r1):
                if (H1[a]>>i)&1:
                    row |= 1 << (left+a*r2+b)
            HZ.append(row)
    return N,HX,HZ


def low_logical(Hother,Srows,n,maxw):
    sb=gf2_basis(Srows)
    for w in range(1,maxw+1):
        for comb in combinations(range(n),w):
            v=sum(1<<i for i in comb)
            if all(((v&r).bit_count()&1)==0 for r in Hother) and not in_span(v,sb):
                return v
    return None


def support(v):
    return [i for i in range(v.bit_length()) if (v>>i)&1]



def sector_schedule(Hchecks,Hopp,n):
    """Exact d=3 hook-CSP solve for one CSS sector.

    Fault columns are data singletons and proper suffix hooks.  A local order is
    kept iff no <=2-column logical uses only that check plus data; pair tables
    then test one hook from each of two checks.
    """
    sb=gf2_basis(Hchecks)
    def is_logical(v):
        return v != 0 and all(((v&r).bit_count()&1)==0 for r in Hopp) and not in_span(v,sb)
    data=[1<<q for q in range(n)]
    domains=[]
    for row in Hchecks:
        supp=[q for q in range(n) if (row>>q)&1]
        good=[]
        for order in permutations(supp):
            hooks=[sum(1<<q for q in order[i:]) for i in range(1,len(order))]
            bad=False
            for h in hooks:
                if is_logical(h) or any(is_logical(h^e) for e in data):
                    bad=True; break
            if not bad and any(is_logical(a^b) for a,b in combinations(hooks,2)):
                bad=True
            if not bad:
                good.append((order,hooks))
        domains.append(good)

    compat={}
    for i in range(len(Hchecks)):
        for j in range(i+1,len(Hchecks)):
            compat[(i,j)]=[[not any(is_logical(a^b) for a in hi for b in hj)
                            for _,hj in domains[j]]
                           for _,hi in domains[i]]
    vars_=sorted(range(len(Hchecks)),key=lambda i:len(domains[i]))
    assign={}
    def rec(t):
        if t==len(vars_): return dict(assign)
        i=vars_[t]
        for ai in range(len(domains[i])):
            ok=True
            for j,aj in assign.items():
                if i<j:
                    ok=compat[(i,j)][ai][aj]
                else:
                    ok=compat[(j,i)][aj][ai]
                if not ok: break
            if ok:
                assign[i]=ai
                ans=rec(t+1)
                if ans is not None: return ans
                del assign[i]
        return None
    return [len(d) for d in domains], rec(0)

def spectator_certificate():
    # HGP(rep_3,rep_4): [[18,1]], d_X=4, d_Z=3; all checks <=4.
    n,HX,HZ = hgp_rep(3,4)
    assert all(((x&z).bit_count()&1)==0 for x in HX for z in HZ)
    k=n-gf2_rank(HX)-gf2_rank(HZ)
    xlt4=low_logical(HZ,HX,n,3)
    x4=low_logical(HZ,HX,n,4)
    zlt3=low_logical(HX,HZ,n,2)
    z3=low_logical(HX,HZ,n,3)
    assert k==1 and xlt4 is None and x4 is not None and x4.bit_count()==4
    assert zlt3 is None and z3 is not None and z3.bit_count()==3
    x_domains,x_sched=sector_schedule(HX,HZ,n)
    z_domains,z_sched=sector_schedule(HZ,HX,n)
    assert x_sched is not None and z_sched is not None
    return {
        "n":n,"rank_HX":gf2_rank(HX),"rank_HZ":gf2_rank(HZ),"k":k,
        "max_w_HX":max(r.bit_count() for r in HX),"max_w_HZ":max(r.bit_count() for r in HZ),
        "dX":4,"dZ":3,"x_logical":support(x4),"z_logical":support(z3),
        "X_safe_order_counts":x_domains,"Z_safe_order_counts":z_domains,
        "X_schedule_exists":True,"Z_schedule_exists":True
    }


def main():
    print("GADGET CERTIFICATES")
    print("BOOL  :", gadget_solutions(BOOL))
    print("CONST0:", gadget_solutions(CONST0))
    print("CONST1:", gadget_solutions(CONST1))
    print("BOOL shared positions per check:", [sorted(s) for s in shared_positions(BOOL)])
    print("CONST0 shared-position counts:", [len(s) for s in shared_positions(CONST0)])
    print("CONST1 shared-position counts:", [len(s) for s in shared_positions(CONST1)])
    assert gadget_solutions(BOOL) == [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
    assert gadget_solutions(CONST0) == [(0,0,3),(0,2,1)]
    assert gadget_solutions(CONST1) == [(1,0,2),(1,2,0)]
    assert min(map(len,shared_positions(BOOL))) >= 2
    assert min(map(len,shared_positions(CONST0))) >= 2
    assert min(map(len,shared_positions(CONST1))) >= 2

    # Satisfiable and unsatisfiable tiny formula tests.
    sat = [[("x",True),("y",True),("z",True)]]
    unsat = [
        [("x",True),("x",True),("x",True)],
        [("x",False),("x",False),("x",False)],
    ]
    for name,F in [("SAT-toy",sat),("UNSAT-toy",unsat)]:
        B=build_formula(F)
        sol=abstract_solution(B.checks)
        P=compile_code(B)
        cert=main_code_certificate(P,B)
        rep=Counter((u,b) for c in B.checks for u,b in zip(c.u,c.b))
        per_check=[sum(rep[(u,b)]>=2 for u,b in zip(c.u,c.b)) for c in B.checks]
        assert min(per_check)>=2
        print(name, "abstract_sat=", sol is not None, "domain_dim=",B.dim, "checks=",len(B.checks))
        print(name, "code=", cert)
    assert abstract_solution(build_formula(sat).checks) is not None
    assert abstract_solution(build_formula(unsat).checks) is None

    print("SPECTATOR", spectator_certificate())
    print("ALL ASSERTIONS PASSED")

if __name__ == "__main__":
    main()
```
