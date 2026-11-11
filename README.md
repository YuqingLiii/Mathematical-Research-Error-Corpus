# Mathematical Research Error Corpus

65 naturally occurring mathematical error records from AI-assisted theoretical research. Each error has its own independent folder; research-problem names are metadata, not directory groups.

## Record format

The organization follows the error-analysis paper's **Research Setting and Error Collection** section. `index.json` contains four fields: `record_id`, `problem`, `summary`, and `evidence`.

```text
index.json
records/
  001/
    witness.md
    original/
  002/
    witness.md
    original/
  ...
```

Each `witness.md` presents the original statement, context and locator, the mathematical defect, checkable evidence, scope, classification, and adjudication notes. `original/` holds the available public source materials, with supplementary source windows in `original/context/`. Sources are preserved from the existing public release; this reorganization does not recover omitted materials or rerun computations. An error in an argument does not necessarily refute its target theorem.

Record identifiers are stable and intentionally nonconsecutive. There are 65 records; a record may have more than one classification label.

## All 65 errors

| Record | Error |
|---|---|
| [001](records/001/witness.md) | Necessity for the particular localization proof is not necessity for every construction. |
| [002](records/002/witness.md) | The self-pair tensor identity does not apply to a conjugate pair. |
| [003](records/003/witness.md) | The asserted uniform bound on epsilon^(-4u) is false. |
| [005](records/005/witness.md) | A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep. |
| [006](records/006/witness.md) | Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression. |
| [007](records/007/witness.md) | A positive finite-M correction factor was discarded when simplifying the upper bound. |
| [008](records/008/witness.md) | For the alternating symplectic kernel, squaring the transform gives the identity, not reflection. |
| [009](records/009/witness.md) | The displayed polynomial has been evaluated incorrectly. |
| [010](records/010/witness.md) | Cross-ruling differences can fall in a third ruling direction. |
| [011](records/011/witness.md) | An aggregate energy budget does not by itself construct coefficients obeying all the retained local magnitude, support, and symmetry constraints. |
| [012](records/012/witness.md) | The printed checksum differs from exact summation of the archived scan. |
| [013](records/013/witness.md) | A variance about its minimizing mean cannot bound squared deviations about every arbitrary center. |
| [014](records/014/witness.md) | A consequence derived only inside a contradiction branch was stated as an unconditional strict bound on a subset of the slacks. |
| [015](records/015/witness.md) | The largest integer strictly less than x is ceil(x)-1, not ceil(x). |
| [016](records/016/witness.md) | The balancing side channel need not have constant dimension or constant additive qubit cost. |
| [017](records/017/witness.md) | The written continuity modulus is undefined at output dimension d=1. |
| [018](records/018/witness.md) | The noncommuting factors are multiplied in the wrong order. |
| [019](records/019/witness.md) | Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace. |
| [020](records/020/witness.md) | The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs. |
| [021](records/021/witness.md) | The environment-support restriction can force phi=&#124;psi><psi&#124;, so the assumed nontrivial comparison domain does not exist. |
| [022](records/022/witness.md) | The comparison omits division by two and the entangled-family threshold is not 2/5. |
| [023](records/023/witness.md) | The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input. |
| [024](records/024/witness.md) | A self-complementary channel gives a counterexample to the universal bracketwise no-go. |
| [025](records/025/witness.md) | Positive two-way-assisted capacity does not exclude antidegradability. |
| [026](records/026/witness.md) | Excluding a counterexample forces some additional separating property, not specifically unitality or absence of a flag. |
| [027](records/027/witness.md) | The proposed universal PSD strengthening is false even for one copy. A positive projector does not make this exchange matrix a Gram matrix with a common ordered vector list. |
| [028](records/028/witness.md) | Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults. |
| [029](records/029/witness.md) | Containment in V permits adding a parity with a logical-observable component. A fault that is logical and undetected by the original detectors can then be detected by the new parity, so the claimed unchanged proof does not apply. |
| [030](records/030/witness.md) | Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ. |
| [031](records/031/witness.md) | Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix. |
| [032](records/032/witness.md) | Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition. |
| [033](records/033/witness.md) | The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget. |
| [034](records/034/witness.md) | The premise R≥d is lost in the root statement and its carried-forward caveats. An implication established under that hypothesis does not by itself establish the same implication for every round count. |
| [035](records/035/witness.md) | Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration. |
| [036](records/036/witness.md) | Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate. |
| [037](records/037/witness.md) | The verified search covered only unstaggered ancilla windows. Removing that restriction from the conclusion excludes legitimate staggered schedules without evidence. |
| [038](records/038/witness.md) | Exhibiting pairwise connectors does not establish that all imposed relations are generated by pairwise equalities. A valid construction imposes a four-term XOR relation while keeping all six pairwise equalities false. |
| [039](records/039/witness.md) | With two occurrences of one variable in the same clause, the wire's auxiliary XOR point is the third clause terminal, not a fresh point. The added gadget imposes an unintended constraint and breaks the satisfiability-preserving direction. |
| [040](records/040/witness.md) | Arbitrary bijections of symbol labels need not respect XOR translations, so they cannot generally be implemented by the asserted fixed conjugation around a single oracle call. |
| [041](records/041/witness.md) | The stated recipe does not supply enough data or inequalities to verify the claimed encoding. |
| [042](records/042/witness.md) | Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false. |
| [043](records/043/witness.md) | A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor. |
| [044](records/044/witness.md) | The uncapped exponent is impossible at the top endpoint q=N. |
| [045](records/045/witness.md) | The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N. |
| [046](records/046/witness.md) | Preserving the numerator and masked matrix norms transfers only the bound already established for the source matrix; it cannot establish an unproved source norm bound. |
| [047](records/047/witness.md) | A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity. |
| [048](records/048/witness.md) | The compressed contraction used &#124;d&#124;^2 instead of raw mass m&#124;d&#124;^2, making the reported T_a twenty times too small. |
| [049](records/049/witness.md) | The displayed integer product is incorrect. |
| [050](records/050/witness.md) | Projection can kill directions; independence before projection does not imply independence afterward. |
| [051](records/051/witness.md) | The decimal expansion of3N is wrong, and the displayed comparison using that wrong number is false. |
| [052](records/052/witness.md) | The contraction supplies a dimension factor that cancels the divisor d_rho. |
| [055](records/055/witness.md) | The direction of the moment/SOS separation was reversed. |
| [056](records/056/witness.md) | For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction. |
| [057](records/057/witness.md) | A competing sign pair outperforms the extrapolated affine branch beyond lambda=1/4. |
| [060](records/060/witness.md) | The follow-up problem formulation drops the positive-gap hypothesis required by the original channel gate. |
| [061](records/061/witness.md) | A valid but strictly dominated Haar bound is advertised as an additional necessary scalar obstruction. |
| [063](records/063/witness.md) | A stale support vector is used in the exploratory weighted calculation. |
| [065](records/065/witness.md) | Two copied input-vector values disagree with the independently regenerated determinant counts. |
| [066](records/066/witness.md) | An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset. |
| [067](records/067/witness.md) | The filter tested only two of four gain-positive residual shapes. In particular, a four-suffix with one qubit outside the target logical support can still give a positive gain after cancellation by a singleton. Requiring each hook to fit entirely inside the target support misses such configurations. |
| [071](records/071/witness.md) | 群平均可以产生不变的最优权重，但不保证所有最优权重都不变。因而只参数化 commutant 中的不变权重不能完成父节点要求的全部极值策略分类。 |
| [072](records/072/witness.md) | 旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。 |
| [074](records/074/witness.md) | A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold. |
| [075](records/075/witness.md) | The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two. |
| [077](records/077/witness.md) | 原程序存在 INCONCLUSIVE 分支，且对该原实例实际返回 INCONCLUSIVE，没有给出该 trivial-isotypic SOS 子问题的可行或不可行证书；这不足以支撑 settles the entire block exactly 的完成声明。 |
