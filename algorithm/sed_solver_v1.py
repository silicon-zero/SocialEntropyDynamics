"""
SocialEntropyDynamics (SED) v1.0 - 三维耦合动力学求解器
=====================================================
完整实现「政府-社会-技术」三层状态变量的非线性耦合微分方程组。
包含层间压力传导、技术赋能/反噬、控制论时滞反馈及临界相变机制。

Author: Open Source Community
License: MIT
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class SEDCoupledParams:
    """SED v1.0 三维耦合参数集"""
    def __init__(self):
        # === 权重系数 (总熵合成) ===
        self.w_G, self.w_C, self.w_T = 0.4, 0.4, 0.2
        
        # === 政府层 (Government) 参数 ===
        self.sigma_G = 0.03      # 制度摩擦/科层制自然老化
        self.alpha_G = 0.6       # 政府韧性恢复率 (自我纠错能力)
        self.beta_GC = 0.45      # 社会压力传导系数 (社会动荡倒逼政府改革/过载)
        self.gamma_TG = 0.3      # 技术赋能政府 (数字治理降低行政熵)
        self.tau_G = 5.0         # 政府响应时滞 (控制论特征)
        
        # === 社会层 (Society) 参数 ===
        self.sigma_C = 0.04      # 信任瓦解/原子化自然趋势
        self.beta_C = 0.5        # 社会自组织修复率 (社区互助/共识凝聚)
        self.alpha_GC = 0.35     # 政策冲击放大系数 (不当干预引发次生摩擦)
        self.gamma_TC = 0.25     # 技术连接增益 (信息流通修复信任)
        
        # === 技术层 (Technology) 参数 ===
        self.sigma_T = 0.02      # 基础设施退化/信息噪声基底
        self.gamma_T = 0.7       # 技术迭代自愈率 (摩尔定律/开源生态)
        self.xi_ext_amp = 0.3    # 外部认知战/AI攻击振幅
        self.xi_ext_freq = 0.2   # 外部攻击频率
        self.alpha_GT = 0.4      # 制度保护系数 (监管/法律对数字空间的稳态作用)
        
        # === 非线性激活阈值 ===
        self.S_crit = 0.6        # 临界相变阈值 (超过此值负熵机制可能失效)


def sed_coupled_ode(t, Y, params: SEDCoupledParams):
    """
    三维耦合常微分方程组
    Y = [S_G, S_C, S_T]
    """
    S_G, S_C, S_T = Y
    
    # 外部时变冲击 (AI认知战主要作用于技术层与社会层)
    xi_ext = params.xi_ext_amp * (1 + np.sin(params.xi_ext_freq * t))
    
    # 临界慢化效应: 当任一层熵接近临界值时，系统恢复力非线性衰减
    crit_factor = 1.0 / (1.0 + np.exp(10 * (max(S_G, S_C, S_T) - params.S_crit)))
    
    # --- 政府层动力学 ---
    # 内生老化 - 自愈(受临界因子调制) + 社会压力传导 - 技术赋能
    dSG_dt = (params.sigma_G 
              - params.alpha_G * S_G * crit_factor 
              + params.beta_GC * S_C 
              - params.gamma_TG * S_T)
    
    # --- 社会层动力学 ---
    # 内生撕裂 - 自组织修复(受临界因子调制) + 政策滞后冲击 - 技术连接增益
    # 注: 此处简化了时滞项，用当前S_G代表累积的政策压力势能
    dSC_dt = (params.sigma_C 
              - params.beta_C * S_C * crit_factor 
              + params.alpha_GC * S_G 
              - params.gamma_TC * S_T)
    
    # --- 技术层动力学 ---
    # 基底噪声 + 外部攻击 - 技术自愈 - 制度保护
    dST_dt = (params.sigma_T 
              + xi_ext 
              - params.gamma_T * S_T * crit_factor 
              - params.alpha_GT * S_G)
    
    return [dSG_dt, dSC_dt, dST_dt]


def run_coupled_simulation():
    """运行三维耦合并绘制多子图演化轨迹"""
    params = SEDCoupledParams()
    Y0 = [0.1, 0.15, 0.05]  # 初始状态: [S_G0, S_C0, S_T0]
    t_span = (0, 80)
    t_eval = np.linspace(*t_span, 2000)
    
    sol = solve_ivp(sed_coupled_ode, t_span, Y0, args=(params,), 
                    t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)
    
    S_G, S_C, S_T = sol.y
    S_sys = params.w_G * S_G + params.w_C * S_C + params.w_T * S_T
    
    # === 可视化 ===
    fig, axes = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})
    
    # 上图: 三层分量演化
    axes[0].plot(sol.t, S_G, label='$S_G$ (Government)', color='#1f77b4', linewidth=2)
    axes[0].plot(sol.t, S_C, label='$S_C$ (Society)', color='#ff7f0e', linewidth=2)
    axes[0].plot(sol.t, S_T, label='$S_T$ (Technology)', color='#2ca02c', linewidth=2)
    axes[0].axhline(params.S_crit, color='red', linestyle='--', alpha=0.7, label=f'Critical Threshold ($S_{{crit}}$={params.S_crit})')
    axes[0].set_title('SED v1.0: Three-Tier Coupled Entropy Dynamics', fontsize=15, fontweight='bold')
    axes[0].set_ylabel('Subsystem Entropy')
    axes[0].legend(loc='upper left')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    
    # 下图: 总系统熵与安全区间
    axes[1].plot(sol.t, S_sys, label='$S_{sys}$ (Total)', color='black', linewidth=2.5)
    axes[1].fill_between(sol.t, 0.2, 0.7, color='green', alpha=0.15, label='Safe Homeostasis Zone')
    axes[1].axhline(0.7, color='darkred', linestyle='-', alpha=0.5)
    axes[1].axhline(0.2, color='darkgreen', linestyle='-', alpha=0.5)
    axes[1].set_xlabel('Time (t)')
    axes[1].set_ylabel('Total System Entropy')
    axes[1].legend(loc='upper left')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('sed_v1_coupled_dynamics.png', dpi=300, bbox_inches='tight')
    print("✅ SED v1.0 三维耦合仿真完成！图表已保存。")
    plt.show()

if __name__ == "__main__":
    run_coupled_simulation()
