import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import MACD
from util.get_start_date_of_symbol import get_start_date_of_symbol


def get_indicator_data(symbol, interval, period):
    # Fetch historical data for TSLA from its inception (2010-06-29)
    # Intraday time intervals (minutes) are only avaialble when period is less than or equal to a month,
    # use day for more than a month

    if period == "max":
        start_date = get_start_date_of_symbol(symbol)
        print("Start date here", start_date)
        data = yf.download(symbol, interval=interval, start=start_date)  # You can adjust the start date
    else:
        data = yf.download(symbol, interval=interval, period=period)

    # If no data is returned, symbol is invalid
    if data.empty:
        return None
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
    return data[['Close', 'RSI', 'MACD', 'MACD_signal', 'MACD_histogram']]
    # data[['Close', 'RSI', 'MACD', 'MACD_signal', 'MACD_histogram']].to_excel("TSLA_RSI_MACD_ALL_TIME_4.xlsx",
                                                                             # sheet_name="RSI_MACD Data")
    # print("Data has been saved to 'TSLA_RSI_MACD_ALL_TIME_4.xlsx'")
