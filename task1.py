import yfinance as yf
import pandas as pd

# Define the stock symbol and the recent date range
stock_symbol = 'AAPL'  # Change to the stock you want to analyze
start_date = '2024-09-18'  # Adjust to match the news API start date
end_date = '2024-10-15'  # Current date, or adjust as needed

# Fetch the stock data from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Check the first few rows of the data
print(stock_data.head())

# Save the stock data to CSV for future use
stock_data.to_csv('historical_stock_data.csv')
