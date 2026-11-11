#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


rows = [line.split(maxsplit=1) for line in (HERE / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(rows) == 6
assert all(sha(HERE / name.strip()) == want for want, name in rows)

data = json.loads((HERE / "effective_rank_review.json").read_text(encoding="utf-8"))
assert data["verdict"] == "CONFIRMED"
assert data["theorem_boundary_audit"]["pass"]
assert data["coisometry_orientation_audit"]["orientation"] == "coisometry X->Y"
rep = data["independent_representation_audit"]
assert rep["all_exact"] and rep["LR_multiplicity_gt_1_rows"] > 0
assert rep["maximum_LR_multiplicity"] >= 2
gates = data["exact_c2_gate_checks"]
assert [row["n"] for row in gates] == [18, 19]
assert all(row["true_rank_cap_over_T"] == "1/5" for row in gates)
assert all(row["c_times_dim_Y_over_T"] == "2/5" for row in gates)
assert Q(gates[0]["carrier_over_BT"]) == Q(101912, 1513017)
assert Q(gates[1]["carrier_over_BT"]) == Q(1075136, 15575175)
assert all(Q(row["physical_T_b"]) < Q(row["physical_T_b_cap"]) for row in gates)
assert data["physical_T_b_consequence"]["uniform_all_admissible_tame_sectors_all_c"]
assert not data["physical_T_b_consequence"]["T_a_claimed"]
assert len(data["source_manifests"]) == 8 and all(row["pass"] for row in data["source_manifests"])
print("PASS: independent effective-rank theorem review")
print("PASS: LR/Pieri, coisometry orientation, and two exact c=2 gates")
print("PASS: uniform physical T-b consequence; SHA256 6/6")
