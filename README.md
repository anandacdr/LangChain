# 🚀 Generative AI using LangChain

A comprehensive collection of LangChain projects with GPU optimization and centralized virtual environment management.

## 📁 Project Structure

```
Generative AI using LangChain/
├── venv/                           # 🎯 Centralized virtual environment
├── activate_venv.sh                # Easy activation script
├── VENV_USAGE.md                   # Virtual environment guide
├── GPU_SETUP.md                    # GPU setup instructions
├── requirements.txt                # All dependencies
├── LangChain Models/
│   ├── 1. LLMs/                   # Language models
│   ├── 2. ChatModels/             # Chat models
│   ├── 3. EmbeddedModels/         # Embeddings
│   ├── gpu_config.py              # GPU utilities
│   └── gpu_optimized_models.py    # GPU-optimized loading
└── LangChain Prompts/
    ├── prompt_ui.py               # Streamlit app
    ├── temperature.py             # Temperature examples
    └── chatbot.py                 # Chatbot examples
```

## 🚀 Quick Start

### 1. **Activate Virtual Environment**
```bash
# From main directory
source venv/bin/activate

# Or use the convenience script
source activate_venv.sh

# From any subdirectory
source ../venv/bin/activate
```

### 2. **Run Examples**

#### From Main Directory:
```bash
# GPU Configuration
python "LangChain Models/gpu_config.py"

# Document Similarity
python "LangChain Models/3. EmbeddedModels/4_document_similarity.py"

# Streamlit App
streamlit run "LangChain Prompts/prompt_ui.py"
```

#### From Subdirectories:
```bash
# From LangChain Models/
cd "LangChain Models"
source ../venv/bin/activate
python "1. LLMs/1_LLM_DEMO.py"

# From LangChain Prompts/
cd "LangChain Prompts"
source ../venv/bin/activate
streamlit run prompt_ui.py
```

## 🎯 Features

### ✅ **Centralized Environment**
- Single virtual environment for all projects
- Easy activation from any directory
- Consistent package versions

### ✅ **GPU Optimization**
- Automatic GPU detection and usage
- CUDA support for PyTorch
- Fallback to CPU when GPU unavailable

### ✅ **Multiple AI Providers**
- **OpenAI** - GPT models
- **Google AI** - Gemini models  
- **HuggingFace** - Local models
- **Anthropic** - Claude models

### ✅ **Ready-to-Use Examples**
- Language Models (LLMs)
- Chat Models
- Embeddings
- Document Similarity
- Streamlit Web Apps

## 📦 Installed Packages

- **langchain** - Core LangChain functionality
- **langchain-openai** - OpenAI integration
- **langchain-google-genai** - Google AI integration
- **langchain-huggingface** - HuggingFace integration
- **langchain-anthropic** - Anthropic integration
- **transformers** - HuggingFace transformers
- **torch** - PyTorch with CUDA support
- **streamlit** - Web app framework
- **sentence-transformers** - Embeddings
- **scikit-learn** - Machine learning utilities
- **python-dotenv** - Environment variables

## 🔧 Setup

### Environment Variables
Create a `.env` file in the main directory:
```bash
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Google AI Configuration
GOOGLE_API_KEY=your_google_api_key_here

# Anthropic Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### GPU Setup (Optional)
```bash
# Run GPU setup script
chmod +x "LangChain Models/enable_gpu.sh"
./"LangChain Models/enable_gpu.sh"

# Reboot system
sudo reboot
```

## 📚 Documentation

- **[VENV_USAGE.md](VENV_USAGE.md)** - Virtual environment usage guide
- **[GPU_SETUP.md](GPU_SETUP.md)** - GPU setup and optimization
- **[LangChain Models/README.md](LangChain%20Models/README.md)** - Models documentation

## 🎉 Benefits

### **Easy Management**
- One place to update packages
- Simple activation from anywhere
- Unified environment

### **Space Efficient**
- Single virtual environment
- Shared package cache
- Reduced disk usage

### **Future-Proof**
- GPU-ready when drivers are installed
- Automatic device detection
- Optimized for both CPU and GPU

---

**🎯 Your LangChain projects are now perfectly organized with centralized management and GPU optimization!** 