# Source context 2

Source: `[PROJECT]/paper/evidence_claim_gap_20260918/sources/historical_provenance_report.md`

Original SHA-256: `ba3fceaca083ce6134ed741676f4b5f2d91b72fe62561b6ef32624b9094e5a60`

Original lines: 599–632.

599	- 模型产物（**同日更早**的验证脚本）：`P/research/ksum/paper/ancillary/ksum_w3e_lemma2_verify.py` 与 `ksum_w3e_lemma2_generalk.py`（均 07-17 21:09）。
600	- 外审逐条意见：session `b5fea9c2`，2026-07-17T22:29。
601	
602	### 3. 最早的相关证据
603	脚本 docstring 写出了**完整配方**（论文中缺的每一项都在这里）：
604	
605	> general-k recipe (t=0):  omega = 2R-1, **u_j = omega^(j-1) (j<k), u_k = -sum**,
606	> tags **w_j = V*(2k+1)^(j-1) (j<k), w_k = -sum**;  V = P+1,
607	> P = k(R-1)(omega^(k-1)-1)/(omega-1), M = ((2k+1)^(k-1)-1)/2, **q = (P+1)(M+1)**.
608	
609	`ksum_w3e_lemma2_generalk.py` 进一步说明验证范围："for k=3..6, R=2..4 … verify EXHAUSTIVELY at **pattern level**"，并且"every wrong block-multiset `mu` (all C(2k-1,k)-1 of them), every payload box"。
610	
611	### 4. 最终声明
612	论文 Lemma 的陈述与 sketch：
613	
614	> For every `k≥3` and `R≥2` there is an **explicit encoding** … Consequently, if … then `Q(kSum) = Ω_k(√N q^{c/(k-1)})`.
615	>
616	> *Proof sketch.* Assign to block `j` a tag `w_j` with `Σ_j w_j=0` and a payload coefficient `u_j`. With `u_j = ω^{j−1}` for `ω = 2R−1`, a cross-block `k`-tuple sums to … (base-`ω` uniqueness), while every other block-multiset pattern is killed by choosing the tags separated at scale larger than the total payload spread … All patterns were enumerated and the encoding verified exhaustively by computer for `k ∈ {3,4,5}`.
617	
618	### 5. 重建的转折
619	
620	> 证据：
621	> 脚本里有完整配方（末位系数 `u_k = −Σ_{j<k} u_j`、显式 tag 公式、显式 `q = (P+1)(M+1)`、以及对所有错误 block-multiset 的模式级穷举），验证范围是 `k=3..6, R=2..4` 的小参数。
622	>
623	> 中间一步：
624	> 论文把配方压缩成一句 sketch：只写了 `u_j = ω^{j−1}`，没写最后一个系数如何取；tag 只说"分离到比 payload 展幅更大的尺度"，没有公式；穷举被写成一句"verified exhaustively by computer"。
625	>
626	> 声明：
627	> 存在显式编码，Lemma 成立（写成已证引理，而非构造设想）。
628	
629	外审列出的缺项与脚本里"有、但论文没写"的项**逐条对应**：`u_j` 的完整定义（若直接取 `u_j=ω^{j−1}`，全输入相等时 payload 和为 `r·Σ_j u_j` 一般非零）、是否取 `u_k=−Σ_{j<k}u_j`、base-ω 唯一性的适用整数范围、tag 的显式公式、任意错误 block multiplicity 不命中的证明。
630	
631	### 6. 溯源状态
632	`RECOVERED`
