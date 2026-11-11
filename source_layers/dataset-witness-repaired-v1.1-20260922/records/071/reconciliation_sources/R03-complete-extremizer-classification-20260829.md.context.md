# Source context 3

Source: `[RESEARCH_GRAPH]/grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md`

Original SHA-256: `44ac28ada792471f5ff014f763a94da16929ac2f6d99df01b2a056f52a47cd99`

Original lines: 147–172.

147	## GOC-T5: why the R/C/H commutant is not the full classification
148	
149	Take `A=I_3` and let `S_3` act simultaneously on rows and columns.  The
150	actions are transitive and `P_g A P_g^T=A`.  Here `U=V=I_3`, `r=3`, and
151	
152	```text
153	S(A) = { H >= 0 : diag(H)=1 }.
154	```
155	
156	For example,
157	
158	```text
159	H = [ 1   1/2  0
160	      1/2 1    0
161	      0   0    1 ]
162	```
163	
164	has eigenvalues `3/2,1/2,1`, hence is positive definite and belongs to
165	`S(A)`.  Any factor `H=T T^T` gives `X=Y=T`, a unit-row strategy of value
166	`3`, so it is an extremizer.  But `H` does not commute with all permutation
167	matrices: its off-diagonal entries are not constant.  It is therefore not in
168	the `S_3` commutant.
169	
170	Thus an R/C/H commutant reduction cannot classify every extremizer.  It can
171	classify the invariant part of `S(A)` or produce a canonical invariant
172	representative.
