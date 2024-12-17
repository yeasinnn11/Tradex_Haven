# Importing Libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import capm_functions as capm_functions

st.set_page_config(page_title = 'Tradex Haven',
                   page_icon= "Tradex.png",
                   layout= 'wide')

st.title("Capital Asset Pricing Model")

# getting input from user

col1, col2 = st.columns([1,1])
with col1:
    stocks_list = st.multiselect("Chose 4 Stock", 
                             ("AAPL",  # Apple
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
                              ),
                            ["AAPL", "MSFT","GOOGL","AMZN"])

with col2:
    year = st.number_input("Number Of years", 1,10)

# downloading data for SP500

end = datetime.date.today()
start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)
SP500 = web.DataReader(['sp500'], 'fred', start,end)


stocks_df = pd.DataFrame()

for stock in stocks_list:
    data = yf.download(stock, start=start, end=end)
    stocks_df[f'{stock}'] = data['Close']

stocks_df.reset_index(inplace=True)
stocks_df.rename(columns={'index': 'Date'}, inplace=True)
SP500.reset_index(inplace = True)
SP500.columns = ['Date', 'sp500']
stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
stocks_df['Date'] = stocks_df['Date'].apply(lambda x:str(x)[:10])
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
stocks_df = pd.merge(stocks_df, SP500, on = 'Date', how = 'inner')

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("### Dataframe Head")
    st.dataframe(stocks_df.head(), use_container_width= True)
with col2:
    st.markdown("### Dataframe tail")
    st.dataframe(stocks_df.tail(), use_container_width= True)


col1, col2 = st.columns([1,1])
with col1:
    st.markdown("### Price of all the Stocks")
    st.plotly_chart(capm_functions.incteractive_plot(stocks_df))

with col2:
    st.markdown("### Price of all the Stocks (After Normalizing)")   
    # Normalize the stock prices and pass the normalized DataFrame to the plot
    normalized_df = capm_functions.normalize(stocks_df)
    st.plotly_chart(capm_functions.incteractive_plot(normalized_df))



stocks_daily_return = capm_functions.daily_return(stocks_df)
beta = {}
alpha = {}

# Print column names for debugging purposes
print("Columns in stocks_daily_return:", stocks_daily_return.columns)

# Loop through each column (excluding 'Date' and 'SP500') to calculate beta and alpha
for i in stocks_daily_return.columns:
    if i != 'Date' and 'sp500' not in i.lower():  # Ensure we are not calculating for 'Date' or 'sp500'
        b, a = capm_functions.calculate_beta(stocks_daily_return, i)
        
        beta[i] = b  # Store the beta value
        alpha[i] = a  # Store the alpha value

# Debug: Print beta and alpha values
print("Beta Values:", beta)
print("Alpha Values:", alpha)

# Create a DataFrame for displaying only the stocks (not SP500)
beta_df = pd.DataFrame(columns=['Stock', 'Beta Value'])

# Populate the 'Stock' and 'Beta Value' columns with the stocks (excluding SP500)
beta_df['Stock'] = list(beta.keys())
beta_df['Beta Value'] = [str(round(i, 2)) for i in beta.values()]

# Display the DataFrame with Beta values in Streamlit
with col1:
    st.markdown('### Calculated Beta Value')
    st.dataframe(beta_df, use_container_width=True)


rf = 0
rm = stocks_daily_return['sp500'].mean()*252

return_df = pd.DataFrame()
return_value = []
for stock in stocks_list:
    if stock in beta:
        value = beta[stock]
        return_value.append(str(round(rf + (value * (rm - rf)), 2)))
    else:
        return_value.append('N/A')  # In case a stock doesn't have a beta value

# Now the lengths should match
return_df['Stock'] = stocks_list
return_df['Return Value'] = return_value

with col2:
    st.markdown('### Calculated Return using CAPM')
    st.dataframe(return_df, use_container_width=True)

