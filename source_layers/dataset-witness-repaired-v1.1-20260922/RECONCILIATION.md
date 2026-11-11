# Record-level reconciliation — v1.1

See [witness repairs](WITNESS_REPAIR.md). The v1 reconciliation is preserved in [history](audit/history/V1_RECONCILIATION.md).

| ID | Admission | Overclaim | Decision |
|---|---|---|---|
| [001](records/001/witness.md) | included | True | 恢复旧确认：同一来源的 dated correction 明确限定不同 tuples 只对所给 iterated-localization 路线必要，并指名原“entire problem”过强；这不是假设全局替代路线已成功，而是该必要性推断没有成立。 |
| [002](records/002/witness.md) | included | True | 恢复旧确认：自配对恒等式不能覆盖共轭信道对。原文纠正明确指向原 self-tensor 排除句，并给出共轭情形仍未排除的正则化差。 |
| [003](records/003/witness.md) | included | False | 固定 n·epsilon²=10^6 时 m=52，而 epsilon^(-4u) 随 n 无界；直接推翻统一常数 C。这里确认的是错误估计，不额外推定存在一项已成立的受限结果被升级。 |
| [004](audit/excluded/004/witness.md) | excluded | None | 原 centered-Cauchy 下端点在完整原系统内严格为负，已经被 x≥0 蕴含；旧退化例 a=v²/n 违反同时存在的 B-rank 约束。新代数推导证明这是原 witness 的域错配，不是缺失材料。 |
| [005](records/005/witness.md) | included | True | 离散字符平移保持模 p 的关系，不保证连续相位变形不变；代表元和为 p 的项带 exp(ip theta) 相位。原论证以离散不变性支持连续变分时忽略 C_dep 的导数，属于适用范围越界。 |
| [006](records/006/witness.md) | included | False | 某个平均后求和项依赖相位，不推出全部项之和依赖相位，因为可以相消。witness 只击中这一步推理，不证明实际总和必定不变；按本轮口径属于直接无效推断，不自动记为 overclaim。 |
| [007](records/007/witness.md) | included | False | M=D=1 时保留项给出的量为 8，而删项后的界为 4，简化不成立。这是界的代数处理错误，不据此另算范围扩张。 |
| [008](records/008/witness.md) | included | False | 交替辛核中两次变换的指数是 [p-l,k]，字符正交性给 F²f(l)=f(l)，不是 f(-l)。因此所述偶性推导无效，偶性是否另有证明不在此条判定内。 |
| [009](records/009/witness.md) | included | False | 777716²+777716+1=604842954373，与原文求值不符；这是局部精确算术错误。 |
| [010](records/010/witness.md) | included | False | 模 7 的两个给定点之差为 (6,5,6)，满足退化判别式且落入第三方向，反驳跨 ruling 差不会落入其他 ruling 的断言。只判这一几何断言。 |
| [011](records/011/witness.md) | included | True | 总能量预算不能构造同时满足逐项幅值、支撑和对称性约束的系数。原文以总量充足宣告局部约束也可满足；确认的是构造论证未闭合，不是构造绝对不存在。 |
| [012](records/012/witness.md) | included | False | 重新读取 150150 条扫描数据，精确二阶矩为 7149371020340889916998112，比打印值大 8000000000；无需假定新扫描结果。 |
| [013](records/013/witness.md) | included | True | 关于均值的方差等式被用于任意 mu。单个非零坐标即使方差为零，偏离其他中心的平方仍为正；均值条件丢失是明确的适用范围扩张。 |
| [014](records/014/witness.md) | included | True | 分支内推出的条件性结论被改成无条件的子集严格界。逻辑赋值已表明该蕴含不成立；不声称该赋值是原物理模型的一个实现，也不宣称目标定理为假。 |
| [015](records/015/witness.md) | included | False | 严格小于 x 的最大整数是 ceil(x)-1，不是 ceil(x)。本轮确认一般取整规则和端点；未重新计算所有历史表格行。 |
| [016](records/016/witness.md) | included | False | 平衡相差 Delta 的 Holevo 量需要约 Delta 比特辅助容量；取 Delta=log2(d) 可使成本无界。常数附加 qubit 开销断言错误；按直接尺度估计错误处理，不以“常数”一词自动计 overclaim。 |
| [017](records/017/witness.md) | included | False | d=1 时 log2(d-1) 无定义，原通用连续性公式需要单独处理平凡输出维度。仅判此边界公式。 |
| [018](records/018/witness.md) | included | False | X、Z 两个 Pauli 矩阵给出明确符号差，所写消去顺序不成立。这是计算/推导本身错误。 |
| [019](records/019/witness.md) | included | False | 交换不变的反对称态不支撑在对称子空间；将前一种可行性替换为后一种，改变了编码模型。此 witness 不证明特定目标态在较大集合内必有扩张，也不自动建立某次最终容量 overclaim。 |
| [020](records/020/witness.md) | included | False | 复输入的特征多项式不等于所列固定谱。原任务明确要求先验证工作公式；保留为研究中被推翻的候选公式，不描述成已证明结果或完成声明。 |
| [021](records/021/witness.md) | included | False | psi=&#124;0> 时环境支撑约束与正性迫使 phi=&#124;0><0&#124;，不存在要求的不同随机配对。错误在试验/构造所假定的非平凡可行域，不在一个已完成容量定理。 |
| [022](records/022/witness.md) | included | True | 两次使用的值须除以 2 才能比较；修正后比值 84841/145000<1，不能支持“更强”的结论。阈值 2/5 也不是给定多项式的零点；后者是同条记录中的额外计算错误。 |
| [023](records/023/witness.md) | included | False | 将脚本自己的 k2 代入互补输出矩阵，在 x=1/2 得非零残差 (1,-i/sqrt(2),0,0)。核投影器错误，不需要依靠后续地位升级来确认。 |
| [024](records/024/witness.md) | included | True | 50% 擦除信道的接收端与环境等价，逐括号相减可以各自为零。特定信道对的逐项策略失败，不支持“任何 Q=0 证明都不能如此”的排他结论。 |
| [025](records/025/witness.md) | included | True | 反可降解的 50% 擦除信道仍有正的双向辅助容量；有效的 Q↔>0 证据不能支持“不是反可降解”的结论。这里只判容量/辅助模型之间的错误桥接。 |
| [026](records/026/witness.md) | included | True | 反例只迫使某种附加条件排除该反例，不能推出每个成功证明必须采用幺正性/无旗性这一特定条件。错误是充分候选与普遍必要性的错换，不宣称候选条件本身错误。 |
| [027](records/027/witness.md) | included | False | 原笔记的正系数分解与“若每个 E_S 为 PSD 则目标成立”均正确，并明确要求先筛查。E=[[0,-1/2],[-1/2,0]] 只推翻拟尝试的逐子集 PSD 条件。保留为失败候选，不记证明错误或 overclaim。 |
| [028](records/028/witness.md) | included | True | 保留为安装节点的适用条件丢失，不指控正文证明错误。原claim独立量化所有legal日程，正文Definition 2.4把legal定义为无资源冲突；MC是额外条件。安装节点caveats补了Pauli群条件却没有MC。给定4比特日程满足该legal谓词但有随机测量记录，故不能无条件导入确定detector的transfer论证。 |
| [029](records/029/witness.md) | included | True | D′⊆V允许加入含logical observable的parity，不等价于D′⊆D。原文明确称较大范围下原论证verbatim适用；该投影实际会被新增parity检测。 |
| [030](records/030/witness.md) | included | False | 删左边界后递推常数κ进入末端detector，末态必须满足H_Zσ_R=κ。原式只改Aκ却继续用v(σ)=1[H_Zσ=0且非零逻辑]，直接算错边界公式。 |
| [031](records/031/witness.md) | included | True | 安装为external-theorem的无条件“min-plus matrix powers are eventually periodic”删掉漂移/归一化和定理适用条件。A=[1]的R次min-plus幂为[R]，精确反驳原泛称。 |
| [032](records/032/witness.md) | included | True | 原文从d_R最终常数推出按冻结定义“最终等于静态d”的R_sat≤d，把已支持的较弱稳定结论当成较强饱和结论。CONJECTURED标签不消除其中明确写出的错误推论。 |
| [033](records/033/witness.md) | included | True | 整体min(d_X,d_Z)的d上界不能逐扇区使用；原§5全为Z-memory，却把搜索权重上限设为整体d。n=6不对称CSS例子该扇区距离3而整体d=2，搜索截断漏解。 |
| [034](records/034/witness.md) | included | True | 保留为组装中的R≥d前提遗漏。原assembly明确把C1–C4解释为整个模型类上的universal，同时§2.1引用的定理要求R≥d；§6宣布携带所有限制但遗漏这一条。后续节点增加C-M7正是修复。不能用修复后的caveat否认旧组装错误。 |
| [035](records/035/witness.md) | included | False | 不同残差不推出不同物理故障位置；同一CNOT位置不同Pauli可给出不同残差，原“since”推理错误。 |
| [036](records/036/witness.md) | included | False | 相同的逐比特先后方向不等于一个check全部在另一个之前。1<2<3<4反例直接击破i.e.处的逻辑等价；这是局部顺序谓词混淆。 |
| [037](records/037/witness.md) | included | True | unstaggered编码的UNSAT被推广成所有六CNOT层SEC不可能；交错跨周期ancilla寿命未在编码中。合法staggered六层安排满足MC，故原泛称超出搜索域。 |
| [038](records/038/witness.md) | included | True | 原文从可用pairwise connectors推广到“only relations”与“exactly”所有可实现标签系统；合法横向coset可强制四项XOR而不强制任何两项相等。部分构造不能支撑穷尽性分类。 |
| [039](records/039/witness.md) | included | False | 一般3-CNF构造遇同一子句重复变量时，连接wire的辅助点a+b与第三文字点相同；引入意外约束，破坏可满足性保持。 |
| [040](records/040/witness.md) | included | True | 保留任意逐坐标字母双射被升级为 XOR oracle 精确一查询等价这一局部错误。原思考已写出 compute-copy-uncompute 的两查询方案，却在正文保留一查询和 Q(g)=Q(f)。错误不是经典谓词编码，也不是否定常数开销的渐近转移。 |
| [041](records/041/witness.md) | included | True | 保留稿件 explicit encoding 引理中的真实局部错误：正文给所有 u_j 取正幂，却宣称等 payload 时和为零；正确脚本有特殊末位负和系数。稿件还把未展开的 tag 分离义务作为已证显式构造。不能把脚本中存在正确完整构造误说成整个 embedding 不可能。 |
| [042](records/042/witness.md) | included | True | 保留从有 alphabet 下限的构造扩展成 all q up to Theta_k(N) 的书面范围错误；不能将其反例描述为同时推翻前面有 q 下限的定理。 |
| [043](records/043/witness.md) | included | False | 保留合数模上非零线性形式纤维计数错误。不能仅因它出现在全称引理里便自动标 overclaim；直接缺陷是把 nonzero 当作满射从而漏 gcd 倍数。 |
| [044](records/044/witness.md) | included | False | 保留被已知上界反驳的候选 witness lemma。原文明确写 Conjectured、Proof plan only、No step ... proved，因此不是把已经建立的证据夸成完成证明。用户允许未完成证明过程中的错误，此项仍入核心数学错误集合。 |
| [045](records/045/witness.md) | included | True | 保留偶数 N 推导的端点直接沿用到冻结一个坐标的奇数 N 的范围缺口。错误是这套 reduction 的覆盖范围，不能夸成最终渐近下界被证伪。 |
| [046](records/046/witness.md) | included | True | 保留正确的 SE→Collision 零填充嵌入被当作完整显式下界证书这一缺口。必须撤掉旧金库标题的‘已经撤回后再次继承’时间叙事：正文完成声明在正式上游撤回前；错误仍是上游未证范数桥被当作闭合。 |
| [047](records/047/witness.md) | included | True | 保留关于 T_b/m 的有效秩界被用于关闭 physical T_b 的证据对象替换。分类 yes 的依据是从归一化量的有效证明跨到不同物理量且明确声称统一关闭，不是把所有漏因子都自动算 overclaim。 |
| [048](records/048/witness.md) | included | True | 保留 normalized contraction 被报成 actual physical T_a 并据此宣称门通过的错误。与047分开：047是一般T_b证明缺口；048有T_a精确失败例。 |
| [049](records/049/witness.md) | included | False | binom(600,2)·598=107460600，与报告值相差 178800。错误不自动污染遍历循环或非负性定理。 |
| [050](records/050/witness.md) | included | True | 28 个旧方向中 16 个在保留坐标上为零；归档非零 minor 与零向量证明像空间维度 12。投影前维数不能支持投影后的改进秩界。此次检查推导及归档证据，未重跑全尺寸 minor 计算。 |
| [051](records/051/witness.md) | included | False | 3×3131353829703088100=9394061489109264300，不是原文的 939406148910924300；误写值甚至小于所比较的 P。修正后原拟比较方向成立，故只判局部算术/转录，不否定修正后的容量障碍。 |
| [052](records/052/witness.md) | included | False | 单向量系数 14400/d_rho 经 Q^T J Q 收缩还乘 Tr(J^-1 J)=d_rho，故直接映射系数应为 14400。原错误在收缩因子；不影响另行归一化的 Schur 阶段。 |
| [053](audit/excluded/053/witness.md) | excluded | None | 原指控把导出脚本中未重印外部定理误当成证明缺桥。原始网页捕获明确引用 Bandeira–Kunisky（arXiv:1812.11583v2），陈述非 cut 的 extreme elliptope point 不能延拓为 degree-4 pseudomoment，并给出 rank(X odot X)=10 的使用条件。随后协调器提供精确 minor，脚本才将其标为 external input。原始引用并未缺失；该外部命题也与所引用论文 Theorem 2.17 相符。现有 witness 只证明 checker 本身不重证外部定理，不能证明这个数学推断有错。 |
| [054](audit/excluded/054/witness.md) | excluded | None | 现有 witness 将 08-29 本地重建时缺少 Bell 矩阵和 9240/6104 推导，推定为 08-27 宣布完成时也没有这些推导。但完整原 rollout 的 01:29、01:31 和 01:44 网页捕获实际保存了 B=3G-13I、9240 的谱上界与单位根向量达界、任意符号配置到 upper filter 的归约、k=98/104 的格同余闭合，以及 6104 的 A1+A6 显式达界构造。网页还明确说存储的 SDP 数值只是归档一致性检查，不是其证明。故缺桥 witness 与当时完整材料冲突，不能据此确认协调器的数学完成声明错误。 |
| [055](records/055/witness.md) | included | True | 上下文中的 L(f)<0、L 对允许平方非负，仅证明不存在指定 SOS 表示；不能证明 f 在 Boolean 输入上非负。证书方向/用途错误，使有效分离证据被用于它不能支撑的上界结论。 |
| [056](records/056/witness.md) | included | True | 保留为零矩阵边界处的构造范围越界，不是最优值定理为假。GO-T2 的 paired-basis 构造要求 sigma>0，但 GO-T4 单独量化 transitive equivariant 矩阵，并在不排除 A=0 时声称 normalized rows of any paired top bases 给出极值向量；同样遗漏进入独立哈希绑定的 transitive-optimum 节点。对 1×2 零矩阵，完整左右 top spaces 的维数分别为 1、2，不能按该定义选择同列数的完整 paired bases。后续范围修复明确承认 earlier unconditional wording was too broad。 |
| [057](records/057/witness.md) | included | False | D3、lambda=1/2 的合法符号对给值 6，而候选通式给 4；精确反例足以否定通式。作为探索中被否定的候选保留，不标为已证明或 overclaim。 |
| [058](audit/excluded/058/witness.md) | excluded | None | 维持旧v04误报排除：被指逐子集不等式不是原来源所断言，原同轮明确否认该强解释。 |
| [059](audit/excluded/059/witness.md) | excluded | None | 初始补丁已经说明文献显示的是通用半径，并明确提出 retaining R 的推导；原参考文献也确实在9.7证明后说明Haar扩展。现 witness 不能仅由这两点建立误引或缺口。 |
| [060](records/060/witness.md) | included | False | 原错误是把研究目标整理成下一轮输入时漏掉必要条件；不是后来明确指出缺条件的回答犯错。以原始输入写入事件加精确实例作为 witness，恢复这条历史错误。 |
| [061](records/061/witness.md) | included | True | 修正 witness 的对象：不是证明 Haar 界错误，而是证明所称新增标量约束在当前可行域内已由旧约束严格支配。保留正确的界和满秩见证，删除旧 witness 对其真假的混淆。 |
| [062](audit/excluded/062/witness.md) | excluded | None | 原文在同一段明确保留 symmetric、混合分母和频率依赖等例外；现 witness 只列出这些已排除的方向。 |
| [063](records/063/witness.md) | included | False | 恢复数值错误确认：原执行日志逐行给出的实际 support 与活跃 C++ 常量不同，合计相差5524；旧程序中常量确用于 weighted_surviving。它不影响已分开验证的最终证书。 |
| [064](audit/excluded/064/witness.md) | excluded | None | 所记录差异是内部证明/独立复核状态用语，未提供数学反例或无效推断。 |
| [065](records/065/witness.md) | included | False | 恢复输入转录错误确认：发送稿两处14928318不等于已有精确日志及接收端独立复核的14926862；接收端在使用前已经纠正。 |
| [066](records/066/witness.md) | included | True | 旧iteration185的部分排除库未在平移作用下闭合，却声称加lex leader后有全局UNSAT提升。其缺少的不只是实验覆盖，而是B(S)⇒B(δS)这一必要桥梁；旧审计给出具体轨道反例，并有原作者撤回该coverage声明。 |
| [067](records/067/witness.md) | included | True | 尽管root明示未证明，局部weight12-pool分层仍被错误宣称全部排除。filter仅覆盖两个suffix形状，遗漏允许外部qubit抵消的4-suffix；明确10故障见证推翻该局部零计数。 |
| [068](audit/excluded/068/witness.md) | excluded | None | 当前所选原句只有“zero voltage/monodromy”，并没有“电压集合等于标量0”或“全部representative电压为0”的错误等式。相同assembly§2.3立即给出存在representative及round assignment的精确定义；U(E)={0,1}不反驳该存在量词。 |
| [069](audit/excluded/069/witness.md) | excluded | None | k=0时无非零逻辑终端的计算正确，但不会使有限min-plus表示等式错误：允许∞且min(empty)=∞时两边均∞。正文明确k≥1，且明确采用扩展值空集最小值约定；安装摘要未重写k域属于精度/自足性问题，现有witness未提供错误数学结论。 |
| [070](audit/excluded/070/witness.md) | excluded | None | 非群fault alphabet反例数学上正确，但原claim引用stated unit-fault model与Lemma2.9；同一安装YAML的caveats第47–54行明确完整Pauli GROUP及均匀单位代价，甚至明确讲非群时不成立。不能抽掉紧邻限定再指控无条件推广。 |
| [071](records/071/witness.md) | included | True | 保留为失败的 all-extremizer 路线，不指控较窄的 invariant averaging 引理。独立可读节点将 commutant-classification 注册为通向 all vector extremizers 的路线，而正文只支持 invariant weights；该路线自身保留 REFUTED 评估及同日反例。A=I3、S3 作用下的非恒定非对角 correlation weight 正定、单位对角，给出最优策略但不属于 commutant，因此 invariant 参数化不能覆盖所有极值策略。未完成路线也属于本数据集允许分析的错误单位。 |
| [072](records/072/witness.md) | included | True | 保留为原节点 minimum-dimension 子句遗漏非空前提，非等式刻画定理错误。原正文 GOC-T3 已写 Whenever it does，但旧节点对任意非零 A 写出 minimum rank；不可行的 diag(2,1) 使通常意义下 minimum 未定义。不可用现在已修好的节点或另一个 rank-threshold 定义中的 infinity 约定反向补入旧节点。F4 给出旧 exact claim 哈希与逐字旧子句，SC2 与节点事件确认修改；这已足够绑定历史错误，不必重新找到最初写入消息。 |
| [073](audit/excluded/073/witness.md) | excluded | None | 原始模型澄清 RM-1/RM-2 明确说明来源 GOC-T6 的 averaging 因为 row/column diagonals are permuted 而成立，任意 orthogonal mixing 是诊断用更广解释，不是原证明的模型。原 shorthand 节点没有在一句话内重抄模型，确有表述可改进，但原始来源并未断言一般正交混合保持常对角。RHR^T 反例落在已说明的 permutation 域之外，不能当本条实际数学错误。 |
| [074](records/074/witness.md) | included | True | 已将旧 KSUM-002 对回真正的交付论文版本：common frozen value 的短统一位移被说成覆盖 every target、no parity condition。压缩包先前仅选到已修复的单坐标位移稿，不能因此把历史错误降为缺源。 |
| [075](records/075/witness.md) | included | True | 纠正原文与 witness 选取后保留历史 KSUM-004 的轨道分类范围错误。不能再引用 regularity-fails 的正确例句并以同方向例子反驳。历史错误单位原本是 barrier orbit classification is exhaustive；原始初稿在同一命题 item1 对任意sigma!=id声称D0不为单轨道，遗漏q=2退化情形。 |
| [076](audit/excluded/076/witness.md) | excluded | None | 原近似次数表正确；找回的1707–1709上下文明确要求审查者核对归一化及转换，并主动提示 correlation > 2*error。未找到已经采用错误阈值推出具体查询界的原事件。不能把正确提出审查问题算成数学错误。 |
| [077](records/077/witness.md) | included | True | 原始网页正文确实写出 the attached program settles the entire trivial-isotypic block exactly。该确切附件 SHA256 与现存原程序一致，而当时运行的原始输出为 invariant_seed_SOS_obstruction.status=INCONCLUSIVE、candidate_Q_if_any=null，程序自身也有 INCONCLUSIVE 分支。故把一个仍可能不作判定的精确 probe 说成已经解决整个 trivial block，构成局部完成能力越界。原文同时保留 OPEN-GAP、全 SOS 未证与 PROVED_IMPOSSIBLE 条件句：本条不扩大成声称整个 classical bound 已证，也不否定正确的 rank12/kernel43 计算。 |
