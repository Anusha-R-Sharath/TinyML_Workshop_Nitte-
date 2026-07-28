import torch 
import torchvision 
import torchaudio 
print("Torch       :", torch.__version__) 
print("TorchVision :", torchvision.__version__) 
print("TorchAudio  :", torchaudio.__version__) 
print("CUDA Available :", torch.cuda.is_available()) 
x=torch.rand(2,3) 
print("\nTensor Test") 
print(x) 
print("\nDeep Learning Environment Ready!") 