from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import HumanMessage, SystemMessage

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent"),
    MessagePlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])

chat_history = []

# load chat history
with open("chat_history.txt", "r") as file:
    chat_history = file.readlines()
    
print(chat_history)
