from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=1.1, max_completion_tokens=100)

result = llm.invoke("What is the capital of Nepal?")

print(result)