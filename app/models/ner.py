from transformers import pipeline
from app.config import ENABLE_TRANSFORMERS

class NERModel:
    def __init__(self):
        if ENABLE_TRANSFORMERS:
            self.model = pipeline("ner", model="dslim/bert-base-NER")

    def predict(self, text):
        if not ENABLE_TRANSFORMERS:
            return []
        return self.model(text)
