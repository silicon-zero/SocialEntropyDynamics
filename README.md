# 🌌 SocialEntropyDynamics (SED)
**An Exploratory Framework for Modeling Social Resilience via Cross-Disciplinary Metaphors**

> **"本仓库是一个探索性的理论沙盒。我们尝试借用热力学与控制论的数学语言来描述社会系统的复杂性，但这仅是一种启发式隐喻，而非对物理定律的直接套用。"**

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: Experimental](https://img.shields.io/badge/Status-Experimental-orange)

## 📖 项目定位 (Project Scope)

**SocialEntropyDynamics (SED)** 是一个旨在探讨社会系统韧性的**概念性建模框架**。面对现代混合冲突与复合型内部转型压力，传统的线性分析工具常显不足。本项目尝试整合热力学、控制论与信息论的视角，构建了一个「政府-社会-技术」三层耦合的微分方程组，作为理解系统稳态与危机演化的**一种可能路径**。

⚠️ **重要免责声明 (Critical Disclaimer)**：
- **非物理定律**：本模型中的“熵”是信息论与系统论意义上的隐喻映射，**绝非**严格的热力学玻尔兹曼熵。社会系统是具备主观能动性的复杂适应系统，不能简单等同于封闭的物理耗散结构。
- **非预测工具**：当前代码仅为定性分析的数值骨架，参数尚未经过大规模实证数据校准。**请勿将其输出结果直接用于现实世界的政策制定或战略决策。**
- **开放证伪**：本框架处于早期探索阶段，必然存在大量简化与缺陷。我们发布此项目的核心目的，正是为了接受跨学科学术共同体的检验、批判与修正。

## 🧮 核心假设 (Core Hypothesis)

作为一种启发式建模尝试，我们假设社会系统的演化动力学可被近似描述为以下三维耦合方程组：

$$
\begin{aligned}
\frac{dS_G}{dt} &= \sigma_G - \alpha_G S_G \cdot f(S) + \beta_{GC} S_C - \gamma_{TG} S_T \$$6pt]
\frac{dS_C}{dt} &= \sigma_C - \beta_C S_C \cdot f(S) + \alpha_{GC} S_G - \gamma_{TC} S_T \$$6pt]
\frac{dS_T}{dt} &= \sigma_T + \xi_{ext}(t) - \gamma_T S_T \cdot f(S) - \alpha_{GT} S_G
\end{aligned}
$$

其中各符号含义如下：

- $S_G, S_C, S_T$：分别表征政府、社会、技术子系统的状态变量（如秩序度、信任水平或信息通量）；
- $\sigma_i$：各子系统的内生演化基率；
- $\alpha, \beta, \gamma$：层间耦合系数，下标 $XY$ 表示子系统 $Y$ 对 $X$ 的作用强度与方向；
- $f(S)$：临界慢化因子，模拟系统逼近阈值时恢复力的非线性衰减；
- $\xi_{ext}(t)$：外部随机扰动项，表征不可预见的 exogenous shock。

> 📖 以上仅为核心符号速查。完整的变量操作化定义、参数取值依据及推导逻辑，请参阅 [理论文档](docs/Theory_and_Cases.md)。

## 💻 算法实现 (Algorithm Implementation)

我们提供了一个基于 `SciPy` 的三维耦合 ODE 求解器，忠实反映了上述理论假设中的层间交互与临界相变机制：
- 👉 **[查看 v1.0 耦合算法源码](algorithm/sed_solver_v1.py)**

### 快速运行
```bash
pip install numpy scipy matplotlib
python algorithm/sed_solver_v1.py
