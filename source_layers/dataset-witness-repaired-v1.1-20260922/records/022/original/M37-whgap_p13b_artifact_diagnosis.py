import numpy as np, sys, json
sys.path.insert(0,'tools')
import whgap_p13b_sweep as S
from whgap_p13b_core import *
from scipy.optimize import minimize
rng=np.random.default_rng(202); x=0.40
# reproduce the F2 x=0.40 incumbent under the CURRENT (strengthened) discipline
pre=[]
for i in range(800):
    p=rng.normal(size=12); pre.append((-S.objective(p,x,S.chart_F2),p))
pre.sort(key=lambda z:-z[0])
best=(-1,None)
seeds=[z[1] for z in pre[:50]]+[rng.normal(size=12) for _ in range(50)]
for p0 in seeds:
    r=minimize(S.objective,p0,args=(x,S.chart_F2),method='Nelder-Mead',options=dict(maxfev=250,xatol=1e-10,fatol=1e-14))
    M=S.chart_F2(r.x); res=weight_operator_rf(x,M)
    if not(res['okB'] and res['okE']): continue
    lm=lam_max(res['D'])
    if lm>best[0]: best=(lm,M,res)
lm,M,res=best
print('incumbent lam_max=%.10f mB=%d okB=%s condB=%.3e condE=%.3e'%(lm,res['mB'],res['okB'],res['diagB']['cond_ratio'],res['diagE']['cond_ratio']))
print('sv(M)=',np.linalg.svd(M,compute_uv=False),' Tr(MM^T)=',np.trace(M@M.T))
print('B spectrum:',np.array(res['diagB']['spectrum']))
D=res['D']; w,V=np.linalg.eigh((D+D.conj().T)/2); phi=np.outer(V[:,-1],V[:,-1].conj())
ok,pred,rat=validate_slope(x,M,phi,D); print('slope gate:',ok,pred,rat)
# rationalise and test EXACTLY
import sympy as sp, whgap_p13b_exact as E
from fractions import Fraction
def rat3(z,den=2520):
    return sp.Rational(round(z.real*den),den)+sp.I*sp.Rational(round(z.imag*den),den)
Ms=sp.Matrix(3,3,lambda i,j: rat3(M[i,j]))
r8=E.weight_operator_exact(Ms, sp.Rational(2,5))
print('rationalised (den 2520): r=%d mB=%d'%(r8['r'],r8['mB']))
c=E.nsd_certificate(r8['D'],r8['Psi']); print('   exact: killsPsi=%s ldl=%s nsd=%s'%(c['kills_psi'],c['ldl_status'],c['nsd']))
print('   exact lam_max(60dps) =', E.lam_max_mp(r8['D'])[0])
