"""
Ollama is a platform that allows you to run large language models (LLMs) locally on your machine. 
It provides an interface to interact with these models without needing to rely on cloud services. This can be particularly useful for privacy,
speed, and cost reasons.
To run models locally using Ollama, you typically need to follow these steps:
1. Install Ollama: You can download and install Ollama from their official website.
2. Download a Model: Ollama provides a variety of pre-trained models that you can download and run locally. 
You can choose a model that suits your needs.
"""
#-----------------------------------------------------------
"""
Ollama Command Line Interface (CLI) Example
After installing Ollama, you can use the command line to interact with it. For example:
1. To list available models:
    ollama list
2. To run a model:
    ollama run <model-name>
3. To interact with the model:
    ollama chat <model-name>
4. To pull a model from the Ollama registry:
    ollama pull <model-name>
    Example: ollama pull gemma:2b
5. To run the pulled model:
    ollama run gemma:2b
6. To see the running models:
    ollama ps
7. To stop a running model:
    ollama stop <model-name>
8. To remove a model:
    ollama rm <model-name>
-----------------------
"""
"""Ollama API Example
Ollama also provides an API that you can use to interact with the models programmatically.
Here’s a simple example using Python to send a request to a model running on Ollama:

port for ollama is 11434.
To test it browser: http://localhost:11434/v1/models
"""
#-----------------------------------------------------------
# Calling Local Ollama Model from Python using langchain-community
from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="gemma:2b")
question = input("Enter your question: ")
response = llm.invoke(question)
print("Response from local Ollama Model:", response.content)

