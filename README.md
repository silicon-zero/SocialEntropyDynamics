# 🌌 SocialEntropyDynamics (SED)
**An Open-Source Theoretical Framework & Algorithm for Complex Social Systems**

> **"在超限战与复杂性危机交织的时代，社会的韧性不取决于刚性的控制，而取决于负熵摄入与转化的动态平衡。"**

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: v1.0](https://img.shields.io/badge/Status-v1.0_Coupled-green.svg)

## 📖 项目简介 (Abstract)
**SocialEntropyDynamics (SED)** 是一套基于热力学、控制论、信息论跨公理推导的原创社会系统动力学模型。本项目首次建立 **「政府-社会-技术三层负熵平衡方程」**，并提供三维耦合的数值求解算法，量化解释社会稳态、系统韧性与危机演化规律。

SED 不将社会视为机械的牛顿系统，而是将其定义为**远离平衡态的耗散结构（Dissipative Structure）**。应对现代混合战争（超限战）的最高策略并非对等反击，而是维持系统总熵在安全区间 $[S_{min}, S_{max}]$ 内的动态稳态。

## 🧮 核心方程 (The Core Equation)
社会系统的演化遵循非平衡态热力学定律，其总熵变率定义为：

$$
\frac{dS_{sys}}{dt} = \underbrace{\sigma_{int}(t) + \xi_{ext}(t)}_{\text{总熵产生率}} - \underbrace{\left[ \alpha \Phi_G(I, R) + \beta \Psi_C(A, K) + \gamma \mathcal{T}(D) \right]}_{\text{系统负熵摄入率}}
$$

### 变量释义：
- **$S_{sys}$**：社会系统总熵（无序度/失能程度）。治理目标是维持 $S_{min} \leq S_{sys} \leq S_{max}$。
- **$\sigma_{int}$**：内生结构性摩擦（经济转型、治理迭代、社会预期重塑等带来的自然熵增）。
- **$\xi_{ext}$**：外源不对称冲击（超限战、AI认知战、地缘脱钩等外部注入的高熵）。
- **$\alpha \Phi_G$**：政府负熵供给（资源调配、信息处理、体制敏捷度）。
- **$\beta \Psi_C$**：社会自组织缓冲（社会资本、认知冗余、社会激活系数）。
- **$\gamma \mathcal{T}$**：技术制度适配（数字基建与治理规则的匹配度）。

## 💻 核心算法 (Core Algorithm - v1.0 三维耦合版)
本项目提供基于 `SciPy` 的三维耦合常微分方程组数值求解器，完整实现政府($S_G$)-社会($S_C$)-技术($S_T$)三层的非线性交互动力学。
- 👉 **[查看核心算法代码](algorithm/sed_solver_v1.py)**：包含层间压力传导、临界慢化效应、外部非对称冲击注入及多稳态相空间轨迹仿真。

## 📚 深度阅读 (Documentation)
- 👉 **[理论推导与现实案例推演](docs/Theory_and_Cases.md)**：包含跨学科推导、AI认知战与复合型内部张力的共振分析。

## 🚀 快速运行 (Quick Start)
```bash
pip install numpy scipy matplotlib
python algorithm/sed_solver_v1.py
