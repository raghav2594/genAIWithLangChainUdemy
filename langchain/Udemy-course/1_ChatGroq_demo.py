#In the course lecture is using OpenAI's API, but in the code snippet,
# it is using Groq's API. The code snippet is for initializing the ChatGroq model from the langchain library and making a request to the model with a user input question.
# The API key is loaded from a .env file and used to authenticate the request to the Groq API.
# I don't have OpenAi's API key, so I am using Groq's API key for testing the code. The code will print the response from the Groq model based on the user's question.

import os
from dotenv import load_dotenv
# Above 2 imports are for loading environment variables from a .env file and accessing them in the code.
from langchain_groq import ChatGroq
# Above import is for using the OpenAI language model from the langchain library.
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GROQ_API_KEY)
# Above lines load the environment variables from the .env file and set the API_KEY variable
# Initialize the OpenAI LLM with the API key
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)
question = input("Enter your question: ")
response = llm.invoke(question)
print("Response from OpenAI:", response.content)