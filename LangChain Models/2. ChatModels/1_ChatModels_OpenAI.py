from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo-instruct", temperature=1.1, max_completion_tokens=100)

result = llm.invoke("What is the capital of Nepal?")

print(result)   