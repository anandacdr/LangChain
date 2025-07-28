from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = dict(
        temperature = 1.1,
        max_new_tokens = 100
    )
)


chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("What is the capital of Nepal?")
print(result.content)