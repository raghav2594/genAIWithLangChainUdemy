import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
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

history_for_chain= ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id : history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

print("Agile Coach App")
question = input("Enter your question: ")
if question:
    response = chain_with_history.invoke(input  = {"input": question},
                                         config ={"configurable" : {"session_id" : "abc123"}})
    print(response.content)
