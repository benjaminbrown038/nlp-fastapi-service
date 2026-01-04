from pydantic import BaseModel
from typing import List, Optional

class TextRequest(BaseModel):
    text: str
    labels: Optional[List[str]] = None

class SentimentResponse(BaseModel):
    label: str
    score: float

class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int
