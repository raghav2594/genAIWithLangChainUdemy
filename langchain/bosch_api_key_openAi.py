# Currently, the code is set up to use the Bosch Model Farm endpoint with the OpenAI API. It loads the API key from a .env file and initializes the ChatOpenAI model with the specified endpoint
# Still there is not working condition.

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize LangChain ChatOpenAI with Bosch Model Farm endpoint
llm = ChatOpenAI(
    model="gpt-5-nano-2025-08-07",
    api_key=API_KEY,
    # Put api-version directly in the base_url
    base_url="https://aoai-farm.bosch-temp.com/api/openai/deployments/gpt-5-nano-2025-08-07/chat/completions?api-version=2024-05-01-preview"
)

# Run a simple query
response = llm.invoke("Just say Hello!")
print(response.content)
