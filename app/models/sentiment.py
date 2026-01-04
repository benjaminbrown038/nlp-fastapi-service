from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from transformers import pipeline
from app.config import ENABLE_TRANSFORMERS

class SentimentModel:
    def __init__(self):
        if ENABLE_TRANSFORMERS:
            self.model = pipeline("sentiment-analysis",
                                  model="distilbert-base-uncased-finetuned-sst-2-english")
        else:
            self.vectorizer = TfidfVectorizer()
            self.clf = LogisticRegression()
            X = self.vectorizer.fit_transform(["good", "bad"])
            self.clf.fit(X, [1, 0])

    def predict(self, text):
        if ENABLE_TRANSFORMERS:
            out = self.model(text)[0]
            return out["label"], out["score"]
        else:
            X = self.vectorizer.transform([text])
            score = self.clf.predict_proba(X)[0][1]
            return ("POSITIVE" if score > 0.5 else "NEGATIVE", score)
