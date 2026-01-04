# Options Pricing & Risk Simulation  
**Black–Scholes and Monte Carlo Validation**

## 📌 Overview
This project implements a complete options pricing and risk simulation pipeline using Python.  
European call options are priced using the Black–Scholes analytical model and validated through Monte Carlo simulations. The project also computes option Greeks and demonstrates numerical convergence behavior.

The focus of this project is to understand **option pricing mechanics, uncertainty modeling, and risk sensitivities**, rather than predicting stock prices.

---

## 🧠 Key Concepts Covered
- Log returns and volatility estimation from historical market data  
- Black–Scholes option pricing model  
- Monte Carlo simulation under Geometric Brownian Motion (GBM)  
- Option Greeks: Delta, Gamma, Vega, Theta, and Rho  
- Validation of Monte Carlo pricing through convergence analysis  

---

## 🛠 Tech Stack
- Python  
- NumPy  
- Pandas  
- SciPy  
- yFinance  

---

## 📂 Project Structure
# Options Pricing & Risk Simulation  
**Black–Scholes and Monte Carlo Validation**

## 📌 Overview
This project implements a complete options pricing and risk simulation pipeline using Python.  
European call options are priced using the Black–Scholes analytical model and validated through Monte Carlo simulations. The project also computes option Greeks and demonstrates numerical convergence behavior.

The focus of this project is to understand **option pricing mechanics, uncertainty modeling, and risk sensitivities**, rather than predicting stock prices.

---

## 🧠 Key Concepts Covered
- Log returns and volatility estimation from historical market data  
- Black–Scholes option pricing model  
- Monte Carlo simulation under Geometric Brownian Motion (GBM)  
- Option Greeks: Delta, Gamma, Vega, Theta, and Rho  
- Validation of Monte Carlo pricing through convergence analysis  

---

## 🛠 Tech Stack
- Python  
- NumPy  
- Pandas  
- SciPy  
- yFinance  

---

## 📂 Project Structure
```
options-pricing-risk-simulation/
│
├── main.py
├── requirements.txt
├── README.md
│
├── src/
│ ├── data.py
│ ├── features.py
│ ├── black_scholes.py
│ ├── greeks.py
│ ├── monte_carlo.py
│ └── validation.py
```

---

## 📈 Methodology

### 1. Market Data & Volatility Estimation
- Historical stock price data is downloaded using `yfinance`
- Log returns are computed from daily closing prices
- Volatility is annualized using √252 scaling

### 2. Black–Scholes Pricing
European call options are priced using the Black–Scholes closed-form formula.  
Time to maturity and the risk-free rate are assumed parameters required by the model.

### 3. Monte Carlo Simulation
- Terminal stock prices are simulated using Geometric Brownian Motion
- Option payoffs are computed at maturity
- Expected payoffs are discounted back to present value

### 4. Greeks Calculation
Option Greeks are computed analytically from the Black–Scholes model to measure sensitivity to underlying parameters.

### 5. Validation & Convergence
Monte Carlo prices are compared against Black–Scholes prices for increasing simulation counts to demonstrate convergence and numerical stability.

---

## ✅ Results
- Monte Carlo prices converge to Black–Scholes prices as the number of simulations increases  
- Estimation error decreases proportional to 1/√N  
- Greeks are numerically stable and economically interpretable  

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the project
```bash
python main.py
