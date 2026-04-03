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
    input_variables = ["country", "no_of_paras", "language"],
    template = 
    """
    You are an expert in traditional cuisine. You provide information about specific dishes
    from a specific country.

    Answer the question: What is a traditional dish from {country}?
    Answer should be in {language} and should be no more than {no_of_paras} paragraphs.
    """
)
st.title("Cuisine App Info")

country = st.text_input("Enter a country: ")
no_of_paras = st.number_input("Enter the number of paragraphs for the answer: ", min_value=1, max_value=10, value=3)
language = st.selectbox("Select the language for the answer: ", options=["English", "Spanish", "French", "German", "Chinese", "Tamil"])
if country:
    response = llm.invoke(prompt_template.format(country=country,
                                                 no_of_paras=no_of_paras,
                                                language=language))
    st.write(response.content)
