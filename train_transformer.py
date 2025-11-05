import torch

# 检查 CUDA (NVIDIA GPU 的并行计算平台) 是否可用
is_gpu_available = torch.cuda.is_available()

print(f"PyTorch version: {torch.__version__}")
print(f"GPU available: {is_gpu_available}")