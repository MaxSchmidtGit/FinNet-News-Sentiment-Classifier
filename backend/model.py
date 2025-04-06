import joblib
import os
import numpy as np

def load_model_and_vectorizer():
    """
    Loads the trained sentiment model and vectorizer using joblib.
    """
    model_path = os.path.join("backend", "models", "sentiment_model.pkl")
    vectorizer_path = os.path.join("backend", "models", "vectorizer.pkl")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    return model, vectorizer

def predict_sentiment(model, vectorizer, text):
    """
    Predicts the sentiment (Bullish/Bearish) and confidence score of the given text.
    """
    vector = vectorizer.transform([text])
    probabilities = model.predict_proba(vector)[0]
    prediction = np.argmax(probabilities)
    confidence = round(probabilities[prediction] * 100, 2)
    label = "Bullish 📈" if prediction == 1 else "Bearish 📉"
    return label, confidence
