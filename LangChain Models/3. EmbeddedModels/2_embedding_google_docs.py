from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

documents = [
    "Kathmandu is the capital of Nepal.",
    "Nepal is a beautiful country.",
    "Nepal is in Asia.",
    "Nepal is a developing country.",
]

result = embedding.embed_documents(documents)

print(str(result))   