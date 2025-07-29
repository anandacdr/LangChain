# 🐍 Virtual Environment Usage Guide

## Current Setup
Your virtual environment is located in the main directory:
```
Generative AI using LangChain/
├── venv/                    # 🎯 Centralized virtual environment
├── LangChain Models/        # Your AI models
├── LangChain Prompts/       # Your prompt projects
└── activate_venv.sh         # Easy activation script
```

## How to Use

### 1. **From Main Directory**
```bash
# Activate virtual environment
source venv/bin/activate

# Or use the convenience script
source activate_venv.sh
```

### 2. **From Any Subdirectory**
```bash
# From LangChain Models/
source ../venv/bin/activate

# From LangChain Prompts/
source ../venv/bin/activate

# Or use the convenience script from anywhere
source ../activate_venv.sh
```

### 3. **Running Scripts**

#### From LangChain Models:
```bash
cd "LangChain Models"
source ../venv/bin/activate
python "1. LLMs/1_LLM_DEMO.py"
```

#### From LangChain Prompts:
```bash
cd "LangChain Prompts"
source ../venv/bin/activate
streamlit run prompt_ui.py
```

#### From Main Directory:
```bash
source venv/bin/activate
python "LangChain Models/1. LLMs/1_LLM_DEMO.py"
python "LangChain Prompts/temperature.py"
```

## Installed Packages

Your virtual environment includes:
- ✅ **langchain** - Core LangChain functionality
- ✅ **langchain-openai** - OpenAI integration
- ✅ **langchain-google-genai** - Google AI integration
- ✅ **langchain-huggingface** - HuggingFace integration
- ✅ **langchain-anthropic** - Anthropic integration
- ✅ **transformers** - HuggingFace transformers
- ✅ **torch** - PyTorch with CUDA support
- ✅ **streamlit** - Web app framework
- ✅ **sentence-transformers** - Embeddings
- ✅ **scikit-learn** - Machine learning utilities
- ✅ **python-dotenv** - Environment variables

## Benefits of Centralized venv

### ✅ **Shared Dependencies**
- All projects use the same packages
- No duplicate installations
- Consistent versions

### ✅ **Easy Management**
- One place to update packages
- Simple activation from anywhere
- Unified environment

### ✅ **Space Efficient**
- Single virtual environment
- Shared package cache
- Reduced disk usage

## Quick Commands

### Check Current Environment
```bash
which python
pip list
```

### Update Packages
```bash
source venv/bin/activate
pip install --upgrade langchain
```

### Add New Package
```bash
source venv/bin/activate
pip install new-package-name
```

### Run GPU Test
```bash
source venv/bin/activate
python GPU/gpu_config.py
```

## Project Structure

```
Generative AI using LangChain/
├── venv/                           # 🎯 Centralized environment
├── activate_venv.sh                # Easy activation
├── VENV_USAGE.md                   # This guide
├── GPU/                            # 🚀 GPU optimization & setup
│   ├── README.md                   # GPU documentation
│   ├── gpu_config.py              # GPU detection & configuration
│   ├── gpu_optimized_models.py    # GPU-optimized model loading
│   ├── enable_gpu.sh              # GPU driver setup script
│   └── GPU_SETUP.md               # Detailed GPU setup guide
├── LangChain Models/
│   ├── 1. LLMs/                   # Language models
│   ├── 2. ChatModels/             # Chat models
│   └── 3. EmbeddedModels/         # Embeddings
└── LangChain Prompts/
    ├── prompt_ui.py               # Streamlit app
    ├── temperature.py             # Temperature examples
    └── chatbot.py                 # Chatbot examples
```

## Tips

1. **Always activate venv first** before running any script
2. **Use relative paths** when activating from subdirectories
3. **Check your environment** with `which python` to ensure you're using the right venv
4. **Update packages regularly** to get the latest features

---

**🎉 Your setup is now perfectly organized with a centralized virtual environment!** 