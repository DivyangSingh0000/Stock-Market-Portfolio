import pandas as pd

# Load stock data and sentiment data
stock_data = pd.read_csv('historical_stock_data.csv')
sentiment_data = pd.read_csv('news_sentiment_data.csv')

# Print column names to debug the issue
print("Stock data columns:", stock_data.columns)
print("Sentiment data columns:", sentiment_data.columns)

# Assuming the sentiment data might lack dates, we check for Date column
# Add a 'Date' column with actual dates if available
if 'Date' not in sentiment_data.columns:
    sentiment_data['Date'] = pd.to_datetime('2024-10-15')  # Placeholder

# Convert 'Date' column to datetime in both datasets
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
sentiment_data['Date'] = pd.to_datetime(sentiment_data['Date'])

# Merge datasets on 'Date' with outer join to keep all data points
combined_data = pd.merge(stock_data, sentiment_data, on='Date', how='outer')

# Only keep weekdays (Monday to Friday)
combined_data = combined_data[combined_data['Date'].dt.weekday < 5]

# Sort by Date before filling missing sentiment data
combined_data.sort_values(by='Date', inplace=True)

# Forward fill and backward fill for missing sentiment values
combined_data['sentiment'].ffill(inplace=True)  # Forward fill
combined_data['sentiment'].bfill(inplace=True)  # Backward fill

# Export the combined data for further use
combined_data.to_csv('combined_stock_sentiment_data.csv', index=False)

print("\nCombined Data:")
print(combined_data)
