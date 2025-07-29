from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.0,
    api_key=os.getenv("GOOGLE_API_KEY")
)

chat_history = [
    SystemMessage(content="You are a Helpful Assistant"),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"Assistant: {result.content}")

print(chat_history)