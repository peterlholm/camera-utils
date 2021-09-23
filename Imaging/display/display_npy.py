from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#import open3d as o3d

file = Path("testdata/render0/nnwrap1.npy")
file = Path("testdata/render0/unwrap.npy")

def npy_info(file):
    img_array = np.load(str(file), allow_pickle=True)
    print("shape", img_array.shape)
    print("dtype", img_array.dtype)

def show_plotlib(file):
    print("Load a ply point cloud, print it, and render it")

    img_array = np.load(str(file), allow_pickle=True)
    plt.imshow(img_array, cmap='gray')
    plt.show()

def show_pil(file):
    img_array = np.load(str(file), allow_pickle=True)
    im = Image.fromarray(img_array)
    # this might fail if `img_array` contains a data type that is not supported by PIL,
    # in which case you could try casting it to a different dtype e.g.:
    # im = Image.fromarray(img_array.astype(np.uint8))

    im.show()

npy_info(file)

#show_plotlib(file)

#show_pil(file)
