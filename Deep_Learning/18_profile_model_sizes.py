"""
===========================================================
18_profile_model_sizes.py

Measure the storage size of the trained models.

Author : Dr. C Sivananda Reddy
===========================================================
"""

from pathlib import Path
import os


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "MODELS"
ONNX_DIR = PROJECT_ROOT / "ONNX"

PYTORCH_MODEL = MODEL_DIR / "mlp_model.pth"
#ONNX_FP32_MODEL = ONNX_DIR / "mlp_model.onnx"


# ==========================================================
# Helper Function
# ==========================================================

def get_file_size(file_path):
    """
    Returns:
        size_bytes
        size_kb
        size_mb
    """

    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024

    return size_bytes, size_kb, size_mb


# ==========================================================
# Display Function
# ==========================================================

def print_model_size(title, file_path):

    print("=" * 60)
    print(title)
    print("=" * 60)

    print(f"File : {file_path.name}")

    size_bytes, size_kb, size_mb = get_file_size(file_path)

    print(f"\nSize : {size_bytes:,} Bytes")
    print(f"       {size_kb:.2f} KB")
    print(f"       {size_mb:.4f} MB")

    return size_bytes


# ==========================================================
# Main
# ==========================================================

print("\n")
print("=" * 60)
print("Model Storage Profiling")
print("=" * 60)

pytorch_size = print_model_size(
    "PyTorch FP32 Model",
    PYTORCH_MODEL
)

#onnx_fp32_size = print_model_size(
 #   "ONNX FP32 Model",
  #  ONNX_FP32_MODEL
#)


# ==========================================================
# Compression Statistics
# ==========================================================

#print(f"PYTORCH FP32 Size : {pytorch_size:,} Bytes")
#print(f"ONNX FP32 Size : {onnx_fp32_size:,} Bytes")

#print("=" * 60)