# Portfolio Optimization Using Time Series Forecasting

## 📌 Project Overview

This project focuses on **time series forecasting and portfolio optimization** using historical stock data from **Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY)**. The goal is to predict future stock prices using **ARIMA, SARIMA, and LSTM models** and optimize the asset allocation to maximize returns while minimizing risk.

## 📂 Project Structure

```
├── data/                   # Contains raw and processed stock data
├── notebooks/              # Jupyter notebooks for EDA, forecasting, and optimization
├── scripts/                # Python scripts for data preprocessing and modeling
├── results/                # Forecasting results, visualizations, and model evaluations
├── README.md               # Project documentation
├── requirements.txt        # Dependencies

```

## 📊 Data Collection & Preprocessing

- **Data Source:** Yahoo Finance
- **Timeframe:** January 1, 2015 - January 31, 2025
- **Preprocessing Steps:**
  - Handling missing values
  - Normalizing data using MinMaxScaler
  - Splitting into training (80%) and testing (20%)

## 🔮 Time Series Forecasting

Three forecasting models were used:

1. **ARIMA (AutoRegressive Integrated Moving Average)** - Best suited for univariate time series data
2. **SARIMA (Seasonal ARIMA)** - Captures seasonality in stock price movements
3. **LSTM (Long Short-Term Memory Neural Network)** - Deep learning approach for sequential data

## 📈 Portfolio Optimization

- Computed **annual returns and covariance matrix**
- Optimized asset allocation using the **Sharpe Ratio**
- Evaluated risk metrics including **Value at Risk (VaR)**

## 📌 Key Results

- **Optimized Portfolio Weights:**
  - TSLA: 33%
  - BND: 33%
  - SPY: 34%
- **Expected Annual Return:** 12%
- **Annual Volatility:** 15%
- **Sharpe Ratio:** 0.73

## 🛠️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kaleabb266/ts-forecast-portfolio-opt.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. 📌 Future Improvements

- Implement additional forecasting techniques (e.g., Prophet, GARCH)
- Enhance portfolio optimization with Monte Carlo simulations
- Incorporate real-time market data for live predictions

## ✍️ Author

**Kaleab Bekele**\
March 1, 2025

