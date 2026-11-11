#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "tame_c2_rcol.json").read_text())
npz = np.load(HERE / "tame_c2_rcol.npz")
assert data["verdict"] == "COMPLETE"
assert data["R_squared_exact"] == "3640/4437"
assert data["R_squared_rational_residual_inf"] < 3e-12
assert data["compressed_dimension_total"] == 141168
assert max(data["fold_vector"]["theta_JM_residuals"]) < 3e-12
assert max(data["fold_vector"]["S11_trivial_generator_residuals"]) < 3e-12
assert npz["query_seeds"].shape == (4896, 2)
assert npz["R_color_to_carrier"].shape == (2, 2)
assert npz["z"].shape == (1105, 2, 1344)
q = [Fraction(row["q_mu"]) for row in data["targets"]]
assert q == [Fraction(int(n), int(d)) for n, d in zip(npz["q_mu_numerator"], npz["q_mu_denominator"])]
assert sum(q) == Fraction(254780, 31059)
assert [Fraction(row["t_norm_squared"]) for row in data["targets"]] == [
    Fraction(16714, 93177), Fraction(51650, 93177), Fraction(57230, 93177),
    Fraction(109418, 93177), Fraction(6284, 4437), Fraction(84440, 31059),
    Fraction(54620, 13311), Fraction(3200, 261)]
gates = data["actual_gates"]
assert Fraction(gates["T_a"]) == Fraction(160582822829, 1705200)
assert Fraction(gates["T_b"]) == Fraction(67576575391, 445057200)
assert gates["T_a_pass"] and gates["T_b_pass"]
assert data["exact_checks"]["sum_q_equals_z_norm"]
print("PASS: R_col, eight R_in weights, and exact actual gates reload")
