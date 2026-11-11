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
