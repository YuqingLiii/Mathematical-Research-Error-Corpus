# Source context 4

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/070/original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md`

Original SHA-256: `38699f1ea65fc3e811f35b06feece9ad464baf7a6fed2f7cee749eefc3e3f985`

Original lines: 226–238.

226	### 6.2 Elementary-fault count versus occupied locations
227	
228	Let `m(e)` be the least cardinality of a multiset of unit elementary faults with total effect `e`, allowing multiple members at one location, and let `c(e)` be the least number of occupied locations in a configuration.
229	
230	A configuration is itself such a multiset, so `m(e)<=c(e)`. Conversely, in any multiset, replace two elements at one location by their product in that location’s full Pauli group. The effect is unchanged. If the product is nonidentity the multiset shrinks by one; if identity it shrinks by two. Repeat until at most one element remains per location. This produces a configuration of weight at most the original multiset size, so `c(e)<=m(e)`. Therefore
231	
232	```text
233	m(e)=c(e).
234	```
235	
236	Disjoint copied round-location sets then give exact additivity across rounds. This proves Lemma 2.9 with both hidden hypotheses exposed: linear effect and group closure with uniform unit cost.
237	
238	A non-group alphabet gives an immediate counterexample. At one CNOT location allow `X_c` and `X_t` but not `X_cX_t`. The collision-permitting multiset realizes the product effect with two elementary faults at that location, while a one-assignment configuration cannot realize it there. A nonuniform model similarly invalidates the weight-nonincreasing projection if `Y` is cheap but its pure X or Z component is expensive.
