import os
from PIL import Image
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Tradex Haven", page_icon="Tradex.png", layout="wide")

# Define the image path
image_path = "pic.webp"  # Adjust the path as needed (use "assets/pic.webp" if in a subfolder)

# Check if the image exists and is a valid file
if os.path.exists(image_path):
    try:
        image = Image.open(image_path)  # Open the image
        st.image(image, caption="Empower Your Trading Journey 📊", use_container_width=True)
    except Exception as e:
        st.error(f"Error opening image: {e}")
else:
    st.error(f"Image file '{image_path}' not found. Please ensure it exists in the specified path.")


# Create the app's About/Guide section
st.title("Welcome to Tradex Haven 🌍")

st.image(image, caption="Empower Your Trading Journey 📊", use_container_width=True)

st.markdown("""
**Tradex Haven** is a cutting-edge trading application designed to empower you to make informed investment decisions. 
Our platform leverages advanced financial models and real-time data analysis to guide you in navigating the dynamic stock market.

With Tradex Haven, you can:
- ✨ Analyze historical stock performance
- 📊 Predict future trends
- ⚡ Evaluate investment risks
- 💼 Optimize your portfolio using CAPM (Capital Asset Pricing Model)

Explore the following features:
- **CAPM Beta** 🔁: Calculate the beta value of a stock using real-time data from the Yahoo Finance API to measure its volatility compared to the overall market.
- **CAPM Return** 🏦: Determine the expected return of an asset based on its beta and the market's risk-free rate, using live market data.
- **Stock Analysis** 🔍: Dive deep into detailed historical and technical analysis of individual stocks.
- **Stock Prediction** 🔢: Use predictive models to forecast future stock prices based on historical data.

---

### How Tradex Haven Helps You Make the Right Decisions 🔄
- **Risk Management** 🛑: Assess the volatility of your investments using CAPM Beta, calculated with real-time market data, to balance risk and return.
- **Forecasting Accuracy** 📊: Leverage our Stock Prediction tool to identify potential growth opportunities.
- **Comprehensive Insights** 🕵‍♂️: Our Stock Analysis feature offers deep insights into market trends and stock performance.
- **Personalized Strategies** 🔐: Combine CAPM calculations and predictive tools to create a strategy that aligns with your financial goals.

### How It Operates 🔬
Our application is built on robust financial algorithms and real-time data fetched using the Yahoo Finance API. Here's how each section works:

1. **CAPM Beta** 🔁:
   - Fetches historical stock and market benchmark data via Yahoo Finance API.
   - Calculates the beta value, giving you an idea of the stock's risk level relative to the market.

2. **CAPM Return** 🏦:
   - Uses real-time beta values, the risk-free rate, and the market's expected return to compute the stock's expected return.
   - This helps you assess if an investment aligns with your risk appetite.

3. **Stock Analysis** 🔍:
   - Select a stock to analyze.
   - The app retrieves data on price trends, volume, moving averages, and other technical indicators to give you a comprehensive overview.

Start exploring Tradex Haven today to transform your trading journey! 🌟
""")
