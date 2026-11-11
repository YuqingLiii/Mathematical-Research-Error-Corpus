# 逐条原文、上下文与 witness 对照

以下原文和 witness 直接来自冻结 65 条数据；只新增分类及其解释。标签不推断隐藏 CoT。

## 001 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/001/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/001/materials.json)

### 原文

> The entire problem is therefore to choose *different* tuples \(U^{(r)}\) so
> that entangled inputs within \(\mathcal R^{[k]}\) do not appreciably lower its
> minimum output entropy.

定位：Proof-development artifact, section 3, lines 211–213; original write 2026-08-20T23:41:57.547Z
上下文：The argument uses different finite unitary tuples at different tensor positions to control minimum output entropy by iterated localization. The selected sentence presents this route choice as necessary for the entire extensive-gap problem.

### Witness

Necessity for the particular localization proof is not necessity for every construction.

For any fixed channel pair (Phi,Psi), the normalized tensor-power gap tends to Sbar_min(Phi)+Sbar_min(Psi)-Sbar_min(Phi tensor Psi). For Psi=conjugate(Phi), this is 2 Sbar_min(Phi)-Sbar_min(Phi tensor conjugate(Phi)), which the localization argument does not show to be zero. Thus the derivation leaves a fixed-pair alternative unexcluded. This diagnoses an unsupported necessity inference; it does not establish that a positive fixed-pair regularized gap exists.

Witness 范围：argument_invalid

### 分类理由

- IV：某一 localization 路线需要不同 tuple，不推出整个问题的所有可行路线都必须使用不同 tuple；witness 指出固定共轭对的正则化间隙并未被排除。

## 002 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/002/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/002/materials.json)

### 原文

> This explains why simply tensoring a single Hastings counterexample with
> itself cannot settle the extensive question.

定位：Proof-development artifact, section 2, lines 150–151; original write 2026-08-20T23:41:57.547Z
上下文：Lemma 4 proves a zero normalized tensor-power gap for a literal self-pair (Phi,Phi). The following explanatory sentence extends its interpretation to a Hastings counterexample, which generally uses the distinct conjugate pair (Phi,conjugate(Phi)).

### Witness

The self-pair tensor identity does not apply to a conjugate pair.

For a_m=S_min(Phi^tensor m), the self-pair gap is 2a_m-a_2m and its ratio to m tends to zero. For a conjugate pair the joint term is S_min((Phi tensor conjugate(Phi))^tensor m), not a_2m. Its normalized limit is a different regularized entropy and the cancellation used in Lemma 4 is unavailable.

Witness 范围：argument_invalid

### 分类理由

- IV：关于自配对 (Phi,Phi) 的消去引理被用于共轭配对 (Phi,bar Phi)。后者的联合熵不是 a_2m，故引理的适用对象不满足原前提。

边界说明：不把对象不同自动再计 II：这里可直接定位的是把一个正确引理应用到不满足对象前提的情形。

## 003 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/003/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/003/materials.json)

### 原文

>  m^{4u}\le e^4,qquad u^{-2}=(1+\log m)^2,qquad
>  \varepsilon^{-4u}\le C,                                    \tag{234}

定位：Proof-development artifact, equation (234), lines 4288–4295; original write 2026-08-21T16:15:33.756Z
上下文：The auxiliary parameters are m=floor(gamma n epsilon^2/log^2(n epsilon^2)), u=1/(1+log m), with m>=2 and epsilon>=2/sqrt(n). The claimed C is independent of epsilon and n.

### Witness

The asserted uniform bound on epsilon^(-4u) is false.

Fix X>4 and gamma>0 with m=floor(gamma X/log^2 X)>=2. Set epsilon=sqrt(X/n) and let n grow. Then n epsilon^2=X and epsilon>=2/sqrt(n); m and u>0 remain fixed. But epsilon^(-4u)=(n/X)^(2u) tends to infinity. For example X=10^6 and gamma=0.01 give m=52.

Witness 范围：statement_false

### 分类理由

- III：统一数量级估计错误：固定 n*epsilon^2 后 m、u 不变，但 epsilon^(-4u)=(n/X)^(2u) 无界，不能吸收入与参数无关的常数。

## 005 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/005/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/005/materials.json)

### 原文

> Choose balanced integer representatives of the three field coefficients \(t_u,t_v,t_w\), and let \(q_T\) be the corresponding vector in the real line-coordinate space. A continuous fixed-magnitude line-phase variation has
> 
> $$
> C_{\rm ind}(\theta)
> =
> 2\sum_T
> \operatorname{Re}
> \left(
> A_Te^{i\langle q_T,\theta\rangle}
> \right).
> $$
> 
> If \(C=1\), then the coefficient field is physical and gives a global maximum of \(C\) on the entire phase torus. Hence
> 
> $$
> \boxed{
> \sum_Tq_T\,\operatorname{Im}A_T=0,
> }
> \tag{10.1}
> $$
> 
> and
> 
> $$
> \boxed{
> \sum_T
> (\operatorname{Re}A_T)\,
> q_Tq_T^{\mathsf T}
> \succeq0.
> }
> \tag{10.2}
> $$
> 
> These are the exact stationarity and Hessian conditions.

定位：round-18-response.md, lines 796–829
上下文：The total cubic objective is C=C_dep+C_ind. The proposed continuous line-phase variation multiplies coefficients by exp(i t theta_L), where t is a balanced integer representative of a finite-field element. The displayed equations differentiate only C_ind.

### Witness

A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

For odd D, set t=(D-1)/2. The same-line triple (t,t,1) sums to zero in F_D, so its cubic term belongs to C_dep. Its balanced integer sum is D, however, so the proposed continuous deformation multiplies that monomial by exp(iD theta_L), which is not constant. The gradient and Hessian of C_dep are therefore generally nonzero; equations using only C_ind are not the derivatives of the full objective. For D=5, the triple is (2,2,1).

Witness 范围：argument_invalid

### 分类理由

- IV：把离散相位不变性沿用到连续变形，进而只对 C_ind 求导。witness 的同线单项在连续变形下含 exp(iD theta)，所以全目标驻点/Hessian 条件不能由该局部导数推出。

边界说明：错误导数是错误不变性假设的后果，未单独定位另一处求导运算错误，因此不重复加 III。

## 006 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/006/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/006/materials.json)

### 原文

> Consequently,
> 
> $$
> \begin{aligned}
> \mathbb E_{s,t}
> \langle\Delta_{L,s}\Theta_{M,t}\rangle
> &=
> \langle\overline\Delta\,\overline\Theta\rangle\\
> &=
> \sum_{k,j}
> \left(\frac1D-p_k\right)
> \left(\frac1D-r_j\right)
> \mathcal B_{kj}.
> \end{aligned}
> \tag{6.1}
> $$
> 
> The phases of \(\mathcal B_{kj}\) remain. The higher terms in
> `TwoLinePlaquette` similarly retain three- and four-point Bargmann data.
> 
> Thus neither the four-corner subtraction nor the full uniform average over the two cyclic shifts reduces the two-line condition to the two autocorrelation shadows.
> 
> A phase-free two-line contradiction is not obtained.

定位：round-20-response.md, lines 653–675
上下文：Delta and Theta are perturbations from shifting two stabilizer lines. The full TwoLinePlaquette expression contains a bilinear term and higher-order terms. The excerpt computes only the bilinear average explicitly.

### Witness

Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

The source evaluates E<Delta Theta>=sum_(k,j)(1/D-p_k)(1/D-r_j) B_(kj), then says the higher terms “similarly retain” phase data without evaluating their sum. A full expression F1(theta)+F2(theta) can be phase-independent even when F1 is not (take F2=-F1+c). Therefore the displayed partial calculation does not imply the claimed noncancellation for TwoLinePlaquette. A complete average, or a coefficient that provably survives the complete sum, is required.

Witness 范围：argument_invalid

### 分类理由

- IV：只算出双线性项的相位依赖，就断言完整平均仍有相位依赖；没有排除高阶项抵消。缺的是全和不消去的推断，不是已展示加法算错。

## 007 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/007/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/007/materials.json)

### 原文

> \boxed{
> |\alpha_z\mathcal R_{\mathbf1_\Gamma}(z)|
> \le
> \sqrt8\,D
> \sqrt{\lambda_z^2+M^2+6M}
> <4DM,
> }
> \tag{8.5}

定位：round-21-response.md, lines 1253–1260
上下文：D>0, M>0, and the stated scalar premise is |lambda_z|<=M. The last strict inequality is a simplification of an upper envelope, not a separately proved estimate.

### Witness

A positive finite-M correction factor was discarded when simplifying the upper bound.

Substituting the allowed endpoint |lambda_z|=M gives sqrt(8)D sqrt(2M^2+6M)=4DM sqrt(1+3/M)>4DM for every finite M>0. Thus the stated premise yields only the larger envelope, and cannot justify the strict inequality printed in (8.5).

Witness 范围：statement_false

### 分类理由

- III：把显式上包络化简成了更小的数值界。代入允许的 |lambda|=M，左边等于 4DM*sqrt(1+3/M)>4DM。

## 008 — Channel additivity violations

**一级类别：II 数学知识错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/008/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/008/materials.json)

### 原文

> The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

定位：round-23-response.md, lines 234
上下文：The transform is the normalized symplectic Fourier transform (Ff)(k)=D^(-1) sum_p f(p) omega^[p,k] on F_D^2, where [p,k] is alternating and omega is a primitive Dth root of unity.

### Witness

For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

Compute F^2 f(l)=D^(-2) sum_(p,k) f(p) omega^([p,k]+[k,l]). Since [k,l]=-[l,k], the exponent is [p-l,k]. Character orthogonality makes the inner sum D^2 when p=l and zero otherwise, so F^2 f(l)=f(l). It does not give f(-l). Evenness must be justified separately.

Witness 范围：statement_false

### 分类理由

- II：把当前交替辛 Fourier 变换的平方说成反射；按已给定义其平方为恒等。这是可见的变换性质错述，而不是已定位到某次数值运算。

边界说明：II/III 边界：原文给出的是变换性质断言，没有展示出错的平方运算步骤，按可见性质错述归 II；不能据此断言模型内部记忆失误。 2026-09-23 核对原响应后，仍未见 F^2=反射这一错误前提的推导，保持 II。

## 009 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/009/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/009/materials.json)

### 原文

> At \(|T|=777716\), this is the first undecided finite determinant/kernel system. The dictionary has at most
> 
> $$
> r_1^2+r_1+1
> =
> 970353651
> $$
> 
> columns, but the coefficient vector has the special nonlinear form (8.2). Merely proving \(G_T\) singular would be necessary, not sufficient: its kernel must contain a vector with that exact conjugate-quadratic structure.

定位：round-28-response.md, lines 725–733
上下文：The displayed dictionary-count expression uses r1=777716. This is a local arithmetic display, not the main theorem’s proof.

### Witness

The displayed polynomial has been evaluated incorrectly.

Exact integer arithmetic gives 777716^2+777716+1=604842954373, whereas 970353651=31151*31150+1. The printed number belongs to a different expression.

Witness 范围：computation_false

### 分类理由

- III：给定 r1=777716，显示的 r1^2+r1+1 应为 604842954373，而非打印值。未见同一次正确结果被抄坏的必要证据，不擅自标成 V。

## 010 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/010/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/010/materials.json)

### 原文

> It is strictly smaller and more structured than the original \(D^2\) baseline phase problem:
> 
> * parameters lie on four explicit ruling lines;
> * each distinct-slope line-pair contributes at most one product to each \(K_\Delta\);
> * rank-one differences are confined to the two ruling directions;
> * every other contribution is a fully explicit nondegenerate dual chirp.
> 
> No exact solution or contradiction is obtained.

定位：round-29-response.md, lines 1356–1363
上下文：The finite-field construction uses two paired ruling directions in the rank-one quadratic cone, represented in coordinates (a,b,c) with discriminant 4ac-b^2. The claimed restriction concerns differences between points on the chosen rulings.

### Witness

Cross-ruling differences can fall in a third ruling direction.

Over F_7, take the selected-ruling points (1,1,0) and (2,3,1). Their difference is (6,5,6)=6(1,2,1), and 4*6*6-5^2=119=0 mod 7. It lies in the rank-one ruling of slope 2, not either chosen ruling direction 0 or 1. Thus the classification of cross differences is false.

Witness 范围：statement_false

### 分类理由

- IV：错误概括所构造差向量的结构。合法的跨 ruling 差可处在第三个秩一方向，故所列穷尽性判断不成立。

## 011 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/011/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/011/materials.json)

### 原文

> 
> 1. the exceptional sequence \(T_\nu\);
> 2. ordinary coordinate magnitudes \(B\);
> 3. central evenness;
> 4. an ordinary support allowance of \(P_{\rm Sid}\) slots per \(\nu\);
> 5. total ordinary \(\ell_2\) energy \(\mathcal E_{\rm ord}\).
> 
> For each \(\nu\), distribute the required cancellation equally over the available ordinary slots. The minimum ordinary coefficient energy needed to cancel the exceptional term is
> 
> $$
> \frac{D+1}{P_{\rm Sid}}|T_\nu|^2.
> $$
> 
> Summed over \(\nu\),
> 
> $$
> \mathcal E_{\min}
> =
> \frac{D+1}{P_{\rm Sid}}\mathcal E_T.
> $$
> 
> [...]
> 
> Hence
> 
> $$
> \mathcal E_{\rm ord}
> \ge
> \frac{D-2}{4}\mathcal E_T
> >
> \frac{D+1}{P_{\rm Sid}}\mathcal E_T.
> $$
> 
> The remaining ordinary energy can be added in coefficient pairs whose physical contributions cancel identically.
> 
> Thus there is an abstract magnitude-compatible, centrally even coefficient relaxation satisfying:
> 
> * every scalar mirror equation;
> * the exact exceptional energy;
> * the exact ordinary total \(\ell_2\) energy;
> * the same support allowance.
> 
> It need not come from cofactor cross-correlations and need not satisfy the global Fourier-\(+1\) phase equations. Therefore:

