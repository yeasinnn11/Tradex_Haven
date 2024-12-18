
# Tradex Haven 🏦

Tradex Haven is a powerful stock market analysis and investment tool built with Python and Streamlit. The app leverages financial models such as the **Capital Asset Pricing Model (CAPM)** and stock analysis to empower users to make informed trading decisions.

---

## Features 🚀

1. **CAPM Beta** 🔁
   - Calculates the **Beta** value of a stock using historical data from Yahoo Finance.
   - Analyzes the stock's volatility relative to the market.

2. **CAPM Return** 📈
   - Computes the **Expected Return** of a stock based on its Beta value, risk-free rate, and market return.
   - Visualizes data using Plotly for enhanced interactivity.

3. **Stock Analysis** 🔍
   - Provides detailed insights into historical performance, technical indicators, and stock fundamentals.
   

4. **Interactive Dashboard** 🎛️
   - Real-time data fetched using the **Yahoo Finance API**.
   - Clean and intuitive Streamlit-based interface.

---

## Project Structure 📂

- `CAPM_Beta.py`: Calculates the Beta value of individual stocks compared to the S&P 500.
- `CAPM_Return.py`: Estimates expected returns using the CAPM model for selected stocks.
- `Stock_Analysis.py`: Offers comprehensive analysis of historical stock performance, including trends and technical details.
- `Tradex_Haven.py`: Serves as the homepage and introductory guide for the application.

---

## Libraries & Dependencies 📦

The following libraries are required to run the Tradex Haven application:

```plaintext
streamlit
yfinance
pandas
numpy
matplotlib
scikit-learn
plotly
Pillow
```

---

## Installation ⚙️

Follow these steps to set up and run the application:

1. **Clone the repository**:
   ```bash
   git clone <repository-link>
   cd tradex-haven
   ```

2. **Install dependencies**:
   Install the required Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit app:
   ```bash
   streamlit run Tradex_Haven.py
   ```

4. **Explore the features**:
   Open the provided Streamlit URL in your browser and enjoy the features of Tradex Haven.

## Future Updates 🌟

- Stock price predictions using advanced Machine Learning models.
- Portfolio optimization tools.
- Integration of additional financial APIs.

---

## Contributing 🤝

We welcome contributions! Feel free to fork the repository and submit a pull request.

---

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and share.

---

**Start your investment journey with Tradex Haven! 📊**  
Happy Trading 🚀
