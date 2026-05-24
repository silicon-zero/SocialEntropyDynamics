# SED v2.0 完整公式手册

> 本文档汇总了 SocialEntropyDynamics v2.0 的所有数学定义、辅助函数、主方程及稳定性判据，可作为理论与代码实现的唯一公式参考。

---

## 1. 状态变量与系统秩序度

五维状态向量：

$$
\mathbf{X}(t) = \begin{bmatrix} S_G(t) \\ S_C(t) \\ S_T(t) \\ M(t) \\ L(t) \end{bmatrix}, \quad t \in [0,\infty)
$$

总熵与总秩序度：

$$
S_{sys}(t) = w_G S_G + w_C S_C + w_T S_T, \quad w_G + w_C + w_T = 1
$$

$$
\Phi_{sys}(t) = 1 - S_{sys}(t)
$$

安全稳态区间：

$$
S_{min} \leq S_{sys} \leq S_{crit} < S_{max}
$$

---

## 2. 核心辅助函数

### 2.1 临界慢化因子

$$
f(S_{sys}) = \frac{1}{1 + \exp\left[\kappa (S_{sys} - S_{crit})\right]}, \quad \kappa > 0
$$

- $S_{sys} \ll S_{crit} \Rightarrow f \approx 1$ （正常恢复力）
- $S_{sys} \to S_{crit} \Rightarrow f = 0.5$ （恢复力减半）
- $S_{sys} \gg S_{crit} \Rightarrow f \to 0$ （临界崩溃）

### 2.2 技术双通道函数

技术层熵同时产生赋能（负熵）和反噬（熵增）：

$$
\phi_{\text{benefit}}(S_T) = \sigma_1(S_T)\bigl[1 - \sigma_2(S_T)\bigr]
$$

$$
\phi_{\text{harm}}(S_T) = \sigma_2(S_T)
$$

其中：

$$
\sigma_1(S_T) = \frac{1}{1 + e^{-k_1(S_T - \theta_1)}}, \quad
\sigma_2(S_T) = \frac{1}{1 + e^{-k_2(S_T - \theta_2)}}, \quad \theta_1 < \theta_2
$$

### 2.3 信息感知过滤函数

**通用形式（无防火墙/完全开放）**：

$$
S_C^{\text{perceived}} = S_C \cdot (1 + \nu \cdot S_T), \quad \nu \geq 0
$$

**GFW 修正形式（适用于中国）**：

$$
S_C^{\text{perceived,CN}} = S_C^{\text{int}} (1 + \nu_{\text{int}} S_T) + S_C^{\text{ext}} \cdot \mathcal{F}_{\text{GFW}}(S_T)
$$

$$
\mathcal{F}_{\text{GFW}}(S_T) = \frac{1}{1 + \exp\bigl[k_{\text{GFW}}(S_T - \theta_{\text{GFW}})\bigr]}
$$

- $\nu_{\text{int}}$：内部感知失真系数（约0.80）
- $\nu_{\text{ext}}$：外部感知失真系数（约0.15，防火墙过滤后极低）
- $k_{\text{GFW}}, \theta_{\text{GFW}}$：防火墙过滤陡峭度与阈值

### 2.4 治理效能衰减函数

$$
\mathcal{E}(S_C, S_T) = \tanh(\eta_C S_C) \cdot \frac{1}{1 + \eta_T S_T}, \quad \eta_C, \eta_T > 0
$$

- 社会接受度：$\tanh(\eta_C S_C)$ ，$S_C$ 越大，社会越分裂，政策越难落地
- 信息渠道通畅度：$1/(1+\eta_T S_T)$ ，$S_T$ 越高，信息越堵塞，政策传达受阻

### 2.5 动员信息带宽（双重银行接口）

隐性银行向实体银行转化负熵信用的能力：

$$
\mathcal{B}(S_{sys}, M, L) = B_{\max} \cdot \max\!\left(0, 1 - \frac{S_{sys}}{S_{crit}}\right) \cdot \tanh\!\left(\frac{M}{M_{\text{ref}}}\right) \cdot \exp\!\left(-\frac{L}{L_{\text{tol}}}\right)
$$

