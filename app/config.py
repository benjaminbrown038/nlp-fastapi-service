import os

ENABLE_TRANSFORMERS = os.getenv("ENABLE_TRANSFORMERS", "false").lower() == "true"
