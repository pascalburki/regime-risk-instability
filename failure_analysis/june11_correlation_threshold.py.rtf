import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

dfSPY = yf.download('SPY', '2018-01-01', '2023-12-31')
dfQQQ = yf.download('QQQ', '2018-01-01', '2023-12-31')
dfGLD = yf.download('GLD', '2018-01-01', '2023-12-31')
dfTLT = yf.download('TLT', '2018-01-01', '2023-12-31')
dfXOM = yf.download('XOM', '2018-01-01', '2023-12-31')

combined = pd.concat([dfSPY["Close"], dfQQQ["Close"], dfGLD["Close"], dfTLT["Close"], dfXOM["Close"]], axis=1)
combined.columns = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']

combined_raw = combined.dropna()
log_returns = np.log(combined_raw / combined_raw.shift(1)).dropna()

assets = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']


real_vols = log_returns.std().values

def build_cov_matrix(vols, corr):
    n = len(vols)
    cov = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i == j:
                cov[i, j] = vols[i] ** 2
            else:
                cov[i, j] = corr * vols[i] * vols[j]
    
    return cov


def portfolio_vol_from_cov(cov_matrix, weights):
    weights = np.array(weights)
    port_var = weights @ cov_matrix @ weights
    return np.sqrt(port_var) * np.sqrt(252)


equal_weights = [1/5] * 5
weighted_avg = np.mean(real_vols) * np.sqrt(252)

correlations = np.linspace(0, 1, 100)
port_benefits = []

for c in correlations:
    cov = build_cov_matrix(real_vols, c)
    port_vol = portfolio_vol_from_cov(cov, equal_weights)
    benefit = (weighted_avg - port_vol) / weighted_avg * 100
    port_benefits.append(benefit)

for i, b in enumerate(port_benefits):
    if b < 20:
        print(f"Benefit drops below 20% at correlation: {round(correlations[i], 3)}")
        break


plt.figure(figsize=(12,6))
plt.plot(correlations, port_benefits)
plt.axhline(y=20, linestyle='--', label='20% threshold')
plt.axhline(y=0)
plt.xlabel('Uniform Correlation')
plt.ylabel('Diversification Benefit (%)')
plt.legend()
plt.show()