定位：round-37-response.md, lines 1044–1063, 1081–1100
上下文：The proposed relaxation fixes exceptional coefficients, ordinary magnitude constraints, central evenness, a support allowance per frequency, and one total squared-norm budget. The response infers existence of a compatible coefficient assignment from an aggregate energy comparison.

### Witness

An aggregate energy budget does not by itself construct coefficients obeying all the retained local magnitude, support, and symmetry constraints.

The comparison E_ord>=(D-2)E_T/4 > (D+1)E_T/P_Sid is only an aggregate energy inequality. The proposed construction must additionally specify allowed coefficient positions, obey each magnitude constraint and central-even pairing, and solve every mirror equation simultaneously. The excerpt gives neither a compatible assignment nor an argument that adding cancelling pairs preserves the already used support and magnitude constraints. Thus the stated existence of the full relaxation is not established by the scalar energy calculation.

Witness 范围：argument_invalid

### 分类理由

- IV：总能量充足不是存在同时满足支撑、幅度、偶性和全部 mirror 方程的系数构造的充分条件；所称 relaxation 的存在未由该比较建立。

## 012 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/012/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/012/materials.json)

### 原文

> $$
> \boxed{
> \sum \theta^2K^{(4)}_\theta
> =
> 7149371020340881916998112.
> }
> \tag{32}

定位：round-51-response.md, lines 681–687
上下文：K_theta^(4) is the exact support count in a saved critical scan with 150150 distinct theta values. The excerpt reports its second-moment checksum.

### Witness

The printed checksum differs from exact summation of the archived scan.

Parsing the archived rows as (theta,K_theta) and evaluating sum(theta*theta*K_theta) using integers gives 7149371020340889916998112. The printed integer is 7149371020340881916998112, smaller by 8000000000. A reproducible check is: rows={int(t):int(k) for t,k in re.findall(r"^theta=(\d+) exact=(\d+) sharp_margin=-?\d+$",scan,re.M)}; assert len(rows)==150150; sum(t*t*k for t,k in rows.items()). The scan must accompany this record as a verification fixture.

Witness 范围：computation_false

### 分类理由

- III：归档扫描行的精确二阶矩和比打印整数大 8000000000，故该数值汇总错误；仅有事后重算不能证明原生成时先算对后抄错。

## 013 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/013/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/013/materials.json)

### 原文

> For cofactor \(i\), pad the magnitude array with zeros to length \(S_i\), and let
> 
> $$
> \bar a_i=\frac{L_i}{S_i}.
> $$
> 
> Then
> 
> $$
> \frac{D_i}{S_i}
> =
> \sum_{\xi=1}^{S_i}
> \bigl(|A_i(\xi)|-\bar a_i\bigr)^2,
> \qquad
> D_i=S_ie_i^2-L_i^2.
> \tag{6.1}
> $$
> 
> Restrict this sum to:
> 
> * the \(G_i\) surviving unit anchors;
> * the \(N_i\) surviving complete opposite-sign pairs.
> 
> For arbitrary \(\mu\in\mathbb R\),
> 
> $$
> \frac{D_i}{S_i}
> \ge
> G_i(1-\mu)^2
> +
> \sum_{p=1}^{N_i}
> \left[
> (r_{p,+}-\mu)^2+(r_{p,-}-\mu)^2
> \right].
> \tag{6.2}
> $$

定位：round-55-response.md, lines 577–612
上下文：D_i=S_i e_i^2-L_i^2 is S_i times the squared-deviation sum about the actual mean bar(a)_i=L_i/S_i. G_i counts retained unit anchors and N_i counts retained opposite-sign pairs with magnitudes r_(p,+),r_(p,-).

### Witness

A variance about its minimizing mean cannot bound squared deviations about every arbitrary center.

For any nonempty selected coordinate set, the right side of (6.2) grows quadratically as |mu| tends to infinity, whereas D_i/S_i is fixed and finite. As a minimal exact example, one unit coordinate has S_i=L_i=e_i^2=G_i=1 and N_i=0, so D_i/S_i=0; choosing mu=0 makes the asserted right side 1. The valid route evaluates the selected deviations at the actual mean first, then lower-bounds them by their minimum over mu.

Witness 范围：statement_false

### 分类理由

- IV：关于实际均值的偏差恒等式，不能推出关于任意中心 mu 的所报下界；witness 可使右侧无界而左侧固定。

## 014 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/014/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/014/materials.json)

### 原文

> with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census gives
> 
> $$
> \boxed{
> \Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
> }
> $$
> 
> [...]
> 
> $$
> \Delta_{\rm ray}
> +\Delta_{\rm flat}
> +\Delta_{\rm Young}
> +\Delta_{\rm group}<HE.
> \tag{1.3}
> $$
> 
> Then, individually,
> 
> $$
> \Delta_{\rm ray}<HE,\qquad
> \Delta_{\rm flat}<HE.
> \tag{1.4}
> $$

定位：round-59-response.md, lines 14–20, 118–132
上下文：The proof introduces four nonnegative slacks: ray, flat, Young, and group. Its detailed argument assumes their total is less than H E as a contradiction hypothesis, with H=3318 in this case.

### Witness

A consequence derived only inside a contradiction branch was stated as an unconditional strict bound on a subset of the slacks.

Let T=Delta_ray+Delta_flat+Delta_Young+Delta_group. The argument derives (T<HE) => (Delta_ray+Delta_flat>HE), contradicting T<HE because all slacks are nonnegative. The valid unconditional conclusion is T>=HE, not Delta_ray+Delta_flat>HE. For a logical counterassignment, E=H=1, Delta_ray=Delta_flat=0, Delta_Young=1, Delta_group=0 makes T>=HE true and the claimed subsidiary bound false, while the contradiction implication holds vacuously.

Witness 范围：argument_invalid

### 分类理由

- IV：反证分支 T<HE 下推得的子量结论，被带出分支当成无条件结论。合法结论是总量 T>=HE，不是所报两项和必大于 HE。

边界说明：缺失的是证明内反证假设，不是原题条件，故不按 I。

## 015 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/015/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/015/materials.json)

### 原文

> Since \(D_i\le\Delta_{\rm flat}<HE\), equations (1.6) and (2.4) give
> 
> $$
> m_i<
> \frac{H\,127^2K^2}
> {126^2(K-H)S_i}.
> $$
> 
> The exact strict-integer ceilings are
> 
> $$
> \boxed{
> \begin{aligned}
> (m_i)=(&60996,48631,44023,40693,39789,38265,39011,\\
>        &38265,39789,40693,44023,48631,60996).
> \end{aligned}}
> \tag{2.6}
> $$

定位：round-59-response.md, lines 222–239
上下文：For each row, the source derives the strict real bound m_i<x_i, where x_i=H*127^2*K^2/[126^2*(K-H)*S_i]. It then labels a vector of ceilings as exact strict-integer values.

### Witness

The largest integer strictly less than x is ceil(x)-1, not ceil(x).

For integer m, m<x is equivalent to m<=ceil(x)-1. If x=2 exactly, the maximum admissible integer is 1, not 2; if x=2.3, it is 2, not 3. Consequently the printed thirteen ceilings must each be reduced by one to be sharp strict-integer maxima. Their use as conservative, larger deletion budgets may still be safe; the error is the exactness claim.

Witness 范围：computation_false

### 分类理由

- III：将严格实数上界转成最大整数时差一：m<x 的精确最大整数是 ceil(x)-1；原十三个 ceiling 不是所称的精确最大值。

## 016 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/016/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/016/materials.json)

### 原文

> A Holevo pair gap g for finite-dimensional channels N and M can, after balancing their one-shot
>   Holevo quantities within one bit by a bounded classical side channel and taking T = N' direct-sum
>   M', be converted into chi(T tensor T) - 2 chi(T) at least g - log_2(9/4), with only constant
>   additive qubit overhead.

定位：Proof-node creation event, 2026-08-30T01:21:04.780Z, JSONL line 3188
上下文：The proposed conversion balances the one-shot Holevo information of two channels by adding a classical side channel of size K, then forms a direct sum. The node was marked CONJECTURED; this record concerns the overly strong dimension-overhead clause, not a falsely certified final theorem.

### Witness

The balancing side channel need not have constant dimension or constant additive qubit cost.

If the Holevo quantities differ by Delta, balancing them within one bit requires |log2 K-Delta|<1, so log2 K>Delta-1. Taking channels with Holevo quantities log2 d and 0 makes the required overhead grow as log2 d. The final direct sum itself adds at most one qubit, but that does not erase the preceding balancing cost. The equal-Holevo special case avoids this cost.

Witness 范围：statement_false

### 分类理由

- III：资源开销估计漏掉平衡步骤：Holevo 差为 Delta 时需 log2 K>Delta-1，不能把总开销计为常数。原节点仍是 conjecture。

## 017 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/017/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/017/materials.json)

### 原文

> For output dimension `d`, define
> 
> `f_d(eps) = eps log_2(d-1) + h_2(eps)`.
> 
> Only sufficiently small `eps` is needed below. Audenaert's Theorem 1 gives
> 
> `|S(rho)-S(sigma)| <= f_d((1/2)||rho-sigma||_1)`
> 
> for `d`-dimensional states.

定位：Proof-artifact creation event, 2026-08-30T02:02:11.343Z, JSONL line 4003
上下文：The surrounding claim covers arbitrary finite output dimensions. This original write lacks the later separate treatment of one-dimensional outputs.

### Witness

The written continuity modulus is undefined at output dimension d=1.

Substituting d=1 produces log2(d-1)=log2(0), not a finite real number. A one-dimensional output state is uniquely [1] and its entropy is exactly zero, so that case must be handled separately with zero entropy variation; it is not covered by the displayed formula. This invalidates the stated all-dimensions argument, not its repaired conclusion.

Witness 范围：argument_invalid

### 分类理由

- IV：把含 log2(d-1) 的定理公式应用到任意有限输出维数，却未单列 d=1；这是适用域问题，不是对数函数的数值算错。

## 018 — Channel additivity violations

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/018/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/018/materials.json)

### 原文

>   - 'math "J=\\frac1{m^2}\\sum_{a,b}|A_{ab}\\rangle\\rangle \\langle\\langle A_{ab}|, \\qquad A_{ab}=U_b^*U_a,"':
> 
> [...]
> 
>   - paragraph: with the multiplicative consistency
>   - 'math "A_{ab}A_{bc}=A_{ac}."':

定位：Follow-up replay R06, final answer, visible DOM lines 654 and 2348–2349
上下文：The response defines the common pair-difference matrices by A_ab=U_b^*U_a and then states a multiplicative consistency relation. This is one occurrence of a unique matrix-order error also seen in other replay outputs.

### Witness

The noncommuting factors are multiplied in the wrong order.

With A_ab=U_b^*U_a, the valid cancellation is A_bc A_ab=U_c^*U_b U_b^*U_a=A_ac. The stated reverse order need not hold. Take U_a=I, U_b=X=[[0,1],[1,0]], and U_c=Z=[[1,0],[0,-1]]. Then A_ab=X, A_bc=ZX, and A_ab A_bc=XZX=-Z, whereas A_ac=Z. Thus the displayed equality is false.

Witness 范围：statement_false

### 分类理由

- III：非交换矩阵乘积的消去次序写反。按定义应为 A_bc A_ab=A_ac，Pauli X、Z 给出精确反例。

## 019 — Werner–Holevo zero-capacity boundary

**一级类别：II 数学知识错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/019/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/019/materials.json)

### 原文

> class ExtensionSDP:
>     def __init__(self) -> None:
>         self.rho = cp.Variable((SYM_DIM, SYM_DIM), symmetric=True, name="rho")
>         self.t = cp.Variable(name="t")
>         self.x = cp.Parameter(name="x")
>         self.eta = V @ self.rho @ V.T

定位：Semidefinite-program script creation, 2026-07-28T22:15:31.150Z, JSONL line 130
上下文：V is the isometry onto A tensor Sym^2(B), of dimension 3 times 6 = 18. The frozen task asked for an extension invariant under swapping two qutrit B systems, not necessarily supported only in their symmetric subspace.

### Witness

Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

Let v=(|01>-|10>)/sqrt(2) and X=|0><0|_A tensor |v><v|. X is positive semidefinite and obeys S X S=X because Sv=-v. It is therefore swap-invariant, but its support lies entirely in the antisymmetric B sector and cannot be written V rho V^T. In the qutrit case the omitted block has dimension 3 times 3 = 9. The code solves a restricted feasibility problem, so its infeasibility cannot certify the original criterion.

Witness 范围：argument_invalid

### 分类理由

- II：把交换不变扩展与只支撑于对称子空间的扩展混同。反对称纯态投影仍交换不变，却不在该参数化内。

