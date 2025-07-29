from optparse import Option
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, List, Optional, Literal
import os
from pydantic import BaseModel, Field

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0
)

# Define the structured output schema - fixed for Google's requirements
class Review(BaseModel):
    key_themes: List[str] = Field(description = "Write down all the key points discussed in the review in a list")
    summary: str = Field(description = "A breif summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description = "Return the sentiment of the review either negative, positive or neutral")
    pros: List[str] = Field(description = "Write down all the pros of the product in a list")
    cons: List[str] = Field(description = "Write down all the cons of the product in a list")
    name: Optional[str] = Field(description = "The name of the product")


# Create structured model
structured_model = model.with_structured_output(Review)

# Test with the review text
result = structured_model.invoke("""
The MacBook M4 Pro (14-inch) with 24GB memory and 1TB SSD delivers blazing-fast performance and incredible efficiency. Powered by Apple's latest M4 chip, it handles multitasking, video editing, and development work with ease. The Liquid Retina XDR display offers stunning clarity and color accuracy, perfect for creatives. It's lightweight, beautifully designed, and boasts excellent battery life, making it ideal for professionals on the move.

Pros:
- Ultra-fast M4 Pro chip performance
- 24GB unified memory for smooth multitasking
- Brilliant 14" Liquid Retina XDR display
- Long battery life and efficient cooling
- 1TB SSD offers ample fast storage

Cons:
- Expensive
- Limited port variety
- No user-upgradable components
""")

# Display the structured result
print("=== Structured Output Result ===")
print(f"Key Themes: {result['key_themes']}")
print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Pros: {result['pros']}")
print(f"Cons: {result['cons']}")

# Alternative: Simple approach if structured output fails
print("\n=== Alternative: Simple Approach ===")
try:
    simple_prompt = """
    Analyze this MacBook M4 Pro review and extract:
    1. Key themes (list)
    2. Summary (brief)
    3. Sentiment (positive/negative/neutral)
    4. Pros (list)
    5. Cons (list)
    
    Review: The MacBook M4 Pro (14-inch) with 24GB memory and 1TB SSD delivers blazing-fast performance and incredible efficiency. Powered by Apple's latest M4 chip, it handles multitasking, video editing, and development work with ease. The Liquid Retina XDR display offers stunning clarity and color accuracy, perfect for creatives. It's lightweight, beautifully designed, and boasts excellent battery life, making it ideal for professionals on the move.
    
    Pros: Ultra-fast M4 Pro chip performance, 24GB unified memory for smooth multitasking, Brilliant 14" Liquid Retina XDR display, Long battery life and efficient cooling, 1TB SSD offers ample fast storage
    
    Cons: Expensive, Limited port variety, No user-upgradable components
    """
    
    simple_result = model.invoke(simple_prompt)
    print(simple_result.content)
    
except Exception as e:
    print(f"Simple approach also failed: {e}")