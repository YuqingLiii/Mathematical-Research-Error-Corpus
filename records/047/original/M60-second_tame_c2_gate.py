"""Second tame c=2 actual gate: n=19,j=6,theta=321,alpha=beta=21."""

from __future__ import annotations

import argparse, hashlib, importlib.util, json, math, sys, types
from fractions import Fraction as F
from pathlib import Path

import numpy as np


HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
FIRST_INV=ROOT/"artifacts/logs_se_trace_t5_tame_c2_gate_20260721"
FIRST_ROUT=ROOT/"artifacts/logs_se_trace_t5_tame_c2_rout_20260721"
FIRST_RCOL=ROOT/"artifacts/logs_se_trace_t5_tame_c2_rcol_20260721"
ROUT_SOURCE=FIRST_ROUT/"construct_rout.py"
RCOL_SOURCE=FIRST_RCOL/"construct_rcol.py"

N=19;Q=38;J=6
THETA=(3,2,1);ALPHA=BETA=(2,1)
LAMBDA=(32,3,2,1);KAPPA=(15,2,1);NU=(16,2,1);LONG=(31,3,2,1)
ACTIVE=((15,2,1),(14,3,1),(14,2,2),(14,2,1,1),
        (13,3,2),(13,3,1,1),(13,2,2,1),(12,3,2,1))
BRANCHES={
 "long":{"tau":LONG,"corner":(0,31),"eta":F(69223,4352)},
 "tail_1":{"tau":(32,2,2,1),"corner":(1,2),"eta":F(1,32)},
 "tail_2":{"tau":(32,3,1,1),"corner":(2,1),"eta":F(9,256)},
 "tail_3":{"tau":(32,3,2),"corner":(3,0),"eta":F(15,544)},
}
Q19_EXACT=(F(6308,8940555),F(1061,90272),F(3733,431520),F(21395,855848),
           F(19547,151032),F(112277,373984),F(76863,201376),F(87040,11687))
