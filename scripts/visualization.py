import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cumulative_returns(portfolio_returns):
    cumulative_returns = (1 + portfolio_returns).cumprod() - 1
    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_returns, label='Cumulative Returns')
    plt.title('Cumulative Returns of the Portfolio')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid()
    plt.show()

def plot_risk_return(annualized_returns, annualized_volatility):
    plt.figure(figsize=(12, 6))
    plt.scatter(annualized_volatility, annualized_returns, marker='o', color='b')
    plt.title('Risk vs Return')
    plt.xlabel('Annualized Volatility')
    plt.ylabel('Annualized Return')
    plt.grid()
    plt.show()

def plot_portfolio_weights(weights, assets):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=assets, y=weights)
    plt.title('Portfolio Weights')
    plt.xlabel('Assets')
    plt.ylabel('Weights')
    plt.ylim(0, 1)
    plt.grid()
    plt.show()