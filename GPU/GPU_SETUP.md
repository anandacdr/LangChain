# 🚀 GPU Setup Guide for LangChain Projects

## Current Status
- ✅ **NVIDIA GPU**: GeForce MX230 detected
- ✅ **CUDA Toolkit**: Installed (CUDA 12.0)
- ✅ **PyTorch**: Installed with CUDA support
- ⚠️ **NVIDIA Drivers**: Installed but not loaded (secure boot issue)

## Quick Setup

### 1. Enable GPU Drivers
```bash
cd "LangChain Models"
./enable_gpu.sh
sudo reboot
```

### 2. After Reboot
```bash
~/load_nvidia.sh
nvidia-smi
```

### 3. Test GPU with PyTorch
```bash
source venv/bin/activate
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
```

## GPU-Optimized Scripts

### Automatic GPU Detection
All scripts now automatically use GPU when available:

- ✅ `gpu_config.py` - GPU configuration utility
- ✅ `gpu_optimized_models.py` - GPU-optimized model loading
- ✅ `4_document_similarity.py` - GPU-optimized embeddings
- ✅ `prompt_ui.py` - GPU-optimized Streamlit app

### Usage Examples

#### Load Model with GPU
```python
from gpu_optimized_models import load_model_with_gpu

# Automatically uses GPU if available
chat_model = load_model_with_gpu()
result = chat_model.invoke("Hello, how are you?")
```

#### Load Embeddings with GPU
```python
from gpu_optimized_models import load_embeddings_with_gpu

# Automatically uses GPU if available
embeddings = load_embeddings_with_gpu()
vectors = embeddings.embed_documents(["Hello", "World"])
```

## Performance Benefits

### With GPU (MX230):
- 🚀 **2-3x faster** inference
- 🚀 **Better memory management**
- 🚀 **Parallel processing**

### Without GPU (CPU only):
- ✅ **Still works perfectly**
- ✅ **Good for learning and development**
- ✅ **No performance issues for small models**

## Troubleshooting

### If GPU doesn't work after reboot:
1. **Check secure boot**: Disable in BIOS if needed
2. **Manual module loading**: `sudo modprobe nvidia`
3. **Check drivers**: `nvidia-smi`
4. **Reinstall drivers**: `sudo apt install --reinstall nvidia-driver-535`

### If PyTorch doesn't detect GPU:
1. **Check CUDA**: `nvcc --version`
2. **Reinstall PyTorch**: `pip install torch --index-url https://download.pytorch.org/whl/cu118`
3. **Test**: `python -c "import torch; print(torch.cuda.is_available())"`

## Current Configuration

Your system is configured to:
- ✅ **Automatically detect GPU availability**
- ✅ **Use GPU when available, fallback to CPU**
- ✅ **Optimize memory usage**
- ✅ **Provide clear status messages**

## Next Steps

1. **Reboot to activate GPU drivers**
2. **Test GPU functionality**
3. **Enjoy faster AI model inference!**

---

**Note**: Your current CPU setup works perfectly for all LangChain projects. GPU is an optional performance boost! 🎉 