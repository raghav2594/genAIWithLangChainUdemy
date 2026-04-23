import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a Agile Coach. You provide information about Agile methodologies and practices."),
        ("human", "{input}")
    ]
)
st.title("Agile Coach App")

input = st.text_input("Enter your question: ")
chain = prompt_template | llm
if input:
    response = chain.invoke({"input": input})
    st.write(response.content)
