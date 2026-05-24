# 双重银行理论与动员信息带宽

## 1. 实体银行（Explicit Bank）

**定义**：存在于资本主义规则内的显性机构，发行通用货币“动员资源”($M$)。涵盖资本、股票、期货、大宗商品、武器、专利、劳动力期权等一切可定价实物与权益。

**实体资源动力学**：

$$
\frac{dM}{dt} = \underbrace{P(t)}_{\text{生产/贸易盈余}} - \underbrace{\sum_{i} C_i(S_i)}_{\text{各层消耗}} + \underbrace{T_{\text{trade}}(t)}_{\text{国际交互}} + \underbrace{\mathcal{B}[1+\chi u]}_{\text{隐性银行注入}}
$$

各层消耗函数：
$$
C_i(S_i) = \mu_i S_i, \quad i \in \{G, C, T\}
$$

## 2. 隐性银行（Implicit Bank）

**定义**：不可观测但可交互的维度，交易“未来秩序”($L$)。抵押品为民族凝聚力、历史正当性、子孙的生存空间。这是国家在绝境中最后的贷款人。

**隐性负债动态**：

$$
\frac{dL}{dt} = \frac{1}{\ell}\mathcal{B}[1+\chi u] - \lambda_{\text{repay}} L \, \mathcal{E}(S_C, S_T) + \sigma_L \xi_L(t)
$$

- $\ell$：杠杆系数，每单位实体注入需增加 $\frac{1}{\ell}$ 的负债
- $\lambda_{\text{repay}}$：偿还速率，受治理效能 $\mathcal{E}$ 调节
- $\sigma_L \xi_L(t)$：黑天鹅冲击（债务重组或突然违约）

## 3. 动员信息带宽 $\mathcal{B}$

### 3.1 定义与公式

$$
\mathcal{B}(S_{sys}, M, L) = B_{\max} \cdot \max\!\left(0, 1 - \frac{S_{sys}}{S_{crit}}\right) \cdot \tanh\!\left(\frac{M}{M_{\text{ref}}}\right) \cdot \exp\!\left(-\frac{L}{L_{\text{tol}}}\right)
$$

### 3.2 三因子隐喻

| 因子 | 数学 | 隐喻 |
|------|------|------|
| **秩序信用** | $\max(0, 1 - S_{sys}/S_{crit})$ | 系统有序，信念强，隐性银行愿放贷 |
| **实体锚定** | $\tanh(M/M_{\text{ref}})$ | 足够实物抵押，隐性信贷才能兑为实际资源 |
| **负债惩罚** | $\exp(-L/L_{\text{tol}})$ | 负债透支未来，信贷额度指数收缩 |

### 3.3 带宽归零的后果

当 $\mathcal{B} \to 0$：
- 隐性银行永久关闭信贷
- 国家丧失最后的精神与物质动员能力
- 进入“历史僵尸”稳态：名义存在，但无法动员任何未来力量

## 4. 隐性负债利率 $r$

$$
r(L, S_{sys}) = r_0 \cdot L \cdot \exp\!\left(\frac{S_{crit} - S_{sys}}{\delta}\right)
$$

**“悬崖效应”**：
- $S_{sys} \ll S_{crit}$ 时利率温和
- $S_{sys} \to S_{crit}$ 时利率指数爆炸
- $\delta$ 越小，悬崖越陡，系统看似稳定实则利率已不可持续

**各国利率乘数**（相对基准 $r_0$）：
- 中国：0.65× （有序化债降低系统风险）
- 美国：1.35× （国债利息突破1万亿，市场定价加息）
- 俄罗斯（战时）：1.50× （制裁与战争消耗叠加）

## 5. 战略赌注与跨期风险交换

赌注决策函数 $u(t) \in [0,1]$，产生的额外负熵注入与负债为：

$$
\Delta M_{\text{bet}} = \omega \cdot u(t) \cdot [1 - f(S_{sys})] \quad (\text{通过带宽注入})
$$

$$
\Delta L_{\text{bet}} = \frac{1}{\ell} \Delta M_{\text{bet}} \quad (\text{等比例增加负债})
$$

- 赌赢（$\omega$ 足够大）：某层熵骤降，系统跃迁至高秩序吸引子
- 赌输：$L$ 飙升，利率 $r$ 暴涨，触发临界崩溃

典型赌注案例：发动特别军事行动（俄罗斯2022）、举国投入AGI竞赛、大规模财政刺激而无改革配套。

## 6. GFW 与选择性带宽架构

中国的GFW构建了非对称信息带宽，核心函数：

$$
\mathcal{F}_{\text{GFW}}(S_T) = \frac{1}{1 + \exp[k_{\text{GFW}}(S_T - \theta_{\text{GFW}})]}
$$

| 带宽类型 | 取值 | 影响 |
|---------|------|------|
| 外部带宽 $\mathcal{B}_{\text{ext}}$ | 0.18 | 过滤认知战、谣言等外部污染，但限制学术技术前沿信息 |
| 内部带宽 $\mathcal{B}_{\text{int}}$ | 0.72 | 内部共识高，社会感知失真 $\nu_{\text{eff}}$ 仅0.32 |

**战略权衡**：
- 优势：外部信息污染极低，社会熵稳定，隐性银行利率可控
- 代价：技术层熵长期比开放国家高0.10-0.15，技术自主压力大

---

*“当一个国家被舆论战破坏，最先坍塌的不是政府层熵，而是动员信息带宽 $\mathcal{B}$。”*