边界说明：同一概念混淆造成可行集缩小，只计 II，不再把同一事实换名重复计 I/IV。 2026-09-23 核对完整 proposer 会话：原任务为正确 27 维条件，错误参数化首次见于第 130 行；48 个加密 reasoning 块无非空明文摘要，未见先行等价推导。

## 020 — Werner–Holevo zero-capacity boundary

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/020/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/020/materials.json)

### 原文

> - **Pure-input structure (verify exactly first):** for a pure qutrit psi (take real psi and
>   generic complex psi), spec Λ_x(psi) = {x/2, x/2, 1-x} and
>   spec Λ_x^c(psi) = {1-x, x/2, x/2, 0} — B-side full rank, E-side one-dimensional kernel.

定位：Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522
上下文：The claim concerns Lambda_x(rho)=(1-x)rho+(x/2)(Tr(rho)I-rho^T), and is explicitly requested for both real and generic complex pure inputs. The commission says “verify exactly first,” so this is an asserted working formula being tested, not a completed theorem.

### Witness

The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

Take x=9/20 and psi=(1,i,1)/sqrt(3). Then |psi^T psi|^2=1/9. Writing a=1-x and b=x/2, Lambda_x(|psi><psi|)=bI+a|psi><psi|-b|bar(psi)><bar(psi)| has eigenvalues b and [(1-b) +/- sqrt((1-b)^2-4ab|psi^T psi|^2)]/2. These are 9/40 and (31 +/- 3 sqrt(97))/80, not {11/20,9/40,9/40}.

Witness 范围：statement_false

### 分类理由

- III：所报纯输入谱公式不等于合法复输入的精确特征值。这里只将谱计算结果判错，不推测其内部怎样产生，也不把待检验公式写成已证定理。

边界说明：III/IV 边界：直接可检验的错误是具体谱值，归 III；不推测其源自实输入向复输入推广的心理过程。

## 021 — Werner–Holevo zero-capacity boundary

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/021/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/021/materials.json)

### 原文

> - D1 (derivation check, exact): verify the pure-output spectra claims symbolically; verify
>   the epsilon-expansion bookkeeping NUMERICALLY at high precision: for random (psi, phi)
>   kernel-avoiding pairs at x = 9/20, fit Ic((1-eps)psi + eps phi) against
>   c1*eps + O(eps^2 log eps) and confirm the fitted c1 matches
>   `-Tr[Λ(phi-psi) log Λ(psi)] + Tr[Λ^c(phi-psi) log Λ^c(psi)]` to >= 8 digits; also confirm
>   kernel-HITTING phi produce the -eps log(1/eps) plunge. GATE G0.
> 
> [...]
> 
>   over pure psi and kernel-avoiding states phi (parameterize phi on the 3-dim support
>   constraint; >= 150 restarts). A_1 > 0 anywhere

定位：Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522
上下文：The proposed first-order test requires a distinct comparison state phi satisfying supp Lambda_x^c(phi) subset supp Lambda_x^c(psi). It treats this as a three-dimensional domain from which random kernel-avoiding pairs can be drawn.

### Witness

The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.

For psi=|0> and 0<x<1, use Kraus operators K0=sqrt(1-x)I and K_(mu+1)=sqrt(x/2)A_mu, (A_mu)_(jk)=epsilon_(mu j k). The complementary output has kernel vector z=(0,1,0,0). Positivity and support inclusion imply Tr(K1 phi K1^dagger)=0, hence supp(phi) subset ker K1=span{|0>}. Since phi has trace one it equals |0><0|. The claimed random distinct-pair construction therefore fails already in this exact instance; generic tests in the recorded check also had one-dimensional allowed support.

Witness 范围：argument_invalid

### 分类理由

- IV：所选探索路线假定存在非平凡 kernel-avoiding 扰动态域，但支撑条件在精确例子中强制 phi=psi；因此所宣称的随机不同对构造不可行。

## 022 — Werner–Holevo zero-capacity boundary

**一级类别：IV 逻辑推理错误、III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/022/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/022/materials.json)

### 原文

> [2/5, 1)**. Below the onset the same machinery is *strictly stronger than at n = 1* — at x = 7/20 an
> entangled 2-copy input gives the exact value **1102933/9570000 = 0.115249007…** versus
> d₁(7/20) = 13/132 = 0.098484848… (17 % larger, exact rationals) — so the n = 2 layer is genuinely
> more powerful, yet it dies at exactly the same threshold 2/5.

定位：Two-copy analysis artifact, 2026-07-30, lines 22–25
上下文：The raw two-use first-order coherent-information coefficient is compared against a one-use coefficient at x=7/20. Capacity is normalized per channel use. The same sentence also asserts a common zero-crossing threshold.

### Witness

The comparison omits division by two and the entangled-family threshold is not 2/5.

The comparable two-use coefficient is (1102933/9570000)/2=1102933/19140000, whereas the one-use coefficient is 13/132. Their exact ratio is 84841/145000, approximately 0.5851<1, so the two-use value is about 41.5% lower per use. The entangled family changes sign at the unique root in (0,1) of 19x^4-21x^3-14x^2+28x-8, approximately 0.3912977695<0.4; substitution x=2/5 gives 64/625>0, not a zero.

Witness 范围：statement_false

### 分类理由

- IV：两次使用的原始系数直接与单次使用系数比较，不能推出每次使用更强；正确除以二后比值约 0.5851。
- III：另有独立的零点数值判断错误：对应多项式在 2/5 的值为 64/625，不是零；实际零点约 0.3913。

边界说明：两个标签有两个不同的 source/witness 子依据：每次使用比较的逻辑失配，以及多项式零点计算错误。

## 023 — Werner–Holevo zero-capacity boundary

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/023/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/023/materials.json)

### 原文

>     # environment kernel: analytic basis  (0, conj(u+iv)) and (1, -i kappa w),
>     # kappa = sqrt(2(1-x)/x); verified below to be a basis of ker Lambda^c(P_psi).
>     kappa = sp.sqrt(2 * (1 - x) / x)
>     k1 = sp.Matrix([0, *list(sp.simplify(sp.sqrt(2) * psi_bar))])
>     k2 = sp.Matrix([1, *list(sp.simplify(-sp.I * kappa * third))])
>     analytic_kernel_pass = zero_matrix(lamc_p * k1) and zero_matrix(lamc_p * k2)
>     analytic_kernel_orthogonal = zero((k1.H * k2)[0, 0])
>     pi_e = sp.simplify(projector(k1) + projector(k2))

定位：Preserved isotropic weight-operator script, function weight_operators, lines 92–101
上下文：The script later instantiates psi=(0,1,-i)/sqrt(2) and third=(1,0,0). It labels third as the oriented cross product and uses the displayed formula for an environment-kernel basis. This release excerpt isolates the concrete basis defect from the legacy record, which also mentioned separate sign corrections.

### Witness

The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.

Let kappa=sqrt(2(1-x)/x). For the script’s psi and Kraus convention, the complementary output has entries G00=1-x, G01=i sqrt(x(1-x)/2), G10=-i sqrt(x(1-x)/2), and G11=x/2. Its proposed k2=(1,-i kappa,0,0) gives G k2=(2(1-x),-i sqrt(2x(1-x)),0,0), nonzero for 0<x<1. At x=1/2 the residual is (1,-i/sqrt(2),0,0). Therefore the constructed projector and resulting weight operator are wrong. The archived script reports d1=1-x, whereas the corrected operator gives (1-x)(2-5x)/(2-x), equal to -11/124 at x=9/20 instead of 11/20.

Witness 范围：computation_false

### 分类理由

- III：核向量符号错误。按脚本 Kraus 约定直接相乘得到 G*k2 非零，导致后续投影与权算子计算错误。

## 024 — Quantum-capacity superactivation

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/024/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/024/materials.json)

### 原文

> 任何 Q=0 证明必须全局控制熵和,不能逐因子分解

定位：Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540
上下文：Translation: “Any Q=0 proof must control the entropy sum globally and cannot decompose factor by factor.” Failure of a bracketwise proof for the selected channel pair was generalized into a universal prohibition.

### Witness

A self-complementary channel gives a counterexample to the universal bracketwise no-go.

For the 50% erasure channel A_(1/2), receiver and environment channels are unitarily equivalent. For A_(1/2) tensor A_(1/2), the corresponding receiver/environment conditional-entropy brackets match individually and each difference is zero. Their sum therefore proves coherent information zero by a legitimate per-bracket argument. Failure of a bracket bound for the originally selected pair cannot rule out this case.

Witness 范围：statement_false

### 分类理由

- IV：一种逐因子界的失败，被推广成所有 Q=0 证明都不许逐因子分解；擦除信道配对的逐项零差给出反例。

## 025 — Quantum-capacity superactivation

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/025/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/025/materials.json)

### 原文

> The two-way capacity K6 shows Q^↔(Λ_ZW) ≥ 0.0409, which proves Λ_ZW itself is not antidegradable. Since two-way capacity of a tensor product is at least the two-way capacity of either factor, this means Q^↔(T) ≥ 0.0409 as well, so T cannot be antidegradable either.

定位：Visible reasoning block, 2026-07-30T05:38:38.545Z, JSONL line 1813
上下文：The agent tries to reject antidegradability of a candidate product channel T using a positive two-way-assisted quantum capacity. The superscript double arrow denotes assistance by two-way classical communication.

### Witness

Positive two-way-assisted capacity does not exclude antidegradability.

The d-dimensional 50% erasure channel is self-complementary and hence antidegradable. Send halves of maximally entangled pairs through it. The receiver identifies non-erased uses and communicates their positions back; half the uses retain maximally entangled pairs, giving a two-way-assisted rate at least (1/2) log2 d>0. Thus antidegradable does not imply Q_two_way=0, and the displayed inference is invalid.

Witness 范围：argument_invalid

### 分类理由

- IV：由正双向辅助容量推出非反可降解的蕴含不成立。50% 擦除信道同时反可降解且有正双向辅助容量。

边界说明：II/IV 边界：容量概念有关，但原文明确可见的是由正容量推出非反可降解的错误蕴含，故只计 IV。

## 026 — Quantum-capacity superactivation

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/026/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/026/materials.json)

### 原文

> 任何证明都不能只靠 Λ_ZW 的 cALN 性;幺正性(无旗性)是被逼出来的必要假设

定位：Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540
上下文：Translation: “No proof can rely only on Lambda_ZW being cALN; unitality (flaglessness) is a forced necessary hypothesis.” The source proposes unitality as the separator between its target and an erasure-channel counterexample. Here cALN refers to a receiver-versus-environment information-order property.

### Witness

Excluding a counterexample forces some additional separating property, not specifically unitality or absence of a flag.

The known activating pair shows only that the information-order assumption alone is insufficient. Formally, from a counterexample C satisfying A but not the desired conclusion, a successful strengthened theorem must restrict A enough to exclude C. It does not follow that every successful restriction equals the particular proposed predicate “unital.” No theorem in the argument makes unitality a necessary property of all zero-capacity pairs. The valid conclusion is that it is one candidate separator.

Witness 范围：argument_invalid

### 分类理由

- IV：必须排除某个反例不等于必须选择指定的 unital/无旗条件；把一种候选限制说成所有成功证明都必需的限制。

## 027 — Bound entanglement with negative partial transpose

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/027/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/027/materials.json)

### 原文

> - 2026-07-29 — decision-layer reduction note (unreviewed): K_i = (1/2)(I + 2 Pi_i^asym) gives
>   K = 2^{-k} sum_S 2^{|S|} Pi_S with POSITIVE coefficients, so M1 follows if each elementary
>   exchange matrix E^S_pq = <x_p (x) y_q, Pi_S(x_q (x) y_p)> is PSD; S = empty is Schur-PSD; k=1
>   S={1} reduces to the Pluecker-type inequality |<x1^y2, x2^y1>|^2 <= ||x1^y1||^2 ||x2^y2||^2.
>   Phase-2 task P1 screens E_S numerically FIRST, then attempts proofs.

定位：Research-node work record dated 2026-07-29, original lines 60-64; assistant report at 2026-07-29T23:07:43.892Z also calls this reduction pending verification.
上下文：A tentative sufficient condition was proposed in an unfinished NPT-bound-entanglement investigation. Here Pi_i^asym=(I-F_i)/2, Pi_S is the product over selected copies, and E^S is the 2 by 2 exchange matrix displayed in the excerpt. The note is explicitly unreviewed and asks for screening before proofs. The positive-coefficient expansion and conditional implication are correct. The refuted mathematical object is the proposed per-subset PSD condition and its k=1 inequality, not the expansion, not the main undistillability theorem, and not a theorem-completion claim.

### Witness

The proposed universal PSD strengthening is false even for one copy. A positive projector does not make this exchange matrix a Gram matrix with a common ordered vector list.

Take k=1, S={1}, d=2 (or embed into any d>=2), x1=y1=e1 and x2=y2=e2 with e1,e2 orthonormal. With Pi=(I-F)/2, E11=E22=0 and E12=E21=-1/2. Thus E=[[0,-1/2],[-1/2,0]], and (1,1) E (1,1)^T=-1<0; the eigenvalues are -1/2 and 1/2. In contrast K=I-F/2 gives G=[[1/2,-1/2],[-1/2,1/2]], which is PSD. This explicitly disproves the proposed per-subset condition without disproving the target matrix condition. The claimed wedge inequality also has right side zero (e_i wedge e_i=0) and nonzero left side. These are exact hand calculations, independently recorded in the archived verification.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：候选子集交换矩阵的结构性 PSD/楔积不等式断言被精确 2x2 反例推翻。正系数分解及“若每项 PSD 则总和 PSD”的条件推理仍正确。

