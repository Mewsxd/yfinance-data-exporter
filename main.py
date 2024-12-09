# File path: stock_indicators_fetcher.py

import yfinance as yf
import pandas_ta as ta
import pandas as pd


def fetch_and_save_stock_indicators(stock_symbol: str, start_date: str, end_date: str, filename: str):
    """
    Fetches historical stock data for a given stock symbol and calculates RSI and MACD indicators.
    Saves the result to a local file.

    Args:
        stock_symbol (str): Stock symbol (e.g., "AAPL").
        start_date (str): Start date for historical data (format: "YYYY-MM-DD").
        end_date (str): End date for historical data (format: "YYYY-MM-DD").
        filename (str): Path to save the resulting file (e.g., "output.csv").
    """
    try:
        # Fetch historical data using yfinance
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

        if stock_data.empty:
            print("No data fetched for the given stock symbol and date range.")
            return

        # Calculate RSI and MACD using pandas_ta
        stock_data["RSI"] = ta.rsi(stock_data["Close"])
        macd = ta.macd(stock_data["Close"])

        # Combine MACD columns into the dataframe
        stock_data = pd.concat([stock_data, macd], axis=1)

        # Save to a CSV file
        stock_data.to_csv(filename)
        print(f"Indicator data saved to {filename}.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Apple Inc.
    start_date = "2023-01-01"
    end_date = "2023-12-01"
    filename = "AAPL_indicators.csv"
#
    fetch_and_save_stock_indicators(stock_symbol, start_date, end_date, filename)
# File path: stock_indicators_fetcher.py

# import yfinance as yf
# import pandas_ta as ta
# import pandas as pd
#
# def fetch_and_save_stock_indicators(stock_symbol: str, start_date: str, end_date: str, filename: str):
#     """
#     Fetches historical stock data for a given stock symbol and calculates RSI and MACD indicators.
#     Saves the result to a local file.
#
#     Args:
#         stock_symbol (str): Stock symbol (e.g., "AAPL").
#         start_date (str): Start date for historical data (format: "YYYY-MM-DD").
#         end_date (str): End date for historical data (format: "YYYY-MM-DD").
#         filename (str): Path to save the resulting file (e.g., "output.csv").
#     """
#     try:
#         # Fetch historical data using yfinance
#         stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
#
#         if stock_data.empty:
#             raise ValueError(f"No data fetched for the stock symbol '{stock_symbol}' within the date range.")
#
#         # Debug: Print available columns
#         print(f"Fetched data columns: {stock_data.columns}")
#
#         # Ensure the 'Close' column exists and is not empty
#         if "Close" not in stock_data.columns or stock_data["Close"].isnull().all():
#             raise ValueError("The 'Close' column is missing or contains no valid data.")
#
#         # Drop rows with NaN values in 'Close' column
#         stock_data.dropna(subset=["Close"], inplace=True)
#
#         # Calculate RSI (14 periods)
#         stock_data["RSI"] = ta.rsi(stock_data["Close"], length=14)
#
#         # Calculate MACD (default periods: 12, 26, 9)
#         macd = ta.macd(stock_data["Close"], fast=12, slow=26, signal=9)
#         stock_data = pd.concat([stock_data, macd], axis=1)
#
#         # Print a preview of the data to check if the indicators are calculated
#         print(stock_data.tail())
#
#         # Save to a CSV file
#         stock_data.to_csv(filename)
#         print(f"Indicator data saved to {filename}.")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# # Example usage
# if __name__ == "__main__":
#     stock_symbol = "AAPL"  # Example: Apple Inc.
#     start_date = "2023-01-01"
#     end_date = "2023-12-01"
#     filename = "AAPL_indicators.csv"
#
#     fetch_and_save_stock_indicators(stock_symbol, start_date, end_date, filename)
