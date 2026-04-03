import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)

# Streamlit title function is used to set the title of the Streamlit app. 
# In this case, it will display "Chat with OpenAI's LLM using Streamlit" at the top of the app.
st.title("Chat with OpenAI's LLM using Streamlit")

# Streamlit text_input function is used to create a 
# text input box where users can enter their questions.

question = st.text_input("Enter your question: ")
if question:
    response = llm.invoke(question)
    # Streamlit write function is used to display the response from the OpenAI model
    # on the Streamlit app.

    st.write("Response from Model:", response.content)


# To run this Streamlit app, save the code in a Python file (e.g., app.py) and run the following command in your terminal:
# streamlit run langchain\Udemy-course\3_Streamlit_demo.py
# This will running with the port 8501 by default,
# and you can access the app in your web browser at http://localhost:8501.
