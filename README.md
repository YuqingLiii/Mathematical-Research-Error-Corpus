# Mathematical Research Error Corpus

65 naturally occurring mathematical errors across 12 AI-assisted research problems. Each entry contains the original statement, context, an explanation and witness, and the scope of the error. Original record IDs are preserved; gaps in numbering are intentional.

This release contains only the 65 core error descriptions. Supporting source files, historical checks and earlier annotations remain accessible through the fixed-version source links in each entry and in Git history. A scoped error does not necessarily refute the overall research theorem.

## All 65 errors

- [001 — Necessity for the particular localization proof is not necessity for every construction.](errors/001.md)
- [002 — The self-pair tensor identity does not apply to a conjugate pair.](errors/002.md)
- [003 — The asserted uniform bound on epsilon^(-4u) is false.](errors/003.md)
- [005 — A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.](errors/005.md)
- [006 — Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.](errors/006.md)
- [007 — A positive finite-M correction factor was discarded when simplifying the upper bound.](errors/007.md)
- [008 — For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.](errors/008.md)
- [009 — The displayed polynomial has been evaluated incorrectly.](errors/009.md)
- [010 — Cross-ruling differences can fall in a third ruling direction.](errors/010.md)
- [011 — An aggregate energy budget does not by itself construct coefficients obeying all the retained local magnitude, support, and symmetry constraints.](errors/011.md)
- [012 — The printed checksum differs from exact summation of the archived scan.](errors/012.md)
- [013 — A variance about its minimizing mean cannot bound squared deviations about every arbitrary center.](errors/013.md)
- [014 — A consequence derived only inside a contradiction branch was stated as an unconditional strict bound on a subset of the slacks.](errors/014.md)
- [015 — The largest integer strictly less than x is ceil(x)-1, not ceil(x).](errors/015.md)
- [016 — The balancing side channel need not have constant dimension or constant additive qubit cost.](errors/016.md)
- [017 — The written continuity modulus is undefined at output dimension d=1.](errors/017.md)
- [018 — The noncommuting factors are multiplied in the wrong order.](errors/018.md)
- [060 — The follow-up problem formulation drops the positive-gap hypothesis required by the original channel gate.](errors/060.md)
- [061 — A valid but strictly dominated Haar bound is advertised as an additional necessary scalar obstruction.](errors/061.md)
- [063 — A stale support vector is used in the exploratory weighted calculation.](errors/063.md)
- [065 — Two copied input-vector values disagree with the independently regenerated determinant counts.](errors/065.md)

- [019 — Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.](errors/019.md)
- [020 — The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.](errors/020.md)
- [021 — The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.](errors/021.md)
- [022 — The comparison omits division by two and the entangled-family threshold is not 2/5.](errors/022.md)
- [023 — The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.](errors/023.md)

- [024 — A self-complementary channel gives a counterexample to the universal bracketwise no-go.](errors/024.md)
- [025 — Positive two-way-assisted capacity does not exclude antidegradability.](errors/025.md)
- [026 — Excluding a counterexample forces some additional separating property, not specifically unitality or absence of a flag.](errors/026.md)

- [027 — The proposed universal PSD strengthening is false even for one copy. A positive projector does not make this exchange matrix a Gram matrix with a common ordered vector list.](errors/027.md)

- [028 — Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.](errors/028.md)
- [029 — Containment in V permits adding a parity with a logical-observable component. A fault that is logical and undetected by the original detectors can then be detected by the new parity, so the claimed unchanged proof does not apply.](errors/029.md)
- [030 — Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.](errors/030.md)
- [031 — Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.](errors/031.md)

- [032 — Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.](errors/032.md)
- [033 — The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.](errors/033.md)
- [034 — The premise R≥d is lost in the root statement and its carried-forward caveats. An implication established under that hypothesis does not by itself establish the same implication for every round count.](errors/034.md)
- [035 — Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.](errors/035.md)

- [036 — Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.](errors/036.md)
- [037 — The verified search covered only unstaggered ancilla windows. Removing that restriction from the conclusion excludes legitimate staggered schedules without evidence.](errors/037.md)
- [066 — An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.](errors/066.md)
- [067 — The filter tested only two of four gain-positive residual shapes. In particular, a four-suffix with one qubit outside the target logical support can still give a positive gain after cancellation by a singleton. Requiring each hook to fit entirely inside the target support misses such configurations.](errors/067.md)

- [038 — Exhibiting pairwise connectors does not establish that all imposed relations are generated by pairwise equalities. A valid construction imposes a four-term XOR relation while keeping all six pairwise equalities false.](errors/038.md)
- [039 — With two occurrences of one variable in the same clause, the wire's auxiliary XOR point is the third clause terminal, not a fresh point. The added gadget imposes an unintended constraint and breaks the satisfiability-preserving direction.](errors/039.md)

- [040 — Arbitrary bijections of symbol labels need not respect XOR translations, so they cannot generally be implemented by the asserted fixed conjugation around a single oracle call.](errors/040.md)
- [041 — The stated recipe does not supply enough data or inequalities to verify the claimed encoding.](errors/041.md)
- [042 — Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.](errors/042.md)
- [043 — A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.](errors/043.md)
- [044 — The uncapped exponent is impossible at the top endpoint q=N.](errors/044.md)
- [045 — The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.](errors/045.md)
- [074 — A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold.](errors/074.md)
- [075 — The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two.](errors/075.md)

- [046 — Preserving the numerator and masked matrix norms transfers only the bound already established for the source matrix; it cannot establish an unproved source norm bound.](errors/046.md)
- [047 — A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.](errors/047.md)
- [048 — The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.](errors/048.md)

- [049 — The displayed integer product is incorrect.](errors/049.md)
- [050 — Projection can kill directions; independence before projection does not imply independence afterward.](errors/050.md)
- [051 — The decimal expansion of3N is wrong, and the displayed comparison using that wrong number is false.](errors/051.md)
- [052 — The contraction supplies a dimension factor that cancels the divisor d_rho.](errors/052.md)
- [055 — The direction of the moment/SOS separation was reversed.](errors/055.md)
- [077 — 原程序存在 INCONCLUSIVE 分支，且对该原实例实际返回 INCONCLUSIVE，没有给出该 trivial-isotypic SOS 子问题的可行或不可行证书；这不足以支撑 settles the entire block exactly 的完成声明。](errors/077.md)

- [056 — For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.](errors/056.md)
- [057 — A competing sign pair outperforms the extrapolated affine branch beyond lambda=1/4.](errors/057.md)
- [071 — 群平均可以产生不变的最优权重，但不保证所有最优权重都不变。因而只参数化 commutant 中的不变权重不能完成父节点要求的全部极值策略分类。](errors/071.md)
- [072 — 旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。](errors/072.md)
