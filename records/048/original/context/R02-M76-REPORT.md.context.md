# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/047/original/M76-REPORT.md`

Original SHA-256: `99172b8af7c95308b033bfcf8dd31d353aa70c6a25d41db3a8806af115e8f62b`

Original lines: 42–68.

42	## 2. Exact reconstruction from the archived witnesses
43	
44	For each tame gate the review reads the exact archived `d^2` and `q_mu`
45	numerator/denominator arrays.  It independently recomputes `f^mu` by the hook
46	formula and then uses
47	
48	`||t_mu||^2 = C(n-1,j) f^theta q_mu/f^mu`,
49	
50	`r_mu=||t_mu||^2/m`, and
51	
52	`a_(gamma,mu)=m|d_(gamma,mu)|^2`.
53	
54	Therefore the raw block contribution has two independently identical forms:
55	
56	`f^mu a_(gamma,mu) r_mu = f^mu |d_(gamma,mu)|^2 ||t_mu||^2`.
57	
58	The review does not take either archived final `T_a` value as an arithmetic
59	input.  It recovers the old divided value only as a diagnostic equality.
60	
61	| gate | corrected raw physical `T_a` | cap | exact excess | cap ratio |
62	|---:|---:|---:|---:|---:|
63	| `n=18,j=6,a=b=3,c=2` | `160582822829/85260` | `51396202/35` | `35381674757/85260` | `36224413/28242984 > 1` |
64	| `n=19,j=6,a=b=3,c=2` | `204466088827/71920` | `137582445/64` | `199431265033/287680` | `10611004/8023575 > 1` |
65	
66	Hence both earlier tame `c=2` (T-a) PASS verdicts are wrong.  This is an
67	actual failure of the registered physical inequality, not a failure of a
68	surrogate estimate.
