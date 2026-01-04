# src/greeks.py

import numpy as np
from scipy.stats import norm
from .black_scholes import d1_d2

def call_greeks(S, K, T, r, sigma):
    d1, d2 = d1_d2(S, K, T, r, sigma)
    pdf = norm.pdf(d1)

    delta = norm.cdf(d1)
    gamma = pdf / (S * sigma * np.sqrt(T))
    vega  = S * pdf * np.sqrt(T)
    theta = (-S * pdf * sigma / (2*np.sqrt(T))
             - r * K * np.exp(-r*T) * norm.cdf(d2))
    rho   = K * T * np.exp(-r*T) * norm.cdf(d2)

    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho
    }
