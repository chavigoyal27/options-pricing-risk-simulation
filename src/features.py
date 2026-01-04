import numpy as np

def compute_log_returns(df):
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df

def estimate_volatility(df):
    log_returns = df["log_return"].dropna()
    sigma = log_returns.std() * np.sqrt(252)
    return sigma
