"""Local deterministic checks of claims in sealed outputs; no network or new generation.
Analytical proof and scope limitations are in MATHEMATICAL_ADJUDICATION.md.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from datetime import datetime, timezone
import hashlib, json, runpy, subprocess, sys, time, os

S = Path(__file__).resolve().parent
V = S / 'verification'
V.mkdir(exist_ok=True)
checks = []
def record(name, ok, evidence):
    checks.append(dict(name=name, passed=bool(ok), evidence=evidence))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

# Check the exact S02 dominance identity on a rational grid. The identity also
# follows by common denominator; grid evaluation is not a universal proof.
for D in range(2, 17):
    for alpha in [F(D), F(3*D,2), F(D*D), F(D*D+D,2)]:
        f=(alpha**2+D**2)/(D**2*(alpha+1))
        g=(alpha+D)/(D*(D+1))
        rhs=(alpha-D)*(D*D-alpha)/(D*D*(D+1)*(alpha+1))
        assert g-f==rhs and rhs>=0
record('S02_dominance_identity_exact_grid', True, '60 rational points; universal identity derived by common denominator in adjudication memo.')

# Check the identity used in the S03 analytic redundancy proof, including tau
# strictly above its lower bound; no sampling claim about the whole domain.
for D in range(3,15):
    for r in [F(1,2), F(D,3), F(D-1)]:
        for t in [F(0),F(1,3),F(3)]:
            tau=D*r*r+t; i=F(D*D)
            n=D*D-1; u=D*r-1; v=D-r
            a=i-2*tau/D+r*r; b=i-1
            a0=a-v*v/n; b0=b-u*u/n
            assert b0-a0==2*(tau/D-r*r)
            assert u*u-v*v==n*(r*r-1)
            assert u+v==(D-1)*(r+1)
record('S03_centered_identities_exact_grid',True,'108 rational evaluations; analytic identity shown in memo.')

def scalar(m,D):
    A=1+F(10,m); alpha=D*D/m; r=alpha/D
    tau=D*r*r; i=r*r+(D-r)**2/(m*(m-1)); c=r
    n=D*D-1; u=alpha-1; v=D-r
    a=i-2*tau/D+r*r; b=i-1
    a0=a-v*v/n; b0=b-u*u/n
    base=D*D+4*D+alpha*alpha+2*(D+4)*alpha
    B0=D*(D*D+4*D+2)+(D+2)*alpha*alpha-2*(D+4)*alpha
    cup=(A/m*(alpha+D)*(D+2)*(D+3)-base-2*i-4*tau)/2
    creq=(D+2)*i+(D+1)*tau+B0/2-A*alpha*D*(D+1)*(D+3)/(2*m)
    slack=A*D*(D+1)-m*(alpha+D)
    ccircle=cup-slack*(D+2)*(D+3)/(2*m*D)
    csharp=cup-slack*(D+2)*(D+3)/(2*m*m)
    clow=((alpha+D)*(D+2)*(D+3)/m-base-2*i-4*tau)/2
    epsilon=A/m-1/D; mu=(alpha-1)/(D*(D+1))
    Eg2=(D*alpha*alpha-2*D*alpha+2*D*c+2*D*i+4*D*tau-D-12*alpha+6)/(D*D*(D+1)*(D+2)*(D+3))
    # The normalized fourth moment follows by undoing f=m^2(1/D+g).
    Ef=m*m*(alpha+D)/(D*(D+1))
    Ef2=m**4*(base+2*i+4*tau+2*c)/(D*(D+1)*(D+2)*(D+3))
    assert Eg2==Ef2/m**4-2*Ef/(D*m*m)+1/(D*D)
    assert ccircle-c == (epsilon*mu-Eg2)*D*(D+1)*(D+2)*(D+3)/2
    assert csharp==( (A+1)/m*(alpha+D)*(D+2)*(D+3)-A/m**2*D*(D+1)*(D+2)*(D+3)-base-2*i-4*tau)/2
    ok=all([slack>=0, a0>=0,b0>=0,a0==b0,i<=alpha,creq<=c,c<=cup,u*v/n-a0<0])
    return dict(basic_scalar_pass=ok, lower_CS_negative=(u*v/n-a0<0),
                centered_fourth_moment_pass=(c<=ccircle),interval_fourth_moment_pass=(clow<=c<=csharp),
                normalized_PA_slack=str(slack), lower_CS=str(u*v/n-a0))

m=F(10**10)
# q=10, log(m)>23 and 2m log(1+10/m)<20, so Gap holds without floating point.
families={'O03':m**4,'O05':m*(m-1)/10,'O09':m*m/5,'O11':m*m,'O12':m*m/5,'O13':m*m/5}
for oid,D in families.items():
    res=scalar(m,D)
    needed=res['basic_scalar_pass'] and (oid!='O05' or res['centered_fourth_moment_pass']) and (oid!='O09' or res['interval_fourth_moment_pass'])
    record(oid+'_scalar_survivor_exact_instance',needed,res)

# New local order error in O05: for A_ab=U_b^* U_a the valid order is A_bc A_ab.
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]
record('O05_pair_difference_order_counterexample',mul(X,Z)!=mul(Z,X),
       dict(Ua=X,Ub=[[1,0],[0,1]],Uc=Z,claimed_product=mul(X,Z),correct_Aac=mul(Z,X)))

# Strict slack does not make the displayed bound certify any entangled rank.
a=F(10,10**10); b=a-a*a/2
record('O04_O17_strict_slack_does_not_imply_rank2_certificate', b<a and b+9*b*b>a,
       dict(a=str(a),b=str(b),rank2_bound=str(b+9*b*b),scope='Counterexample to the claimed inference from their bound; not a physical counterexample to the channel theorem.'))

# The two archived scripts were read in full before execution. They import
# stdlib combinatorial helpers only and perform no IO except stdout.
env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
for oid in ['O10','O15']:
    p=next((S/'masked'/oid/'artifacts').glob('*.py'))
    start=time.monotonic()
    try:
        out=subprocess.run([sys.executable,str(p)],cwd=V,env=env,capture_output=True,text=True,timeout=60)
        (V/(oid+'-archived-script.stdout.txt')).write_text(out.stdout)
        (V/(oid+'-archived-script.stderr.txt')).write_text(out.stderr)
        record(oid+'_archived_script',out.returncode==0,dict(sha256=sha(p),exit_code=out.returncode,seconds=time.monotonic()-start,stdout=oid+'-archived-script.stdout.txt'))
    except subprocess.TimeoutExpired as e:
        record(oid+'_archived_script',False,dict(sha256=sha(p),timeout_seconds=60,stdout=str(e.stdout),stderr=str(e.stderr)))

o10=next((S/'masked/O10/artifacts').glob('*.py'))
mod=runpy.run_path(str(o10),run_name='scoring_local_check')
formula=[[('x',True),('x',True),('y',True)], [('x',True)]*3, [('y',False)]*3]
truth=[]
for x,y in product([False,True],repeat=2):
    asn={'x':x,'y':y}
    if all(any(asn[v]==pos for v,pos in clause) for clause in formula): truth.append(asn)
B=mod['build_formula'](formula)
ans=mod['abstract_solution'](B.checks)
record('O10_repeated_literal_reduction_counterexample', bool(truth) and ans is None,
       dict(formula=formula,satisfying_assignments=truth,compiled_abstract_satisfiable=ans is not None,compiled_checks=len(B.checks),script_sha256=sha(o10)))

result=dict(created_at_utc=datetime.now(timezone.utc).isoformat(),python=sys.version,
            checks=checks,all_checks_pass=all(c['passed'] for c in checks),
            limitations=['Finite checks do not prove universal theorems.','Four other S01 certificate scripts not rerun; their report constructions were inspected.','External complexity and literature citations not independently fetched.'])
(V/'math-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
