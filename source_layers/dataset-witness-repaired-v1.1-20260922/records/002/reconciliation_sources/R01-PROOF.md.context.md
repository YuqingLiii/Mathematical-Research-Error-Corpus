# Source context 1

Source: `[PROJECT]/tracking/ai-proof-records-20260912/recovered-marathon-20260821/additivity-gap/PROOF.md`

Original SHA-256: `7bcddfcf1e7db06c2c3a4e812e51c28d33afe33434842e3463c56eec6f699ea7`

Original lines: 1735–1770.

1735	### Lemma 25 (the fixed conjugate-pair route is not ruled out by Lemma 4)
1736	
1737	For every finite-dimensional channel \(\Phi\),
1738	
1739	\[
1740	 \lim_{m\to\infty}{1\over m}
1741	 \Delta(\Phi^{\otimes m},\overline\Phi^{\otimes m})
1742	 =2\overline S_{\min}(\Phi)
1743	  -\overline S_{\min}(\Phi\otimes\overline\Phi).              \tag{99}
1744	\]
1745	
1746	There is no algebraic reason in Lemma 4 for the right side of (99) to vanish.
1747	
1748	**Proof.**  Entrywise conjugation preserves every output spectrum, so
1749	
1750	\[
1751	 S_{\min}(\overline\Phi^{\otimes m})
1752	 =S_{\min}(\Phi^{\otimes m}).
1753	\]
1754	
1755	After permuting tensor factors,
1756	\(\Phi^{\otimes m}\otimes\overline\Phi^{\otimes m}\) is
1757	unitarily equivalent to
1758	\((\Phi\otimes\overline\Phi)^{\otimes m}\).  Divide the definition of
1759	the gap by (m) and take the three regularized limits, exactly as in Lemma 3.
1760	This proves (99).  Lemma 4 instead uses the special identity
1761	\(\Phi^{\otimes m}\otimes\Phi^{\otimes m}=\Phi^{\otimes2m}\), which has
1762	no analogue for a general conjugate pair. \(\square\)
1763	
1764	### Dated correction 2026-08-20
1765	
1766	The sentence in Section 2 that Lemma 4 explains why
1767	~~simply tensoring a single Hastings counterexample with itself cannot settle
1768	the extensive question~~ is valid only for literal self-pairs
1769	\((\Phi,\Phi)\).  It does not rule out powers of a fixed conjugate pair
1770	\((\Phi,\overline\Phi)\); their normalized gap is (99).
