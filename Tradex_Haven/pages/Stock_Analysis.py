import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
from pages.utils.plotly_figure import plotly_table, plotly_table_for_days

# Setting page config
st.set_page_config(
    page_title="Tradex Haven",
    page_icon="Tradex.png",
    layout="wide",
)

st.title("Stock Analysis")


col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.selectbox("Stock Ticker", 
                              options= ["AAPL",  # Apple
                              "MSFT",  # Microsoft
                              "GOOGL", # Alphabet (Google, Class A)
                              "AMZN",  # Amazon
                              "NVDA",  # Nvidia
                             "META",  # Meta Platforms
                              "TSLA",  # Tesla
                              "BRK.B", # Berkshire Hathaway (Class B)
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
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year -1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose End Date", datetime.date(today.year, today.month, today.day))

st.subheader(ticker)

stock = yf.Ticker(ticker)


st.write(stock.info['longBusinessSummary'])
st.write("**Sector** :", stock.info['sector'])
st.write("**Full Time Employees** :", stock.info['fullTimeEmployees'])
st.write("**Website** :", stock.info['website'])


col1 , col2 = st.columns(2)

with col1:
    # Create DataFrame
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [
        stock.info['marketCap'],
        stock.info['beta'],
        stock.info['trailingEps'],
        stock.info['trailingPE']
    ]
    
    # Generate Plotly table
    fig_df = plotly_table(df)

    # Display in Streamlit
    st.plotly_chart(fig_df, use_container_width=True)
with col2:
    df = pd.DataFrame(index= ['Qucik Ratio', 'Revenue per share', 'Profit Margins',
                      'Debt to Equity', 'Return on Equity'])
    df[''] = [stock.info["quickRatio"], stock.info["revenuePerShare"],stock.info["profitMargins"],
              stock.info["debtToEquity"],stock.info["returnOnEquity"]]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

data = yf.download(ticker, start= start_date, end = end_date)

col1, col2, col3 = st.columns(3)

# Extract last two Close values as scalars
last_close = data['Close'].iloc[-1].item()  # Ensures scalar
prev_close = data['Close'].iloc[-2].item()

daily_change = last_close - prev_close

# Pass the values as scalars to Streamlit metric
col1.metric("Daily Change", round(last_close, 2), round(daily_change, 2))


last_10_df = data.tail(10).sort_index(ascending = False).round(3)
fig_df = plotly_table_for_days(last_10_df)

# Display in Streamlit
st.write('##### Historical Data (last 10 days)')
st.plotly_chart(fig_df, use_container_width=True)
