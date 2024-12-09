import yfinance as yf


def get_start_date_of_symbol(symbol):
    try:
        # Download historical data
        data = yf.download(symbol, start="2000-01-01")

        # Check if data is empty
        if data.empty:
            return f"No data available for {symbol}"

        # Return the first available date in the dataset
        return data.index[0].date()
    except Exception as e:
        return f"Error fetching data: {e}"


# Example usage
print(get_start_date_of_symbol("TSLA"))
