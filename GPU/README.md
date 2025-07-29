# 🚀 GPU Optimization & Setup

This folder contains all GPU-related utilities, configuration scripts, and documentation for optimizing your LangChain projects with NVIDIA GPU acceleration.

## 📁 GPU Folder Contents

```
GPU/
├── README.md                    # This guide
├── gpu_config.py               # GPU detection and configuration
├── gpu_optimized_models.py     # GPU-optimized model loading
├── enable_gpu.sh               # GPU driver setup script
└── GPU_SETUP.md                # Detailed GPU setup guide
```

## 🎯 Quick Start

### 1. **Check GPU Availability**
```bash
# From main directory
source venv/bin/activate
python GPU/gpu_config.py
```

### 2. **Load GPU-Optimized Models**
```bash
# From main directory
source venv/bin/activate
python GPU/gpu_optimized_models.py
```

### 3. **Setup GPU Drivers (First Time)**
```bash
# Make script executable
chmod +x GPU/enable_gpu.sh

# Run GPU setup
./GPU/enable_gpu.sh

# Reboot system
sudo reboot
```

## 🔧 GPU Utilities

### **gpu_config.py**
**Purpose**: Detect and configure GPU for optimal performance

**Features**:
- ✅ Automatic GPU detection
- ✅ CUDA availability check
- ✅ Device information display
- ✅ Memory usage monitoring
- ✅ Environment variable setup

**Usage**:
```bash
source venv/bin/activate
python GPU/gpu_config.py
```

**Output Example**:
```
🔍 Checking GPU availability...
✅ CUDA is available!
🎮 GPU Device: NVIDIA GeForce GTX 1650
💾 GPU Memory: 4.0 GB
🚀 GPU configured for optimal performance!
📍 Current device: cuda:0
```

### **gpu_optimized_models.py**
**Purpose**: Load HuggingFace models with automatic GPU optimization

**Features**:
- ✅ Automatic device detection (GPU/CPU)
- ✅ GPU memory optimization
- ✅ Model loading with device placement
- ✅ Pipeline creation with GPU support
- ✅ LangChain integration

**Usage**:
```python
from GPU.gpu_optimized_models import load_model_with_gpu, load_embeddings_with_gpu

# Load chat model
chat_model = load_model_with_gpu(
    model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200,
    temperature=0.7
)

# Load embeddings
embeddings = load_embeddings_with_gpu(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

### **enable_gpu.sh**
**Purpose**: Automated GPU driver installation and setup

**Features**:
- ✅ NVIDIA GPU detection
- ✅ Driver installation
- ✅ Module loading setup
- ✅ Persistence daemon configuration
- ✅ System reboot instructions

**Usage**:
```bash
chmod +x GPU/enable_gpu.sh
./GPU/enable_gpu.sh
```

## 🎮 GPU Integration in Projects

### **Using GPU in LangChain Models**

#### **1. Chat Models with GPU**
```python
from GPU.gpu_optimized_models import load_model_with_gpu

# Load GPU-optimized chat model
chat_model = load_model_with_gpu()

# Use in your application
response = chat_model.invoke("What is the capital of Nepal?")
print(response.content)
```

#### **2. Embeddings with GPU**
```python
from GPU.gpu_optimized_models import load_embeddings_with_gpu

# Load GPU-optimized embeddings
embeddings = load_embeddings_with_gpu()

# Use for document similarity
documents = ["Kathmandu is the capital of Nepal."]
query = "What is the capital of Nepal?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)
```

#### **3. Automatic GPU Detection**
```python
from GPU.gpu_config import get_device, print_device_info

# Get current device
device = get_device()
print(f"Using device: {device}")

# Print device information
print_device_info()
```

## 🔍 GPU Status Commands

### **Check GPU Status**
```bash
# Check if NVIDIA GPU is detected
lspci | grep -i nvidia

# Check GPU driver status
nvidia-smi

# Check CUDA availability in Python
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

### **Monitor GPU Usage**
```bash
# Real-time GPU monitoring
watch -n 1 nvidia-smi

# Check GPU memory usage
nvidia-smi --query-gpu=memory.used,memory.total --format=csv
```

## 🚀 Performance Optimization

### **GPU Memory Management**
- **Automatic**: Models automatically use GPU when available
- **Memory Efficient**: Uses `torch.float16` on GPU for memory savings
- **Device Mapping**: Automatic device placement for optimal performance

### **Fallback Strategy**
- **Primary**: GPU with CUDA support
- **Fallback**: CPU when GPU unavailable
- **Automatic**: No code changes needed

### **Optimization Tips**
1. **Use GPU for large models** (>1B parameters)
2. **Use CPU for small models** (<100M parameters)
3. **Monitor memory usage** with `nvidia-smi`
4. **Batch processing** for better GPU utilization

## 🔧 Troubleshooting

### **Common Issues**

#### **1. CUDA Not Available**
```bash
# Check if NVIDIA drivers are installed
nvidia-smi

# If not available, run GPU setup
./GPU/enable_gpu.sh
```

#### **2. Out of Memory**
```bash
# Reduce model size or batch size
# Use smaller models for GPU
# Monitor memory usage
nvidia-smi
```

#### **3. Driver Issues**
```bash
# Reinstall drivers
sudo apt remove nvidia-*
sudo apt install nvidia-driver-535

# Reboot system
sudo reboot
```

## 📚 Documentation

- **[GPU_SETUP.md](GPU_SETUP.md)** - Detailed GPU setup guide
- **[gpu_config.py](gpu_config.py)** - GPU configuration utility
- **[gpu_optimized_models.py](gpu_optimized_models.py)** - GPU-optimized model loading
- **[enable_gpu.sh](enable_gpu.sh)** - GPU driver setup script

## 🎉 Benefits

### **Performance**
- ⚡ **10-50x faster** inference with GPU
- 🧠 **Larger models** can be loaded
- 📊 **Better throughput** for batch processing

### **Ease of Use**
- 🔄 **Automatic detection** of GPU availability
- 🎯 **No code changes** needed
- 📱 **Seamless fallback** to CPU

### **Optimization**
- 💾 **Memory efficient** loading
- 🔧 **Automatic device placement**
- 📈 **Scalable** for different GPU sizes

---

**🚀 Your GPU optimization is now perfectly organized and ready to accelerate your LangChain projects!** 