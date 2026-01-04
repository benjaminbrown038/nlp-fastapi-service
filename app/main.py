from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="NLP FastAPI Service")
app.include_router(router)
