#!/usr/bin/env python3
"""
GPU-Optimized Model Loading for LangChain
Automatically uses GPU when available for better performance
"""

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch

def load_model_with_gpu(model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0", max_new_tokens=200, temperature=0.7):
    """
    Load a HuggingFace model optimized for GPU usage
    
    Args:
        model_name: HuggingFace model name
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
    
    Returns:
        chat_model: LangChain chat model ready to use
    """
    
    # Check device availability
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"🚀 Loading model on: {device}")
    
    # Load tokenizer
    print("📝 Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Load model with device placement
    print("🧠 Loading model...")
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
    print("🔧 Creating pipeline...")
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        device=device
    )
    
    # Create LangChain wrapper
    llm = HuggingFacePipeline(pipeline=pipe)
    chat_model = ChatHuggingFace(llm=llm)
    
    print(f"✅ Model loaded successfully on {device}!")
    return chat_model

def load_embeddings_with_gpu(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Load embeddings model optimized for GPU usage
    
    Args:
        model_name: HuggingFace embeddings model name
    
    Returns:
        embeddings: HuggingFace embeddings model
    """
    
    from langchain_huggingface import HuggingFaceEmbeddings
    
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"🚀 Loading embeddings on: {device}")
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device}
    )
    
    print(f"✅ Embeddings loaded successfully on {device}!")
    return embeddings

# Example usage
if __name__ == "__main__":
    # Test model loading
    print("🧪 Testing GPU-optimized model loading...")
    chat_model = load_model_with_gpu()
    
    # Test embeddings loading
    print("\n🧪 Testing GPU-optimized embeddings loading...")
    embeddings = load_embeddings_with_gpu()
    
    print("\n🎉 All models loaded successfully!") 