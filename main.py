# main.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

#from src.config import *
from src.data import load_price_data
from src.features import compute_log_returns, estimate_volatility
from src.black_scholes import call_price
from src.greeks import call_greeks
from src.validation import convergence_test

TICKER = "AAPL"
START_DATE = "2023-01-01"
END_DATE = "2024-01-01"

RISK_FREE_RATE = 0.05      # 5%
TIME_TO_MATURITY = 0.5     # 6 months (in years)

MC_SIMULATIONS = [1_000, 5_000, 10_000, 50_000, 100_000]

# 1. Load data
df = load_price_data(TICKER, START_DATE, END_DATE)

# 2. Features
df = compute_log_returns(df)
sigma = estimate_volatility(df)
S0 = df["Close"].iloc[-1]
K = S0

print(f"S0 = {S0:.2f}")
print(f"Sigma = {sigma:.4f}")

# 3. Black–Scholes
bs_call = call_price(S0, K, TIME_TO_MATURITY, RISK_FREE_RATE, sigma)
print(f"Black–Scholes Call Price = {bs_call:.4f}")

# 4. Greeks
greeks = call_greeks(S0, K, TIME_TO_MATURITY, RISK_FREE_RATE, sigma)
print("Greeks:", greeks)

# 5. Monte Carlo convergence
results = convergence_test(
    S0, K, TIME_TO_MATURITY, RISK_FREE_RATE, sigma,
    bs_call, MC_SIMULATIONS
)

print("\nMonte Carlo Convergence:")
for r in results:
    print(r)
