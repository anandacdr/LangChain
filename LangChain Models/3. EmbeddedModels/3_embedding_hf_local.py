from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs = {"device": "cpu"}
)

documents = [
    "Kathmandu is the capital of Nepal.",
    "Nepal is a beautiful country.",
    "Nepal is in Asia.",
    "Nepal is a developing country.",
]

# text = "Kathmandu is the capital of Nepal."

# vector = embeddings.embed_query(text)

# print(str(vector))

vectors = embeddings.embed_documents(documents)

print(str(vectors))


