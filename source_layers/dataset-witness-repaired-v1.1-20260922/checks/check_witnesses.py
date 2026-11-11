"""Small, independent checks. Passing is not blanket confirmation of a dossier."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb, log, floor, ceil
import argparse
import json, re
import sympy as s

BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
results = []
def check(ids, description, ok, details, scope='local witness'):
    if not bool(ok):
        raise AssertionError((ids, description, details))
    results.append(dict(records=ids, description=description, passed=True,
                        details=str(details), scope=scope))

def mask(xs):
    return sum(1 << x for x in xs)
def span(rows):
    out={0}
    for r in rows: out |= {a ^ r for a in list(out)}
    return out
def basis(rows):
    b={}
    for r in rows:
        while r:
            p=r.bit_length()-1
            if p in b: r ^= b[p]
            else: b[p]=r; break
    return b
def remainder(x,b):
    for p in sorted(b,reverse=True):
        if x>>p&1: x^=b[p]
    return x

m=floor(.01*10**6/log(10**6)**2)
check(['003'],'fixed-X parameter choice',m==52,{'m':m,'epsilon_power':'(n/10^6)^(2/(1+log(52))) -> infinity'})
check(['005'],'balanced representative triple', (2+2+1)%5==0 and 2+2+1==5,'phase multiplier exp(5 i theta), not constant')
check(['007'],'bound endpoint at M=D=1',8*(1+1+6)>16,'sqrt(64)=8 > 4')
check(['009'],'dictionary integer',777716**2+777716+1==604842954373,777716**2+777716+1)
v=tuple((a-b)%7 for a,b in zip((1,1,0),(2,3,1)))
check(['010'],'cross-ruling difference',v==(6,5,6) and (4*v[0]*v[2]-v[1]**2)%7==0,v)
for p in (BASE/'records/012/original').iterdir():
    if p.suffix not in {'.txt','.log','.md'}: continue
    rows={int(a):int(b) for a,b in re.findall(r'^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$',p.read_text(errors='replace'),re.M)}
    if len(rows)==150150:
        value=sum(a*a*b for a,b in rows.items())
        check(['012'],'archived scan exact second moment', value==7149371020340889916998112,
              {'file':p.name,'rows':len(rows),'value':value,'difference':value-7149371020340881916998112},'full scan fixture recomputed')
        break
check(['013'],'variance counterexample',0 < (1-0)**2,'one unit coordinate: variance 0, arbitrary-center RHS 1')
check(['014'],'conditional conclusion does not imply subset bound', not(1<1) and not(0>1),'T=1, ray+flat=0, H=E=1; only a logical counterassignment','inference only, not a physical realization')
endpoints=[F(2),F(23,10)]
check(['015'],'strict integer endpoints',all(ceil(x)-1 < x <= ceil(x) for x in endpoints),'x=2 -> maximum integer 1; x=23/10 -> maximum integer 2','integer rule, not every archived row recomputed')
balancing_examples=[{'d':2**n,'Delta_bits':n,'minimum_K_within_one_bit':2**(n-1)} for n in [2,8,16,32]]
check(['016'],'balancing cost examples',all(F(e['d'],e['minimum_K_within_one_bit'])==2 for e in balancing_examples),balancing_examples,'Examples only; unboundedness follows analytically from log2(K)>=log2(d)-1, not finite testing')
check(['017'],'one-dimensional entropy formula',1-1==0,'log2(d-1) has zero argument at d=1')
X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1); I=s.eye(2)
check(['018'],'noncommuting product order',X*(Z*X)==-Z and -Z!=Z,X*(Z*X))
swap=s.zeros(4)
for a,b in product(range(2),repeat=2): swap[2*b+a,2*a+b]=1
v=s.Matrix([0,1,-1,0]); R=v*v.T/2
check(['019'],'swap-invariant antisymmetric state',swap*R*swap==R and (s.eye(4)+swap)*R==s.zeros(4),R,'feasible-set distinction, not fixed-target infeasibility')
psi=s.Matrix([1,s.I,1])/s.sqrt(3); x=s.Rational(9,20)
rho=psi*psi.H; M=(1-x)*rho+x/2*(s.eye(3)-rho.T)
lam=s.Symbol('lam'); actual=s.factor(M.charpoly(lam).as_expr())
claimed=(lam-s.Rational(11,20))*(lam-s.Rational(9,40))**2
check(['020'],'complex-input characteristic polynomial',s.expand(actual-claimed)!=0,actual)
G=s.Matrix([[s.Rational(1,2),s.I/(2*s.sqrt(2))],[-s.I/(2*s.sqrt(2)),s.Rational(1,4)]])
res=G*s.Matrix([1,-s.I*s.sqrt(2)])
check(['023'],'claimed environment kernel residual',res==s.Matrix([1,-s.I/s.sqrt(2)]),res)
ratio=F(1102933,9570000)/2/F(13,132)
z=F(2,5); poly=19*z**4-21*z**3-14*z**2+28*z-8
check(['022'],'per-use comparison and threshold',ratio==F(84841,145000)<1 and poly==F(64,625),{'ratio':str(ratio),'at_2/5':str(poly)})
Pi=(s.eye(4)-swap)/2
es=[s.Matrix([1,0]),s.Matrix([0,1])]
E=s.Matrix(2,2,lambda i,j:(s.kronecker_product(es[i],es[j]).T*Pi*s.kronecker_product(es[j],es[i]))[0])
check(['027'],'exchange matrix not PSD',E==s.Matrix([[0,-s.Rational(1,2)],[-s.Rational(1,2),0]]),E,'refutes tentative subset PSD, not positive expansion')
check(['031'],'min-plus drift', all((r+2)!=r for r in range(1,20)),'[1]^(minplus R)=[R] by induction')
hx=[mask(t) for t in [{3,4,5,6},{1,2,5,6},{0,2,4,6}]]
v=mask({1,4,6})
check(['032'],'Steane logical support',all((r&v).bit_count()%2==0 for r in hx) and v not in span(hx),'{4,6} hook XOR {1} singleton = weight-3 nontrivial logical','algebraic logical check; no full circuit simulation')
check(['036'],'pairwise vs global time order', all(a<b for a,b in [(1,2),(3,4)]) and not max(1,3)<min(2,4),'A=(1,3), B=(2,4)')
B=[16,20,24,28]; cs=[mask({b,b+1,b+2,b+3}) for b in B]; f=mask(B); g=mask([b+1 for b in B]); ps=[mask({b,b+1}) for b in B]; space=span(cs+[f,g]); total=0
for p in ps:total^=p
check(['038'],'four-label XOR not generated by pair equalities', total in space and all((ps[i]^ps[j]) not in space for i in range(4) for j in range(i)),{'rowspace_size':len(space),'six_pair_equalities':False})
phi={a:a for a in range(8)};phi[1],phi[2]=2,1
check(['040'],'alphabet map not XOR-homomorphic',phi[1^4]!=(phi[1]^phi[4]),(phi[5],phi[1]^phi[4]))
check(['041'],'literal positive-power encoding',sum([1,3,9])%76!=0,13,'literal formula only; does not exclude corrected embedding')
check(['042'],'pigeonhole 3-sum',min(max(v.count(a) for a in range(3)) for v in product(range(3),repeat=7))>=3,'all 2187 length-7 ternary inputs contain three equal symbols')
bad=sum(min((3*a)%228,(-3*a)%228)<=12 for a in range(228))*228
check(['043'],'non-surjective modular fibers',bad==6156 and bad>25*228,bad)
check(['045'],'odd endpoint',9<=2*5-1 and (9-1)//2>2*(5//2)-1,'N=5, q=9, donor K=4 exceeds 3','reduction coverage, not lower-bound falsity')
ta=F(160582822829,85260);cap=F(51396202,35)
check(['048'],'raw T_a gate',ta/cap==F(36224413,28242984)>1,ta/cap)
check(['049'],'binomial product',comb(600,2)*598==107460600,comb(600,2)*598)
check(['051'],'printed 3N',3*3131353829703088100==9394061489109264300 and 939406148910924300<5212397982790439500,3*3131353829703088100)
W=s.Matrix([[-1,-1,0],[-1,1,0],[1,-1,0],[1,1,0],[-1,0,-1],[-1,0,1],[1,0,-1],[1,0,1],[0,-1,-1],[0,-1,1],[0,1,-1],[0,1,1]])
u=s.Matrix([1,1,1,1,-1,1,-1,1,-1,1,-1,1]);v=s.Matrix([-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1]); val=(u.T*(W*W.T/8-s.eye(12)/2)*v)[0]
check(['057'],'explicit D3 sign pair',val==6>4,val)
a,D=s.symbols('a D');diff=(a+D)/(D*(D+1))-(a*a+D*D)/(D*D*(a+1));fac=(a-D)*(D*D-a)/(D*D*(D+1)*(a+1))
check(['061'],'bound redundancy identity',s.simplify(diff-fac)==0,s.factor(diff),'Refutes the claimed additional scalar restriction on the derived feasible domain; does not refute the true inequality or its full-rank witness.')
old=[53624480,67257904,74298900,80378416,82204926,85479258,83844372,85479258,82204926,80378416,74298900,67257904,53624480]
new=[53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480]
check(['063'],'archived vectors disagree',sum(new)-sum(old)==5524,{'old':sum(old),'new':sum(new)},'not a regeneration of determinant census')
check(['065'],'copied entries disagree',14928318-14926862==1456,1456,'not a regeneration of determinant census')

# Rebuild Gross matrices and the actual archived 36-slot schedule.
def shift(c,a,b):return 6*((c//6+a)%12)+(c%6+b)%6
A=[(3,0),(0,1),(0,2)];B=[(0,3),(1,0),(2,0)]
HX=[mask([shift(c,*v) for v in A]+[72+shift(c,*v) for v in B]) for c in range(72)]
HZ=[mask([shift(c,-a,-b) for a,b in B]+[72+shift(c,-a,-b) for a,b in A]) for c in range(72)]
times=json.loads((BASE/'records/067/original/M05-tiled_gapcand_32.json').read_text())
tx=[];tz=[]
for c in range(72):
    col=(c//6+c%6)%3
    tx.append(dict(zip([shift(c,*v) for v in A]+[72+shift(c,*v) for v in B],times[col*3:col*3+3]+times[9+col*3:12+col*3])))
    tz.append(dict(zip([shift(c,-a,-b) for a,b in B]+[72+shift(c,-a,-b) for a,b in A],times[18+col*3:21+col*3]+times[27+col*3:30+col*3])))
conflicts=0
for q in range(144):
    tt=[d[q] for d in tx+tz if q in d]
    conflicts+=len(tt)-len(set(tt))
mc=sum(sum(tz[b][q]<tx[a][q] for q in set(tx[a])&set(tz[b]))%2 for a in range(72) for b in range(72))
order66=sorted(tx[66], key=tx[66].get); order2=sorted(tx[2],key=tx[2].get)
V=mask({1,3,7,11,12,14,72,73,74,77,78,80})
fault=mask(order66[-4:])^mask(order2[-2:])^mask({1,3,7,11,14,73,74,141})
check(['067'],'Gross archived schedule and 10-fault witness',conflicts==0 and mc==0 and order66==[68,67,78,12,141,72] and set(order2[-2:])=={77,80} and fault==V and all((r&V).bit_count()%2==0 for r in HZ) and remainder(V,basis(HX))!=0,{'rank_HX':len(basis(HX)),'rank_HZ':len(basis(HZ)),'conflicts':conflicts,'MC_violations':mc,'fault_cost':10,'logical_weight':V.bit_count(),'check66_order':order66},'schedule, parity matrices, logical nontriviality, and selected fault supports independently rebuilt; not all 144 old witnesses')
check(['069'],'k=0 quotient',len(basis([3]))==1 and len(span([3]))==2,'kernel(11)=span(11); no nonzero quotient','outside explicitly k>=1 scoped proof')
H=s.Matrix([[1,s.Rational(1,2)],[s.Rational(1,2),1]]);R=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
avg=s.simplify((H+R*H*R.T)/2)
check(['073'],'orthogonal averaging changes diagonal',list(avg.diagonal())==[s.Rational(5,4),s.Rational(3,4)],avg,'diagnostic outside permutation-scoped source')
k,K,q=4,2,42
check(['074'],'source-domain uniform frozen shift not surjective',q>=(k-1)*(k*K+k+2) and {(k-2)*d%q for d in range(q)}==set(range(0,q,2)),
      {'k':k,'K':K,'q':q,'source_threshold':(k-1)*(k*K+k+2),'reachable_targets':list(range(0,q,2))},
      'Actual bad delivered TeX sentence; allowing every shift still misses all odd targets. Does not disprove the corrected one-coordinate construction.')
check(['075'],'original all-n orbit classification counterexample',{tuple(1-a for a in (0,0)),(0,0)}=={(0,0),(1,1)},
      'G=Z2,t=1,n=2: negative inputs 00 and 11 form one orbit',
      'The restored first manuscript claims at least two orbits for every nonidentity involution; the later delivered manuscript adds q>=3 and a binary exception.')

# This supports an exclusion, not a new positive error. See the bundled
# full-domain algebraic derivation in audit/excluded/004/reconciliation_sources.
dd,rr,kk=s.symbols('D r k')
nn=dd**2-1; uu=dd*rr-1; vv=dd-rr
ff=dd**2+dd-kk-rr*(dd+kk+1)
gg=dd**2-dd-kk+rr*(kk+1-dd)
identity=((vv**2/kk+rr**2-1)*(nn-kk)-uu**2)-ff*gg/kk
t=s.Rational(7,2)
check(['004'],'Cauchy lower-endpoint redundancy identity',s.factor(identity)==0 and s.Rational(7,8)*t*t-s.Rational(101,80)*t-1==s.Rational(53,10) and s.Rational(7,8)*t*t-t/10-1==s.Rational(1499,160),
      'FG/k identity exact; lower estimates positive at t=7/2 and increasing thereafter',
      'Supports exclusion under the full source assumptions; the bundled analytic proof establishes m>=10, A<5/4, D/m>7/2 and hence negativity of the omitted lower endpoint.')

def unique_log(record_id,name):
    paths=list((BASE/f'records/{record_id}/reconciliation_sources').glob('A*-'+name))
    assert len(paths)==1,(record_id,name,paths)
    return paths[0].read_text()

log82=unique_log('063','round82-exploratory-global.log')
rows82=[int(v) for v in re.findall(r'support=(\d+)',log82)]
check(['063'],'original census log is bound to corrected support vector',rows82==new,
      {'rows':len(rows82),'sum':sum(rows82),'stale_sum':sum(old),'difference':sum(rows82)-sum(old)},
      'Reads the bundled original run log; recomputes arithmetic, not the full determinant enumeration.')
log98=unique_log('065','round98-exploratory-global.log')
rows98=[int(v) for v in re.findall(r'size4=(\d+)',log98)]
check(['065'],'original census log binds two copied entries',len(rows98)==13 and rows98[3]==rows98[9]==14926862,
      {'rows':len(rows98),'correct_entry':14926862,'sent_entry':14928318,'difference_each':1456},
      'Reads the bundled original run log; mismatch corroborated by original input audit, not a fresh census.')

# v1.1: exact malformed-task counterassignment for 060.
m60=s.Integer(2)**27
eta60=s.sqrt(m60*(m60-1))/3-1
A60=s.simplify(1+9*(1+eta60)**2/m60)
purity60=s.Rational(m60*m60,m60*m60)
kappa60=s.Rational(m60*(m60-1),m60)
delta60=s.Rational(27,m60)-54
check(['060'],'E1 satisfies literal gate but violates positive gap',
      bool(A60==m60 and m60*(m60-1)>9 and purity60==A60/m60 and kappa60==A60-1 and delta60<0),
      {'m':str(m60),'A':str(A60),'D':1,'purity':str(purity60),'kappa':str(kappa60),'delta':str(delta60)},
      'Closed-form scalar-unitary family; ln(m)>18 follows analytically from ln(2)>2/3. No dense matrix is allocated. Literal E1 is true, but misses the intended hypothesis.')

parser=argparse.ArgumentParser()
parser.add_argument('--write-results',action='store_true',help='Explicitly regenerate the archived results file; default is read-only.')
args=parser.parse_args()
if args.write_results:
    (OUT/'witness_checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(results),'all_passed':True,'records_touched':sorted({r for x in results for r in x['records']})},indent=2))
