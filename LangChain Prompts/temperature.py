from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=1.0, max_completion_tokens=100)

result = model.invoke("Write About Tharu people from Nepal.")

print(result)