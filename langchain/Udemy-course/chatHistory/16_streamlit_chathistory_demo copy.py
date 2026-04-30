import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=GROQ_API_KEY)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a Agile Coach. You provide information about Agile methodologies and practices."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
)

chain = prompt_template | llm

history_for_chain= StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id : history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

st.title("Agile Coach App")
input = st.text_input("Enter your question: ")
if input:
    response = chain_with_history.invoke(input  = {"input": input},
                                         config ={"configurable" : {"session_id" : "abc123"}})
    st.write(response.content)
    st.write(history_for_chain)