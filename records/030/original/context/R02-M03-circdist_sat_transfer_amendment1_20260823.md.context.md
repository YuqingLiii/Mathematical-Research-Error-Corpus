# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/030/original/M03-circdist_sat_transfer_amendment1_20260823.md`

Original SHA-256: `6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e`

Original lines: 224–257.

224	The `A_κ` half is right and the `v` half is wrong. Re-run the document's own Lemma 6.2 computation
225	with `D_{b,0}` deleted: the terminal detector reads
226	
227	```
228	      D_{b,R} = (H_Z σ_R)_b + [ (H_Z σ_{R−1}) + u(S_{R−1}) ]_b = (H_Z σ_R)_b + κ_b ,
229	```
230	
231	so the terminal condition is `H_Z σ_R = κ`, **not** `H_Z σ_R = 0`. And since `E_tot ∉ ker H_Z` in
232	general once `κ ≠ 0`, Lemma 6.3's shortcut ("logical iff `σ_R ≠ [0]`", which is valid only on
233	`ker H_Z`) is unavailable: the logical condition is `λ(σ_R) = 1`. Keeping `v` fixed forces `κ = 0`
234	and collapses the family, so the printed formula does not merely lose precision — it computes the
235	wrong number, in **16 of 16** instances tested (§6.2).
236	
237	### 3.2 The replacement (governing)
238	
239	**Remark 6.5's first two sentences are replaced verbatim by:**
240	
241	> **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
242	> unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
243	> `κ ∈ F₂^ℬ`, and the terminal detector reads
244	> `D_{b,R} = (H_Z σ_R)_b + [(H_Z σ_{R−1}) + u(S_{R−1})]_b = (H_Z σ_R)_b + κ_b`, so the terminal
245	> condition becomes `H_Z σ_R = κ`. Since `σ_R` then need not lie in `ker H_Z`, Lemma 6.3's form of
246	> the logical condition is unavailable and the condition is `λ(σ_R) = 1` — for `k = 1`,
247	> `λ(σ) = ⟨σ, χ_{Z_L}⟩`, which descends to `Σ` by 4.2. The correct object is therefore no longer a
248	> single `(u,A,v)` but the family **`(A_κ, v_κ)`**,
249	> ```
250	>       A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ) ,     v_κ[σ] := 0 if H_Z σ = κ and λ(σ) = 1, else +∞ ,
251	>       d_R = min_{κ ∈ F₂^ℬ} ( u ⊙ A_κ^{⊙R} ⊙ v_κ ) ,
252	> ```
253	> — equivalently a state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component, the
254	> terminal test reading the `κ`-component. **`v` must move with `κ`:** holding `v` fixed at
255	> `v[σ] = 0 iff H_Z σ = 0 and σ ≠ [0]` forces `κ = 0`, collapses the family, and returns the wrong
256	> value (§11.6: wrong in 16 of 16 tested instances; the `κ`-dependent form right in 16 of 16). At
257	> `κ = 0` the two coincide, which is why nothing in Theorem T is affected. Drop the terminal
