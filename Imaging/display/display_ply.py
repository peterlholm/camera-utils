from pathlib import Path
import numpy as np
import open3d as o3d



def show(pcd):
    o3d.visualization.draw_geometries([pcd],
                                    window_name="ply", width=800, height=800,
                                    zoom=12.3412,
                                    front=[0.4257, -0.2125, -0.8795],
                                    lookat=[2.6172, 2.0475, 1.532],
                                    up=[-0.0694, -0.9768, 0.2024])

def show_voxel(pcd):
    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    o3d.visualization.draw_geometries([downpcd],
                                    zoom=0.3412,
                                    front=[0.4257, -0.2125, -0.8795],
                                    lookat=[2.6172, 2.0475, 1.532],
                                    up=[-0.0694, -0.9768, 0.2024])

print("Load a ply point cloud, print it, and render it")
TESTDATA = Path("testdata/pointcl-depth.ply")
pcd = o3d.io.read_point_cloud(str(TESTDATA))
#3print(pcd)
#print(np.asarray(pcd.points))

show(pcd)

#show_voxel(pcd)
