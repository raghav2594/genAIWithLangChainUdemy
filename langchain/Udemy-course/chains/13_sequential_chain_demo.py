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
title_prompt = PromptTemplate(
    input_variables = ["topic",],
    template = 
    """
    You are an experienced speech writer. 
    You need to craft an impactful title for a speech  
    on the following topic: {topic} 
    Answer exactly with one title.   
    """
)

#Prompt Template 2
speech_prompt = PromptTemplate(
    input_variables = ["title", ["emotion"]],
    template = 
    """
    You need to write a {emotion} speech of 350 words 
     for the following title: {title}    
    """
)

st.title("Speech Generator")

topic = st.text_input("Enter a topic: ")
emotion = st.selectbox("Select the emotion for the speech:", ["Inspiring", "Motivational", "Persuasive", "Informative"])
# Create the first chain to generate the title
    # first_chain = title_prompt | llm | StrOutputParser()
# Create the first chain to generate the title and print it
first_chain = title_prompt | llm | StrOutputParser() | (lambda title : (st.write(title), title)[1])
# Pass the output of the first chain as input to the second chain
second_chain = speech_prompt | llm
final_chain = first_chain | (lambda title: {"title": title, "emotion": emotion}) | second_chain
if topic:
    # Invoke the final chain with the user input
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)
