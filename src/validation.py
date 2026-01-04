# src/validation.py

from .monte_carlo import monte_carlo_call

def convergence_test(S0, K, T, r, sigma, bs_price, sim_counts):
    results = []

    for n in sim_counts:
        mc_price, se = monte_carlo_call(S0, K, T, r, sigma, n)
        results.append({
            "simulations": n,
            "mc_price": mc_price,
            "std_error": se,
            "abs_error": abs(mc_price - bs_price)
        })

    return results
