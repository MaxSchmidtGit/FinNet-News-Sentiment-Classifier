import requests
from datetime import datetime, timedelta
import random

NEWS_API_KEY = "Your API here"

def fetch_crypto_news():
    """
    Fetches recent crypto-related news headlines using NewsAPI.
    Returns a list of headline strings.
    """
    yesterday = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
    page = random.randint(1, 3)  # Random page for variety

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "crypto OR bitcoin OR ethereum OR blockchain OR fintech OR token",
        "from": yesterday,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 5,
        "page": page,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        return ["⚠️ Error fetching news"]

    headlines = [article["title"] for article in data.get("articles", []) if article.get("title")]
    return headlines
