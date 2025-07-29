#!/usr/bin/env python3
"""
GPU Configuration Utility for LangChain Projects
Automatically detects and configures GPU usage
"""

import torch
import os

def setup_gpu():
    """Setup GPU configuration for optimal performance"""
    
    print("🔍 Checking GPU availability...")
    
    # Check if CUDA is available
    if torch.cuda.is_available():
        print(f"✅ CUDA is available!")
        print(f"🎮 GPU Device: {torch.cuda.get_device_name(0)}")
        print(f"💾 GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
        
        # Set default device to GPU
        device = torch.device("cuda:0")
        torch.cuda.set_device(device)
        
        # Set environment variables for better GPU performance
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        
        print("🚀 GPU configured for optimal performance!")
        return device
        
    else:
        print("⚠️  CUDA not available, using CPU")
        print("💡 To enable GPU: Install NVIDIA drivers and reboot")
        device = torch.device("cpu")
        return device

def get_device():
    """Get the current device (GPU or CPU)"""
    return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def print_device_info():
    """Print current device information"""
    device = get_device()
    print(f"📍 Current device: {device}")
    
    if device.type == "cuda":
        print(f"🎮 GPU: {torch.cuda.get_device_name(0)}")
        print(f"💾 Memory: {torch.cuda.memory_allocated(0) / 1024**2:.1f} MB allocated")
        print(f"💾 Memory: {torch.cuda.memory_reserved(0) / 1024**2:.1f} MB reserved")

if __name__ == "__main__":
    device = setup_gpu()
    print_device_info() 