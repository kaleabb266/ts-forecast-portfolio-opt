# Investment Portfolio Optimization

This project aims to optimize a sample investment portfolio based on forecasted data for Tesla Stock (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY). The optimization process includes calculations for annual return, portfolio weights, Sharpe Ratio, and visualizations of portfolio performance.

## Project Structure

```
investment-portfolio-optimization/
├── data/
│   ├── tesla_data.csv       # Historical daily closing prices for Tesla stock (TSLA)
│   ├── bond_data.csv        # Historical daily closing prices for Vanguard Total Bond Market ETF (BND)
│   └── spy_data.csv         # Historical daily closing prices for S&P 500 ETF (SPY)
├── src/
│   ├── data_preprocessing.py # Functions for loading and preprocessing data
│   ├── portfolio_optimization.py # Functions for portfolio optimization and risk analysis
│   ├── visualization.py      # Functions for visualizing portfolio performance
│   └── main.py              # Entry point for the project
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd investment-portfolio-optimization
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to execute the portfolio optimization process:
   ```
   python src/main.py
   ```

2. The script will load the data, preprocess it, optimize the portfolio, and generate visualizations of the portfolio performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.