# Source context 1

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/039/original/M01-circdist_cplx_islandv_20260820.md`

Original SHA-256: `cc090b85b715f0474431b5ff0eedfb8b976f33a95402af9696dfb3c11effe76e`

Original lines: 251–276.

251	Given a 3-CNF formula, give clause `t` two fresh basis vectors `a_t,b_t` and use the three occurrence points
252	
253	`p_{t1}=a_t`, `p_{t2}=b_t`, `p_{t3}=a_t+b_t`.
254	
255	They are a binary line by construction.
256	
257	For every literal occurrence point `p`, attach a private BOOL gadget on `{p,r_p,p+r_p}` with fresh `r_p`; hence `g(p) in {0,1}`.
258	
259	For each Boolean variable, choose one occurrence as reference. Wire every other occurrence to the reference:
260	
261	* same literal polarity -> equality wire;
262	* opposite polarity -> negation wire.
263	
264	Interpret occurrence value `0` as “this literal is true”.
265	
266	Finally, for each clause add the single zero-map constraint
267	
268	`(0,0,0)`
269	
270	on its occurrence line. It is hit iff at least one of the three occurrence bits is zero, exactly the OR condition for the clause.
271	
272	All auxiliary points use fresh basis coordinates, so unintended line coincidences are avoided. The number of points and constraints is linear in the formula size.
273	
274	**Correctness.** A Boolean satisfying assignment sets every literal occurrence to `0` iff that literal is true; the wires and clause check are then satisfied, and all private helpers can be filled from the finite gadget tables. Conversely any section solution can be totalised. The private BOOL gadgets make every occurrence Boolean, the wires give a consistent truth value per variable, and every zero-map clause has a zero occurrence, hence a true literal.
275	
276	Therefore LINE-SECTION is NP-hard already with `dim L_0=2`. Combining with Theorem 2 gives NP-hardness for **code-realizable** Island-V X-sector instances with weight-4 X checks, `d_X=4`, and `k>=2`.
