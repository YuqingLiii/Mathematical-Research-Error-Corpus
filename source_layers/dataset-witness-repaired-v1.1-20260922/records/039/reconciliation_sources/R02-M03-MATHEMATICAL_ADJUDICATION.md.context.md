# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/039/original/M03-MATHEMATICAL_ADJUDICATION.md`

Original SHA-256: `c1e6365f612a4aed7926c4068306be4e732dda43321f74c39b4c6f11c4664278`

Original lines: 64–68.

64	The stated general 3-CNF builder chooses clause points u,v,u+v and uses the first occurrence of a variable as the reference for a BOOL/XOR wire. The report claims fresh auxiliary points avoid unintended line coincidences. With repeated literals in a clause, the wire's u+v is instead the third clause terminal.
65	
66	Take F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y). F is satisfiable with x=true,y=false. In the first clause the intended literal labels are (0,0,1), where 0 means true. The equality wire between the first two x occurrences enforces the BOOL table on all three points, forcing the third label to 0; the y consistency wires and last clause force it to 1. The archived builder creates an unsatisfiable abstract instance (107 checks) for this satisfiable F. A deterministic replay reproduces the mismatch.
67	
68	This invalidates the reduction as stated for unrestricted 3-CNF. Restricting the source to three distinct variables per clause, or preprocessing, may repair it, but that repair is not credited to the output. The separate principal-atom compiler and gadget tables still provide valid local progress. The original archived script's two toy tests pass, illustrating the limited coverage of those tests. This is a **new error**, not recurrence of the historical exclusivity error; it does not disprove all possible NP-hardness results.
