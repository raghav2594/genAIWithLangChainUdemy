import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="gemma:2b")
prompt_template = PromptTemplate(
    input_variables = ["city", "month", "language", "budget"],
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
if city and month and language and budget:
    response = llm.invoke(prompt_template.format(city=city,
                                                 month=month,
                                                language=language,
                                                budget=budget))
    st.write(response.content)
