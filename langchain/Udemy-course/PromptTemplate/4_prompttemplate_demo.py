import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)

prompt_template = PromptTemplate(
    input_variables = ["country"],
    template = 
    """
    You are an expert in traditional cuisine. You provide information about specific dishes
    from a specific country.

    Answer the question: What is a traditional dish from {country}?
    """
)
st.title("Cuisine App Info")

country = st.text_input("Enter a country: ")
if country:
    response = llm.invoke(prompt_template.format(country=country))
    st.write(response.content)
