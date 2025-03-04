import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def calculate_annual_return(prices):
    daily_returns = prices.pct_change().dropna()
    annual_return = daily_returns.mean() * 252  # Assuming 252 trading days
    return annual_return

def calculate_covariance_matrix(prices):
    daily_returns = prices.pct_change().dropna()
    covariance_matrix = daily_returns.cov() * 252  # Annualize the covariance matrix
    return covariance_matrix

def portfolio_performance(weights, annual_returns, covariance_matrix):
    portfolio_return = np.dot(weights, annual_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
    return portfolio_return, portfolio_volatility

def negative_sharpe_ratio(weights, annual_returns, covariance_matrix, risk_free_rate=0.01):
    portfolio_return, portfolio_volatility = portfolio_performance(weights, annual_returns, covariance_matrix)
    return -(portfolio_return - risk_free_rate) / portfolio_volatility

def optimize_portfolio(annual_returns, covariance_matrix):
    num_assets = len(annual_returns)
    args = (annual_returns, covariance_matrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
    bounds = tuple((0, 1) for asset in range(num_assets))  # Weights between 0 and 1
    result = minimize(negative_sharpe_ratio, num_assets * [1. / num_assets], args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result

def calculate_value_at_risk(returns, confidence_level=0.95):
    return np.percentile(returns, 100 * (1 - confidence_level))