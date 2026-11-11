# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/029/original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md`

Original SHA-256: `38699f1ea65fc3e811f35b06feece9ad464baf7a6fed2f7cee749eefc3e3f985`

Original lines: 330–350.

330	On Steane with a redundant X row, let `P_X` be the round-zero dependent-row parity and let `lambda` be the logical observable. The old mitigation admitted
331	
332	```text
333	D' = span(D_b) + span(D_a) + span(P_X+lambda),
334	```
335	
336	because `D'` contains the short set and lies in `V`. Yet `P_X+lambda` detects the projected logical witness. The exact reproduced data are:
337	
338	| R | record dimension | `dim V` | `dim D` | `rank span(D_b)` | `rank span(D_b,D_a)` | `d^{2.7}` | `d^{D'}` |
339	|---:|---:|---:|---:|---:|---:|---:|---:|
340	| 2 | 21 | 15 | 14 | 9 | 13 | 2 | 3 |
341	| 3 | 28 | 22 | 21 | 12 | 20 | 2 | 4 |
342	
343	At `R=3` this is the recorded quintuple `28/22/21/12/20`. Amendment 1 correctly replaces the false condition by
344	
345	```text
346	span(D_b) subseteq D' subseteq D.
347	```
348	
349	That containment is sufficient by the same projection proof. No version with only `D' subseteq V` survives.
350	
