run:
	uvicorn app.main:app --reload

test:
	pytest

docker:
	docker build -t nlp-api .
