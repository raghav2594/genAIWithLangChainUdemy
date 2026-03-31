# Sample code to test the Bosch Model Farm API key and client setup
# https://inside-docupedia.bosch.com/confluence2/spaces/FARM/pages/562171306/%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB+Code+Examples
import os
from dotenv import load_dotenv
from openai import OpenAI  # Bosch farm uses OpenAI-compatible client

# Load environment variables
load_dotenv()
os.environ["API_KEY"] = os.getenv("API_KEY")
API_KEY = os.getenv("API_KEY")
subscription_key = API_KEY

# Initialize client for Bosch Model Farm
client = OpenAI(
    api_key=subscription_key,
    base_url="https://aoai-farm.bosch-temp.com/api/openai/deployments/gpt-5-nano-2025-08-07",
    default_query={"api-version": "2024-05-01-preview"},
)

# Send a chat completion request
response = client.chat.completions.create(
    model="gpt-5-nano-2025-08-07",
    messages=[{"role": "user", "content": "How are you!"}]
)

# print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)
