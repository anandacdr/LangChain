from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch

from dotenv import load_dotenv

# Use GPU if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"🚀 Using device: {device}")

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': device}
)

documents = [
    "Kathmandu is the capital of Nepal."
]

query = "What is the capital of Nepal?" 

doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index,score = max(enumerate(scores), key=lambda x: x[1])

print(f"The most similar document is: {documents[index]}")
print(f"The similarity score is: {score}")




