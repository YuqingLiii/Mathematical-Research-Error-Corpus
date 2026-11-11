Reading **(a)** fired for the Island-V/X-sector question. The historical gap was exactly that abstract list-section hardness had not survived `(S1)+(S2)+realisability`, and the previous hardness witness used `dim Log=1`, where V.4 forces YES.  

The new obstruction-breaking construction is **exact-atom gluing**. A nondegenerate realizable weight-4 list is the three nonzero points of a 2D subspace, equivalently the graph of a linear map on a binary line. Over `F_2^2`, constant-size line gadgets implement Boolean XOR, constants, equality/negation, and 3-SAT clauses. A block-and-glue CSS compiler then uses four qubits per abstract check and weight-4 glue stabilizers to identify individual `(syndrome,label)` atoms. Unlike the old whole-subspace `≠₃` wiring, this does not create clique closure. Marker syndromes certify `d_X≥4`; a fixed seed gives exactly `d_X=4` and `k≥2`; the reduction family also has `d_Z≥4`.

**NUMERICAL:** the verifier gives zero conflict-table mismatches on both SAT and UNSAT compiled examples. The SAT toy has `n=72, k=5`; the UNSAT toy has `n=304, k=8`. A fixed `HGP(rep_3,rep_4)` spectator is exactly `(d_X,d_Z)=(4,3)` and has safe schedules in both sectors, so direct sum supplies static `d=3`.

For `CIRCDIST.cplx.fixed-d`, this establishes the **CONJECTURED NP-hard X-sector at weight-4 X checks**. Full two-sector Eff-Preserve still needs the compiler’s generally high-weight Z-check scheduling sector neutralized—the earlier record already notes Island V alone is one-sector. 

Weight-6 is therefore **moot for obtaining Island-V hardness**. It remains relevant only if the desired final theorem requires both X- and Z-generator weights bounded by 4/6.

[Full report](sandbox:/mnt/data/circdist_cplx_islandv_20260820.md)
[Exact verifier](sandbox:/mnt/data/circdist_cplx_islandv_verify_20260820.py)