| 因子 | 数学表示 | 社会隐喻 |
|------|----------|----------|
| 秩序信用 | $\max(0, 1 - S_{sys}/S_{crit})$ | 系统越有序，信念越强，隐性银行越愿意放贷 |
| 实体锚定 | $\tanh(M/M_{\text{ref}})$ | 实体资源充足，隐性信贷才能兑换成实际物资 |
| 负债惩罚 | $\exp(-L/L_{\text{tol}})$ | 隐性负债越高，信贷额度越紧，直至归零 |

**分国别带宽修正**：

$$
\mathcal{B}_{\text{eff}} = \mathcal{B} \times \begin{cases}
\mathcal{B}_{\text{int}} & (\text{内部动员})\\
\mathcal{B}_{\text{ext}} & (\text{外部动员})
\end{cases}
$$

### 2.6 隐性负债利率

$$
r(L, S_{sys}) = r_0 \cdot L \cdot \exp\!\left(\frac{S_{crit} - S_{sys}}{\delta}\right), \quad r_0 > 0,\; \delta > 0
$$

- 利率随负债存量线性增长，且当系统逼近临界时指数爆炸
- $\delta$ 越小，悬崖越陡，崩溃越突然

### 2.7 生产与贸易函数

内生生产（秩序越好产出越高）：

$$
P(t) = \pi \cdot \max\!\left(0, 1 - \frac{S_{sys}}{S_{crit}}\right), \quad \pi > 0
$$

国际贸易交互：

$$
T_{\text{trade}}(t) = A_{\text{trade}} \sin(\omega_{\text{trade}} t) - \tau \cdot \text{Tariff}(t)
$$

---

## 3. 五维耦合主方程

$$
\boxed{
\begin{aligned}
\frac{dS_G}{dt} &= \sigma_G 
- \alpha_G S_G \, f(S_{sys}) \, \mathcal{E}(S_C, S_T) \\
&\quad + \beta_{GC} \, S_C^{\text{perceived}} \\
&\quad - \gamma_{TG}^{\text{benefit}} \, \phi_{\text{benefit}}(S_T) \, S_T 
+ \gamma_{TG}^{\text{noise}} \, \phi_{\text{harm}}(S_T) \, S_T \\
&\quad - \delta_G \, M \, \mathcal{E}(S_C, S_T) \\
&\quad + \theta_G \, r(L, S_{sys}) \, L \\[8pt]
\frac{dS_C}{dt} &= \sigma_C 
- \beta_C S_C \, f(S_{sys}) \, \mathcal{E}(S_C, S_T) \\
&\quad + \alpha_{GC} S_G \\
&\quad - \gamma_{TC}^{\text{benefit}} \, \phi_{\text{benefit}}(S_T) \, S_T 
+ \gamma_{TC}^{\text{noise}} \, \phi_{\text{harm}}(S_T) \, S_T \\
&\quad - \delta_C \, M \, \mathcal{E}(S_C, S_T) \\
&\quad + \theta_C \, r(L, S_{sys}) \, L \\[8pt]
\frac{dS_T}{dt} &= \sigma_T + \xi_{\text{ext}}(t) \\
&\quad - \gamma_T S_T \, f(S_{sys}) \\
&\quad + \tau_{\text{debt}} \, \phi_{\text{harm}}(S_T) \\
&\quad - \alpha_{GT} S_G \, \mathcal{E}(S_C, S_T) \\
&\quad - \delta_T \, M \, \mathcal{E}(S_C, S_T) \\
&\quad + \theta_T \, r(L, S_{sys}) \, L \\
&\quad - \omega \cdot u(t) \cdot \bigl[1 - f(S_{sys})\bigr] \\[8pt]
\frac{dM}{dt} &= \pi\!\left(1 - \frac{S_{sys}}{S_{crit}}\right) + T_{\text{trade}}(t) \\
&\quad - \bigl( \mu_G S_G + \mu_C S_C + \mu_T S_T \bigr) \\
&\quad + \mathcal{B}(S_{sys}, M, L) \cdot \bigl[1 + \chi \cdot u(t)\bigr] \\[8pt]
\frac{dL}{dt} &= \frac{1}{\ell} \mathcal{B}(S_{sys}, M, L) \cdot \bigl[1 + \chi \cdot u(t)\bigr] \\
&\quad - \lambda_{\text{repay}} L \, \mathcal{E}(S_C, S_T) \\
&\quad + \sigma_L \, \xi_L(t)
\end{aligned}
}
$$

---

## 4. 双边耦合项（两国模型）

