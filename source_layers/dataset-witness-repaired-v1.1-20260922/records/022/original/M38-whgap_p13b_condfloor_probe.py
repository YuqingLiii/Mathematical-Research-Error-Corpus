import numpy as np, sys, functools
sys.path.insert(0,'tools')
import whgap_p13b_core as C
import whgap_p13b_sweep as S
from scipy.optimize import minimize
orig=C.kernel_projector
C.kernel_projector=lambda H,gap_factor=1e6,cond_floor=1e-3: orig(H,gap_factor,cond_floor)
rng=np.random.default_rng(202)
for x in (0.40,0.45,0.49,0.35):
    pre=[]
    for i in range(600):
        p=rng.normal(size=12); pre.append((-S.objective(p,x,S.chart_F2),p))
    pre.sort(key=lambda z:-z[0]); best=(-np.inf,0); amb=0
    for p0 in [z[1] for z in pre[:40]]+[rng.normal(size=12) for _ in range(40)]:
        r=minimize(S.objective,p0,args=(x,S.chart_F2),method='Nelder-Mead',options=dict(maxfev=250,xatol=1e-10,fatol=1e-14))
        M=S.chart_F2(r.x); res=C.weight_operator_rf(x,M)
        if not(res['okB'] and res['okE']): amb+=1; continue
        lm=C.lam_max(res['D'])
        if lm>best[0]: best=(lm,res['diagB']['cond_ratio'])
    print('F2 (cond_floor=1e-3) x=%.2f  best=%+.3e  condB=%.2e  ambiguous excluded %d/80'%(x,best[0],best[1],amb))