边界说明：从有限答案任务适配到研究候选：结构性候选被推翻仍保留；不把正确的条件性归约和未完成研究当错误。

## 028 — Circuit-distance stabilization

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/028/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/028/materials.json)

### 原文

>   For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal
>   boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer
>   system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS
>   sectors, boundary conditions, unreachable states, and logical terminal condition represented
>   exactly.

定位：Archived theorem statement installed on 23 August 2026, transfer claim, lines 6–10.
上下文：The installed claim uses a 'legal' schedule condition while the relevant legality notion guarantees only that no qubit participates in two gates simultaneously. Measurement consistency is separately required for the parity checks to be deterministic detectors.

### Witness

Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.

On four data qubits, take H_X=H_Z=(1,1,1,1). Prepare X ancilla a in |+> and Z ancilla b in |0>. Execute sequentially: q0→b, a→q0, a→q1, q1→b, a→q2, q2→b, a→q3, q3→b. The sequence is conflict-free, but exactly one common-support qubit has the Z CNOT before the X CNOT, an odd MC count. Back-propagating b's Z measurement creates Z on the fresh |+> ancilla a. That operator anticommutes with a's input stabilizer, so the check outcome is uniformly random and its proposed parity is not a deterministic detector. The transfer object needs MC as an additional hypothesis.

Witness 范围：argument_invalid

### 分类理由

- IV：由无冲突调度条件推出精确 detector 转移表示时缺少 measurement consistency；合法调度仍可有随机检查结果，故所述充分条件不成立。

边界说明：新提出的充分性定理漏条件，归 IV；没有据此推断原题文字被读错。

## 029 — Circuit-distance stabilization

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/029/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/029/materials.json)

### 原文

> **Why this is a gap and not a result:** Definition 3.5 is introduced in *this* document. If a
> reviewer prefers a different canonical split — for instance one defined by a family of *code-state*
> inputs rather than logical-basis inputs, which is a genuinely different family because
> `|0⟩^{⊗n}` is not a code state and makes the round-0 X-check outcomes random — then `𝒟_X` changes
> and, in principle, so could `d_R`. Three things reduce the risk and should be recorded with the
> sub-claim: (a) whatever `𝒟` is chosen, if it contains the Definition-2.7 set and is contained in
> `V`, then Proposition 3.7's argument goes through verbatim, because `F^X` annihilates *all* of
> `V_X` and all of `𝒟_Z`; (b) the split is forced on the Z-side by 3.6's dimension count; (c) it is
> confirmed numerically on 18 instances including a dependent generating set (11.2). **What is not
> established is that Definition 3.5 is the split the frozen 公共定义 intends.** This is precisely the
> hole the window theorem labelled W-G3 and its review answered with S3′; §3 answers it more sharply,
> but the answer rests on a definition a reviewer must ratify.

定位：Proof draft dated 23 August 2026, section 12, proposed mitigation (a), lines 1426–1437.
上下文：The draft proposes robustness under replacing its canonical detector space D by any intermediate space D' containing the short detector list and contained in the larger deterministic-parity space V. The latter also contains logical observable directions.

### Witness

Containment in V permits adding a parity with a logical-observable component. A fault that is logical and undetected by the original detectors can then be detected by the new parity, so the claimed unchanged proof does not apply.

Let λ be a logical observable and P_X the round-zero redundant-X-check parity of Steane with an added dependent X-check row. Set D'=span(D_b)+span(D_a)+span(P_X+λ). This contains the original short detector set and lies in V. A projected logical witness flips P_X by 0 and λ by 1, hence flips P_X+λ and is detected by D'. The archived exact example changes distance from 2 to 3 at R=2 and from 2 to 4 at R=3. The safe hypothesis is D'⊆D, not merely D'⊆V. The failure of the inference follows already from the displayed logical component; the canonical-space theorem is unaffected.

Witness 范围：argument_invalid

### 分类理由

- IV：把命题的 detector 空间条件 D-prime subset D 放宽到更大 V，允许混入逻辑可观测方向；原证明因此不能原样转移。

## 030 — Circuit-distance stabilization

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/030/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/030/materials.json)

### 原文

> > **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> > unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> > `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> > `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> > state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> > instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> > and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> > this is the precise form of the round-0/terminal asymmetry.

定位：Proof draft dated 23 August 2026, Remark 6.5, lines 603–610.
上下文：The model studies a counterfactual boundary convention in which the initial detector is removed. It correctly introduces a free recursion constant κ into the transition matrix but leaves the terminal vector v unchanged.

### Witness

Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

The detector recursion becomes u(S_r)=H_Zσ_r+κ. The terminal detector is D_{b,R}=(H_Zσ_R)_b+[(H_Zσ_{R−1})+u(S_{R−1})]_b=(H_Zσ_R)_b+κ_b. Therefore vanishing terminal detectors require H_Zσ_R=κ, not H_Zσ_R=0. Since σ_R need not lie in ker H_Z, 'σ_R≠[0]' is no longer the correct logical test; the observable condition is λ(σ_R)=1. The correct v_κ is zero only where both H_Zσ_R=κ and the target logical flip occur. The archived tests matched in 0/16 cases with fixed v and 16/16 after this correction.

Witness 范围：computation_false

### 分类理由

- IV：改变初始边界后仍把旧终端 v 接到新 A_kappa 上，未保留公式各部件对应关系。正确终端约束依赖 kappa，还须检验目标逻辑翻转。

边界说明：不是识别不到边界已经变化，而是在更新后的公式中错误沿用旧终端对应关系，归 IV。

## 031 — Circuit-distance stabilization

**一级类别：II 数学知识错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/031/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/031/materials.json)

### 原文

> min-plus matrix powers are eventually periodic

定位：Archived external-theorem assumption registered 23 August 2026, assumption statement, lines 21–23.
上下文：A registered external-theorem assumption summarizes a min-plus matrix theorem as unqualified eventual periodicity. It is an auxiliary asymptotic assertion, not the finite-round transfer identity.

### Witness

Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

For the one-by-one min-plus matrix A=[1], min-plus multiplication adds its only entry. By induction A^{⊙R}=[R] for every positive integer R. For any period p>0, A^{⊙(R+p)}=[R+p]≠[R]=A^{⊙R}, at every R. This exactly refutes the unqualified statement. It does not refute the finite-round transfer formula or the more careful zero-cycle normalized argument for the specific transfer matrices.

Witness 范围：statement_false

### 分类理由

- II：外部定理被表述成不加限定的 min-plus 幂最终周期性，漏掉可能的线性漂移/归一化。A=[1] 的幂为 [R]，直接否定所述定理内容。

边界说明：II/IV 边界：引用的外部定理本身被写成错误的无条件命题，归 II；与一个正确定理被用于错误实例相区分。 2026-09-23 核对：注册项自称引用外部定理、未在项目重推；早期有限条件推导不等于无条件安装声明的生成事件，保持 II。

## 032 — Circuit versus effective distance

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/032/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/032/materials.json)

### 原文

> **CONJECTURED 5.10 (saturation and one-round decidability).** Consequences of 5.9:
> 
> 1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
>    `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model.

定位：Proof draft dated 20 August 2026, conjectured Corollary 5.10(1), lines 855–858.
上下文：The historical saturation index was defined as the first round count after which circuit distance equals the static code distance d forever, with infinity if this never happens. It was not the index of convergence to an arbitrary lower limiting value. The quoted corollary was labelled CONJECTURED.

### Witness

Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

Take the Steane [[7,1,3]] code with X- and Z-check supports {3,4,5,6}, {1,2,5,6}, and {0,2,4,6}. Use increasing within-check orders, all X checks followed by all Z checks, and ideal temporal boundaries. In the X check ordered (0,2,4,6), an ancilla-X fault after the second CNOT produces residual X on {4,6}. Add one data-X fault on qubit 1 before the Z-check block. The net support {1,4,6} meets each listed Z check in zero or two positions, and is not an X stabilizer: every nonzero word in their X-check rowspace has weight four, whereas this support has weight three. Thus two faults produce an undetected logical X. Appending fault-free rounds preserves this witness, so d_R≤2 for every R; it can never equal the static distance d=3 eventually. Therefore R_sat=infinity, contradicting R_sat≤3. Only the saturation-to-d claim is refuted, not eventual constancy at a lower value. The original archived calculation also reports d_eff=2 and d_R=2 for R=1,2,3,4.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：原推导由有限窗口得到 d_R 最终恒定，接着以 i.e. 推出 R_sat<=d；但 R_sat 要求最终等于静态码距 d。缺失的是 d_infinity=d，错误推断直接见于原文 5.10(1) 与其 Derivation；可见过程亦先区分过 R_sat=无穷的情形。

边界说明：以已定位推导为依据改归 IV：最终恒定不能推出恒等于目标 d。不是纯输出抄写，也不因同一错误可描述为概念混淆而再加 II。

## 033 — Circuit versus effective distance

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/033/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/033/materials.json)

### 原文

> 2. `d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a
>    search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds. No
>    multi-round circuit is constructed at any point.

定位：Proof draft dated 20 August 2026, conjectured Corollary 5.10(2), lines 859–861; sector convention in Definition 1.5.
上下文：All statements in the relevant part of the proof concern one memory sector. The variable d is the static whole-code distance min(d_X,d_Z), but the algorithmic search truncates both fault weight and round span at d.

### Witness

The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

Use n=6, X-check supports {0,1},{2,3},{4,5}, and Z-check supports {0,1,2,3},{2,3,4,5}. The code has k=1, d_X=3, d_Z=2, and d=2. A non-interleaved list schedule with ideal boundaries has effective and Z-memory circuit distance 3; the archived direct multi-round check reports 3 for R=1,2,3,4. Consequently searching only fault multisets of size ≤d=2 returns no Z-memory logical witness; using the sector bound d_X=3 returns the correct value. The claimed global proof target is not thereby refuted; the per-sector truncation constant is wrong.

Witness 范围：argument_invalid

### 分类理由

- IV：将全码距离 min(d_X,d_Z) 用作每个独立扇区的搜索上限。全局最小值不能为较大扇区提供这个截断保证。

## 034 — Circuit versus effective distance

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/034/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/034/materials.json)

### 原文

> > In graph-like detector error models with fixed boundaries, a proven necessary-and-sufficient
> > structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when
> > d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma
> > of the length of the shortest closed spacetime lift of gamma", with zero time-direction
> > voltage/monodromy as the equal-weight liftability condition; the criterion recovers the
> > non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit
> > interleaved example with d_circ > d_eff.

定位：Root assembly dated 22 August 2026, root statement, lines 121–127; imported criterion in section 2.1.
上下文：An assembly imported a proved-under-assumptions equality criterion from a child theorem into an unrestricted root statement. The original child theorem explicitly assumes a memory experiment with R≥d rounds.

### Witness

The premise R≥d is lost in the root statement and its carried-forward caveats. An implication established under that hypothesis does not by itself establish the same implication for every round count.

The assembly restates the imported result as: for every legal, measurement-consistent schedule M and R≥d, d_circ(C_R(M))=d_eff(M) iff a minimum effective logical γ has repair(γ)=0. Its root claim instead says the structural criterion characterizes d_circ=d_eff without an R quantifier or restriction. None of the assembly's listed caveats restores R≥d. This is a direct premise-versus-conclusion scope mismatch. The independent audit found no counterexample at R=1 on its d=2 test instance, so the witness invalidates the unrestricted inference, not the theorem for small R.

Witness 范围：argument_invalid

### 分类理由

- IV：子定理明确要求 R>=d，根结论却没有保留该前提。这里是定理重述/应用越界，不是题目原始要求被误读。

边界说明：证明之间的前提传递错误，归 IV；I 不作为所有漏条件的总括类。

## 035 — Circuit versus effective distance

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/035/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/035/materials.json)

### 原文

> *Derivation.* Take an optimal certificate `(r_i, u_i)`. For each `i` choose a fault `f_i` with
> `E(f_i) = E_i` and `u(f_i) = u_i` (one exists, by definition of `U(E_i)`) and place it in round
> `r_i`; these are `w = |γ|` distinct circuit locations, since distinct residuals force distinct
> locations. Their detector chain is `(1+x)(A_0 + xC)` by 4.2. Let `D := A_0 + xC ∈ V` and write

定位：Proof draft dated 20 August 2026, derivation of Lemma 5.3, lines 672–675.
上下文：To construct a circuit lift, the draft chooses one elementary fault for each distinct effective residual and treats those choices as faults at distinct physical locations. The fault model allows only one Pauli assignment per location.

### Witness

Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.

At a single ancilla-to-data CNOT a→q_j, the draft's own Proposition 1.13(4) lists possible residuals ∅, S_j, {q_j}, S_{j−1}. Here S_j is the subsequent data suffix and S_{j−1}=S_j⊕{q_j}. Choosing the ancilla-X and data-X faults for S_j and {q_j} selects the same physical location twice. Their product is one X⊗X fault of cost one with residual S_{j−1}, not two occupied locations. The formal effective basis vector [S_{j−1}] also need not equal [S_j]+[{q_j}]. This refutes the distinct-location inference; a repaired existence proof requires a collision argument.

Witness 范围：argument_invalid

### 分类理由

- IV：不同残差不推出不同物理位置；同一 CNOT 上可有多种残差，逐项选出的代表未必组成合法且等权的联合故障配置。

