"""
Bosch Model Farm - Chat API smoke test (OpenAI-compatible client)

Docs:
https://inside-docupedia.bosch.com/confluence2/spaces/FARM/pages/562171306/%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB+Code+Examples
"""

import os
from dotenv import load_dotenv
import requests
# Above import is for using the OpenAI language model from the langchain library.
load_dotenv()
os.environ["API_KEY"] = os.getenv("API_KEY")
API_KEY = os.getenv("API_KEY")
print(API_KEY)
# Above lines load the environment variables from the .env file and set the API_KEY variable
# Initialize the OpenAI LLM with the API key
response = requests.post(
    "https://aoai-farm.bosch-temp.com/api/openai/deployments/gpt-5-nano-2025-08-07/chat/completions?api-version=2024-05-01-preview",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-5-nano-2025-08-07",
        "messages": [{"role": "user", "content": "Just say Hello!"}]
    }
)
print(response.text)
