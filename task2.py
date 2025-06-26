import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# NewsAPI configuration
api_key = 'fa5b58e3a9194da6bdbee7e966612157'
search_query = 'Apple'  # Change to the stock/company you're interested in
# Adjust the date to 2024-09-18 or later to fit within the free plan limits
url = f'https://newsapi.org/v2/everything?q={search_query}&from=2024-09-18&sortBy=publishedAt&apiKey={api_key}'

# Fetch news data
response = requests.get(url)
news_data = response.json()

# Debugging: Print the full response from the API
print(news_data)

# Check if 'articles' is in the response
if 'articles' in news_data:
    # Initialize VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Analyze sentiment of each headline
    news_sentiments = []
    for article in news_data['articles']:
        title = article['title']
        sentiment_score = analyzer.polarity_scores(title)['compound']
        news_sentiments.append({'title': title, 'sentiment': sentiment_score})

    # Create a DataFrame
    news_df = pd.DataFrame(news_sentiments)

    # Save the data to CSV
    news_df.to_csv('news_sentiment_data.csv', index=False)

    print(news_df.head())
else:
    print("No articles found or an error occurred.")
