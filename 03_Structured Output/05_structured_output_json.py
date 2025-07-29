from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0,
    max_tokens=500
)

# Load JSON schema
try:
    with open("05_json_schema.json", "r") as f:
        json_schema = json.load(f)
    print("✅ JSON schema loaded successfully")
except FileNotFoundError:
    print("❌ JSON schema file not found")
    exit(1)
except json.JSONDecodeError:
    print("❌ Invalid JSON schema")
    exit(1)

# Test review text
review_text = """
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
"""

def test_structured_output():
    """Test the structured output with JSON schema"""
    print("\n🚀 Testing Structured Output with JSON Schema")
    print("=" * 60)
    
    try:
        # Try different approaches for structured output
        print("🔄 Attempting structured output...")
        
        # Method 1: Direct structured output
        try:
            structured_model = model.with_structured_output(json_schema)
            start_time = time.time()
            result = structured_model.invoke(review_text)
            elapsed_time = time.time() - start_time
            
            print(f"✅ Structured output generated in {elapsed_time:.2f} seconds")
            print("\n📊 Results:")
            print(f"   Name: {result.get('name', 'N/A')}")
            print(f"   Rating: {result.get('rating', 'N/A')}/10")
            print(f"   Sentiment: {result.get('sentiment', 'N/A')}")
            print(f"   Summary: {result.get('summary', 'N/A')}")
            print(f"   Key Themes: {result.get('key_themes', [])}")
            print(f"   Pros: {result.get('pros', [])}")
            print(f"   Cons: {result.get('cons', [])}")
            
            # Save results to file
            with open("structured_output_result.json", "w") as f:
                json.dump(result, f, indent=2)
            print("\n💾 Results saved to 'structured_output_result.json'")
            return
            
        except Exception as e1:
            print(f"❌ Method 1 failed: {e1}")
            
        # Method 2: Using structured_output parameter
        try:
            start_time = time.time()
            result = model.invoke(review_text, structured_output=json_schema)
            elapsed_time = time.time() - start_time
            
            print(f"✅ Structured output generated in {elapsed_time:.2f} seconds")
            print("\n📊 Results:")
            print(f"   Name: {result.get('name', 'N/A')}")
            print(f"   Rating: {result.get('rating', 'N/A')}/10")
            print(f"   Sentiment: {result.get('sentiment', 'N/A')}")
            print(f"   Summary: {result.get('summary', 'N/A')}")
            print(f"   Key Themes: {result.get('key_themes', [])}")
            print(f"   Pros: {result.get('pros', [])}")
            print(f"   Cons: {result.get('cons', [])}")
            
            # Save results to file
            with open("structured_output_result.json", "w") as f:
                json.dump(result, f, indent=2)
            print("\n💾 Results saved to 'structured_output_result.json'")
            return
            
        except Exception as e2:
            print(f"❌ Method 2 failed: {e2}")
            
        # If both methods fail, use fallback
        print("🔄 Both structured methods failed, using fallback...")
        fallback_approach()
        
    except Exception as e:
        print(f"❌ Error with structured output: {e}")
        print("🔄 Trying fallback approach...")
        fallback_approach()

def fallback_approach():
    """Fallback to simple text output if structured output fails"""
    print("\n🔄 Fallback: Simple Text Output")
    print("=" * 40)
    
    try:
        simple_prompt = """
        Analyze this MacBook M4 Pro review and provide:
        1. Product name
        2. Rating (1-10)
        3. Sentiment (positive/negative/neutral)
        4. Brief summary
        5. Key themes
        6. Pros (list)
        7. Cons (list)
        
        Review: """ + review_text
        
        start_time = time.time()
        result = model.invoke(simple_prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Fallback completed in {elapsed_time:.2f} seconds")
        print("\n📝 Result:")
        print(result.content)
        
    except Exception as e:
        print(f"❌ Fallback also failed: {e}")

def test_multiple_products():
    """Test with multiple products"""
    print("\n🔄 Testing Multiple Products")
    print("=" * 40)
    
    products = [
        "iPhone 15 Pro with A17 Pro chip and titanium design",
        "Samsung Galaxy S24 Ultra with S Pen and AI features",
        "Dell XPS 13 with Intel Core i7 and InfinityEdge display"
    ]
    
    for i, product in enumerate(products, 1):
        print(f"\n📱 Product {i}: {product}")
        try:
            start_time = time.time()
            result = model.invoke(product)
            elapsed_time = time.time() - start_time
            
            print(f"   ⏱️ Time: {elapsed_time:.2f}s")
            print(f"   📝 Result: {result.content[:100]}...")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    print("🎯 JSON Schema Structured Output Demo")
    print("=" * 50)
    
    # Test main functionality
    test_structured_output()
    
    # Test multiple products
    test_multiple_products()
    
    print("\n💡 Tips:")
    print("- JSON schema provides strict validation")
    print("- Structured output ensures consistent format")
    print("- Fallback approach for reliability")
    print("- Results are saved to JSON file")