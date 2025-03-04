import pandas as pd
from data_preprocessing import load_and_preprocess_data
from portfolio_optimization import optimize_portfolio
from visualization import plot_portfolio_performance

def main():
    # Load and preprocess data
    data = load_and_preprocess_data()

    # Optimize portfolio
    optimal_weights, portfolio_return, portfolio_risk, sharpe_ratio = optimize_portfolio(data)

    # Print results
    print("Optimal Portfolio Weights:")
    print(optimal_weights)
    print(f"Expected Annual Return: {portfolio_return:.2f}")
    print(f"Portfolio Risk (Standard Deviation): {portfolio_risk:.2f}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

    # Visualize portfolio performance
    plot_portfolio_performance(data, optimal_weights)

if __name__ == "__main__":
    main()