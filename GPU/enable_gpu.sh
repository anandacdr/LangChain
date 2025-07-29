#!/bin/bash

echo "🚀 Enabling NVIDIA GPU Drivers..."

# Check if NVIDIA GPU is detected
if lspci | grep -i nvidia > /dev/null; then
    echo "✅ NVIDIA GPU detected"
else
    echo "❌ No NVIDIA GPU found"
    exit 1
fi

# Install NVIDIA drivers if not already installed
echo "📦 Installing NVIDIA drivers..."
sudo apt update
sudo apt install nvidia-driver-535 nvidia-utils-535 -y

# Update initramfs
echo "🔄 Updating initramfs..."
sudo update-initramfs -u

# Create a script to load NVIDIA modules
echo "📝 Creating NVIDIA module loading script..."
cat > ~/load_nvidia.sh << 'EOF'
#!/bin/bash
# Load NVIDIA modules
sudo modprobe nvidia
sudo modprobe nvidia-drm
sudo modprobe nvidia-uvm

# Check if modules loaded successfully
if lsmod | grep nvidia > /dev/null; then
    echo "✅ NVIDIA modules loaded successfully"
    nvidia-smi
else
    echo "❌ Failed to load NVIDIA modules"
fi
EOF

chmod +x ~/load_nvidia.sh

echo "🔧 Setting up NVIDIA persistence daemon..."
sudo systemctl enable nvidia-persistenced
sudo systemctl start nvidia-persistenced

echo "📋 Next steps:"
echo "1. Reboot your system: sudo reboot"
echo "2. After reboot, run: ~/load_nvidia.sh"
echo "3. Test GPU: nvidia-smi"
echo "4. Test PyTorch: python -c 'import torch; print(torch.cuda.is_available())'"

echo "🎉 GPU setup complete! Reboot to activate NVIDIA drivers." 