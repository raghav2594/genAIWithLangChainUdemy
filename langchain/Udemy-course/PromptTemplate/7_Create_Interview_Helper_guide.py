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
    input_variables = ["company", "positionTitle", "strengths", "weaknesses"],
    template = 
    """
   You are an expert career coach. 
   You help candidates prepare for job interviews by providing them with potential interview questions and answers
   based on the {company} and {positionTitle} they are applying for.
   You also provide feedback on the candidate's {strengths} and {weaknesses} to help them improve their interview skills"""
)
st.title("Interview Helper App")

company = st.text_input("Enter the company name: ")
positionTitle = st.text_input("Enter the position title: ")
strengths = st.text_area("Enter your strengths: ", max_chars=100)
weaknesses = st.text_area("Enter your weaknesses: ", max_chars=100)
if company and positionTitle and strengths and weaknesses:
    response = llm.invoke(prompt_template.format(company=company,
                                                 positionTitle=positionTitle,
                                                 strengths=strengths,
                                                 weaknesses=weaknesses))
    st.write(response.content)