对于国家 $A$ 和国家 $B$，外部冲击包含对方技术反噬的叠加：

$$
\xi_{\text{ext}}^A(t) = \xi_{\text{base}}^A(t) + \zeta^{B \to A} \cdot S_T^B(t) \cdot \bigl[1 + \phi_{\text{harm}}^B(S_T^B)\bigr]
$$

贸易交互：

$$
T_{\text{trade}}^A(t) = T_{\text{base}}^A(t) + \tau^{B \to A} M^B(t) - \tau^{A \to B} M^A(t) - \tau_{\text{tariff}} \cdot \text{Tariff}^{B \to A}(t)
$$

带宽竞争（全球隐性银行信贷额度有限）：

$$
\mathcal{B}_{\text{global}}^A(t) = \mathcal{B}^A(t) \cdot \left[1 - \rho \cdot \frac{\mathcal{B}^B(t)}{B_{\max}^A + B_{\max}^B}\right]
$$

---

## 5. 离散事件注入

元首会晤、企业外交等作为瞬时脉冲：

$$
\mathbf{X}(t^+) = \mathbf{X}(t^-) + \Delta \mathbf{X}_{\text{event}}
$$

示例（2026年中美企业会见）：

$$
\Delta \mathbf{X}_{\text{CN}} = 
\begin{bmatrix}
-0.03 \\ 0 \\ -0.04 \\ +0.03 \\ 0
\end{bmatrix}, \quad
\Delta \mathbf{X}_{\text{US}} = 
\begin{bmatrix}
0 \\ +0.01 \\ -0.02 \\ +0.05 \\ 0
\end{bmatrix}
$$

---

## 6. 系统稳定性与相变条件

### 6.1 稳态吸引子

$$
\frac{d\mathbf{X}}{dt}\bigg|_{\mathbf{X}^*} = \mathbf{0}
$$

### 6.2 临界崩溃条件

当同时满足：

1. $S_{sys} \geq S_{crit}$
2. $\mathcal{B}(S_{sys}, M, L) \to 0$
3. $f(S_{sys}) \cdot \mathcal{E}(S_C, S_T) < \epsilon$

系统发生不可逆相变。

### 6.3 历史僵尸态

$\mathcal{B} = 0$ 且 $S_{sys} < S_{max}$ ，国家名义存在但熵值单调递增，直至解体。

### 6.4 帝国疲劳定律

$$
\frac{d\Phi_{sys}}{dt} \propto -\kappa_{\text{empire}} \cdot (\text{GlobalCommitments}) \cdot \frac{1}{\mathcal{B}_{\text{eff}}}
$$

---

## 7. 参数速查表

| 参数 | 含义 | 中国典型值 | 美国典型值 | 俄罗斯(战时) |
|------|------|:--------:|:--------:|:---------:|
| $w_G, w_C, w_T$ | 总熵权重 | 0.35,0.40,0.25 | 0.30,0.45,0.25 | 0.45,0.35,0.20 |
| $S_{crit}$ | 临界阈值 | 0.70 | 0.65 | 0.65 |
| $\kappa$ | 相变陡峭度 | 10 | 8 | 10 |
| $\nu$ | 感知失真系数 | 0.32 (eff) | 1.30 | 0.90 |
| $B_{\max}$ | 最大带宽 | 0.65 | 0.45 | 0.35 |
| $M_{\text{ref}}$ | 锚定参考 (万亿) | 3.0 | 0.5 | 0.3 |
| $L_{\text{tol}}$ | 负债容忍阈值 | 90 | 38 | — |
| $r_0$ (×基准) | 基础利率倍数 | 0.65 | 1.35 | 1.50 |
| $\delta$ | 悬崖陡峭度 | 0.15 | 0.10 | 0.08 |
| $\ell$ | 杠杆系数 | 3.0 | 2.5 | 2.0 |
| $\omega$ | 赌注收益 | 0.15 | 0.20 | 0.10 |
| $\mathcal{B}_{\text{int}}$ | 内部共识带宽 | 0.72 | 0.38 | 0.45 |
| $\mathcal{B}_{\text{ext}}$ | 外部信息带宽 | 0.18 | 0.55 | 0.25 |

---

*本文档与 `sed_solver.py` 中的参数类 `SEDParams` 保持严格对应，任何参数变更须同时更新两者。*