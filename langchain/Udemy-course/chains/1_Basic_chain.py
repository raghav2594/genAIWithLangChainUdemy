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
    input_variables = ["city", "no_of_paras", "language"],
    template = 
    """
   Welcome to the {city} travel guide!
   If you are visiting in {month}, here is what you can expect:
   1. Must-visit attractions.
   2. Local cuisine you must try.
   3. Usual phrases in {language} that can be helpful.
   4. Tips for travelling on a {budget} budget.

   Enjoy your trip.
    """
)
st.title("Travel Guide App")

city = st.text_input("Enter a city: ")
month = st.text_input("Enter the month you are visiting: ")
language = st.selectbox("Select the language for the answer: ", options=["English", "Spanish", "French", "German", "Chinese", "Tamil"])
budget = st.selectbox("Select your budget for the trip: ", ["low", "medium", "high"])
chain = prompt_template | llm
if city:
    response = chain.invoke({"city": city,
                             "month": month,
                             "language": language,
                             "budget": budget})
    st.write(response.content)
