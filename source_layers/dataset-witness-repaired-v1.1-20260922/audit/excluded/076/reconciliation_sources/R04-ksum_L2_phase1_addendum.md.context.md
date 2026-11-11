# Source context 4

Source: `[PROJECT]/artifacts/ksum_L2_phase1_addendum.md`

Original SHA-256: `8bf417243714b1f43022c56c34ef94724d23f07590ec00d2f137b60b6a7c0a44`

Original lines: 20–38.

20	This section is the canonical convention for the L2 repair.  Let (F=-1) on NO inputs and (F=+1)
21	on YES inputs.  If a (T)-query quantum algorithm has output error (e), its acceptance-probability
22	polynomial has degree at most (2T), and its expected-sign polynomial (p=2P[\mathrm{YES}]-1)
23	satisfies
24	
25	\[
26	  \deg p\le 2T,\qquad \lVert p-F\rVert_\infty\le 2e.
27	\]
28	
29	At (e=1/3), the uniform error is (2/3).  Hence a unit-(\ell_1) dual witness of pure high degree
30	(d) directly excludes every such degree-(<d) expected-sign polynomial only when
31	
32	\[
33	  \langle\mu,F\rangle>\frac23.
34	\]
35	
36	Under this strict threshold, the certificate gives (Q_{1/3}(F)\ge d/2).  Equality at (2/3) does
37	not certify.  The phase-1 (>1/3) test remains a valid sign-approximate-degree test at uniform
38	approximation error (1/3), but it is not the direct (Q_{1/3}\ge d/2) test.
