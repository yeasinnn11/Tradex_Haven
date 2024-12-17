import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# --- Page Config ---
st.set_page_config(page_title="Tradex Haven", 
                   page_icon= "Tradex.png",
                   layout="wide")

# --- Helper Functions ---
def calculate_stock_beta(stock_symbol, market_symbol, years):
    """
    Calculate Beta and Expected Return using CAPM.
    """
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years * 365)
    
    # Fetch stock and market data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date, interval="1wk")['Adj Close']
    market_data = yf.download(market_symbol, start=start_date, end=end_date, interval="1wk")['Adj Close']

    # Calculate returns
    stock_returns = stock_data.pct_change().dropna()
    market_returns = market_data.pct_change().dropna()

    # Align data
    aligned_data = pd.concat([stock_returns, market_returns], axis=1).dropna()
    aligned_data.columns = ['Stock', 'Market']

    # Linear Regression
    X = aligned_data['Market'].values.reshape(-1, 1)
    y = aligned_data['Stock'].values.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    beta = model.coef_[0][0]

    return beta, aligned_data

# --- UI Code ---
st.title("Calculate Beta Return for Individual Stock")

col1, col2 = st.columns([1,1])
# --- Inputs ---
with col1:
    stock_symbol = st.selectbox("Chose a Stock", 
                              options= ["AAPL",  # Apple
                              "MSFT",  # Microsoft
                              "GOOGL", # Alphabet (Google, Class A)
                              "AMZN",  # Amazon
                              "NVDA",  # Nvidia
                             "META",  # Meta Platforms
                              "TSLA",  # Tesla
                              "BRK.B", # Berkshire Hathaway (Class B)
                              "JPM",   # JPMorgan Chase
                              "V",     # Visa
                              "MA",    # Mastercard
                              "XOM",   # Exxon Mobil
                              "UNH",   # UnitedHealth Group
                              "PG",    # Procter & Gamble
                              "KO",    # Coca-Cola
                              "PEP",   # PepsiCo
                              "WMT",   # Walmart
                              "HD",    # Home Depot
                              "CVX",   # Chevron
                              "DIS"    # Walt Disney
                              ],
                            index=0) 
market_symbol = "^GSPC"  # Default: S&P 500 as Market
with col2:
    years = st.number_input("Number of Years", min_value=1, max_value=10, value=1, step=1)

# --- Calculate Beta ---
try:
    beta, aligned_data = calculate_stock_beta(stock_symbol, market_symbol, years)

    # Display Beta
    st.markdown(f"### Beta : {beta:.4f}")
        
    # Expected Return (CAPM formula with assumed risk-free rate and market return)
    risk_free_rate = 0.03  # Assumed 3%
    market_return = 0.1  # Assumed 10%
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
        
    st.markdown(f"### Return : {expected_return*100:.2f}")
        
        # --- Plot ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(aligned_data['Market'], aligned_data['Stock'], color="blue", alpha=0.6, label="Data Points")
    ax.plot(aligned_data['Market'], beta * aligned_data['Market'], color="darkred", label="Expected Return")
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    ax.set_title(f"{stock_symbol} vs Market Returns")
    ax.set_xlabel("Market Returns")
    ax.set_ylabel(f"{stock_symbol} Returns")
    ax.legend()

    st.pyplot(fig)

except Exception as e:
    st.error(f"Error: {e}")
