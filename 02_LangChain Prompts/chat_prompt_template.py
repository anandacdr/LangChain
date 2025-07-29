from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

'''
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} Expert"),
    HumanMessage(content="Explain in simple terms what is {input}")
])
'''

# Using ChatPromptTemplate
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} Expert"),
    ("human", "Explain in simple terms what is {input}")
])

input = "how to develop Nepal a Digital Nepal?"    

print(chat_template.invoke({"input": input, "domain": "Nepal"}))


