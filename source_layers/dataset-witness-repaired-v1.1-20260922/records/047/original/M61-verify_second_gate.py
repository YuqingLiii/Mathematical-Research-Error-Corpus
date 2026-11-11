"""Fast exact reload verifier for the second tame c=2 gate."""

from __future__ import annotations
import hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def hook(shape):
    product=1
    for i,row in enumerate(shape):
        for j in range(row):product*=row-j+sum(x>j for x in shape[i+1:])
    return math.factorial(sum(shape))//product

def main():
    data=json.loads((HERE/"second_gate.json").read_text(encoding="utf-8"));w=np.load(HERE/"second_gate_witness.npz",allow_pickle=False)
    assert data["verdict"]=="COMPLETE" and data["target"]["strict_tame"] and data["target"]["LR_multiplicity"]==2
    assert data["reuse"]["no_first_gate_numeric_witness_reused"] is True
    assert all(row["match"] for rows in data["source_manifests"].values() for row in rows)
    rin=data["R_in_and_gate"];R=w["R_color_to_carrier"];r2=F(rin["R_squared_exact"])
    assert r2==F(2240,2697)
    assert np.linalg.norm(R.T@R-float(r2)*np.eye(2),ord=np.inf)<4e-12
    q=[F(int(n),int(d)) for n,d in zip(w["q_mu_numerator"],w["q_mu_denominator"])]
    assert q==[F(row["q_mu"]) for row in rin["targets"]] and sum(q,F())==F(67196,8091)
    assert max(row["q_error"] for row in rin["targets"])<3e-12
    active=[tuple(row["mu"]) for row in rin["targets"]];fmu=[hook(mu) for mu in active]
    rmu=[F(row["r_mu"]) for row in rin["targets"]]
    names=("long","tail_1","tail_2","tail_3")
    d2=[[F(int(w["d2_numerator"][a,i]),int(w["d2_denominator"][a,i])) for i in range(8)] for a in range(4)]
    branches=[sum(F(fmu[i])*d2[a][i]*rmu[i] for i in range(8)) for a in range(4)]
    assert str(branches[0])==rin["T_a"] and str(sum(branches[1:],F()))==rin["T_b"]
    assert branches[0]==F(204466088827,1438400) and sum(branches[1:],F())==F(8391760923,44590400)
    assert branches[0]<F(rin["T_a_cap"]) and sum(branches[1:],F())<F(rin["T_b_cap"])
    expected=(F(18897879,64),F(4641,8),F(41769,64),F(4095,8))
    assert all(sum(F(fmu[i])*d2[a][i] for i in range(8))==expected[a] for a in range(4))
    manifest=HERE/"SHA256SUMS.txt"
    if manifest.exists():
        lines=manifest.read_text(encoding="utf-8").splitlines()
        for line in lines:
            checksum,name=line.split("  ",1);assert digest(HERE/name)==checksum,name
        print(f"SHA256 {len(lines)}/{len(lines)} PASS")
    print("INVARIANTS PASS")

if __name__=="__main__":main()
