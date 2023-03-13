"""
Author: Ibrahim Almakky
Date: 13/02/2022
"""
import yaml
from torchvision import transforms

from PIL import Image

def random_horizontal_flip(params: dict):
    return transforms.RandomHorizontalFlip(**params)


def random_rotation(params: dict):
    return transforms.RandomRotation(**params)


def gaussian_blur(params: dict):
    return transforms.GaussianBlur(**params)


def resize(params: dict):
    return transforms.Resize(**params)

def random_vertical_flip(params: dict):
    return transforms.RandomVerticalFlip(**params)

def random_distortion(params: dict):
    return transforms.RandomPerspective(**params)

def random_affine(params: dict):
    return transforms.RandomAffine(**params)

TRANSFORMS = {
    "horizontal_flip": random_horizontal_flip,
    "random_rotation": random_rotation,
    "gaussian_blur": gaussian_blur,
    "resize": resize,
    "vertical_flip": random_vertical_flip,
    "random_distortion": random_distortion,
    "random_affine": random_affine,
}


def compose(transforms_strs: dict):
    """
    Input images are assumed to be tensors
    """
    transforms_list = []
    # from numpy.ndarray to PIL.Image
    transforms_list.append(transforms.ToPILImage())
    for name, params in transforms_strs.items():
        assert name in TRANSFORMS.keys()
        transforms_list.append(TRANSFORMS[name](params))
        print(name, params)
    transforms_list.append(transforms.ToTensor())
    # add normalization mean is [0.5145, 0.2434, 0.0807], std 0.2870, 0.1415, 0.0531
    # transforms_list.append(transforms.Normalize([0.5145, 0.2434, 0.0807], [0.2870, 0.1415, 0.0531]))
    transforms_composed = transforms.Compose(transforms_list)
    return transforms_composed


if __name__ == "__main__":
    # Test case
    transforms_file = open("/home/hong/hc701/HC701-PROJECT/hc701fed/params/transforms.yaml")
    transforms_params = yaml.load(
        transforms_file,
        Loader=yaml.FullLoader,
    )
    test_transforms = compose(transforms_params["train"])