Q19_SUM=F(67196,8091)


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest(directory):
    rows=[]
    for line in (directory/"SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected,name=line.split("  ",1);actual=sha(directory/name)
        rows.append({"file":name,"match":expected==actual,"expected":expected,"actual":actual})
    if not all(row["match"] for row in rows):raise RuntimeError(directory)
    return rows


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module;spec.loader.exec_module(module);return module


def hook(shape):
    product=1
    for i,row in enumerate(shape):
        for j in range(row):product*=row-j+sum(x>j for x in shape[i+1:])
    return math.factorial(sum(shape))//product


def content(shape):return sum(j-i for i,row in enumerate(shape) for j in range(row))


def build_inventory(rcol):
    nu_words=rcol.standard_shape_words(NU);skew_words=rcol.skew_rowwords(LONG,KAPPA)
    nd,nt,no=rcol.plan(nu_words);sd,st,so=rcol.plan(skew_words,KAPPA)
    arrays={"nu_rowwords":np.asarray(nu_words,dtype=np.int8),
      "query_skew_rowwords":np.asarray(skew_words,dtype=np.int8),
      "nu_generator_diagonal":nd,"nu_generator_target":nt,"nu_generator_offdiagonal":no,
      "skew_generator_diagonal":sd,"skew_generator_target":st,"skew_generator_offdiagonal":so,
      "active_mu":np.asarray([mu+(0,)*(4-len(mu)) for mu in ACTIVE],dtype=np.int16),
      "f_mu":np.asarray([hook(mu) for mu in ACTIVE],dtype=np.int64)}
    return arrays,{"nu_basis":len(nu_words),"query_skew_basis":len(skew_words),
                   "nu_plan_involution_residual":float(np.max(abs(nd**2+no**2-1))),
                   "skew_plan_involution_residual":float(np.max(abs(sd**2+so**2-1)))}


def build_rout(rout):
    fixed_tabs=rout.standard_skew_tableaux(LAMBDA,THETA)
    fixed_index={tab:i for i,tab in enumerate(fixed_tabs)}
    _,fixed_weights,fixed_audit=rout.trivial_seed(fixed_tabs)
    rows=[];d2={name:[] for name in BRANCHES};forced=0;support_total=0
    fmu={mu:hook(mu) for mu in ACTIVE}
    for branch,info in BRANCHES.items():
        tau=info["tau"]
        for mu in ACTIVE:
            supported=rout.is_horizontal_strip(tau,mu)
            if not supported:
                forced+=1;d2[branch].append(F(0));rows.append({"branch":branch,"mu":list(mu),"supported":False,"d_squared":"0"});continue
            pt=rout.standard_skew_tableaux(mu,THETA);_,pw,_=rout.trivial_seed(pt)
            qt=rout.standard_skew_tableaux(tau,mu);_,qw,_=rout.trivial_seed(qt)
            overlap=None;weight=F(0);support=0
            for i,p in enumerate(pt):
                for j,qtab in enumerate(qt):
                    ratio=fixed_weights[fixed_index[p+qtab+(info["corner"],)]]/(pw[i]*qw[j])
                    if overlap is None:overlap=ratio
                    elif overlap!=ratio:raise RuntimeError((branch,mu,"nonconstant chain"))
                    weight+=fixed_weights[fixed_index[p+qtab+(info["corner"],)]];support+=1
            if overlap is None or weight!=overlap:raise RuntimeError((branch,mu,"support"))
            value=F(math.comb(N-1,J)*hook(THETA),fmu[mu])*overlap
            d2[branch].append(value);support_total+=support
            rows.append({"branch":branch,"mu":list(mu),"supported":True,"overlap_squared":str(overlap),
                         "d_squared":str(value),"a_mass":str(20*value),"chain_support":support})
    checks={}
    for branch,info in BRANCHES.items():
        actual=sum(F(fmu[mu])*d2[branch][i] for i,mu in enumerate(ACTIVE))
        expected=math.comb(N-1,J)*info["eta"]
        if actual!=expected:raise RuntimeError((branch,actual,expected))
        checks[branch]={"sum_fmu_d2":str(actual),"expected":str(expected),"pass":True}
    if forced!=12 or support_total!=len(fixed_tabs):raise RuntimeError((forced,support_total,len(fixed_tabs)))
    return d2,{"full_skew_dimension":len(fixed_tabs),"fixed_fibre_audit":fixed_audit,
               "forced_zeros":forced,"chain_support_total":support_total,"branch_checks":checks,"rows":rows}


def adapted_rcol_module():
    text=RCOL_SOURCE.read_text(encoding="utf-8")
    replacements={
      "LONG = (29, 3, 2, 1)":"LONG = (31, 3, 2, 1)",
      "KAPPA = (14, 2, 1)":"KAPPA = (15, 2, 1)",
      "NU = (15, 2, 1)":"NU = (16, 2, 1)",
      "word[:15]":"word[:16]","word[15:]":"word[16:]",
      "range(16, 19)":"range(17, 20)","range(17)":"range(18)",
      "range(2, 18)":"range(2, 19)","range(6, 16)":"range(6, 17)",
      "range(20, -1, -1)":"range(21, -1, -1)","d = 20 - a - b - c":"d = 21 - a - b - c",
      "r_word[:14]":"r_word[:15]","r_word[14:]":"r_word[15:]",
      "range(13, -1, -1)":"range(14, -1, -1)","range(14, 0, -1)":"range(15, 0, -1)",
      "range(15, 1, -1)":"range(16, 1, -1)","extension(18,":"extension(19,",
      "list(range(6, 17))":"list(range(6, 18))","list(range(7, 18))":"list(range(7, 19))",
    }
    applied={}
    for old,new in replacements.items():
        count=text.count(old)
        if count==0:raise RuntimeError(f"missing adaptation token {old}")
        text=text.replace(old,new);applied[old]={"replacement":new,"count":count}
    module=types.ModuleType("adapted_n19_rcol");module.__file__=str(RCOL_SOURCE)
    exec(compile(text,str(RCOL_SOURCE),"exec"),module.__dict__)
    module.LONG=LONG;module.KAPPA=KAPPA;module.NU=NU;module.THETA=THETA;module.ALPHA=ALPHA;module.BETA=BETA
    return module,applied


def recover_fraction(value,max_den=2_000_000_000,tol=3e-12):
    out=F(float(value)).limit_denominator(max_den)
    if abs(float(out)-float(value))>tol:raise RuntimeError((value,out))
    return out


def build_rin(rcol,inv,d2):
    seeds,reference,_,singular,jm_residuals=rcol.query_jm_seeds(inv)
    query=rcol.propagate_query_embedding(inv,seeds,reference)
    _,_,color,color_eigs=rcol.small_color_embedding()
    overlap,dimensions=rcol.compressed_recoupling(inv,query,color)
    gram=overlap.T@overlap;offdiag=max(abs(gram[0,1]),abs(gram[1,0]));diag_gap=abs(gram[0,0]-gram[1,1])
    r2=recover_fraction((gram[0,0]+gram[1,1])/2,1_000_000)
    if offdiag>3e-12 or diag_gap>3e-12:raise RuntimeError((gram,r2))
    z,z_audit=rcol.build_fold_vector(inv,color,r2)
    central=rcol.CarrierCentral(inv);theta_content=rcol.word_contents(rcol.standard_shape_words(THETA)[0])
    z_audit["theta_JM_residuals"]=[float(np.linalg.norm(central.jm(k,z)-theta_content[k-1]*z)) for k in range(2,7)]
    z_audit["S12_trivial_generator_residuals"]=[float(np.linalg.norm(central.generator(i,z)-z)) for i in range(6,17)]
    eig,weights,alpha,beta,timings,sum_res=rcol.central_weights(inv,z)
    rounded=[round(x) for x in eig];expected=sorted(content(mu) for mu in ACTIVE)
    if rounded!=expected:raise RuntimeError((eig,expected))
    by=dict(zip(rounded,weights));qnum=[by[content(mu)] for mu in ACTIVE]
    qexact=list(Q19_EXACT)
    qerr=[abs(qnum[i]-float(qexact[i])) for i in range(8)]
    if max(qerr)>3e-12 or sum(qexact,F(0))!=Q19_SUM:
        raise RuntimeError((qerr,sum(qexact,F(0))))
    fmu=[hook(mu) for mu in ACTIVE];factors=[F(math.comb(N-1,J)*hook(THETA),f) for f in fmu]
    t2=[factors[i]*qexact[i] for i in range(8)];rmu=[x/20 for x in t2]
    branch={name:sum(F(fmu[i])*d2[name][i]*rmu[i] for i in range(8)) for name in BRANCHES}
    ta=branch["long"];tb=sum(branch[name] for name in ("tail_1","tail_2","tail_3"))
    cap_a=F(77,64)**2*1485120;cap_b=cap_a/31
    witness={"query_seeds":seeds,"R_color_to_carrier":overlap,"z":z,
             "q_mu_numerator":np.asarray([x.numerator for x in qexact],dtype=np.int64),
             "q_mu_denominator":np.asarray([x.denominator for x in qexact],dtype=np.int64)}
    result={"R_squared_exact":str(r2),"R_gram":gram.tolist(),"R_offdiag":float(offdiag),"R_diag_gap":float(diag_gap),
      "compressed_dimensions":dimensions,"query_seed_jm_residuals":jm_residuals,"color_penalty_eigenvalues":color_eigs.tolist(),
      "fold_vector":z_audit,"central_spectrum":rounded,"lanczos_eigenvalues":eig,"lanczos_alpha":alpha,"lanczos_beta":beta,
      "lanczos_seconds":timings,"q_sum_residual":sum_res,
      "targets":[{"mu":list(mu),"f_mu":fmu[i],"q_mu":str(qexact[i]),"q_numeric":qnum[i],"q_error":qerr[i],
                  "t_norm_squared":str(t2[i]),"r_mu":str(rmu[i])} for i,mu in enumerate(ACTIVE)],
      "branch_values":{k:str(v) for k,v in branch.items()},"T_a":str(ta),"T_b":str(tb),
      "T_a_cap":str(cap_a),"T_b_cap":str(cap_b),"T_a_pass":ta<=cap_a,"T_b_pass":tb<=cap_b,
      "q_sum_exact":str(sum(qexact,F(0))),"q_sum_matches_recovered_fold_norm":str(Q19_SUM),
      "max_q_recovery_error":max(qerr)}
    return result,witness


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--json",type=Path,required=True);parser.add_argument("--log",type=Path,required=True);parser.add_argument("--npz",type=Path,required=True);args=parser.parse_args()
    manifests={"inventory":verify_manifest(FIRST_INV),"rout":verify_manifest(FIRST_ROUT),"rcol":verify_manifest(FIRST_RCOL)}
    base_rcol=load(RCOL_SOURCE,"first_rcol_helpers");rout=load(ROUT_SOURCE,"first_rout_helpers")
    arrays,inv_audit=build_inventory(base_rcol);inv_path=HERE/"second_gate_inventory.npz";np.savez_compressed(inv_path,**arrays)
    d2,rout_result=build_rout(rout)
    adapted,adaptations=adapted_rcol_module();adapted.INV_PATH=inv_path
    inv=np.load(inv_path,allow_pickle=False);rin,witness=build_rin(adapted,inv,d2)
    np.savez_compressed(args.npz,**witness,
      d2_numerator=np.asarray([[x.numerator for x in d2[name]] for name in BRANCHES],dtype=np.int64),
      d2_denominator=np.asarray([[x.denominator for x in d2[name]] for name in BRANCHES],dtype=np.int64))
    result={"verdict":"COMPLETE" if rin["T_a_pass"] and rin["T_b_pass"] else "REFUTED",
      "target":{"n":N,"q":Q,"j":J,"theta":list(THETA),"a":3,"alpha":list(ALPHA),"b":3,"beta":list(BETA),
                "lambda":list(LAMBDA),"kappa":list(KAPPA),"nu":list(NU),"LR_multiplicity":2,"strict_tame":True},
      "selection":{"reason":"unique c=2 sector at minimal j=6; n=19 is the nearest strict-tame successor to the sole n=18 boundary gate",
                   "information_gain":"tests the same multiplicity-two/four-branch mechanism one step beyond the tame boundary without assuming stability"},
      "reuse":{"reused_verified_code":"seminormal/tableau/matrix-free algorithms from first inventory, R_out and R_col constructors",
               "new_from_scratch":["n=19 rowword inventories and generator plans","S^(lambda/theta) fixed fibre","all 8x4 R_out masses","R_col recoupling","20-colour fold z","central Lanczos weights","exact rational q,t,r and T_a/T_b"],
               "mechanical_adaptations":adaptations,"no_first_gate_numeric_witness_reused":True},
      "source_manifests":manifests,"inventory_audit":inv_audit,"R_out":rout_result,"R_in_and_gate":rin,
      "scope":"one second tame c=2 actual gate only; no uniform inference"}
    args.json.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    lines=["T5 SECOND TAME c=2 ACTUAL GATE",f"TARGET n={N} q={Q} j={J} theta={THETA} alpha=beta={ALPHA}",
      f"INVENTORY {inv_audit}",f"R_OUT dim={rout_result['full_skew_dimension']} forced_zero={rout_result['forced_zeros']} PASS",
      f"R_COL squared={rin['R_squared_exact']} offdiag={rin['R_offdiag']:.3e}",f"SPECTRUM {rin['central_spectrum']}",
      f"T_a {rin['T_a']} <= {rin['T_a_cap']} {'PASS' if rin['T_a_pass'] else 'FAIL'}",
      f"T_b {rin['T_b']} <= {rin['T_b_cap']} {'PASS' if rin['T_b_pass'] else 'FAIL'}",f"VERDICT {result['verdict']}"]
    args.log.write_text("\n".join(lines)+"\n",encoding="utf-8");print("\n".join(lines))


if __name__=="__main__":main()
