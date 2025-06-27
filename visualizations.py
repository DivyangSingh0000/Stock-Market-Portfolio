import pandas as pd
import matplotlib.pyplot as plt

# Load the combined dataset
data = pd.read_csv('combined_stock_sentiment_data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the date as index for easier plotting
data.set_index('Date', inplace=True)

# Create a figure and a set of subplots with dual axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the stock closing price on the left y-axis
ax1.set_xlabel('Date')
ax1.set_ylabel('Closing Price', color='blue')
ax1.plot(data.index, data['Close'], color='blue', label='Stock Closing Price')
ax1.tick_params(axis='y', labelcolor='blue')

# Create another y-axis for sentiment on the right side
ax2 = ax1.twinx()
ax2.set_ylabel('Sentiment Score', color='green')
ax2.plot(data.index, data['sentiment'], color='green', label='Sentiment Score', linestyle='--')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('Stock Closing Price and Sentiment Score Over Time')
fig.tight_layout()
plt.grid(True)

# Show plot
plt.show()
