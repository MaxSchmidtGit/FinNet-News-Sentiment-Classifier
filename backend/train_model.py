import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from backend.preprocess import clean_text

# Load dataset
df = pd.read_csv("train_data.csv")

# Clean headlines
df["cleaned"] = df["headline"].apply(clean_text)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned"])
y = df["label"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Optional: Evaluate accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f} %")

# Save model and vectorizer
with open("backend/models/sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("backend/models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved.")
