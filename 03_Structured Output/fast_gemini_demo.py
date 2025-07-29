from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import time
import json
from typing import Dict, Any
import os

load_dotenv()

# 🚀 FAST GEMINI TECHNIQUES

# 1. OPTIMIZED MODEL SETTINGS
fast_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Fastest model
    temperature=0,             # No randomness = faster
    max_tokens=100,           # Very short responses
    top_p=0.8,               # Reduce sampling complexity
    top_k=10,                # Limit token selection
    timeout=5                # 5 second timeout (correct parameter)
)

# 2. CACHE FOR REPEATED QUERIES
response_cache: Dict[str, Any] = {}

def get_cached_response(prompt: str) -> str:
    """Get cached response or generate new one"""
    if prompt in response_cache:
        print("⚡ Using cached response!")
        return response_cache[prompt]
    
    print("🔄 Generating new response...")
    start_time = time.time()
    result = fast_model.invoke(prompt)
    elapsed = time.time() - start_time
    
    response_cache[prompt] = result.content
    print(f"✅ Generated in {elapsed:.2f}s")
    return result.content

# 3. ULTRA-SHORT PROMPTS
def create_ultra_fast_prompt(topic: str) -> str:
    """Create minimal prompts for maximum speed"""
    return f"Rate {topic} 1-10. 2 pros, 1 con."

# 4. BATCH PROCESSING
def batch_process_topics(topics: list[str]) -> list[str]:
    """Process multiple topics efficiently"""
    print(f"🚀 Processing {len(topics)} topics...")
    start_time = time.time()
    
    results = []
    for topic in topics:
        prompt = create_ultra_fast_prompt(topic)
        result = get_cached_response(prompt)
        results.append(result)
    
    total_time = time.time() - start_time
    print(f"✅ Batch completed in {total_time:.2f}s ({total_time/len(topics):.2f}s per topic)")
    return results

# 5. PREPROCESSED TEMPLATES
REVIEW_TEMPLATES = {
    "laptop": "Rate {product} 1-10. 2 pros, 1 con.",
    "phone": "Rate {product} 1-10. 2 pros, 1 con.",
    "software": "Rate {product} 1-10. 2 pros, 1 con."
}

def template_review(product: str, category: str) -> str:
    """Use pre-built templates for speed"""
    template = REVIEW_TEMPLATES.get(category, "Rate {product} 1-10. 2 pros, 1 con.")
    prompt = template.format(product=product)
    return get_cached_response(prompt)

# 6. PERFORMANCE MONITORING
class PerformanceMonitor:
    def __init__(self):
        self.times = []
    
    def time_function(self, func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        self.times.append(elapsed)
        return result, elapsed
    
    def get_stats(self):
        if not self.times:
            return "No data"
        return {
            "avg": sum(self.times) / len(self.times),
            "min": min(self.times),
            "max": max(self.times),
            "total": sum(self.times)
        }

# 🎯 DEMO FUNCTIONS

def demo_fast_reviews():
    """Demonstrate fast review generation"""
    print("🚀 ULTRA-FAST GEMINI DEMO")
    print("=" * 50)
    
    monitor = PerformanceMonitor()
    
    # Test 1: Single ultra-fast review
    print("\n1️⃣ Single Ultra-Fast Review:")
    result, time_taken = monitor.time_function(
        get_cached_response, 
        "Rate MacBook M4 Pro 1-10. 2 pros, 1 con."
    )
    print(f"⏱️ Time: {time_taken:.2f}s")
    print(f"📝 Result: {result}")
    
    # Test 2: Cached review (should be instant)
    print("\n2️⃣ Cached Review (Same Query):")
    result, time_taken = monitor.time_function(
        get_cached_response, 
        "Rate MacBook M4 Pro 1-10. 2 pros, 1 con."
    )
    print(f"⏱️ Time: {time_taken:.2f}s")
    print(f"📝 Result: {result}")
    
    # Test 3: Batch processing
    print("\n3️⃣ Batch Processing:")
    topics = [
        "iPhone 15 Pro",
        "Samsung Galaxy S24", 
        "Dell XPS 13"
    ]
    
    results = batch_process_topics(topics)
    
    # Test 4: Template reviews
    print("\n4️⃣ Template Reviews:")
    products = [
        ("MacBook Pro M4", "laptop"),
        ("iPhone 15", "phone"),
        ("Adobe Photoshop", "software")
    ]
    
    for product, category in products:
        result, time_taken = monitor.time_function(
            template_review, product, category
        )
        print(f"📱 {product}: {time_taken:.2f}s")
        print(f"   {result}")
    
    # Performance stats
    print(f"\n📊 Performance Stats:")
    stats = monitor.get_stats()
    print(f"   Average: {stats['avg']:.2f}s")
    print(f"   Fastest: {stats['min']:.2f}s")
    print(f"   Slowest: {stats['max']:.2f}s")
    print(f"   Total: {stats['total']:.2f}s")

def speed_comparison():
    """Compare different optimization techniques"""
    print("\n🏁 SPEED COMPARISON")
    print("=" * 50)
    
    # Standard model
    standard_model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        max_tokens=300
    )
    
    # Ultra-fast model
    ultra_fast_model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=50,
        timeout=3
    )
    
    prompt = "Rate MacBook M4 Pro 1-10. 2 pros, 1 con."
    
    # Test standard
    print("🐌 Standard Model:")
    start = time.time()
    result1 = standard_model.invoke(prompt)
    time1 = time.time() - start
    print(f"   Time: {time1:.2f}s")
    print(f"   Length: {len(result1.content)} chars")
    
    # Test ultra-fast
    print("⚡ Ultra-Fast Model:")
    start = time.time()
    result2 = ultra_fast_model.invoke(prompt)
    time2 = time.time() - start
    print(f"   Time: {time2:.2f}s")
    print(f"   Length: {len(result2.content)} chars")
    
    # Speed improvement
    improvement = ((time1 - time2) / time1) * 100
    print(f"🚀 Speed Improvement: {improvement:.1f}% faster!")

# 7. INSTANT CACHE DEMO
def instant_cache_demo():
    """Show how caching makes responses instant"""
    print("\n⚡ INSTANT CACHE DEMO")
    print("=" * 50)
    
    queries = [
        "Rate iPhone 15 1-10. 2 pros, 1 con.",
        "Rate Samsung S24 1-10. 2 pros, 1 con.",
        "Rate MacBook Air 1-10. 2 pros, 1 con."
    ]
    
    # First run (slow)
    print("🔄 First Run (Generating):")
    for query in queries:
        start = time.time()
        result = get_cached_response(query)
        elapsed = time.time() - start
        print(f"   {query}: {elapsed:.2f}s")
    
    # Second run (instant from cache)
    print("\n⚡ Second Run (Cached):")
    for query in queries:
        start = time.time()
        result = get_cached_response(query)
        elapsed = time.time() - start
        print(f"   {query}: {elapsed:.2f}s")

if __name__ == "__main__":
    # Run demos
    demo_fast_reviews()
    speed_comparison()
    instant_cache_demo()
    
    print("\n💡 ULTRA-FAST TIPS:")
    print("1. Use gemini-1.5-flash (fastest model)")
    print("2. Set temperature=0 (deterministic)")
    print("3. Limit max_tokens=50-100 (very short)")
    print("4. Use caching for repeated queries")
    print("5. Create ultra-short prompts")
    print("6. Set timeout=3-5 seconds")
    print("7. Use templates for consistency")
    print("8. Batch similar queries together")
    print("9. Avoid complex structured output")
    print("10. Use simple text responses") 