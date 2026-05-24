# SocialEntropyDynamics (SED) v2.0 - The Implicit Bank / 隐性银行

**A Cross-Disciplinary Framework for Modeling Social System Resilience via Thermodynamics, Cybernetics, and Information Theory**

> 本仓库是一个探索性的理论沙盒。我们借用热力学与控制论的数学语言来描述社会系统的复杂性，但这仅是一种启发式隐喻，而非对物理定律的直接套用。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

---

## 项目定位

**SocialEntropyDynamics (SED)** 是一套基于热力学、控制论、信息论跨公理推导的原创社会系统动力学模型，首次建立「政府-社会-技术三层负熵平衡方程」，并引入**双重银行体系**与**动员信息带宽**概念，量化解释社会稳态、系统韧性与危机演化规律。

面对现代混合冲突（认知战、超限战、金融制裁）与复合型内部转型压力，传统的线性分析工具常显不足。本项目构建五维耦合微分方程组，作为理解系统稳态与危机演化的**一种可能路径**。

⚠️ **重要免责声明**：
- **非物理定律**：本模型中的“熵”是信息论意义上的隐喻映射，**绝非**严格的热力学玻尔兹曼熵。
- **非预测工具**：当前代码仅为定性分析的数值骨架，参数尚未经过大规模实证数据校准。
- **开放证伪**：本框架处于早期探索阶段，欢迎跨学科学术共同体的检验、批判与修正。

---

## 核心框架：五维双重银行模型

系统由五个宏观状态变量完全描述：

$$X(t) = [S_G(t), S_C(t), S_T(t), M(t), L(t)]$$

| 变量 | 定义 | 含义 |
|------|------|------|
| $S_G$ | 政府层熵 | 制度摩擦、决策滞胀、合法性损耗 |
| $S_C$ | 社会层熵 | 信任瓦解、共识断裂、原子化程度 |
| $S_T$ | 技术层熵 | 信息噪声、技术债务、基础设施脆弱性 |
| $M$ | 动员资源 | 实体银行可调动的实物与权益总量 |
| $L$ | 隐性负债 | 向不可解释维度借贷的“未来秩序”总额 |

### 双重银行体系

| | 实体银行 (Explicit) | 隐性银行 (Implicit) |
|------|------|------|
| **交易货币** | 动员资源 $M$ | 未来秩序 $L$ |
| **抵押品** | 黄金、油田、国债 | 民族凝聚力、文明叙事、子孙的生存空间 |
| **信息带宽** | 金融网络、通信协议 | 信仰强度、叙事效能、集体无意识共振 |

**动员信息带宽** $\mathcal{B}$ 是连接两个银行的关键通道：

$$\mathcal{B}(S_{sys}, M, L) = B_{\max} \cdot \max(0, 1 - \frac{S_{sys}}{S_{crit}}) \cdot \tanh(\frac{M}{M_{ref}}) \cdot \exp(-\frac{L}{L_{tol}})$$

---

## 快速开始

```bash
pip install -r requirements.txt
python algorithm/sed_solver.py