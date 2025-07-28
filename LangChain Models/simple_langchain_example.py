#!/usr/bin/env python3
"""
Simple LangChain Example
This script demonstrates basic usage of LangChain with OpenAI.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

def main():
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable")
        print("You can create a .env file with: OPENAI_API_KEY=your_api_key_here")
        return
    
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    # Create messages
    messages = [
        SystemMessage(content="You are a helpful AI assistant that provides clear and concise answers."),
        HumanMessage(content="What is LangChain and how can it be used in AI applications?")
    ]
    
    # Get response from the model
    print("🤖 LangChain Example")
    print("=" * 50)
    
    try:
        response = llm.invoke(messages)
        print("Response:")
        print(response.content)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your OpenAI API key is valid and you have sufficient credits.")

if __name__ == "__main__":
    main() 