## 036 — Optimal circuit distance of the Gross code

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/036/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/036/materials.json)

### 原文

> 1. **For the gross code, (MC) *is* [SBB26]'s non-interleaving condition.** Every overlapping
>    (X,Z) check pair shares exactly two qubits (§1), so `c_ab ∈ {0,1,2}`, and `c_ab` even means the
>    two shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede
>    all of `b`'s, or vice versa — S5 verbatim. **CONJECTURED** (the derivation is one line given §1;
>    the risk is only in whether S5's "either…or" is per-pair or global — S6 forces per-pair, since a
>    low-depth LRC cannot satisfy a global split).

定位：Proof draft dated 20 August 2026, section 2.4(1), lines 246–251.
上下文：For overlapping X and Z checks, measurement consistency (MC) requires an even number of shared data qubits with Z-before-X local ordering. The draft identifies this pairwise parity condition with non-interleaving, which requires all operations of one check on their common support to precede all operations of the other. The proposed equivalence was labelled CONJECTURED.

### Witness

Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

Take common-support gate times A_1=1, B_1=2, A_2=3, B_2=4. Both comparisons B_i<A_i are false, so the MC count is zero (even), but neither max(A)<min(B) nor max(B)<min(A) holds. The archived Gross-specific witness uses time arrays LX(left)=[11,10,3], LX(right)=[7,5,8], LZ(left)=[6,8,5], LZ(right)=[2,1,10]. It has zero MC violations among 648 overlaps, while 288 pairs are interleaved. The elementary four-time example independently refutes the inference from pairwise order agreement to non-interleaving.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：原文明确从共享两比特且 MC 计数为偶数，推出两个局部次序一致，再以 i.e. 推出整组 CNOT 不交错。前一步不保证 max(A)<min(B) 或反向；这是有原始推导的错误逻辑蕴含，不只孤立概念错述。

边界说明：以原文逐比特顺序到整组顺序的无效 i.e. 推导及生成过程为依据改归 IV；MC 与非交错的概念区别保留在解释中，不重复计 II。

## 037 — Optimal circuit distance of the Gross code

**一级类别：I 问题理解错误、IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/037/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/037/materials.json)

### 原文

> `T = 6` UNSAT is the sharp statement: **the gross code has no measurement-consistent
> single-ancilla SEC with six CNOT layers at all** — a 55-second exact result over the full
> 864-edge scheduling problem, with no assumption on the within-check orders, no tiling and no
> symmetry. Rows beyond the first are whatever closed inside the box.

定位：Proof draft dated 20 August 2026, section 2.4(5), lines 315–318.
上下文：An UNSAT result from a scheduling encoding was promoted to a universal nonexistence statement. The encoding put both ancilla families entirely within one round window, whereas the schedule class under discussion permits ancilla lifetimes crossing period boundaries.

### Witness

The verified search covered only unstaggered ancilla windows. Removing that restriction from the conclusion excludes legitimate staggered schedules without evidence.

Use the Gross left/right check blocks L_X=A, R_X=B, L_Z=B^T, R_Z=A^T, each of degree three. In CNOT layers 0,1,2 run L_X in parallel with R_Z; in layers 3,4,5 run R_X in parallel with L_Z. Each layer is a matching. The X ancilla for period p lives within p; the Z ancilla labelled p is prepared before layer 3 of p and measured after layer 2 of p+1. This gives six CNOT layers per period (864 CNOTs). For each of the 648 overlapping pairs, the MC counts for X_p against Z_p and Z_{p−1} are respectively 0 and 2, both even. The archived independent simulation also found all detectors deterministic in both memory sectors. This contradicts the unqualified six-layer impossibility, not the UNSAT result for the narrower unstaggered encoding.

Witness 范围：statement_false

### 分类理由

- I：原研究对象允许跨周期的 ancilla 生存窗口，但提交的编码把两类 ancilla 都限制在单轮内，实际模型遗漏了合法调度。
- IV：随后把受限编码 UNSAT 解释为全部六层调度不存在。六层 staggered 构造推翻这个提升；求解器对窄编码的结果本身没有被否定。

边界说明：双标签分别指实际编码忽略问题允许的调度，以及把窄编码 UNSAT 提升为全域结论；这不是“所有数学错误都再加 IV”的规则。

## 038 — Complexity of distance-preserving schedules

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/038/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/038/materials.json)

### 原文

> **Proposition 5 (prescribability, CONJECTURED).** Fix a line `L = {0,u_1,u_2,u_3} ≤ S` and a set of
> checks on it — necessarily disjoint cosets `B_i + L` of the qubit-column set. Write
> `φ_r(i) ∈ Log` for the class label of check `i` at `u_r` relative to a reference section chosen with
> `z(u_3) = z(u_1)+z(u_2)`. Then
> 
> 1. **`φ_1(i) + φ_2(i) + φ_3(i) = 0` is forced** — not a design choice. *Proof:* the three "cross"
>    4-sets `W^r_{ij} = {B_i, B_i+u_r, B_j, B_j+u_r}` satisfy `W^1_{ij}+W^2_{ij}+W^3_{ij} = χ_{c_i} +
>    χ_{c_j} ∈ S_X`, so the three class-differences sum to `0`; the same for the labels. ∎
> 2. **The only relations that can be imposed are `φ_r(i) = φ_r(j)`**, and each is imposed by
>    declaring the single weight-4 X-check `W^r_{ij}` (a legal coset 4-set) to be a stabiliser — a
>    *connector*. Any consistent system of such relations is realisable, and everything not forced is
>    generically independent in `Log`.
> 3. Consequently the realisable label systems on a line are exactly the triples of partitions
>    `(Π_1,Π_2,Π_3)` of the checks with `Π_a ∧ Π_b = Π_1∧Π_2∧Π_3` for all `a ≠ b`.

定位：Proof draft dated 20 August 2026, Proposition 5(2)-(3), lines 236–249.
上下文：A candidate reduction studies logical quotient labels φ_r(i) attached to stabilizer checks on a binary line. Proposition 5 is explicitly labelled CONJECTURED. Its second and third clauses nevertheless assert exhaustiveness: only pairwise equalities can be imposed and partition triples describe every realizable label system.

### Witness

Exhibiting pairwise connectors does not establish that all imposed relations are generated by pairwise equalities. A valid construction imposes a four-term XOR relation while keeping all six pairwise equalities false.

Work in F_2^5, encoding vectors as integers with XOR addition. Let L0={0,1,2,3}, V0={0,4,8,12}, and B=(16,20,24,28). The 16 qubits are B_i+L0. Take X-check supports c_i=B_i+L0 for i=1,...,4 and F={16,20,24,28}, G={17,21,25,29}. For P_i={B_i,B_i+1}, χ(P_1)+χ(P_2)+χ(P_3)+χ(P_4)=χ(F)+χ(G) belongs to S_X=span{χ(c_i),χ(F),χ(G)}. For every i≠j, χ(P_i)+χ(P_j) does not belong to S_X (six finite rowspace checks). Thus the four labels sum to zero, but no two labels are equal. This directly contradicts the claimed exhaustiveness; it does not refute every possible corrected hardness reduction.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：能施加两两相等关系，不推出可实现的关系只有两两相等。四标签 XOR 为零而任意两标签不等的构造否定所称穷尽分类。

## 039 — Complexity of distance-preserving schedules

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/039/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/039/materials.json)

### 原文

> Given a 3-CNF formula, give clause `t` two fresh basis vectors `a_t,b_t` and use the three occurrence points
> 
> `p_{t1}=a_t`, `p_{t2}=b_t`, `p_{t3}=a_t+b_t`.
> 
> They are a binary line by construction.
> 
> For every literal occurrence point `p`, attach a private BOOL gadget on `{p,r_p,p+r_p}` with fresh `r_p`; hence `g(p) in {0,1}`.
> 
> For each Boolean variable, choose one occurrence as reference. Wire every other occurrence to the reference:
> 
> * same literal polarity -> equality wire;
> * opposite polarity -> negation wire.
> 
> Interpret occurrence value `0` as “this literal is true”.
> 
> Finally, for each clause add the single zero-map constraint
> 
> `(0,0,0)`
> 
> on its occurrence line. It is hit iff at least one of the three occurrence bits is zero, exactly the OR condition for the clause.
> 
> All auxiliary points use fresh basis coordinates, so unintended line coincidences are avoided. The number of points and constraints is linear in the formula size.
> 
> **Correctness.** A Boolean satisfying assignment sets every literal occurrence to `0` iff that literal is true; the wires and clause check are then satisfied, and all private helpers can be filled from the finite gadget tables. Conversely any section solution can be totalised. The private BOOL gadgets make every occurrence Boolean, the wires give a consistent truth value per variable, and every zero-map clause has a zero occurrence, hence a true literal.
> 
> Therefore LINE-SECTION is NP-hard already with `dim L_0=2`. Combining with Theorem 2 gives NP-hardness for **code-realizable** Island-V X-sector instances with weight-4 X checks, `d_X=4`, and `k>=2`.

定位：Follow-up generated proof artifact collected 20 September 2026, section 3.4, lines 251–276.
上下文：A follow-up continuation proposes a general 3-CNF-to-line-section reduction. Each clause uses three occurrence points a,b,a+b; a BOOL/XOR gadget plus a constant gadget wires repeated occurrences. The reported theorem remains CONJECTURED, but the construction asserts that all auxiliary points are fresh.

### Witness

With two occurrences of one variable in the same clause, the wire's auxiliary XOR point is the third clause terminal, not a fresh point. The added gadget imposes an unintended constraint and breaks the satisfiability-preserving direction.

Use F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y), satisfiable at x=true,y=false. In the first clause, occurrence labels are (0,0,1), where 0 denotes a true literal. Wiring the first two x occurrences at a and b applies the BOOL/XOR gadget on {a,b,a+b}, forcing g(a+b)=g(a) XOR g(b)=0. But a+b is the y occurrence; consistency with the final ¬y clause forces its label to 1. Thus the compiled instance is inconsistent. The archived builder produces an unsatisfiable 107-check abstract CSP for this satisfiable input. A restriction to clauses with distinct variables or an explicit preprocessing step could repair the route, but neither is part of the stated general reduction.

Witness 范围：argument_invalid

### 分类理由

- IV：归约正确性声称辅助点均新鲜，但重复变量的接线可落在第三个 clause terminal 上；一个可满足输入被编译成不可满足实例。

边界说明：错误在新构造的正确性断言；没有证据指向对已知定理/概念的记忆错误，故不按 II。

## 040 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/040/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/040/materials.json)

### 原文

> the relabeling is an input-independent unitary on the value register applied around each query, so one query to either oracle simulates one query to the other.

定位：Manuscript Edit event, 2026-07-17T21:36:50.131Z, query-model paragraph.
上下文：The manuscript asserted exact one-query equivalence for arbitrary per-symbol bijections in the XOR oracle O_x|i,b>=|i,b XOR x_i>.

### Witness

Arbitrary bijections of symbol labels need not respect XOR translations, so they cannot generally be implemented by the asserted fixed conjugation around a single oracle call.

Take three-bit symbols and a bijection phi that swaps 1 and 2 and fixes 0,3,4,5,6,7. Fixed before/after value-register unitaries implementing every relabeled oracle, with phi(0)=0, would conjugate X_a to X_phi(a), where X_a|b>=|b XOR a>. Since X_a X_b=X_(a XOR b), this requires phi(a XOR b)=phi(a) XOR phi(b). But phi(1 XOR 4)=phi(5)=5, whereas phi(1) XOR phi(4)=2 XOR 4=6. Querying into an ancilla, applying phi, updating the response, and uncomputing uses two oracle calls; constant-factor asymptotic transfers may survive.

Witness 范围：argument_invalid

### 分类理由

- IV：把任意符号重标记当成可由固定前后酉操作实现的 XOR oracle 变换；该表示需保留 XOR 加法关系，而一般双射不满足。

边界说明：不是两次查询相加算成一次，而是所声称的一查询模拟根本不可实现，故归 IV 而不重复计 III。

## 041 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/041/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/041/materials.json)

### 原文

> With $u_j=\omega^{\,j-1}$ for $\omega=2R-1$, a cross-block $k$-tuple sums to $\sum_j u_j(g_j-g_k)$-type combinations that vanish iff all payloads are equal (base-$\omega$ uniqueness), while every other block-multiset pattern is killed by choosing the tags separated at scale larger than the total payload spread, which forces $q=\Theta_k(R^{k-1})$.

定位：Full-manuscript Write event, 2026-07-17T20:31:31.554Z; k-collision embedding proof sketch.
上下文：The original manuscript labels the encoding explicit but gives a proof sketch without the tag values, the special final payload coefficient, or a quantified modular separation argument.

### Witness

The stated recipe does not supply enough data or inequalities to verify the claimed encoding.

For one position from every block, the sum is sum_j w_j+sum_j u_j a_j. With sum_j w_j=0, equal payloads a_j=a require a sum_j u_j=0 mod q; the final coefficient must be specified to enforce this. Literal positive powers for all k coefficients do not: k=3, R=2 gives omega=3 and sum u=1+3+9=13, nonzero mod76. For each wrong multiset mu one must additionally prove dist_q(sum_j mu_j w_j,0)>max|sum_j u_j s_j|. 'Tags separated at scale larger' specifies neither the tags nor this inequality for every multiset. This records an incomplete manuscript proof, not impossibility of a repaired embedding.

Witness 范围：argument_invalid

