# Source context 3

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/028/original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md`

Original SHA-256: `38699f1ea65fc3e811f35b06feece9ad464baf7a6fed2f7cee749eefc3e3f985`

Original lines: 120–128.

120	### 4.1 Concrete conflict-free but MC-failing attack
121	
122	Take `H_X=H_Z=(1111)` on four data qubits. Schedule the eight CNOTs sequentially as
123	
124	```text
125	q0->b, a->q0, a->q1, q1->b, a->q2, q2->b, a->q3, q3->b.
126	```
127	
128	No qubit participates in two CNOTs in one time step, so the schedule is conflict-free. Exactly one common-support qubit has `t(q->b)<t(a->q)`, hence `c_ab=1`. Back-propagating the `Z` measurement of `anc(b)` produces a `Z` on the freshly `|+>`-prepared `anc(a)`; that anticommutes with its input stabilizer, so the check record is uniformly random. The Definition-2.7 parity is not a detector. This is not a marginal convention: the finite-state proof has no defined object to compute until MC is imposed.
