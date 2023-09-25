import yfinance as yf
import pandas as pd

# Function to screen NYSE stocks
def screen_nyse_stocks():
    # Get a list of all NYSE stocks
    nyse_stocks = pd.read_csv("https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download")
    nyse_symbols = nyse_stocks['Symbol'].tolist()
    print(nyse_symbols)
    nyse_symbols = ['AAPL']
    # Initialize an empty list to store selected stocks
    selected_stocks = []

    # Define the criteria for screening
    for symbol in nyse_symbols:
        try:
            # Fetch historical daily data for the stock
            stock_data = yf.download(symbol, start="2022-01-01", end="2023-09-25")
            #print(stock_data)
            # Check if there are at least 3 days of data
            if len(stock_data) >= 3:
                # Calculate the average volume of the past 3 days
                avg_volume = stock_data['Volume'][-3:].mean()

                # Check if the volume is increasing for the past 3 days
                if (
                    stock_data['Volume'][-1] > stock_data['Volume'][-2] and
                    stock_data['Volume'][-2] > stock_data['Volume'][-3]
                ):
                    # Check if the closing price is rising for the past 3 days
                    if (
                        stock_data['Close'][-1] > stock_data['Close'][-2] and
                        stock_data['Close'][-2] > stock_data['Close'][-3]
                    ):
                        selected_stocks.append(symbol)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")

    return selected_stocks

# Screen NYSE stocks based on the criteria
selected_stocks = screen_nyse_stocks()

# Print the selected stocks
print("Selected NYSE stocks for BTST & Swing trade:")
print(selected_stocks)