### 分类理由

- IV：构造的消去/分离正确性没有成立：字面正幂系数不保证相同 payload 消去，tag 值和逐模式模间隔条件亦未提供，不能据此称编码已显式建立。

边界说明：未提供足够构造数据与错误消去声明共同构成编码正确性论证不成立；“证明缺口”不另设标签。

## 042 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/042/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/042/materials.json)

### 原文

> \Q\bigl(\kSum_{\Zq,t,N}\bigr)\;=\;\Omega_k\!\left(\sqrt N\, q^{1/6}\right)
> \qquad\text{for all } q\ \text{up to}\ \Theta_k(N).

定位：Full-manuscript Write event, 2026-07-17T20:31:31.554Z; inherited-floor theorem.
上下文：The displayed 'in particular' conclusion ranges over all small q, although the preceding construction has a sufficiently-large-alphabet condition.

### Witness

Small alphabets can make the target-zero problem constant, so the unconditional displayed range is false.

Set k=3, q=3, t=0, N>=7. Among N residues in Z3, some residue a occurs at least three times. Their sum is3a=0 mod3, so every input is a YES instance and Q=0. This contradicts a positive Omega(sqrt(N)*3^(1/6)) lower bound stated for all q up to a linear ceiling. The counterexample does not refute the preceding theorem restricted by q>=(k-1)(kK+k+2).

Witness 范围：statement_false

### 分类理由

- IV：从有字母表下限的构造推出所有小 q 的下界，丢掉定理应用前提。q=3、k=3、N>=7 时问题恒 YES，复杂度为零。

## 043 — Quantum k-sum with small alphabets

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/043/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/043/materials.json)

### 原文

> The bad
> event $\dist_q(T_\mu,t)\le P$ constrains the nonzero linear form $\nu\cdot w'$ to a set of at most
> $2P+1$ residues, so it forbids at most $(2P+1)q^{k-2}$ of the $q^{k-1}$ vectors $w'$.

定位：Appendix all-targets lemma Edit event, 2026-07-18T02:44:18.919Z.
上下文：The appendix uses a fiber count for a nonzero linear form over Z_q without assuming its coefficients generate the whole ring modulo q.

### Witness

A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

For k=3, choose wrong block multiplicities mu=(3,0,0), so nu=(3,0), and choose t=0, q=228, P=12. There are9 multiples of3 in the circular interval[-12,12]. Each equation3w1=r mod228 for such a residue has3 solutions, and w2 is arbitrary. Thus the bad set has9*3*228=6156 pairs, exceeding (2P+1)q=25*228=5700. Here q>9(2P+1)=225, so even the displayed counting threshold does not validate the faulty per-pattern estimate. A gcd factor or an invertibility hypothesis is needed.

Witness 范围：computation_false

### 分类理由

- III：模合数上线性形式的纤维数估计错误；反例中坏向量数为 6156，而所报上界只有 5700，缺少 gcd 因子。

边界说明：III/IV 边界：具体落点是有限集合纤维计数不正确，归 III；同一计数缺失的可逆性条件留在解释中。

## 044 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/044/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/044/materials.json)

### 原文

> There exist constants
> \(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
> \(3\le q\le N\)

定位：Report-writing event, 2026-07-19T18:54:14.287Z; P4 conjectured joint-histogram witness lemma.
上下文：The report explicitly labels this a conjectured asymptotic witness lemma and states that it has not been proved. The source-writing command uses the placeholder § for a backslash before saving.

### Witness

The uncapped exponent is impossible at the top endpoint q=N.

The proposed signed measure has unit l1 norm, correlation at least1/3+delta, and annihilates every query polynomial of degree below c0*sqrt(N)*q^eta. It would therefore force approximate degree Omega(N^(1/2+eta)) at q=N. A bounded-error quantum-walk algorithm uses O(N^(2/3)) queries for2-sum; constant-error amplification gives an approximating polynomial of degree O(N^(2/3)) at the required fixed accuracy. For eta>1/6, N^(1/2+eta) grows faster. This refutes the candidate as stated, not a claimed completed proof.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：提出的统一候选下界在 q=N 推出比已知上界更快的增长，因而候选不相容。没有把明确标注的 conjecture 误写成证明完成。

边界说明：保留原 conjecture 状态；归类的是候选结构/渐近断言被反驳，不声称发生过已证状态升级。

## 045 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/045/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/045/materials.json)

### 原文

> **定理 A**(奇 q≥5,任意 t,任意 N):Q(2-Sum) = Ω(√N·q^{1/6}),范围到 q ≤ 2N−1;

定位：Assistant final-report summary, July17; main-session JSONL lines447–468.
上下文：The construction uses two equally sized lists. Odd total N is handled by reserving one unused coordinate.

### Witness

The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

Writing n=floor(N/2) and K=(q-1)/2, the invoked donor permits K<=2n-1. This yields q<=4floor(N/2)-1. For even N this equals2N-1; for odd N it equals2N-3. At N=5,q=9, the stated2N-1 condition passes, but K=4 exceeds2n-1=3. The recorded reduction does not cover that endpoint; this is not a proof that the asymptotic bound itself is false.

Witness 范围：argument_invalid

### 分类理由

- IV：调用 donor 下界时未保留 K<=2 floor(N/2)-1；奇 N 时推导只覆盖 q<=2N-3，不能支持所报端点。

## 046 — Set equality and collision

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/046/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/046/materials.json)

### 原文

> 证明完成了。核心比预想的简单：**SE 是 Collision 的一个固定承诺子问题**，所以 SE 的显式矩阵可以原封不动嵌入 Collision。

定位：Assistant message, 2026-07-16T10:55:28.849Z; mathematical follow-up, 13:49:09.641Z.
上下文：The proposed explicit collision lower bound imported a set-equality adversary matrix. The completion statement was made before the formal upstream withdrawal; the zero-padding embedding itself was correct.

### Witness

Preserving the numerator and masked matrix norms transfers only the bound already established for the source matrix; it cannot establish an unproved source norm bound.

For the coordinate isometry J, Gamma_Col=J Gamma_SE gives ||Gamma_Col||=||Gamma_SE|| and ||Gamma_Col o Delta_i||=||Gamma_SE o Delta_i||. The inherited denominator still needs ||K_N* G K_N|| <= C^2/j. Its proposed derivation lacked the identity j U(K_N* G K_N)U*=M/[B_theta(q)^2 omega] in a common normalization. Thus the displayed Omega(N^(1/3)) certificate remains conditional on that identity. Finite checks at N=2,4,6 establish the embedding, not the uniform bound.

Witness 范围：argument_invalid

### 分类理由

- IV：正确的零填充嵌入只转移源证书已有的条件性界，不能补出未建立的承重范数/归一化恒等式，因此完成推断不成立。

## 047 — Set equality and collision

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/047/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/047/materials.json)

### 原文

> 有效秩证明严格成立，uniform physical \(T_b\) 对所有 admissible tame sector、所有正 LR 重数 \(c\) 全部关闭。

定位：Assistant message, 2026-07-22T13:19:00.659Z.
上下文：The completion message applies a normalized effective-rank calculation to the unnormalized physical trace quantity T_b.

### Witness

A normalization factor m=binom(j,a) was lost when identifying the script output with the physical quantity.

The raw physical maps obey S_gamma S_gamma*=m K_gamma, so their nonzero A_gamma=S_gamma* S_gamma eigenvalues are m times the normalized k_gamma,mu. The common-line formulas are r_mu=||t_mu||^2/m and a_gamma,mu=m|d_gamma,mu|^2. Contracting |d|^2*r_mu instead of a_mass*r_mu computes the divided quantity T_b/m. A derived bound T_b/m<=B implies only T_b<=mB, not T_b<=B when m>1. This defeats the claimed uniform proof. The corrected finite T_b examples still pass; no physical T_b counterexample is claimed.

Witness 范围：argument_invalid

### 分类理由

- IV：已算的是 T_b/m，却将其界直接作为物理 T_b 的界；有效推论只有 T_b<=mB。现有有限修正例仍可通过，witness 否定的是这条证明桥梁。

边界说明：III/IV 边界：归一化量本身可以计算正确；所定位错误是把它的证据用于另一物理量，故归 IV。

## 048 — Set equality and collision

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/048/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/048/materials.json)

### 原文

> 结合已确认的 `R_out`，actual T-a 约 `94,172`、T-b 约 `151.84`，都低于各自 cap。

定位：Assistant message, 2026-07-22T05:14:47.680Z; raw-normalization review, section2.
上下文：The first tame c=2 gate was reported passing. Its parameters are n=18,j=6,a=b=3 and color multiplicity m=binom(6,3)=20.

### Witness

The compressed contraction used |d|^2 instead of raw mass m|d|^2, making the reported T_a twenty times too small.

The reported normalized value is160582822829/1705200. Multiplication by20 gives raw T_a=160582822829/85260. Its cap is51396202/35. Their exact ratio is36224413/28242984>1, with positive numerator excess7981429. Thus this gate fails. The second gate n=19 similarly has raw T_a=204466088827/71920 and cap137582445/64, ratio10611004/8023575>1. This refutes the physical T_a gate claim; it does not refute the original set-equality lower-bound theorem.

Witness 范围：computation_false

### 分类理由

- IV：将压缩计算所得值标成 actual T_a，并与物理 cap 比较。归一化量的计算不能直接用于物理量；恢复 m=20 后精确比值大于一。

边界说明：与 047 一致：此条的压缩值被错误标为 physical actual value，再据此判门通过；不把正确压缩计算重新说成算术错误。

## 049 — Finite-dimensional Grothendieck bounds

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/049/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/049/materials.json)

### 原文

> \binom{600}{2}\,598=107281800

定位：Triangle/hypermetric no-go note, lines114–123.
上下文：The proof note counts index choices with an unordered pair of two distinct vertices and a third distinct vertex.

### Witness

The displayed integer product is incorrect.

binom(600,2)=600*599/2=179700; multiplying by598 gives107460600, not107281800. The discrepancy is178800. This is a local arithmetic/count-reporting error; it does not by itself invalidate the checker loops or the associated nonnegativity result.

Witness 范围：computation_false

### 分类理由

- III：明确整数乘法显示错误：binom(600,2)*598=107460600。该局部算式不否定整个非负性检验。

## 050 — Finite-dimensional Grothendieck bounds

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/050/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/050/materials.json)

### 原文

> 等号面支撑核至少为 28 维，而非此前的 12 维，因此算子秩上界严格改进为 746,797。

定位：Assistant message, 2026-08-29T02:46:52.613Z; transcript lines2965–2970.
上下文：The assistant promoted a pre-projection equality-space dimension to a bound on the retained746825 coordinates.

### Witness

Projection can kill directions; independence before projection does not imply independence afterward.

Of the28 old directions,16 degree-3/4 Walsh directions are individually zero on all retained coordinates. The surviving image has rank12: a retained12-by-12 minor has determinant -120231596497305600, and the16 zero directions give the matching upper bound. Therefore the supported kernel bound is at least12, giving rank<=746825-12=746813; the claimed746825-28=746797 does not follow.

Witness 范围：argument_invalid

### 分类理由

- IV：投影前 28 个独立方向不推出保留坐标上的像仍为 28 维；16 个方向被投影为零，所报秩改进没有依据。

## 051 — Finite-dimensional Grothendieck bounds

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/051/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/051/materials.json)

### 原文

> 3N=939406148910924300 > 5212397982790439500=P,

定位：Exact-cut proof draft creation, 2026-08-30T21:00; transcript lines6940–6979.
上下文：The preceding definition sets N=3131353829703088100, the total negative edge demand.

### Witness

The decimal expansion of3N is wrong, and the displayed comparison using that wrong number is false.

3*3131353829703088100=9394061489109264300. The incorrectly displayed939406148910924300 is smaller than5212397982790439500, not larger. After correcting the product, the intended inequality9394061489109264300>5212397982790439500 holds, so this is a local arithmetic transcription error and not a refutation of the corrected capacity obstruction.

Witness 范围：computation_false

### 分类理由

- III：3N 的十进制值及随附大小关系不符。修正乘法后原定比较成立；未找到生成时正确完整算式，不能仅凭错位数码认定纯抄写。

## 052 — Finite-dimensional Grothendieck bounds

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/052/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/052/materials.json)

### 原文

> Here the direct covariant product map in irrep \(\rho\) is exactly
> `14400/d_rho` times the canonical K-pencil adjoint

定位：Exact certificate draft write, 2026-08-31T03:29:17.319Z; correction at03:30:16.130Z.
上下文：The draft reused a single-vector Schur normalization after contraction over representation indices.

### Witness

The contraction supplies a dimension factor that cancels the divisor d_rho.

The single-vector formula has prefactor14400/d_rho. In Q^T J Q, contraction with J^{-1} contributes Tr(J^{-1}J)=d_rho. Thus the direct contracted coefficient map has prefactor(14400/d_rho)*d_rho=14400, independent of representation degree. The old code used ORDER*inverse(degree) modulo24001; the corrected code uses ORDER. Residual minor values consequently change from1400 and15799 to13280 and7143 modulo24001. The normalized Schur stage is unaffected.

Witness 范围：computation_false

### 分类理由

- III：指标收缩时漏乘 Tr(J^-1 J)=d_rho，导致收缩后系数错误；单向量阶段的归一化本身没有被推翻。

## 055 — Finite-dimensional Grothendieck bounds

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/055/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/055/materials.json)

### 原文

