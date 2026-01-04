import numpy as np

def monte_carlo_call(S0, K, T, r, sigma, n_sim, seed=42):
    rng = np.random.default_rng(seed)
    Z = rng.normal(0, 1, n_sim)

    ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)

    price = np.exp(-r*T) * payoff.mean()
    std_error = np.exp(-r*T) * payoff.std(ddof=1) / np.sqrt(n_sim)

    return price, std_error
