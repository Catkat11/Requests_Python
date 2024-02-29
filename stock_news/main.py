import requests
from twilio.rest import Client

# Stock and company details
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints and keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = "15FNOSQ9ZGK3KF8P"
NEWS_API = "2fc59537760e4e5cac4ee32b474ef222"
TWILIO_SID = "AC9237e3c5b844ead669f24a93eeb80797"
TWILIO_AUTH_TOKEN = "TOKEN"

# Parameters for API requests
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}

# Fetching stock data
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday = stock_data_list[0]["4. close"]
more_yesterday = stock_data_list[1]["4. close"]

# Calculating stock change
difference = float(yesterday) - float(more_yesterday)
up_down = "UP" if difference > 0 else "DOWN"
difference_percentage = round(difference / float(yesterday) * 100)

# Checking for significant change and fetching news
if abs(difference_percentage) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

    # Formatting news articles
    formatted_articles = [f"{STOCK}: {up_down}{difference_percentage}%\nHeadline: {article['title']}. \n" \
                          f"Brief: {article['description']}" for article in news_data]

    # Sending news alerts via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+15737495194",
            to="+48666666666"
        )
