# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/047/original/M76-REPORT.md`

Original SHA-256: `99172b8af7c95308b033bfcf8dd31d353aa70c6a25d41db3a8806af115e8f62b`

Original lines: 70–89.

70	## 3. T-b consequence
71	
72	The common-line tail formula has the same branch mass
73	`a_(z,mu)=m|d_(z,mu)|^2`.  Writing
74	`h_mu=sum_z |d_(z,mu)|^2`, the raw trace is
75	
76	`T_b(raw)=m sum_mu f^mu r_mu h_mu`.
77	
78	The carrier/effective-rank theorem correctly bounds
79	`R_h=sum_mu f^mu r_mu=||(F/sqrt(m))L_h||_HS^2`, and the output frame correctly
80	bounds `h_mu`.  Their combination therefore bounds `T_b(raw)/m`, not
81	`T_b(raw)`.  The advertised uniform physical (T-b) closure is invalid and
82	must be reopened.
83	
84	This is not yet a (T-b) counterexample.  Direct exact reconstruction gives:
85	
86	| gate | corrected raw physical `T_b` | cap | result |
87	|---:|---:|---:|---:|
88	| `n=18` | `67576575391/22252860` | `51396202/1015` | PASS |
89	| `n=19` | `8391760923/2229520` | `137582445/1984` | PASS |
