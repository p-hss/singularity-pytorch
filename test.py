import torch
import xarray
import torchvision

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
print(torchvision.__version__)

