from pathlib import Path
import numpy as np
import open3d as o3d

file = Path("testdata/render0/nnwrap1.npy")
file = Path("testdata/render0/unwrap.npy")


def pic2pcloud(arr):
    list =[]
    for i in range(0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            #print("i,j",i,j)
            val=arr[i,j]
            #print("i,j",i,j, val)
            list.append((i,j,val))
    print(list)
    return list

def list2pcloud(plist):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(plist)
    o3d.io.write_point_cloud("sync.ply", pcd)

arr = np.load(str(file), allow_pickle=True)
piclist = pic2pcloud(arr)

list2pcloud(piclist)
