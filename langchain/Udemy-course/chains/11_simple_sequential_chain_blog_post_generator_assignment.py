from itertools import chain
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)
#Prompt Template 1
outline_prompt = PromptTemplate(
    input_variables = ["topic",],
    template = 
    """
      Create an outline for a blog post on the following topic: {topic} 
    The outline should include: 
    - Introduction 
    - 3 main points with subpoints 
    - Conclusion    
    """
)

#Prompt Template 2
introduction_prompt = PromptTemplate(
    input_variables = ["outline",],
    template = 
    """
   You are a professional blogger. 
    Write an engaging introduction paragraph based on the following 
    outline:{outline} 
    The introduction should hook the reader and provide a brief 
    overview of the topic. 
    """
)

st.title("Blog Post Generator")

topic = st.text_input("Enter a topic: ")
# Create the first chain to generate the outline
    # first_chain = outline_prompt | llm | StrOutputParser()
# Create the first chain to generate the outline and print it
first_chain = outline_prompt | llm | StrOutputParser() | (lambda outline : (st.write(f'Outline Started:----{outline}-----Outline Ended'), outline)[1])
# Pass the output of the first chain as input to the second chain
second_chain = introduction_prompt | llm
final_chain = first_chain | second_chain
if topic:
    # Invoke the final chain with the user input
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)
