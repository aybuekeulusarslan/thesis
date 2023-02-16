import torch
from torchvision import datasets

def getData(path=None):
    if not path: path = "C:/Users/Aybüke/PycharmProjects/testBerkin"
    data_set: datasets = datasets.MNIST(root=path,
                                    train=False,
                                    download=True,
                                    transform=None)

    data_set.classes
    data_set.targets

    labels: list = data_set.targets.tolist()

    return labels