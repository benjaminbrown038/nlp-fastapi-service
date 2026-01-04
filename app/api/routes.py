from fastapi import APIRouter
from app.api.schemas import *
from app.core.pipeline import sentiment, ner, zero_shot

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
def sentiment_endpoint(req: TextRequest):
    label, score = sentiment.predict(req.text)
    return {"label": label, "score": score}

@router.post("/ner")
def ner_endpoint(req: TextRequest):
    return ner.predict(req.text)

@router.post("/zero-shot")
def zero_shot_endpoint(req: TextRequest):
    return zero_shot.predict(req.text, req.labels)
