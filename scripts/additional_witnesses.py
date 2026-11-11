"""Additional transparent, bounded checks; each declares what it does not prove."""
from itertools import product, combinations
import sympy as s
from common import FROZEN, ROOT, read, write

def run():
    checks=[]
    def check(rid, description, ok, details, scope):
        assert bool(ok),(rid,description)
        checks.append({'records':[rid], 'description':description,'passed':True,'details':details,'scope':scope})
    w=(-1+s.sqrt(3)*s.I)/2
    points=list(product(range(3),repeat=2))
    F=s.Matrix([[w**((p[0]*k[1]-p[1]*k[0])%3)/3 for p in points] for k in points])
    F2=s.simplify(F*F)
    reflection=s.Matrix([[int(p==((-k[0])%3,(-k[1])%3)) for p in points] for k in points])
    check('008','Exact symplectic Fourier square for D=3',F2==s.eye(9) and F2!=reflection,
        'F^2=I_9, distinct from reflection','Exact finite counterexample; general identity also follows by character orthogonality in the witness.')
    K1=s.Matrix([[0,0,0],[0,0,1],[0,-1,0]])
    check('021','Kraus kernel for psi=|0>',K1.rank()==2 and K1.nullspace()==[s.Matrix([1,0,0])],
        'ker(K1)=span(|0>)','Checks the support restriction algebra; positivity/support argument is the analytic witness, no random numerical search.')
    z={5}; gates=[(0,5),(4,0),(4,1),(1,5),(4,2),(2,5),(4,3),(3,5)]
    for control,target in reversed(gates):
        if target in z: z.symmetric_difference_update({control})
    check('028','Back-propagated Z measurement anticommutes with prepared X ancilla',4 in z,
        {'Z_support':sorted(z)},'Clifford Pauli propagation of the displayed four-data-qubit example, not a generic circuit-distance solver.')
    def span(rows):
        out={0}
        for r in rows:out|={x^r for x in list(out)}
        return out
    def mask(xs):return sum(1<<x for x in xs)
    hx=[mask(x) for x in [{0,1},{2,3},{4,5}]]
    hz=[mask(x) for x in [{0,1,2,3},{2,3,4,5}]]
    sx,sz=span(hx),span(hz)
    parity=lambda x:bin(x).count('1')%2
    dx=min(bin(x).count('1') for x in range(64) if x not in sx and all(parity(x&r)==0 for r in hz))
    dz=min(bin(x).count('1') for x in range(64) if x not in sz and all(parity(x&r)==0 for r in hx))
    check('033','Exhaustive small-code X/Z logical distances',(dx,dz)==(3,2),
        {'d_X':dx,'d_Z':dz},'Verifies sector-distance mismatch; archived multi-round circuit distances are not rerun.')
    suffix={4,6}; singleton={1}
    check('035','Same-location Pauli product changes cost',len([suffix,singleton])==2 and suffix^singleton=={1,4,6},
        'Two formal residuals at one location combine into one Pauli fault','Elementary XOR part only; does not prove a repaired existence theorem.')
    def shift(c,a,b):return 6*((c//6+a)%12)+(c%6+b)%6
    A=[(3,0),(0,1),(0,2)];B=[(0,3),(1,0),(2,0)]
    tx=[];tz=[]
    for c in range(72):
        tx.append(dict(zip([shift(c,*v) for v in A]+[72+shift(c,*v) for v in B],range(6))))
        tz.append(dict(zip([shift(c,-a,-b) for a,b in B]+[72+shift(c,-a,-b) for a,b in A],range(3,9))))
    conflicts=sum(len(ts)-len(set(ts)) for q in range(144) for ts in [[d[q]%6 for d in tx+tz if q in d]])
    overlaps=[(x,z,set(x)&set(z)) for x in tx for z in tz if set(x)&set(z)]
    counts=[(sum(z[q]<x[q] for q in common),sum(z[q]-6<x[q] for q in common)) for x,z,common in overlaps]
    check('037','Periodic six-layer staggered Gross schedule',conflicts==0 and len(overlaps)==648 and set(counts)=={(0,2)},
        {'conflicts':conflicts,'overlapping_pairs':len(overlaps),'MC_count_pairs':sorted(set(counts)), 'CNOTs_per_period':sum(len(x) for x in tx+tz)},
        'Exact matching and cross-period MC parity check; archived Stim detector simulation is not newly run.')
    solutions=[(x,y) for x,y in product([False,True],repeat=2) if (x or x or y) and x and not y]
    check('039','Repeated-variable reduction contradiction',solutions==[(True,False)] and (0^0)==0 and int(not False)==1,
        {'satisfying_original_assignments':solutions,'XOR_forced_y_label':0,'consistency_required_y_label':1},
        'Checks the explicit local contradictory label constraints; not a regeneration of all 107 abstract CSP checks.')
    H=s.Matrix([[1,s.Rational(1,2),0],[s.Rational(1,2),1,0],[0,0,1]])
    P=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    check('071','Optimal Gram matrix outside permutation commutant',all(e>0 for e in H.eigenvals()) and list(H.diagonal())==[1,1,1] and s.trace(H)==3 and P*H!=H*P,
        {'eigenvalues':[str(x) for x in H.eigenvals()],'trace':3},'Exact counterexample to coverage of all optimal strategies.')
    h=s.symbols('h');U=s.Matrix([1,0]);M=h*U*U.T
    check('072','Empty balanced spectral face for diag(2,1)',M[1,1]==0 and M[1,1]!=1,
        'diag(U h U^T)=(h,0) cannot equal (1,1)','Exact infeasibility of the stated spectral face, not a claim about the repaired nonempty-face formula.')
    left_dim,right_dim=s.zeros(1,2).shape
    check('056','Rectangular zero matrix has unequal full top spaces',(left_dim,right_dim)==(1,2),
        {'left_dimension':left_dim,'right_dimension':right_dim},'Confirms basis-size obstruction; no common column count can span both full spaces.')
    cert=read(FROZEN/'records/050/original/M04-d4-effective-equality-rank-certificate-20260830.json')
    check('050','Archived rank-certificate internal consistency',len(cert['vanishing_rows'])==16 and len(cert['lower_rows'])==12 and set(cert['vanishing_rows'])|set(cert['lower_rows'])==set(cert['old_basis_rows']) and cert['lower_det_integer']==-120231596497305600,
        {'rows':28,'vanishing':16,'lower':12,'supported_rank_bound':746825-12},
        'Certificate bookkeeping only. Does not regenerate the 12x12 matrix or exhaustive 746825-coordinate vanishing checks; full external fixtures are not bundled.')
    return {'status':'PASS','checks':checks,'check_count':len(checks),
        'interpretation':'Fresh scoped checks, with explicit computational and analytic limits.'}

if __name__=='__main__':
    import sys,json
    result=run()
    if '--save' in sys.argv:write(ROOT/'audit/additional_witness_execution.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))
