from flask import Flask, render_template, request
from backend.model import load_model_and_vectorizer, predict_sentiment
from backend.preprocess import clean_text

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer once at startup
model, vectorizer = load_model_and_vectorizer()


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the homepage and handles sentiment classification.
    """
    sentiment = None
    confidence = None
    headline = ""

    if request.method == "POST":
        headline = request.form["headline"]
        cleaned = clean_text(headline)
        sentiment, confidence = predict_sentiment(model, vectorizer, cleaned)

    return render_template("index.html", sentiment=sentiment, confidence=confidence, headline=headline)


@app.route("/api/news")
def api_news():
    """
    Optional: News API route if you use it for live headlines.
    """
    from backend.news_api import fetch_crypto_news  # Lazy import
    headlines = fetch_crypto_news()
    results = []

    for item in headlines:
        cleaned = clean_text(item)
        sentiment, confidence = predict_sentiment(model, vectorizer, cleaned)
        results.append({
            "headline": item,
            "sentiment": sentiment,
            "confidence": f"{confidence} %"
        })

    return {"news": results}


if __name__ == "__main__":
    app.run(debug=True)
