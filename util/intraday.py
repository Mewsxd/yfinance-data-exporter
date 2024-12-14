# import ccxt
# import pandas as pd
# import pandas_ta as ta
# from datetime import datetime, timedelta
#
#
# def fetch_crypto_data(exchange_name, symbol, timeframe, limit):
#     """Fetch cryptocurrency data using ccxt."""
#     exchange = getattr(ccxt, exchange_name)()
#     ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
#     df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
#     df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
#     return df
#
#
# def calculate_technical_indicators(df):
#     """Calculate MACD, RSI, and add to the DataFrame."""
#     # Add MACD
#     macd = df.ta.macd(close="close")
#     df = pd.concat([df, macd], axis=1)
#
#     # Add RSI
#     rsi = df.ta.rsi(close="close")  # Calculate RSI
#     if isinstance(rsi, pd.DataFrame):  # Check if RSI is a DataFrame
#         rsi = rsi.iloc[:, 0]  # Extract the first column (default RSI)
#     df["RSI"] = rsi  # Assign the single-column RSI
#
#     return df
#
#
# def save_to_excel(df, filename):
#     """Save the DataFrame to an Excel file."""
#     df.to_excel(filename, index=False)
#     print(f"Data saved to {filename}")
#
#
# def main():
#     # User configurations
#     exchange_name = "binance"  # Example: 'binance', 'kraken'
#     symbol = "BTC/USDT"  # Crypto pair
#     timeframe = "5m"  # 5-minute interval
#     duration = 2  # Duration in hours
#     limit = (duration * 60) // 5  # Number of 5-minute intervals
#
#     print(f"Fetching {symbol} data from {exchange_name}...")
#     df = fetch_crypto_data(exchange_name, symbol, timeframe, limit)
#     df = calculate_technical_indicators(df)
#
#     # Save to Excel
#     filename = f"{symbol.replace('/', '_')}_technical_data.xlsx"
#     save_to_excel(df, filename)
#
#     # Display recent data
#     print("Latest Technical Data:")
#     print(df[["timestamp", "close", "MACD_12_26_9", "MACDs_12_26_9", "MACDh_12_26_9", "RSI"]].tail())
#
#
# if __name__ == "__main__":
#     main()
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)

new_df = df.tail(1)
new_df2 = df.head(1)

combined_df = pd.concat([new_df, new_df2], ignore_index=True)
print(combined_df)