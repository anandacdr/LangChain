from traceback import print_tb
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-9b-it",
    task = "text-generation",
)

parser = JsonOutputParser()

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template = "Give me the name, age, and city of a fictional person \n {format_instructions}",
    input_variables = [],
    partial_variables = {"format_instructions": parser.get_format_instructions()},
)

# prompt = template.format()
chain = template | model | parser

result = chain.invoke({})


print(result)







