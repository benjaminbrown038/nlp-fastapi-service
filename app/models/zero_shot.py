from transformers import pipeline
from app.config import ENABLE_TRANSFORMERS

class ZeroShotModel:
    def __init__(self):
        if ENABLE_TRANSFORMERS:
            self.model = pipeline("zero-shot-classification",
                                  model="facebook/bart-large-mnli")

    def predict(self, text, labels):
        if not ENABLE_TRANSFORMERS:
            return {}
        return self.model(text, labels)
