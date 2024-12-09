# from tradingview_ta import *
#
# tesla = TA_Handler(
#     symbol="TSLA",
#     screener="america",
#     exchange="NASDAQ",
#     interval=Interval.INTERVAL_1_DAY
# )
# print(tesla.get_analysis().summary)
# # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
#
# handler = TA_Handler(
#     symbol="",
#     exchange="",
#     screener="",
#     interval="",
#     timeout=None
# )
# analysis = tesla.get_analysis()
# print(analysis.indicators["RSI"])
# import yfinance as yf
# import pandas as pd
# from ta.momentum import RSIIndicator
#
# # Fetch historical data for TSLA for the past 2 years
# # data = yf.download("TSLA", interval="1wk", period="2y")
# data = yf.download("TSLA", interval="1wk", start="2010-06-29")  # You can adjust the start date
#
# # Calculate the RSI with a 14-period (standard)
# rsi_indicator = RSIIndicator(close=data['Close'].squeeze(), window=14)
# data['RSI'] = rsi_indicator.rsi()
# data['RSI'] = data['RSI'].fillna(0)
#
# # Save the result to an Excel file
# data[['Close', 'RSI']].to_excel("TSLA_RSI_ALL_TIME.xlsx", sheet_name="RSI Data")
#
# print("Data has been saved to 'TSLA_RSI_ALL_TIME.xlsx'")

import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD

# Fetch historical data for TSLA from its inception (2010-06-29)
# Intraday time intervals (minutes) are only avaialbel when period is less than or equal to a month, use day for more than a month
data = yf.download("TSLA", interval="1d", start="2010-06-29")  # You can adjust the start date
# data = yf.download("TSLA", interval="30m", period="1d")

# Ensure 'Close' is a 1D Series
close_data = data['Close'].squeeze()

# Calculate the RSI with a 14-period (standard)
rsi_indicator = RSIIndicator(close=close_data, window=14)
data['RSI'] = rsi_indicator.rsi()

# Fill NaN values in RSI with 0 (you can use other methods like forward fill or drop NaNs)
data['RSI'] = data['RSI'].fillna(0)

# Calculate MACD (12-period, 26-period, 9-period standard)
macd = MACD(close=close_data, window_slow=26, window_fast=12, window_sign=9)

# Add MACD, Signal Line, and Histogram to the DataFrame
data['MACD'] = macd.macd()  # This returns a pandas Series now
data['MACD_signal'] = macd.macd_signal()
data['MACD_histogram'] = macd.macd_diff()

# Fill NaN values in MACD (similar to RSI)
data['MACD'] = data['MACD'].fillna(0)
data['MACD_signal'] = data['MACD_signal'].fillna(0)
data['MACD_histogram'] = data['MACD_histogram'].fillna(0)

# Save the result to an Excel file
# data[['Close', 'RSI', 'MACD', 'MACD_signal', 'MACD_histogram']].to_excel("TSLA_RSI_MACD_ALL_TIME_4.xlsx", sheet_name="RSI_MACD Data")

# print("Data has been saved to 'TSLA_RSI_MACD_ALL_TIME_4.xlsx'")

import yfinance as yf

# Define the stock ticker (e.g., TSLA for Tesla)
ticker = "BTC-USD"

# Download historical data (you can adjust the start and end dates)
data = yf.download(ticker, start="2000-01-01")

# Print the first available date in the dataset
print(data.index[0].date())

import yfinance as yf

# Example: Search for Apple
symbol = "XRP"  # Replace with any ticker you know
ticker = yf.Ticker(symbol)

# Print information about the ticker
print(ticker.info)
