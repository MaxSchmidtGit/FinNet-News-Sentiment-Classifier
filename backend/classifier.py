import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dummy training data
train_texts = [
    "Stock prices are rising",
    "The market is bullish today",
    "Investors are optimistic",
    "Shares fall sharply",
    "The economy is weakening",
    "Bearish sentiment surrounds crypto"
]

train_labels = [1, 1, 1, 0, 0, 0]  # 1 = Bullish, 0 = Bearish

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train_texts)

# Train Logistic Regression classifier
model = LogisticRegression()
model.fit(X, train_labels)

# Save model and vectorizer
joblib.dump(model, "backend/sentiment_model.pkl")
joblib.dump(vectorizer, "backend/vectorizer.pkl")

def classify_text(text: str) -> str:
    """
    Loads the trained model and vectorizer, classifies the text.
    """
    model = joblib.load("backend/sentiment_model.pkl")
    vectorizer = joblib.load("backend/vectorizer.pkl")
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return "Bullish 📈" if prediction == 1 else "Bearish 📉"
