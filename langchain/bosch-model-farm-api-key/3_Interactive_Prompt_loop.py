"""
Bosch Model Farm - Chat API smoke test (OpenAI-compatible client)

Docs:
https://inside-docupedia.bosch.com/confluence2/spaces/FARM/pages/562171306/%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB+Code+Examples
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------
# Configuration
# -------------------------
API_VERSION = "2024-05-01-preview"
CHAT_DEPLOYMENT = "gpt-5-nano-2025-08-07"

BASE_URL = f"https://aoai-farm.bosch-temp.com/api/openai/deployments/{CHAT_DEPLOYMENT}"

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

api_key = os.getenv("API_KEY")  # keep as per your .env
if not api_key:
    raise ValueError(
        "❌ API_KEY not found. Please set API_KEY in your .env file.\n"
        "Example:\n"
        "API_KEY=your_farm_subscription_key"
    )

# -------------------------
# Initialize client
# -------------------------
client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL,
    default_query={"api-version": API_VERSION},
)

print("✅ Bosch Model Farm client initialized")
print(f"   Deployment : {CHAT_DEPLOYMENT}")
print(f"   API Version: {API_VERSION}")
print("Type 'exit' to quit.\n")

# -------------------------
# Interactive prompt loop
# -------------------------
while True:
    question = input("What do you want to ask the model? ").strip()
    if not question:
        print("⚠ Please enter a question.\n")
        continue
    if question.lower() in ("exit", "quit", "q"):
        print("👋 Exiting.")
        break

    try:
        response = client.chat.completions.create(
            model=CHAT_DEPLOYMENT,
            messages=[{"role": "user", "content": question}],
        )

        answer = response.choices[0].message.content
        print("\n🧠 Model response:\n", answer, "\n")

        # Optional: print metadata (uncomment if needed)
        # print("Model:", response.model)
        # if getattr(response, "usage", None):
        #     print("Usage:", response.usage)

    except Exception as e:
        print("❌ Request failed:", type(e).__name__)
        print("   Details:", str(e), "\n")