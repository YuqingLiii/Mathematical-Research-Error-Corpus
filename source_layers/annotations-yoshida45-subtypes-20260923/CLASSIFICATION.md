# 45条逻辑与推理错误：Yoshida八子类对照

依据：[Yoshida et al., Table 2](https://arxiv.org/html/2609.15145)。本轮是二级标注层，不修改原始材料、witness、65条收录范围或论文。

## 编码规则

每条既有 IV 记录选择一个主子类，便于展示；这是本次约定，不声称原论文八类互斥或原研究采用单标签。优先按可定位的错误动作分类：明确误用已有定理/界用 IV-1，明确不成立的推导用 IV-2。IV-5必须有前提满足而代入/对应错误的证据，不把所有对象错配自动放入该类。IV-6须直接涉及题目条件的推理，不能把中间定理前提都算成题目条件。

IV-4 的021/027/044和 IV-7 的010/057是研究场景适配（5条），不是原论文逐条标注。这些记录仍有既有数学witness；适配的不确定性不等于数学缺陷尚未确认。尤其027/044，反例否定候选目标，不否定提出并检验猜想的研究行为；不把正确条件推理说成错误。

本轮没有新运行大型witness，也没有对所有原始长会话重审；逐条对照现有源引文、上下文、witness及一级边界说明。

## 汇总

|子类|数量|占45条|记录|
|---|---:|---:|---|
|IV-1 定理应用不当|13|28.9%|002, 017, 029, 030, 033, 034, 042, 045, 046, 055, 066, 071, 072|
|IV-2 错误的逻辑蕴含|27|60.0%|001, 005, 006, 011, 013, 014, 022, 024, 025, 026, 028, 032, 035, 036, 037, 038, 039, 040, 041, 047, 048, 050, 056, 061, 067, 074, 077|
|IV-3 最终答案选择错误|0|0.0%|—|
|IV-4 策略选择不当|3|6.7%|021, 027, 044|
|IV-5 公式与定理使用错误|0|0.0%|—|
|IV-6 对题目条件的推理错误|0|0.0%|—|
|IV-7 规律与重复结构的表达错误|2|4.4%|010, 057|
|IV-8 不适当的处理操作|0|0.0%|—|

0条只表示本轮没有将现有记录主归入该类，不说明这种错误不会发生。

## 逐条判定

|记录|问题|主子类|判定理由|映射|
|---|---|---|---|---|
|[001](../dataset-witness-repaired-v1.1-20260922/records/001/witness.md)|Channel additivity violations|IV-2|某一局部化路线的必要要求不推出所有解决路线都必要；固定对的可能性未排除。|直接对应|
|[002](../dataset-witness-repaired-v1.1-20260922/records/002/witness.md)|Channel additivity violations|IV-1|自配对引理被解释为适用于一般共轭配对；所需对象同一性不成立。|直接对应|
|[005](../dataset-witness-repaired-v1.1-20260922/records/005/witness.md)|Channel additivity violations|IV-2|离散相位关系不推出连续变形下被遗漏项恒定；部分目标的导数不是完整目标导数。|直接对应|
|[006](../dataset-witness-repaired-v1.1-20260922/records/006/witness.md)|Channel additivity violations|IV-2|部分项含相位不推出总和含相位；尚未排除其余项抵消。|直接对应|
|[010](../dataset-witness-repaired-v1.1-20260922/records/010/witness.md)|Channel additivity violations|IV-7|错误概括差向量只能落在两个指定 ruling；有限域反例给出第三方向。|研究场景适配|
|[011](../dataset-witness-repaired-v1.1-20260922/records/011/witness.md)|Channel additivity violations|IV-2|总能量充足不推出逐坐标约束及所有方程可同时满足；不存在已给出的兼容赋值证明。|直接对应|
|[013](../dataset-witness-repaired-v1.1-20260922/records/013/witness.md)|Channel additivity violations|IV-2|实际均值处的偏差下界被改成任意中心处的下界；量词扩张不成立。|直接对应|
|[014](../dataset-witness-repaired-v1.1-20260922/records/014/witness.md)|Channel additivity violations|IV-2|反证分支里的子项结论被当作无条件结论；反证只能给出总量下界。|直接对应|
|[017](../dataset-witness-repaired-v1.1-20260922/records/017/witness.md)|Channel additivity violations|IV-1|含 log(d-1) 的连续性定理公式被用于 d=1，超出其适用范围。|直接对应|
|[021](../dataset-witness-repaired-v1.1-20260922/records/021/witness.md)|Werner–Holevo zero-capacity boundary|IV-4|计划在三维约束空间内搜索不同的 kernel-avoiding 扰动，但合法空间退化为原态，无所需自由度。|研究场景适配|
|[022](../dataset-witness-repaired-v1.1-20260922/records/022/witness.md)|Werner–Holevo zero-capacity boundary|IV-2|两次使用的原始系数更大不推出每次使用效果更强；本子类只针对归一化比较，不包含另一个阈值计算错误。|直接对应|
|[024](../dataset-witness-repaired-v1.1-20260922/records/024/witness.md)|Quantum-capacity superactivation|IV-2|某个逐因子界失败不推出所有逐因子证明都不可能；擦除信道给出反例。|直接对应|
|[025](../dataset-witness-repaired-v1.1-20260922/records/025/witness.md)|Quantum-capacity superactivation|IV-2|正的双向辅助容量不推出非反可降解；半擦除信道同时具有这两个性质。|直接对应|
|[026](../dataset-witness-repaired-v1.1-20260922/records/026/witness.md)|Quantum-capacity superactivation|IV-2|一个反例要求添加限制，不推出必须添加特定的 unital 限制。|直接对应|
|[027](../dataset-witness-repaired-v1.1-20260922/records/027/witness.md)|Bound entanglement with negative partial transpose|IV-4|路线把每个子集交换矩阵 PSD 设为待证明的充分条件；该加强目标被精确反例否定。正系数分解及条件蕴含没有错。|研究场景适配|
|[028](../dataset-witness-repaired-v1.1-20260922/records/028/witness.md)|Circuit-distance stabilization|IV-2|从合法无冲突调度推出确定性 detector/精确转移表示，缺少 MC；这里是新构造的保证，不是已定位的外部定理误用。|直接对应|
|[029](../dataset-witness-repaired-v1.1-20260922/records/029/witness.md)|Circuit-distance stabilization|IV-1|将原 detector 子空间命题用于更大的含逻辑分量空间 V；原命题的消去前提失效。|直接对应|
|[030](../dataset-witness-repaired-v1.1-20260922/records/030/witness.md)|Circuit-distance stabilization|IV-1|边界改变后复用原终端条件 v；该条件依赖原零偏移假设，不能直接沿用。|直接对应|
|[032](../dataset-witness-repaired-v1.1-20260922/records/032/witness.md)|Circuit versus effective distance|IV-2|最终恒定不推出最终等于静态码距；所需极限值等式没有建立。|直接对应|
|[033](../dataset-witness-repaired-v1.1-20260922/records/033/witness.md)|Circuit versus effective distance|IV-1|整体/最小扇区界被用于另一个 memory sector 的截断；界的适用对象不同。|直接对应|
|[034](../dataset-witness-repaired-v1.1-20260922/records/034/witness.md)|Circuit versus effective distance|IV-1|子定理的 R>=d 前提在根结论中丢失。|直接对应|
|[035](../dataset-witness-repaired-v1.1-20260922/records/035/witness.md)|Circuit versus effective distance|IV-2|残差不同不推出物理故障位置不同；同位置的不同 Pauli 可产生不同残差。|直接对应|
|[036](../dataset-witness-repaired-v1.1-20260922/records/036/witness.md)|Optimal circuit distance of the Gross code|IV-2|两组逐对次序相同不推出整组门不交错。|直接对应|
|[037](../dataset-witness-repaired-v1.1-20260922/records/037/witness.md)|Optimal circuit distance of the Gross code|IV-2|受限同周期编码的 UNSAT 不推出所有合法跨周期调度不存在；不重复标为问题理解。|直接对应|
|[038](../dataset-witness-repaired-v1.1-20260922/records/038/witness.md)|Complexity of distance-preserving schedules|IV-2|能施加两两相等关系不推出关系仅限于此；四项 XOR 关系提供反例。|直接对应|
|[039](../dataset-witness-repaired-v1.1-20260922/records/039/witness.md)|Complexity of distance-preserving schedules|IV-2|辅助点采用新坐标不保证 wiring 无意外耦合；可满足原式被编译成不可满足系统。|直接对应|
|[040](../dataset-witness-repaired-v1.1-20260922/records/040/witness.md)|Quantum k-sum with small alphabets|IV-2|任意字母重标记不推出单次 XOR oracle 酉共轭模拟；非线性双射不保持 XOR 结构。|直接对应|
|[041](../dataset-witness-repaired-v1.1-20260922/records/041/witness.md)|Quantum k-sum with small alphabets|IV-2|基数表示的唯一性不能保证所写正系数构造消去相同 payload，tag 分离也未覆盖所有模式。|直接对应|
|[042](../dataset-witness-repaired-v1.1-20260922/records/042/witness.md)|Quantum k-sum with small alphabets|IV-1|使用有字母表下限的构造定理推出无下限范围的结论。|直接对应|
|[044](../dataset-witness-repaired-v1.1-20260922/records/044/witness.md)|Quantum k-sum with small alphabets|IV-4|计划构造具有过高纯次数的 signed measure；该候选目标与既有算法上界冲突。不是将 conjecture 误写成已证。|研究场景适配|
|[045](../dataset-witness-repaired-v1.1-20260922/records/045/witness.md)|Quantum k-sum with small alphabets|IV-1|donor 结果的 K<=2 floor(N/2)-1 前提在奇 N 端点不满足。|直接对应|
|[046](../dataset-witness-repaired-v1.1-20260922/records/046/witness.md)|Set equality and collision|IV-1|正确嵌入只能继承源证书的条件性结论，不能把缺失范数恒等式的证书作为完成结果使用。|直接对应|
|[047](../dataset-witness-repaired-v1.1-20260922/records/047/witness.md)|Set equality and collision|IV-2|T_b/m<=B 不推出 T_b<=B；被计算量本身可正确。|直接对应|
|[048](../dataset-witness-repaired-v1.1-20260922/records/048/witness.md)|Set equality and collision|IV-2|归一化数值低于 cap 不推出未归一化物理量低于 cap。|直接对应|
|[050](../dataset-witness-repaired-v1.1-20260922/records/050/witness.md)|Finite-dimensional Grothendieck bounds|IV-2|投影前的独立方向不推出投影后保持独立，16个方向消失。|直接对应|
|[055](../dataset-witness-repaired-v1.1-20260922/records/055/witness.md)|Finite-dimensional Grothendieck bounds|IV-1|诉诸弱对偶把分离 moment 可行性当作上界证书；引用构造的证书方向不符。|直接对应|
|[056](../dataset-witness-repaired-v1.1-20260922/records/056/witness.md)|Group-orbit Bell matrices|IV-2|从顶奇异空间推出无条件存在等列数完整配对基；矩形零矩阵反驳构造。|直接对应|
|[057](../dataset-witness-repaired-v1.1-20260922/records/057/witness.md)|Group-orbit Bell matrices|IV-7|注册的全区间仿射极值规律错误；另一符号对在参数端点超过所报仿射分支。|研究场景适配|
|[061](../dataset-witness-repaired-v1.1-20260922/records/061/witness.md)|Channel additivity violations|IV-2|推出一个真不等式不意味着得到更强的标量排除能力；旧约束已经严格蕴含它。|直接对应|
|[066](../dataset-witness-repaired-v1.1-20260922/records/066/witness.md)|Optimal circuit distance of the Gross code|IV-1|对不被平移保持的 base 约束使用对称商覆盖论证，缺少不变性前提。|直接对应|
|[067](../dataset-witness-repaired-v1.1-20260922/records/067/witness.md)|Optimal circuit distance of the Gross code|IV-2|遗漏域外抵消模式的搜索不能支持所称子池排除结论。|直接对应|
|[071](../dataset-witness-repaired-v1.1-20260922/records/071/witness.md)|Group-orbit Bell matrices|IV-1|群平均给出不变最优代表，不给出全部最优策略的 commutant 参数化。|直接对应|
|[072](../dataset-witness-repaired-v1.1-20260922/records/072/witness.md)|Group-orbit Bell matrices|IV-1|最小秩结论应用时没有保留可行集非空条件。|直接对应|
|[074](../dataset-witness-repaired-v1.1-20260922/records/074/witness.md)|Quantum k-sum with small alphabets|IV-2|共同位移不能推出覆盖所有目标剩余类；偶系数只产生偶目标。|直接对应|
|[077](../dataset-witness-repaired-v1.1-20260922/records/077/witness.md)|Finite-dimensional Grothendieck bounds|IV-2|局部秩和 INCONCLUSIVE 输出不推出整个子问题已被程序完整判定。|直接对应|

## 范围与边界

022只把未按使用次数归一化的强弱推断放入 IV-2；它另一个阈值计算错误仍是 III，不重复纳入45条分母。037只按受限UNSAT到一般不存在性的推断归 IV-2；本文件不替代一级表的后续同步。
027的正系数分解及“每项PSD则总和PSD”均正确；IV-4只指不可能实现的加强目标。044明确为未证明候选；不伪造此前存在错误推导。
IV-1与IV-2在概念上并不天然互斥，本次对明确引用已有结果的错误优先使用IV-1；覆盖不完整不另创一类。
若要求完全不适配原竞赛题框架，可将上述5条报告为待适配，而不是将其当作新确认的无效推导。
