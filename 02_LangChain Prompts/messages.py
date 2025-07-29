from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.0,
    api_key=os.getenv("GOOGLE_API_KEY")
)

messages = [
    SystemMessage(content="You are a Helpful Assistant"),
    HumanMessage(content="Tell me about LangChain.")
]

response = llm.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)

