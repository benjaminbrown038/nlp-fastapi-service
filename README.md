# nlp-fastapi-service

A modular NLP web service supporting:
- Sentiment analysis
- Named Entity Recognition
- Zero-shot classification

Features:
- TF-IDF + Logistic Regression baselines
- Optional transformer pipelines
- Pydantic v2 schemas
- Swagger UI and REST automation
- Dockerized deployment
- <100 ms CPU latency for baseline models

Toggle transformers via:
export ENABLE_TRANSFORMERS=true
