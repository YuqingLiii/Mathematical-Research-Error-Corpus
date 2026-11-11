#!/usr/bin/env python3
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
d=json.loads((HERE/'normalization_review.json').read_text(encoding='utf-8'))
assert d['verdict']=='CONFIRMED_WITH_SCOPE_CORRECTION'
assert len(d['dependency_manifests'])==8 and all(x['pass'] for x in d['dependency_manifests'])
c=d['c1_orbital_audit'];assert len(c['j2_independent_full_state_crosschecks'])==5 and all(x['pass'] for x in c['j2_independent_full_state_crosschecks'])
j=c['j5_minimal_reproduction'];assert j['pair_count_sum']==j['physical_colored_M']==10010 and F(j['raw_over_cap'])==F(j['stored_ratio'])<1 and F(j['cap_minus_raw'])>0
g=d['c2_compressed_gate_audit']['gates'];assert len(g)==2
assert all(x['raw_T_a_fails'] and F(x['raw_T_a_over_cap'])>1 and x['raw_T_b_passes'] and F(x['raw_T_b_over_cap'])<1 for x in g)
assert d['theta41_stop']=={'family_certificates':0,'pid':45136,'raw_samples':'84/96 through m=23 for all six targets','stopped':True,'symbolic_kernels':0}
m=HERE/'SHA256SUMS.txt'
if m.exists():
 rows=[x.split(None,1) for x in m.read_text(encoding='utf-8').splitlines() if x.strip()]
 for digest,name in rows:assert sha(HERE/name.strip())==digest,(name,'manifest mismatch')
 print(f'SHA256 {len(rows)}/{len(rows)} PASS')
print('DEPENDENCIES 8/8 PASS')
print('INVARIANTS PASS')
