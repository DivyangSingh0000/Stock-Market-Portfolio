import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the combined dataset
data = pd.read_csv('combined_stock_sentiment_data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index
data.set_index('Date', inplace=True)

# 1. Time Series Plot for Stock Prices
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title('Stock Prices Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.legend()
plt.grid()
plt.show()

# 2. Time Series Plot for Sentiment
plt.figure(figsize=(14, 7))
plt.plot(data['sentiment'], label='Sentiment Score', color='orange')
plt.title('Sentiment Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Sentiment Score', fontsize=14)
plt.legend()
plt.grid()
plt.show()

# 3. Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation = data[['Open', 'High', 'Low', 'Close', 'Volume', 'sentiment']].corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap', fontsize=16)
plt.show()

# 4. Box Plot for Sentiment Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['sentiment'], color='lightgreen')
plt.title('Distribution of Sentiment Scores', fontsize=16)
plt.xlabel('Sentiment Score', fontsize=14)
plt.grid()
plt.show()

# 5. Combined Plot of Stock Prices and Sentiment
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['sentiment'] * 100, label='Sentiment Score (scaled)', color='orange')  # Scale sentiment for better visibility
plt.title('Stock Prices and Sentiment Score Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.legend()
plt.grid()
plt.show()
