# 🧠 FinNet – News Sentiment Classifier

**FinNet** is a lightweight yet powerful sentiment analysis app focused on financial and crypto-related news headlines. It classifies input as **Bullish 📈** or **Bearish 📉** in real-time and includes a confidence score.

---

## 🚀 Features

- 🔄 Real-time crypto/fintech news via NewsAPI
- 🧠 Logistic Regression + TF-IDF for text classification
- 🧼 NLP preprocessing using spaCy (lemmatization, stopword removal)
- 📊 Confidence scores for each prediction
- 🌑 Modern dark-themed UI with live result rendering
- 🔧 Modular structure (easy to extend or swap ML models)

---

## 📂 Project Structure

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/finnet.git
cd finnet

pip install -r requirements.txt
python -m spacy download en_core_web_sm

Set your NewsAPI key

Got to backend/news_api.py and replace
API_KEY = "Your API here"
with your actual NewsAPI.org key.

Train the model (or use the pre-trainedversion)

bash
python backend/train_model.py

Run the app

bash
python app.py

Open your browser and got to:

http://127.0.0.1.5000

📘 Example Usage
Enter your own financial news headline

Or click the Live Data button to get real-time crypto/fintech headlines and see the predicted sentiment

🧪 Customization
You can easily:

Replace the model with a more advanced one (e.g., BERT, Watson NLP)

Add a database to store historical predictions

Style the frontend further or embed into dashboards

