#!/usr/bin/env python3
"""
Resource Monitor for LangChain Development
Helps prevent Cursor freezes by monitoring system resources
"""

import psutil
import time
import os
import sys

def get_memory_info():
    """Get detailed memory information"""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total / 1024**3,  # GB
        'available': memory.available / 1024**3,  # GB
        'used': memory.used / 1024**3,  # GB
        'percent': memory.percent
    }

def get_cpu_info():
    """Get CPU information"""
    return {
        'usage': psutil.cpu_percent(interval=1),
        'count': psutil.cpu_count()
    }

def get_process_info():
    """Get current process information"""
    process = psutil.Process(os.getpid())
    return {
        'memory_mb': process.memory_info().rss / 1024**2,
        'cpu_percent': process.cpu_percent(),
        'name': process.name()
    }

def check_system_health():
    """Check if system is healthy for AI/ML work"""
    memory = get_memory_info()
    cpu = get_cpu_info()
    process = get_process_info()
    
    print("🖥️  System Health Check")
    print("=" * 50)
    
    # Memory check
    print(f"💾 Memory:")
    print(f"   Total: {memory['total']:.1f} GB")
    print(f"   Available: {memory['available']:.1f} GB")
    print(f"   Used: {memory['used']:.1f} GB ({memory['percent']:.1f}%)")
    
    # CPU check
    print(f"🖥️  CPU:")
    print(f"   Usage: {cpu['usage']:.1f}%")
    print(f"   Cores: {cpu['count']}")
    
    # Process check
    print(f"📊 Current Process ({process['name']}):")
    print(f"   Memory: {process['memory_mb']:.1f} MB")
    print(f"   CPU: {process['cpu_percent']:.1f}%")
    
    # Health warnings
    warnings = []
    if memory['percent'] > 80:
        warnings.append("⚠️  High memory usage (>80%)")
    if memory['available'] < 2:
        warnings.append("⚠️  Low available memory (<2GB)")
    if cpu['usage'] > 90:
        warnings.append("⚠️  High CPU usage (>90%)")
    
    if warnings:
        print("\n🚨 Warnings:")
        for warning in warnings:
            print(f"   {warning}")
    else:
        print("\n✅ System is healthy for AI/ML work!")
    
    return len(warnings) == 0

def monitor_continuously(interval=5):
    """Monitor resources continuously"""
    print(f"🔄 Starting continuous monitoring (every {interval} seconds)")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        while True:
            check_system_health()
            print("-" * 50)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped")

def quick_check():
    """Quick system check"""
    is_healthy = check_system_health()
    if not is_healthy:
        print("\n💡 Recommendations:")
        print("   - Close unnecessary applications")
        print("   - Restart Cursor if it's frozen")
        print("   - Use smaller models for development")
        print("   - Run heavy tasks in terminal")
    return is_healthy

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--monitor":
        monitor_continuously()
    else:
        quick_check() 