> A feasible unrestricted degree-4 moment/SOS dual whose objective equals the stated integer is a global upper bound on the sign optimization problem.

定位：Exact proof-node creation event, 2026-08-30T01:29:22.886Z; first event. Referenced archived system constructor, Mathematics represented by the output, lines22–45; archived JSON normalization and feasibility fields.
上下文：The implication names the full 746825-coordinate system with 20 PSD blocks as its premise and directly cites the archived system constructor. That constructor defines a moment functional L, with theta_empty=L(1), and imposes C*theta_empty-sum_t objective_B[t]*theta_t=-1. Thus the specifically referenced feasibility problem has L(f)=-1 for f=C-a^T A b; it is a separating moment problem, not an upper-bounding SOS certificate. The generic statement about a correctly oriented SOS dual is not the error.

### Witness

The direction of the moment/SOS separation was reversed.

If a degree-four functional L is nonnegative on every allowed square and respects the Boolean relations, then any SOS representation f=sum_j p_j^2 modulo those relations implies L(f)=sum_j L(p_j^2)>=0. A feasible separating functional with L(f)<0 therefore excludes that SOS representation; it does not prove f>=0 on Boolean inputs. Such separation also need not supply an actual negative Boolean input.

Witness 范围：argument_invalid

### 分类理由

- IV：原 proof sketch 明确诉诸 weak duality，把所引用 L(f)=-1 的分离 moment 可行性推出全局上界。弱对偶原理本身不是被推翻对象；错误在把它用于证明方向相反的证书。原始 DAG 写入保存这一应用，未找到生成者的对应明文推理。

边界说明：与 002 的定理应用边界一致：这里明确写出 weak-duality 推理，但引用系统不是上界证书，故改归 IV。证据是原始 proof sketch，不冒称找到隐藏推理。

## 056 — Group-orbit Bell matrices

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/056/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/056/materials.json)

### 原文

> The proof also gives explicit extremizing vectors: the normalized rows of any
> paired top left/right singular bases.

定位：Original balanced-rank theorem draft, GO-T4, lines 66–85.
上下文：The theorem applies to real rectangular matrices with transitive row and column permutation actions and does not exclude the zero matrix.

### Witness

For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

Let A be the 1-by-2 zero matrix. The two-element group acts trivially on its one row and swaps the two columns, so both actions are transitive and equivariance holds. The full top left space is R and the full top right space is R^2. Bases spanning these spaces have one and two columns, respectively; there is no pair with a common column count. Every feasible strategy still has the correct optimum value zero, so only the unconditional construction clause fails.

Witness 范围：argument_invalid

### 分类理由

- IV：从顶奇异空间推出任意矩形矩阵都可使用等列数完整配对基，未处理零矩阵左右维数不同的情形；A=0 的 1x2 例子否定无条件构造。

边界说明：零矩阵是新构造论断未覆盖的合法情形；原题未被重新定义，归 IV。

## 057 — Group-orbit Bell matrices

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/057/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/057/materials.json)

### 原文

> For every r>=3 and 0<=lambda<=1/2, the full D_r root projection A_r=WW^T/[4(r-1)], n=2r(r-1), satisfies
>   beta_cl(A_r-lambda I)=2r(2r-1)/3-n*lambda.

定位：Registered shift-linear candidate, claim lines1–4; exact D3 envelope dossier, D3-1 and D3-3–D3-4.
上下文：The universal affine formula was registered as a candidate and later retained as refuted. beta_cl(B)=max_{s,t in {−1,+1}^n} s^T B t.

### Witness

A competing sign pair outperforms the extrapolated affine branch beyond lambda=1/4.

For r=3 let W have rows(-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),(-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),(0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1), and A=WW^T/8. Take s=(1,1,1,1,-1,1,-1,1,-1,1,-1,1) and t=(-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1). Then s^TAt=8 and s^Tt=4. At lambda=1/2 their value is8-2=6, whereas the claimed formula gives10-12/2=4. One allowed pair already refutes the universal equality; no exhaustive upper-bound enumeration is needed.

Witness 范围：tentative_candidate_refuted

### 分类理由

- IV：注册的仿射极值规律被合法符号对严格超过。按研究候选的结构判断编码，不凭最终反例推测它一定来自某次算术差错。

边界说明：只知道注册的结构性候选被反例推翻；本次编码不推断其隐蔽形成原因。

## 060 — Channel additivity violations

**一级类别：I 问题理解错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/060/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/060/materials.json)

### 原文

> Specialize to `J=1`, so `q=m`, `H=C^D`,
> 
>     C(X)_(v,w) = m^(-1) Tr(X U_w^* U_v),
> 
> for one finite deterministic complex tuple `U=(U_1,...,U_m) in U(D)^m`, and
> 
>     A = 1 + 9(1+eta)^2/m,        eta>0,        ln m>18.
> 
> Assume the audited one-copy bound
> 
>     p_1(C):=sup_rho ||C(rho)||_2^2 <= A/m.
> 
> [...]
> 
> ## Exact task
> 
> Give one precise verdict on the existential finite-dimensional statement
> 
>     (E1)  There exist finite m,D, eta>0, and one complex tuple U such that
>           ln m>18, p_1(C)<=A/m, and kappa_1(U)<=A-1.
> 
> The verdict must be `PROVED`, `DISPROVED`, or `OPEN WITH EARLIEST GAP`.

定位：reconciliation_sources/W11-round-01-prompt.md:55–73; W11-round-02-prompt.md:12–22,73–80; W11-write-event.json (original event line 2100).
上下文：Round 1 explicitly requires J(log_2 m)/m > 2 log_2 A. The agent-authored J=1 follow-up drops it when specifying E1. The solver response correctly notices this omission.

### Witness

The task reformulation permits exact instances outside the intended positive-gap domain.

The error is the loss of a necessary hypothesis while formulating the next task, not the receiving solver's explicitly qualified answer. Round 1 requires J(log_2 m)/m > 2 log_2 A. After specializing to J=1, Round 2's literal E1 omits the equivalent condition A^2 < m^(1/m).

Take m=2^27, D=1, U_1=...=U_m=1, and eta=sqrt(m(m-1))/3-1. Then eta>0 and A=1+9(1+eta)^2/m=m. Also ln m>18, since ln 2>2/3 (the positive-series expansion ln 2=2(1/3+1/(3^3*3)+...) proves this bound). The output C(1) is the m-by-m all-ones matrix divided by m; it is rank one with purity 1. Thus p_1(C)=1=A/m. For every scalar T with |T|=1, every X_vw(T)=1, so R_U(T)=m(m-1)/m=m-1 and kappa_1(U)=A-1. All literal E1 conditions are satisfied.

Nevertheless delta=(log_2 m)/m-2 log_2 A=27/m-54<0, and A^2=m^2>m^(1/m). This is an explicit witness that the reformulated task does not retain the intended positive-gap requirement. It is not a counterexample to literal E1: E1 is true. It does not settle the original research problem. The later response correctly detects this input-specification error and is retained as detection evidence, not mislabeled as its source.

Witness 范围：missing_hypothesis_in_problem_reformulation_not_false_literal_E1

### 分类理由

- I：从上一轮目标制定下一轮任务时漏掉正间隙条件，改变了要解决的问题。文字 E1 本身可成立，接收方也正确指出遗漏；错误在任务重述。

边界说明：研究场景适配：I 的问题条件对象包括 agent 自己转写的后续任务；不把接收方正确回应归为其错误。

## 061 — Channel additivity violations

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/061/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/061/materials.json)

### 原文

> # 6. New full-Schmidt-rank obstruction
> 
> The following lemma goes beyond rank-one inputs, a single Bell input, and the universal \(m-1\) estimate.
> 
> [...]
> 
> \boxed{
> m\alpha_U^2
> -
> AD^2\alpha_U
> +
> D^2(m-A)
> \le0.
> }
> \tag{HC}
> $$
> 
> This is a new necessary scalar condition.

定位：reconciliation_sources/W11-round-03-response.md:912–914,1197–1208; W11-round-04-response.md:1–11 and section A.
上下文：The source presents HC as a new scalar obstruction beyond the rank-one lower bound. The correction distinguishes this strength claim from the valid full-rank inequality and witness.

### Witness

The existing one-copy rank-one condition strictly implies HC throughout the claimed feasible regime; HC supplies no additional scalar exclusion.

The target of this witness is the advertised additional scalar obstruction, not the truth of the Haar lower bound or the existence of a full-Schmidt-rank witness. In section 7, the source calls HC a "new necessary scalar condition" after presenting it as progress beyond the rank-one bound; the next response explicitly retracts that scalar-obstruction claim while retaining the inequality.

Write alpha=||C(I_D)||_2^2. Rank-one Haar averaging gives q_pure=(alpha+D)/(D(D+1)); the one-copy assumption p_1(C)<=A/m already implies m*q_pure<=A. The claimed full-rank average is q_full=(alpha^2+D^2)/(D^2(alpha+1)). Exact subtraction gives

q_pure-q_full = ((alpha-D)(D^2-alpha))/(D^2(D+1)(alpha+1)).

The relevant domain is not assumed without proof. In the low-A feasible regime, m>exp(18) and A^2<m^(1/m). In particular m>=10 and A<5/4: log(m)/m is decreasing for m>=10 and (5/4)^20>10. Thus A<2m/(m+1). Since C(I_D/D) is an m-dimensional density matrix, alpha>=D^2/m. Combining this with m*q_pure<=A yields (m-A)<=D(A-1), hence D>m. Consequently alpha>D. The same scalar bound yields alpha<=A*D(D+1)/m-D<A*D^2/m<D^2 (using A<m). The displayed difference is therefore strictly positive throughout the feasible domain.

It follows that m*q_full < m*q_pure <= A. Multiplying out m*q_full<=A gives precisely HC: m*alpha^2-A*D^2*alpha+D^2*(m-A)<=0. HC excludes no additional scalar candidates beyond the already required rank-one condition in this regime. Calling it an additional necessary scalar obstruction overstates what the derived bound establishes.

This is a claim about relative constraint strength inside the specified feasible domain, not a literature-wide novelty judgment. A different full-rank witness may still be mathematically interesting, and the inequality itself remains valid. If "new" were only a statement about deriving a differently written true formula, redundancy would not refute that narrower claim. The source's obstruction/progress framing and its subsequent explicit retraction determine the narrower, record-specific target used here.

Witness 范围：overstated_additional_scalar_constraint_not_false_inequality

### 分类理由

- IV：真不等式 HC 在指定可行域内已由旧 rank-one 条件严格蕴含，不能提供所称额外标量排除能力；只标约束强弱推断，不标一般文献新颖性。

边界说明：标签只针对记录已限定的约束强弱声明，不扩大成 HC 为假或一般意义的“不新颖”。

## 063 — Channel additivity violations

**一级类别：V 其他错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/063/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/063/materials.json)

### 原文

>     constexpr std::array<std::uint64_t, N> SUPPORT = {
>         53624480, 67257904, 74298900, 80378416, 82204926, 85479258, 83844372,
>         85479258, 82204926, 80378416, 74298900, 67257904, 53624480,
>     };
> 
> [...]
> 
>         weighted_surviving += static_cast<u128>(SUPPORT[deleted]) *
>                               static_cast<u128>(
>                                   matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0
>                               );

定位：explore_round82_global.cpp, lines 340–343, 458–461
上下文：The exploratory program computes weighted_surviving using the active SUPPORT array for a later finite-slope instance whose exact support total is K=970337664. The selected constants come from a prior instance.

### Witness

A stale support vector is used in the exploratory weighted calculation.

The thirteen printed SUPPORT entries sum to 970332140. The independently enumerated target vector reported in the round-82 thirteen-row census is (53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480), whose sum is 970337664. The difference is 5524. Because weighted_surviving multiplies each row by SUPPORT[deleted], these are not interchangeable constants. The archived final proof did not depend on this exploratory diagnostic. The original thirteen-row execution log is now bundled in reconciliation_sources. This release recomputes its sum and compares the active constants with those recorded rows; it does not claim a new full determinant enumeration.

Witness 范围：computation_false

### 分类理由

- V：后续实例程序仍载入上一实例的 SUPPORT 数据，实际数组与对应归档计数不一致。此处按数据更新/转录失配处理，不假定正确运算过程本身失败。

边界说明：研究场景适配：V 包括程序材料的数据更新失配，不等于原论文较窄的最终答案抄写子类；不据此推断生成者的数学推理正确。

## 065 — Channel additivity violations

**一级类别：V 其他错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/065/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/065/materials.json)

### 原文

> \[
> (H_{4,i})=(
> 8437248,11517728,12835576,14928318,15308304,16650864,15684084,
> 16650864,15308304,14928318,12835576,11517728,8437248).
> \tag{98.10}
> \]

定位：round-98-prompt-sent.md, lines 148–153
上下文：The transmitted input contains a thirteen-entry vector of raw-size-four determinant counts. Two entries were altered during prompt preparation; the receiving response recomputed the vector before use. This is an input-preparation error, not attributed to the receiving solver.

### Witness

Two copied input-vector values disagree with the independently regenerated determinant counts.

The transmitted vector contains 14928318 in zero-based rows 3 and 9. The regenerated raw-size-four vector is (8437248,11517728,12835576,14926862,15308304,16650864,15684084,16650864,15308304,14926862,12835576,11517728,8437248). The erroneous entries exceed the recomputed entries by 1456 each. The receiving response exposes and corrects this mismatch before using the data. The original thirteen-row execution log and the contemporaneous input audit are bundled in reconciliation_sources. Their source-bound mismatch is confirmed; a new full determinant enumeration was not performed in this release pass.

