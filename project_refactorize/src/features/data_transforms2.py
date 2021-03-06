# library import
import torchvision as vision
from Cutout import Cutout
import sys

# module import
sys.path.append('/home/shared/sykim/lab_kaggle_practice1/project_refactorize/src/features/')
from policy_list.CIFAR10 import CIFAR10Policy

# main code
image_size = 224 
target_size = (image_size, image_size)

data_transforms_2 = {
    'train': vision.transforms.Compose([
        vision.transforms.Resize(target_size),
        vision.transforms.RandomHorizontalFlip(),
        vision.transforms.RandomRotation(20),
        CIFAR10Policy(),
        vision.transforms.ToTensor(),
        Cutout(n_holes=1, length=image_size//4),
        vision.transforms.Normalize(
            [0.485, 0.456, 0.406], 
            [0.229, 0.224, 0.225])
    ]),
    'valid': vision.transforms.Compose([
        vision.transforms.Resize(target_size),
        vision.transforms.RandomResizedCrop(target_size, scale=(0.8,1.0)),
        vision.transforms.RandomHorizontalFlip(),
        vision.transforms.ToTensor(),
        vision.transforms.Normalize(
            [0.485, 0.456, 0.406], 
            [0.229, 0.224, 0.225])
    ]),
    'test': vision.transforms.Compose([
        vision.transforms.Resize(target_size),
        vision.transforms.RandomResizedCrop(target_size, scale=(0.8,1.0)),
        vision.transforms.ToTensor(),
        vision.transforms.Normalize(
            [0.485, 0.456, 0.406], 
            [0.229, 0.224, 0.225])
    ]),
    'tta': vision.transforms.Compose([
        vision.transforms.Resize(target_size),
        vision.transforms.RandomHorizontalFlip(),
        vision.transforms.RandomRotation(20),
        CIFAR10Policy(),
        vision.transforms.ToTensor(),
        vision.transforms.Normalize(
            [0.485, 0.456, 0.406], 
            [0.229, 0.224, 0.225])
    ]),
}