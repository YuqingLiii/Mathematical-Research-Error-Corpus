# Independent review: second tame `c=2` actual gate

Date: 2026-07-22  
Reviewed source: `artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/`

## Verdict

**CONFIRMED — single gate only.** The archived witness proves both actual caps for

`n=19, q=38, j=6, theta=(3,2,1), a=b=3, alpha=beta=(2,1), c=2`.

This is strictly a finite `n=19` verdict. It does not prove a uniform theorem in `n`, all `c=2` sectors, any `c>2` statement, or T5.

## Integrity and isolated reload

- The source manifest passes `8/8`.
- `COMMANDS.txt` names the generator, syntax check, reload verifier, and hash check; all referenced source files exist.
- The complete source directory was copied to a fresh temporary directory. Running `verify_second_gate.py` there exited zero and reported both internal SHA and invariant checks PASS.

## Independent parameter and inventory checks

No proposer module is imported by the review script.

- `19>3*6=18` and `q=2n=38`, so this point is strictly tame.
- Direct Littlewood–Richardson word enumeration gives `c_(2,1),(2,1)^(3,2,1)=2`.
- Independent hook/Aitken formulas give dimensions `1615`, `5814`, and `29760` for `V_(16,2,1)`, the query skew module, and the fixed fibre respectively.
- Applying the two horizontal-strip conditions independently recovers exactly the eight archived active `mu` partitions. Their hook dimensions equal the NPZ inventory.
- Both saved seminormal generator plans satisfy involution, reciprocal-target, sign, and off-diagonal symmetry identities to residual below `1e-12`; rowword inventories are unique.

## `R_out` and `R_col`

The review reconstructs the `4x8` rational `d_mu^2` table from the NPZ numerator/denominator arrays and compares it to every JSON row. Independent horizontal-strip tests reproduce exactly 20 supported and 12 forced-zero cells.

Using

`B_theta(38)=C(38,6) f^(3,2,1)/f^(32,3,2,1)=77/64`,

the four independently derived fibre factors are

`eta=(69223/4352, 1/32, 9/256, 15/544)`.

The four recomputed aggregates are exactly

`(18897879/64, 4641/8, 41769/64, 4095/8)`.

The saved reduced recoupling matrix independently gives

`R_col^* R_col = (2240/2697) I_2`

with infinity-norm residual `2.36e-13`.

## Fresh spectrum and `q_mu`

The strongest extra check does not trust the JSON spectrum, Lanczos coefficients, or rational `q_mu` claims. From the NPZ generator plan, an independently reconstructed seminormal plan for `V_(15,2,1)`, and the new `z` tensor of shape `(1344,2,1615)`, the review directly applies the diagonal-`S18` central class sum and runs a new, fully reorthogonalized Lanczos reduction.

It recovers

`60, 71, 73, 75, 85, 87, 89, 102`,

exactly the contents of the eight independently enumerated active `mu`. The recovered spectral weights agree with all eight stored rational `q_mu` values with maximum error `6.83e-15`; their exact sum is `67196/8091` and matches `||z||^2` numerically.

## Exact normalization and caps

The cap dimension is independently reconstructed as

`T=C(18,6) C(6,3) f^(2,1) f^(2,1)=1485120`.

The input-line norms use `C(18,6) f^(3,2,1)/f^mu`, and `r_mu=||t_mu||^2/C(6,3)`. Contracting these exact values with the complete rational `d_mu^2` table gives

- `T_a=204466088827/1438400 < 137582445/64`, exact margin `721924840637/359600`;
- `T_b=8391760923/44590400 < 137582445/1984`, exact margin `770943422613/11147600`.

The tail denominator `31` is independently the minimum of `delta_z+1=(31,33,35)`.

## Reuse boundary

The generator reuses the previously reviewed tableau/seminormal/matrix-free Python algorithms. That is algorithm reuse, not an independent derivation of the mechanism.

It does not reuse the `n=18` numerical witness:

- inventory shapes change from `(1344,18)` to `(1615,19)`;
- `z` shapes change from `(1105,2,1344)` to `(1344,2,1615)`;
- the raw `z` payload SHA-256 changes;
- all eight `q_mu` values change;
- `R^2` changes from `3640/4437` to `2240/2697`;
- static dataflow loads the old Python constructors but neither old numeric NPZ witness.

The proposer embeds candidate `Q19` fractions in its source, so its own verifier is not blind to those targets. This review removes that independence concern by recovering the same fractions directly from the newly shaped `z` witness via a fresh central-operator computation.

## Scope boundary

The review confirms only this stored `n=19` gate and its exact normalization. Two adjacent passing gates are evidence that the computational mechanism reuses, but they do not supply a uniform identity or inequality. No proof-DAG or global-status promotion is licensed by this packet alone.
