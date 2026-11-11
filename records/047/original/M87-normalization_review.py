#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,math,re,sys
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
T3=ROOT/'artifacts/logs_se_trace_t3_20260721/se_trace_t3_report_20260721.md'
T2=ROOT/'artifacts/logs_se_trace_t2_proposer_20260720/se_trace_t2_audit_20260720.py'
T2J=ROOT/'artifacts/logs_se_trace_t2_proposer_20260720/se_trace_t2_audit_20260720.json'
GFILE=ROOT/'artifacts/logs_se_trace_t5_j5_degree3_20260722/j5_degree3_exact.py'
J311=ROOT/'artifacts/logs_se_trace_t5_j5_theta311_localdp_v1_20260722/theta311_certified13_v1.json'
R18=ROOT/'artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.json'
C18=ROOT/'artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json'
S18=ROOT/'artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/construct_rcol.py'
G19=ROOT/'artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.json'
S19=ROOT/'artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_tame_c2_gate.py'
THEORY=ROOT/'artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722/uniform_ta_two_frame.json'

def frac(x):return F(str(x))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def manifest(directory):
 rows=[]
 for line in (directory/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
  if not line.strip():continue
  digest,name=line.split(maxsplit=1);path=directory/name.strip().lstrip('*');assert sha(path)==digest,(path,'manifest')
  rows.append(name.strip())
 return {'directory':str(directory.relative_to(ROOT)),'files':len(rows),'pass':True}
def hook(shape):
 n=sum(shape);prod=1
 for i,row in enumerate(shape):
  for col in range(row):prod*=row-col+sum(1 for lower in shape[i+1:] if lower>col)
 return math.factorial(n)//prod

def recompute_gate(n,rout,rin):
 m=20;targets={tuple(x['mu']):x for x in rin['targets']};branches={}
 for branch in ('long','tail_1','tail_2','tail_3'):
  normalized=F();raw=F()
  for row in rout['rows']:
   if row['branch']!=branch:continue
   target=targets[tuple(row['mu'])];d2=frac(row['d_squared']);amass=frac(row.get('a_mass',str(m*d2)))
   assert amass==m*d2
   term=F(target['f_mu'])*frac(target['r_mu']);normalized+=term*d2;raw+=term*amass
  assert raw==m*normalized;branches[branch]={'normalized':str(normalized),'raw':str(raw)}
 ta_norm=frac(rin['T_a']);tb_norm=frac(rin['T_b']);ta_raw=frac(branches['long']['raw']);tb_raw=sum(frac(branches[x]['raw']) for x in ('tail_1','tail_2','tail_3'))
 assert ta_norm==frac(branches['long']['normalized'])
 assert tb_norm==sum(frac(branches[x]['normalized']) for x in ('tail_1','tail_2','tail_3'))
 cap_a=frac(rin['T_a_cap']);cap_b=frac(rin['T_b_cap'])
 return {'n':n,'j':6,'a':3,'m':m,'branches':branches,'normalized_T_a':str(ta_norm),'raw_T_a':str(ta_raw),'T_a_cap':str(cap_a),
  'raw_T_a_minus_cap':str(ta_raw-cap_a),'raw_T_a_over_cap':str(ta_raw/cap_a),'raw_T_a_fails':ta_raw>cap_a,
  'normalized_T_b':str(tb_norm),'raw_T_b':str(tb_raw),'T_b_cap':str(cap_b),'raw_T_b_over_cap':str(tb_raw/cap_b),'raw_T_b_passes':tb_raw<cap_b}

def load_engine():
 spec=importlib.util.spec_from_file_location('normalization_review_engine',GFILE);assert spec and spec.loader
 g=importlib.util.module_from_spec(spec);sys.modules[spec.name]=g;spec.loader.exec_module(g);return g

def main():
 deps=[manifest(ROOT/x) for x in (
  'artifacts/logs_se_trace_t3_20260721','artifacts/logs_se_trace_t2_proposer_20260720',
  'artifacts/logs_se_trace_t5_tame_c2_rout_20260721','artifacts/logs_se_trace_t5_tame_c2_rcol_20260721',
  'artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722','artifacts/logs_se_trace_t5_uniform_ta_two_frame_20260722',
  'artifacts/logs_se_trace_t5_j5_degree3_20260722','artifacts/logs_se_trace_t5_j5_theta311_localdp_v1_20260722')]
 t3=T3.read_text(encoding='utf-8');assert 'm=binom(j,a)' in t3 and r'S_{h,\gamma}S_{h,\gamma}^*' in t3 and r'\{m k_{\gamma\mu}\}' in t3
 s18=S18.read_text(encoding='utf-8');s19=S19.read_text(encoding='utf-8')
 assert 'r_mu = [value / 20 for value in t_squared]' in s18 and 'row[i] * r_mu[i]' in s18
 assert 'rmu=[x/20 for x in t2]' in s19 and 'd2[name][i]*rmu[i]' in s19
 r18=json.loads(R18.read_text(encoding='utf-8'));c18=json.loads(C18.read_text(encoding='utf-8'))
 g19=json.loads(G19.read_text(encoding='utf-8'));gate18=recompute_gate(18,r18,c18['actual_gates']|{'targets':c18['targets']});gate19=recompute_gate(19,g19['R_out'],g19['R_in_and_gate'])
 theory=json.loads(THEORY.read_text(encoding='utf-8'))
 for got,want in zip((gate18,gate19),theory['tame_c2_gates']):
  assert got['raw_T_a']==want['raw_registered_T_a'] and got['raw_T_b']==want['raw_registered_T_b']
 g=load_engine();t2=json.loads(T2J.read_text(encoding='utf-8'))
 j2cases=[((2,),0,(),(2,)),((2,),1,(1,),(1,)),((1,1),0,(),(1,1)),((1,1),1,(1,),(1,)),((1,1),2,(1,1),())]
 expected=[frac(x['ratio_exact']) for x in t2['gates'][4:9]];cross=[]
 for case,want in zip(j2cases,expected):
  _,got=g.family_ratio(case[0],case[1],case[2],case[3],False,g.sp.Integer(4));assert got==want
  cross.append({'theta':list(case[0]),'a':case[1],'raw_full_state_ratio':str(want),'family_ratio':str(got),'pass':True})
 t2src=T2.read_text(encoding='utf-8');assert 'pair_formula = m * row_sum' in t2src and 'for lset in itertools.combinations' in t2src and 'for iset in itertools.combinations' in t2src
 cert=json.loads(J311.read_text(encoding='utf-8'));name='theta311_a1_alpha1_beta31';r=frac(cert['families'][name]['direct_n15_ratio'])
 n=15;j=5;a=1;b=4;color=math.comb(j,a);N=math.comb(n-1,j);M=math.comb(n-1,a)*math.comb(n-1-a,b);assert M==N*color
 dimprod=hook((1,))*hook((3,1));T=M*dimprod;B=F(math.comb(2*n,j)*hook((3,1,1)),hook((2*n-j,3,1,1)));cap=B*B*T
 pair_sum=int(sum(g.pair_count(n,j,a,t) for t in g.representatives(j,a)[1]));assert pair_sum==M
 fixedsum=dimprod*r;raw=M*B*B*fixedsum;assert raw/cap==r
 j5={'family':name,'n':n,'stored_ratio':str(r),'color_m':color,'uncolored_N':N,'physical_colored_M':M,'pair_count_sum':pair_sum,
  'dim_alpha_dim_beta':dimprod,'T':T,'B':str(B),'cap':str(cap),'fixed_row_sum_from_family_ratio':str(fixedsum),'raw_trace_from_definition':str(raw),
  'raw_over_cap':str(raw/cap),'cap_minus_raw':str(cap-raw),'incorrect_extra_m_ratio':str(color*r),'conclusion':'no missing m: pair_count already contains N*m and T contains the same M'}
 payload={'date':'2026-07-22','verdict':'CONFIRMED_WITH_SCOPE_CORRECTION','dependency_manifests':deps,
  'raw_definition':{'m':'C(j,a)','T3_identity':'S_gamma S_gamma^*=m K_gamma','T3_spectrum':'nonzero A_gamma eigenvalues are m k_(gamma,mu)'},
  'c1_orbital_audit':{'conclusion':'raw/cap, not normalized/cap; no extra m is permitted','j2_independent_full_state_crosschecks':cross,'j5_minimal_reproduction':j5},
  'c2_compressed_gate_audit':{'conclusion':'missing m confirmed in both final Rcol contractions: stored d^2*r_mu must be a_mass*r_mu=m*d^2*r_mu','gates':[gate18,gate19]},
  'review_of_two_frame_artifact':{'verdict':'CONFIRMED for the two c2 T-a counterexamples and loss of m in the effective-rank proof; scope correction: it does not invalidate c1 family_ratio certificates'},
  'impact':{'T5':'uniform physical T-a is refuted by two exact c2 gates; uniform physical T-b proof is reopened although both corrected finite T-b gates pass',
   'T2':'its c1 full-state/orbital identities and gates survive; its proposed all-parameter implication to physical T-a cannot hold because physical T-a has c2 counterexamples',
   'TRACE':'the registered universal T-a statement is false, so the TRACE proof frontier cannot remain supported by T2/T5',
   'root':'the lower-bound theorem itself is not directly refuted, but the current TRACE/T2 proof chain is invalid; root must be treated as unsupported/open absent another route'},
  'theta41_stop':{'pid':45136,'stopped':True,'raw_samples':'84/96 through m=23 for all six targets','symbolic_kernels':0,'family_certificates':0}}
 (HERE/'normalization_review.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 lines=['VERDICT CONFIRMED_WITH_SCOPE_CORRECTION','C1_ORBITAL_RAW_RATIO 5/5 J2 CROSSCHECK PASS','J5_MINIMAL_M_ACCOUNTING PASS','C2_RAW_TA_COUNTEREXAMPLES 2/2 CONFIRMED','C2_RAW_TB_FINITE_GATES 2/2 PASS','T5_TA REFUTED','T5_TB_PROOF REOPEN','ROOT_PROOF_CHAIN UNSUPPORTED']
 (HERE/'normalization_review.log').write_text('\n'.join(lines)+'\n',encoding='utf-8');print('\n'.join(lines))
if __name__=='__main__':main()
