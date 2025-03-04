import pandas as pd

def load_data():
    tesla_data = pd.read_csv('../data/tesla_data.csv', parse_dates=['Date'], index_col='Date')
    bond_data = pd.read_csv('../data/bond_data.csv', parse_dates=['Date'], index_col='Date')
    spy_data = pd.read_csv('../data/spy_data.csv', parse_dates=['Date'], index_col='Date')
    
    # Combine the data into a single DataFrame
    combined_data = pd.DataFrame({
        'TSLA': tesla_data['Close'],
        'BND': bond_data['Close'],
        'SPY': spy_data['Close']
    })
    
    return combined_data

def compute_daily_returns(data):
    daily_returns = data.pct_change().dropna()
    return daily_returns