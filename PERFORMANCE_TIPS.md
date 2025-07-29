# 🚀 Performance Tips for LangChain Development

## 🛡️ **Preventing Cursor Freezes**

### **1. Memory Management**
```bash
# Monitor system resources
htop
# or
top

# Check available memory
free -h
```

### **2. Model Loading Best Practices**
```python
# Load models with memory optimization
import torch

# Use CPU for smaller models
device = torch.device("cpu")  # Force CPU for development

# Load models with memory limits
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,  # Use float32 instead of float16
    low_cpu_mem_usage=True,
    device_map=None  # Don't use auto device mapping
)
```

### **3. Batch Processing**
```python
# Process data in smaller batches
def process_in_batches(data, batch_size=10):
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        # Process batch
        yield batch
```

### **4. Resource Monitoring**
```python
# Add to your scripts
import psutil
import os

def print_memory_usage():
    process = psutil.Process(os.getpid())
    print(f"Memory usage: {process.memory_info().rss / 1024 / 1024:.2f} MB")

# Call before/after heavy operations
print_memory_usage()
```

## 🔧 **Cursor-Specific Optimizations**

### **1. Increase Memory Limits**
- Open Cursor settings
- Search for "memory"
- Increase memory allocation if available

### **2. Disable Heavy Extensions**
- Temporarily disable AI assistants
- Close unused tabs
- Disable heavy language servers

### **3. Use Terminal for Heavy Tasks**
```bash
# Run heavy operations in terminal instead of Cursor
cd "LangChain Prompts"
source ../venv/bin/activate
python your_heavy_script.py
```

## 🚨 **Emergency Recovery**

### **If Cursor Freezes:**
1. **Wait 1-2 minutes** - Often recovers automatically
2. **Force Quit** - Use system dialog or `pkill -f cursor`
3. **Restart Cursor** - Clean restart
4. **Check system resources** - Ensure adequate memory/CPU

### **System Commands:**
```bash
# Kill Cursor process
pkill -f cursor

# Check for hanging processes
ps aux | grep python

# Clear memory cache
sudo sync && sudo sysctl -w vm.drop_caches=3
```

## 📊 **Resource Monitoring Script**
```python
#!/usr/bin/env python3
"""
Resource Monitor for LangChain Development
"""

import psutil
import time
import os

def monitor_resources():
    """Monitor system resources"""
    print("🖥️  System Resources:")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Available Memory: {psutil.virtual_memory().available / 1024**3:.1f} GB")
    
    # Check current process
    process = psutil.Process(os.getpid())
    print(f"Current Process Memory: {process.memory_info().rss / 1024**2:.1f} MB")

if __name__ == "__main__":
    while True:
        monitor_resources()
        print("-" * 40)
        time.sleep(5)
```

## 🎯 **Quick Fixes for Common Issues**

### **1. Model Loading Too Slow**
```python
# Use smaller models for development
model_name = "distilbert-base-uncased"  # Instead of large models
```

### **2. Memory Overflow**
```python
# Clear GPU cache
import torch
if torch.cuda.is_available():
    torch.cuda.empty_cache()
```

### **3. Process Hanging**
```bash
# Kill hanging Python processes
pkill -f python
```

## 💡 **Pro Tips**

1. **Use Virtual Environments** - Isolate dependencies
2. **Monitor Resources** - Keep an eye on system usage
3. **Batch Operations** - Process data in chunks
4. **Use Terminal** - Run heavy tasks outside Cursor
5. **Regular Restarts** - Restart Cursor periodically

## 🔍 **Troubleshooting Checklist**

- [ ] Check available memory: `free -h`
- [ ] Monitor CPU usage: `htop`
- [ ] Kill hanging processes: `pkill -f python`
- [ ] Clear cache: `torch.cuda.empty_cache()`
- [ ] Restart Cursor
- [ ] Use smaller models for development
- [ ] Process data in batches
- [ ] Run heavy tasks in terminal

---

**Remember**: It's better to use smaller models and slower processing during development than to have your IDE freeze constantly! 