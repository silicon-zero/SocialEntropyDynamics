"""
SocialEntropyDynamics (SED) v2.0 - 双重银行五维求解器
=====================================================
完整实现「政府-社会-技术-动员资源-隐性负债」五维非线性耦合微分方程组。
包含技术双通道、信息过滤、治理效能衰减、动员信息带宽及战略赌注机制。

数学定义严格对应 docs/Formulas_Summary.md

Author: Open Source Community
License: MIT
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os

class SEDParams:
    """SED v2.0 参数集，与公式手册第7节对应"""
    def __init__(self):
        # 权重
        self.w_G, self.w_C, self.w_T = 0.35, 0.40, 0.25
        
        # 临界参数
        self.S_crit = 0.70
        self.kappa = 10.0
        
        # 政府层
        self.sigma_G = 0.03
        self.alpha_G = 0.65
        self.beta_GC = 0.45
        self.gamma_TG_benefit = 0.30
        self.gamma_TG_noise = 0.35
        self.delta_G = 0.15
        self.theta_G = 0.20
        
        # 社会层
        self.sigma_C = 0.04
        self.beta_C = 0.55
        self.alpha_GC = 0.35
        self.gamma_TC_benefit = 0.25
        self.gamma_TC_noise = 0.40
        self.delta_C = 0.20
        self.theta_C = 0.25
        
        # 技术层
        self.sigma_T = 0.02
        self.gamma_T = 0.70
        self.alpha_GT = 0.40
        self.delta_T = 0.10
        self.theta_T = 0.15
        self.tech_debt = 0.15
        self.omega = 0.15
        
        # 外部冲击
        self.xi_ext_amp = 0.30
        self.xi_ext_freq = 0.20
        
        # 技术双通道
        self.k1, self.theta1 = 8.0, 0.30
        self.k2, self.theta2 = 8.0, 0.55
        
        # 信息感知
        self.nu = 1.30  # 通用，中国修正见GFW特化
        self.nu_int = 0.80
        self.nu_ext = 0.15
        self.k_GFW, self.theta_GFW = 12.0, 0.50
        
        # 治理效能
        self.eta_C, self.eta_T = 3.0, 1.5
        
        # 动员资源
        self.pi = 0.50
        self.mu_G, self.mu_C, self.mu_T = 0.10, 0.15, 0.08
        self.trade_amp, self.trade_freq = 0.20, 0.10
        
        # 隐性负债
        self.l = 3.0  # 杠杆系数 (注意：变量名'l'避免与数字1混淆)
        self.lambda_repay = 0.15
        self.sigma_L = 0.05
        self.chi = 0.30  # 赌注额外放大
        
        # 带宽
        self.B_max = 0.65
        self.M_ref = 3.0
        self.L_tol = 90.0
        
        # 利率
        self.r0 = 0.02
        self.delta = 0.15


def compute_auxiliaries(S_G, S_C, S_T, M, L, params: SEDParams, u=0.0, t=0.0):
    """计算所有辅助函数，对应公式手册第2节"""
    S_sys = params.w_G * S_G + params.w_C * S_C + params.w_T * S_T
    
    # 临界慢化 (2.1)
    f = 1.0 / (1.0 + np.exp(params.kappa * (S_sys - params.S_crit)))
    
    # 技术双通道 (2.2)
    sigma1 = 1.0 / (1.0 + np.exp(-params.k1 * (S_T - params.theta1)))
    sigma2 = 1.0 / (1.0 + np.exp(-params.k2 * (S_T - params.theta2)))
    phi_benefit = sigma1 * (1.0 - sigma2)
    phi_harm = sigma2
    
    # 感知过滤 (2.3 通用形式)
    S_C_perceived = S_C * (1.0 + params.nu * S_T)
    
    # 治理效能 (2.4)
    eff_social = np.tanh(params.eta_C * S_C)
    eff_info = 1.0 / (1.0 + params.eta_T * S_T)
    efficacy = eff_social * eff_info
    
    # 动员带宽 (2.5)
    order_credit = max(0, 1.0 - S_sys / params.S_crit)
    anchor = np.tanh(M / params.M_ref)
    liability_penalty = np.exp(-L / params.L_tol)
    B = params.B_max * order_credit * anchor * liability_penalty
    
    # 隐性利率 (2.6)
    r = params.r0 * L * np.exp((params.S_crit - S_sys) / params.delta)
    
    # 外部冲击与生产贸易 (2.7)
    xi_ext = params.xi_ext_amp * (1.0 + np.sin(params.xi_ext_freq * t))
    production = params.pi * max(0, 1.0 - S_sys / params.S_crit)
    trade = params.trade_amp * np.sin(params.trade_freq * t)
    
    return S_sys, f, phi_benefit, phi_harm, S_C_perceived, efficacy, B, r, xi_ext, production, trade


def sed_v2_ode(t, Y, params: SEDParams, u_func=None):
    """五维耦合主方程 (对应公式手册第3节)"""
    S_G, S_C, S_T, M, L = Y
    
    if u_func is None:
        u = 0.0
    else:
        u = u_func(t, Y, params)
    
    (S_sys, f, phi_benefit, phi_harm, S_C_perceived,
     efficacy, B, r, xi_ext, production, trade) = compute_auxiliaries(S_G, S_C, S_T, M, L, params, u, t)
    
    # 政府层
    dSG_dt = (params.sigma_G
              - params.alpha_G * S_G * f * efficacy
              + params.beta_GC * S_C_perceived
              - params.gamma_TG_benefit * phi_benefit * S_T
              + params.gamma_TG_noise * phi_harm * S_T
              - params.delta_G * M * efficacy
              + params.theta_G * r * L)
    
    # 社会层
    dSC_dt = (params.sigma_C
              - params.beta_C * S_C * f * efficacy
              + params.alpha_GC * S_G
              - params.gamma_TC_benefit * phi_benefit * S_T
              + params.gamma_TC_noise * phi_harm * S_T
              - params.delta_C * M * efficacy
              + params.theta_C * r * L)
    
    # 技术层
    dST_dt = (params.sigma_T
              + xi_ext
              - params.gamma_T * S_T * f
              + params.tech_debt * phi_harm
              - params.alpha_GT * S_G * efficacy
              - params.delta_T * M * efficacy
              + params.theta_T * r * L
              - params.omega * u * (1.0 - f))
    
    # 动员资源
    consumption = params.mu_G * S_G + params.mu_C * S_C + params.mu_T * S_T
    implicit_injection = B * (1.0 + params.chi * u)
    dM_dt = production + trade - consumption + implicit_injection
    
    # 隐性负债
    repayment = params.lambda_repay * L * efficacy
    dL_dt = implicit_injection / params.l - repayment + params.sigma_L * np.random.normal(0, 1)
    
    return [dSG_dt, dSC_dt, dST_dt, dM_dt, dL_dt]


def run_simulation():
    """运行仿真并绘图"""
    params = SEDParams()
    Y0 = [0.30, 0.35, 0.30, 0.70, 0.50]  # 初始状态
    t_span = (0, 100)
    t_eval = np.linspace(*t_span, 2000)
    
    sol = solve_ivp(sed_v2_ode, t_span, Y0, args=(params,),
                    t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)
    
    S_G, S_C, S_T, M, L = sol.y
    S_sys = params.w_G * S_G + params.w_C * S_C + params.w_T * S_T
    Phi_sys = 1.0 - S_sys
    
    # 创建输出目录
    os.makedirs('results', exist_ok=True)
    
    fig, axes = plt.subplots(3, 1, figsize=(14, 14))
    
    axes[0].plot(sol.t, S_G, label='$S_G$ (Government)')
    axes[0].plot(sol.t, S_C, label='$S_C$ (Society)')
    axes[0].plot(sol.t, S_T, label='$S_T$ (Technology)')
    axes[0].axhline(params.S_crit, color='red', linestyle='--', label=f'Critical ($S_{{crit}}$={params.S_crit})')
    axes[0].set_title('SED v2.0: Three-Tier Entropy Dynamics')
    axes[0].legend()
    axes[0].grid(True, linestyle=':', alpha=0.6)
    
    axes[1].plot(sol.t, M, label='$M$ (Mobilization Resources)', color='green')
    axes[1].plot(sol.t, L, label='$L$ (Implicit Liability)', color='purple')
    axes[1].set_title('Dual Bank Dynamics')
    axes[1].legend()
    axes[1].grid(True, linestyle=':', alpha=0.6)
    
    axes[2].plot(sol.t, Phi_sys, label='$\Phi_{sys}$ (System Order)', color='black', linewidth=2)
    axes[2].fill_between(sol.t, 0.3, 0.7, color='green', alpha=0.1, label='Safe Zone')
    axes[2].axhline(0.3, color='red', linestyle='--', alpha=0.5)
    axes[2].set_title('Total System Order')
    axes[2].legend()
    axes[2].grid(True, linestyle=':', alpha=0.6)
    axes[2].set_xlabel('Time')
    
    plt.tight_layout()
    plt.savefig('results/sed_v2_simulation.png', dpi=300)
    print("Simulation complete. Figure saved to results/sed_v2_simulation.png")
    plt.show()


if __name__ == "__main__":
    run_simulation()