Witness 范围：computation_false

### 分类理由

- V：输入准备的文本替换把原计数 14926862 改成 14928318；同期审计记录了具体替换及接收方纠正。属于传递材料的数值损坏，不归因于接收方数学推理。

边界说明：研究场景适配：V 的材料传递错误发生在下一轮输入，而不是最终答案；其具体文本替换由归档审计支持。

## 066 — Optimal circuit distance of the Gross code

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/066/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/066/materials.json)

### 原文

> UNSAT of the checked quotient plus sound base exclusions would prove every legal schedule has a weight<=10 direct mechanism; SAT supplies only a canonical candidate.

定位：Archived computational certificate dated 1 September 2026, iteration-185 quotient, finite_coverage_theorem.root_use.
上下文：A finite search quotient appended lexicographic symmetry-breaking clauses to an exclusion registry. The quotient was intended to cover the full legal schedule class. The registry had not been closed under the 72-element translation group.

### Witness

An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

Let B be the base formula with 330 selectors and 14,484 untranslated block cuts, and let L be its 71 nonidentity translation lex-leader constraints. The archived independent counter-scenario provides a legal base model S. Among all 72 translated schedules, only the identity translate satisfies B. The lexicographically least translate is at δ=(1,5), and it violates 75 installed block cuts. Therefore this orbit has a B-model but no model of B∧L. The required implication B(S)⇒B(δS) fails, so orbit-wise coverage and lifting an UNSAT result are unjustified. Both old formulas happened to be SAT; this witness invalidates the coverage theorem rather than claiming the quotient itself is UNSAT.

Witness 范围：argument_invalid

### 分类理由

- IV：对不被平移群保持的 base 子句套用对称商覆盖推论，lex-leader 可删掉一个仍有合法 base model 的完整轨道。所需不变性前提不满足。

## 067 — Optimal circuit distance of the Gross code

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/067/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/067/materials.json)

### 原文

> * weight-≤10 configurations from the weight-12 pool: **0** in both sectors.
> 
> [Excerpt break]
> 
> 1. **`d_eff = 11` is not certified.** Only the weight-12-pool disqualifier is clean. Uncovered:
>    `|gamma| <= 10` arising from weight-14 logicals, or from overlapping residual configurations
>    (`Σ|E_i| = |V| + 2m`, `m >= 1`). Weight-13 is now **provably empty** (§2, even weight). Closing
>    this is exactly the campaign's 990-slot SAT machinery, per sector.

定位：Candidate-search report dated 23 August 2026, section 6 audit and section 6.2(1), lines 177 and 185–188.
上下文：The model explicitly kept its proposed schedule as a candidate, not a proved distance-12 construction. The erroneous part is the zero-count audit and the assertion that all weight-12-pool distance-at-most-10 mechanisms had been excluded.

### Witness

The filter tested only two of four gain-positive residual shapes. In particular, a four-suffix with one qubit outside the target logical support can still give a positive gain after cancellation by a singleton. Requiring each hook to fit entirely inside the target support misses such configurations.

The same candidate admits target support V={1,3,7,11,12,14,72,73,74,77,78,80}. Use check 66's four-suffix {78,12,141,72}, check 2's two-suffix {77,80}, and eight singleton faults {1,3,7,11,14,73,74,141}. Their symmetric difference is exactly V; qubit 141 cancels. The total cost is 1+1+8=10, not more than 10. The raw order for check 66 is (68,67,78,12,141,72) at times (5,8,9,11,12,32); check 2's last two times are (12,32). The archived verifier checks V∈ker H_Z and V∉rowspace H_X and finds 72 such witnesses in each sector. The effective-distance audit is false; no false completed-root claim is attributed.

Witness 范围：computation_false

### 分类理由

- IV：对遗漏合法残差形状的搜索作穷尽解释，未考虑域外 qubit 可由 singleton 抵消。十故障 witness 只推翻所报子池排除，不推翻一个原本就未认证的根命题。

边界说明：数量 0 是不完整搜索被当成穷尽搜索的结论；不是穷尽枚举之后简单加错，因此归 IV 而不是看到数值就归 III。

## 071 — Group-orbit Bell matrices

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/071/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/071/materials.json)

### 原文

>     implication: Equality in the spectral upper bound confines every extremizer to paired top singular
>       spaces; group averaging and real Schur theory then reduce invariant Gram weights to R/C/H multiplicity
>       variables, while row norms become explicit balance constraints.
>     proof:
>       sketch: Combine equality conditions for the norm bound with the isotypic commutant decomposition.
>         The current draft only sketches the necessity direction.

定位：See reconciliation source window 1
上下文：这是 GROTHORB.extremizer-classification 节点保留的 commutant-classification 旧路线。父 claim 的目标是 all vector extremizers，而这条路线只把 invariant Gram weights 约化到 commutant。错误位于这项受限约化被注册为完成全部极值策略分类的路线，不在正确的 invariant averaging 子结论。节点同时保留该路线后来 REFUTED/retired 的记录和正确的替代 spectrahedral 路线；这里引用的是原退休路线，不是替代路线。

### Witness

群平均可以产生不变的最优权重，但不保证所有最优权重都不变。因而只参数化 commutant 中的不变权重不能完成父节点要求的全部极值策略分类。

取 A=I_3，群 S_3 同时置换行列，U=V=I_3。令 H=[[1,1/2,0],[1/2,1,0],[0,0,1]]；其特征值为3/2、1/2、1且对角均为1，故正定并满足全部平衡条件。任意分解 H=TT^T 给出 X=Y=T，目标值 Tr(H)=3，达到谱上界。H 的非对角元不恒定，所以不与全部 S_3 置换矩阵交换，不属于 commutant。该具体极值策略没有被旧 commutant 路线覆盖。

Witness 范围：argument_invalid

### 分类理由

- IV：正确的群平均只给出不变最优代表，不能用 invariant commutant 参数化覆盖父目标中的全部极值策略；存在合法非不变最优 H。

## 072 — Group-orbit Bell matrices

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/072/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/072/materials.json)

### 原文

> the minimum real vector dimension among such strategies is the minimum rank of a feasible H.

定位：See reconciliation source window 1
上下文：此句由2026-09-07同期独立审查 F4 逐字保留，审查绑定的是旧 GROTHORB.equality-characterization.claim，SHA256 b0247e9891b03886886050461c971ee8f44b8535257deeeaacea7c5da1d2184e。该旧节点对任意非零 A 量化，却遗漏可行集非空限定；原 GOC-T3 正文有 Whenever it does，后来 SC2 与节点事件明确补回。这里不是首次写入事件的恢复，也不把已经修正的当前节点当成旧原文。

### Witness

旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。

取 A=diag(2,1)。其最大奇异值为2且重数r=1，可取 U=V=(1,0)^T。任意标量权重h的 VhV^T 对角为(h,0)，不能等于(1,1)，故平衡谱面体为空，不存在达到谱上界的策略，也不存在该集合上的最小秩。反例只击中未限定的 minimum 子句；等式刻画以及可行集非空条件下的秩公式仍正确。

Witness 范围：argument_invalid

### 分类理由

- IV：将只在可行集非空时有意义的最小秩表述推广到任意非零 A；diag(2,1) 使该平衡可行集为空，没有通常意义下的 minimum。

边界说明：minimum 的非空适用前提未保留，归 IV；不声称所有数学知识缺失或术语混淆。

## 074 — Quantum k-sum with small alphabets

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/074/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/074/materials.json)

### 原文

> A short shift of the frozen value (offset $\delta$ with $|\delta|\le C_0-kK-1$) then realizes every target $t$, at the slightly larger threshold $q\ge(k-1)(kK+k+2)$, with no parity condition.

定位：See reconciliation source window 1
上下文：交付TeX第234行的同一证明先把k−2个坐标冻结到共同值C0=floor(q/(k−1))、目标t0=(k−2)C0，然后声称对这个共同值作短位移覆盖所有目标。不是已修复稿中只移动某个坐标或逐坐标不同取值的构造。

### Witness

A common shift of all k−2 frozen coordinates changes the target by (k−2)δ. This modular map need not cover every residue, even for parameters satisfying the theorem's stated alphabet threshold.

Choose k=4, K=2, q=42. The stated condition q≥(k−1)(kK+k+2) holds with equality, and C0=floor(42/3)=14. The common frozen sum after shifting is 2(14+δ)=28+2δ mod42. Every reachable target is even. Under the stated restriction |δ|≤C0−kK−1=5, the image is {18,20,22,24,26,28,30,32,34,36,38}; it excludes t=1. Allowing an additional global translation of all k coordinates adds4a and still yields only even residues. Thus the written common-shift proof cannot establish every target with no parity condition. This does not refute a repaired construction using independently chosen frozen coordinates.

Witness 范围：argument_invalid

### 分类理由

- IV：共同位移只能改变目标 (k-2)delta，不能保证覆盖所有剩余类。k=4,q=42 的构造只能到偶数目标，故“任意目标”推断错误。

## 075 — Quantum k-sum with small alphabets

**一级类别：III 计算与代数错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/075/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/075/materials.json)

### 原文

> Fix any $(G,t)$ with $\sigma\ne\mathrm{id}$ (i.e.\ $\tau<q$), and let $D_0\subseteq G^n$ be the set of negative inputs. Then, already for $n=2$ and for every $n\ge2$:
> \begin{enumerate}
> \item $D_0$ is not a single $S_n\times C(\sigma)$-orbit; the number of orbits equals
> $\sum_{f} p_{\le m}(n-f)$, where $m=(q-\tau)/2$, $f$ ranges over the possible numbers of fixed-point values used, and $p_{\le m}(\cdot)$ counts partitions into at most $m$ parts; this is $\ge2$ and grows with $n$ for $m \ge 2$.

定位：See reconciliation source window 2
上下文：这是2026-07-17T20:31:31.554Z原始完整稿Write中同一Rosmanis barrier proposition的item1，尚未排除q=2。后来交付版加入q≥3并明确称q=2为single-orbit degeneracy。原包装选的item2 regularity-fails例句与其witness同方向，不应作为错误句。

### Witness

The unrestricted non-single-orbit claim omits the order-two degeneracy. For a nonidentity involution over Z2, the negative inputs can form one orbit rather than at least two.

Let G=Z2, t=1, and n=2. Then σ(x)=1−x swaps0 and1, so σ≠id, τ=0, and m=1, all within the quoted claim's domain. A negative input has no pair summing to1; hence D0={(0,0),(1,1)}. The alphabet swap belongs to C(σ) and sends(0,0) to(1,1). Therefore D0 is a single S2×C(σ) orbit. Equivalently, its displayed orbit-count formula specializes to p_{≤1}(2)=1, not≥2. This refutes the original universal item1. It neither refutes the later q≥3 version nor the valid q=3/q=4 examples of regularity failure.

Witness 范围：statement_false

### 分类理由

- III：原文自己的轨道数公式在允许的 Z2 情形给出 p_{<=1}(2)=1，而非至少二；精确轨道计数判断错误。

边界说明：III/IV 边界：所给公式在合法参数处算出一轨道，原文却声称至少二；按直接计数/数量比较错误归 III。

## 077 — Finite-dimensional Grothendieck bounds

**一级类别：IV 逻辑推理错误**

[原记录](../dataset-witness-repaired-v1.1-20260922/records/077/record.json) · [完整证据目录](../dataset-witness-repaired-v1.1-20260922/records/077/materials.json)

### 原文

> the attached program settles the entire trivial-isotypic block exactly.

定位：See reconciliation source window 1
上下文：该原句直接来自2026-08-27T03:39:59.333Z网页 DOM 捕获，原 rollout JSONL1598-1599。它出现在 OPEN-GAP 段，整段把剩余工作指向 nontrivial isotypic blocks，同时称所附程序已经能精确解决整个 trivial block。相邻正文仍明确全 classical upper bound 未获证明，并将不可能性引理条件限定为程序返回 PROVED_IMPOSSIBLE。因此错误只指所附程序对 trivial block 的完整判定能力/完成声明，不能扩大为整个 SOS 定理已证。

### Witness

原程序存在 INCONCLUSIVE 分支，且对该原实例实际返回 INCONCLUSIVE，没有给出该 trivial-isotypic SOS 子问题的可行或不可行证书；这不足以支撑 settles the entire block exactly 的完成声明。

原附件 SHA256为98fb98a0ff6486f9646c72c61621aaa6a63261c30a1042ada3a04828b050dd8e，与现存 bootstrap/h4_invariant_vanishing_probe.py 字节一致。2026-08-27T04:06:43.955Z原运行stdout（JSONL1971-1972）及冻结输出均记录 combined_restriction_rank_QQ=12、invariant_vanishing_dimension=43、candidate_Q_if_any=null，且 invariant_seed_SOS_obstruction={kernel_dimension:43,status:INCONCLUSIVE,symmetric_product_columns:946,test_points:1200}。这些结果保留了正确的局部秩信息，却没有决定整个 trivial block。后来1200×946有理秩运行未完成只是补充上下文，不作为唯一witness。

Witness 范围：argument_invalid

### 分类理由

- IV：程序保留且实际返回 INCONCLUSIVE，局部秩输出不能支持已完整判定整个 trivial block 的声明；不把它扩大为整个 SOS 定理完成。

