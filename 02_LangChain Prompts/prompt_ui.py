from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_core.prompts import PromptTemplate
import streamlit as st
import torch

from dotenv import load_dotenv

load_dotenv()

# Use GPU if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
st.sidebar.success(f"🚀 Using device: {device}")

# Load model locally with GPU optimization
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
    device_map="auto" if device.type == "cuda" else None,
    low_cpu_mem_usage=True if device.type == "cuda" else False
)

# Move model to device if not using device_map
if device.type == "cuda" and model.device.type != "cuda":
    model = model.to(device)

# Create pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.7,
    device=device
)

# Create LangChain wrapper
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)

st.header("Research Paper Summarizer")

# Dynamic Prompt
paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is All You Need", "The Illustrated Transformer", "A Brief History of Neural Machine Translation", "A Comprehensive Survey on Transfer Learning"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Educational"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 Paragraphs)", "Medium (3-4 Paragraphs)", "Long (5+ Paragraphs)"])

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
Please Summarize the Research Paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If Certain information is not available in the paper, respond with: "Insufficient Information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.    
"""
)

if st.button("Generate Summary"):
    if paper_input != "Select...":
        with st.spinner("Generating summary..."):
            # Fill the Placeholders
            prompt = prompt_template.format(paper_input=paper_input, style_input=style_input, length_input=length_input)
            result = chat_model.invoke(prompt)
            st.write(result.content)
    else:
        st.warning("Please select a research paper first!")

