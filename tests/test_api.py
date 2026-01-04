from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment():
    r = client.post("/sentiment", json={"text": "I love this"})
    assert r.status_code == 200
    assert "label" in r.json()
