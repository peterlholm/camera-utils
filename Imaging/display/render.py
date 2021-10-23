from pathlib import Path
import numpy as np
import open3d as o3d
from matplotlib import pyplot as plt
#from mpl_toolkits import mplot3d

#file = "testdata/Crankshaft_HD.ply"
file = "imaging/display/testdata/image8.ply"
#file = "sync.ply"
#file2 = "testdata/Crankshaft_HD.stl"

def show(pcd):
    o3d.visualization.draw_geometries([pcd],
                                    window_name="ply", width=800, height=800,
                                    front=[0.4257, -0.2125, -0.8795],
                                    lookat=[2.6172, 2.0475, 1.532],
                                    up=[-0.0694, +0.9768, 0.2024],
                                    zoom=22.3412
                                    )

def show2(pcd):
    o3d.visualization.draw_geometries([pcd],
                                    window_name="ply2", width=400, height=400,
                                    front=[-10.0, +0.01020, -25.080],
                                    lookat=[0, 0, 22],
                                    up=[+10.20694, 0, 00], 
                                    zoom=1
                                    )

def show_voxel(pcd):
    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    o3d.visualization.draw_geometries([downpcd],window_name="voxel",
                                    width=800, height=800,
                                    front=[-25.4257, -0.2125, -0.8795],
                                    lookat=[2.6172, 2.0475, 1.532],
                                    up=[-0.0694, -0.9768, 0.2024],
                                    zoom=0.3412,                                   )


def render_image(pcd):
    arr = np.asarray(pcd.points)
    print(arr)
    ax = plt.axes(projection='3d')
    ax.scatter(arr[:,0], arr[:,1], arr[:,2], c = "#222222", s=0.1)

    plt.savefig("my.jpg")
    plt.show()

def pcl2png(infilename, outfilename):
    pcd1 = o3d.io.read_point_cloud(str(infilename))
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible = False) 
    vis.add_geometry(pcd)
    #is.get_render_option().load_from_json("Imaging/display/RenderOption.json")
    ctr = vis.get_view_control()
    ctr.set_zoom(0.4)
    ctr.set_front([-0.084777469999256949, -0.30273583588141922, -0.94929647331784794])
    ctr.set_lookat([0.0,0.0,26.0])
    ctr.set_up([+10.20694, 0, 00])
    #vis.run()
    img = vis.capture_screen_float_buffer(True)
    plt.imshow(np.asarray(img))
    vis.capture_screen_image(str(outfilename), do_render=True)



TESTDATA = Path(file)
pcd1 = o3d.io.read_point_cloud(str(TESTDATA))
#textured_mesh = o3d.io.read_triangle_mesh(str(Path(file2)))
#3print(pcd)
#print(np.asarray(pcd.points))
#show(pcd1)

show2(pcd1)
render_image(pcd1)

# o3d.visualization.capture_screen_image(pcd1,"ud.png", do_render=True)

# o3d.visualization.capture_screen_image(pcd1,"ud2.png", do_render=False)
#show_voxel(pcd1)

#show(textured_mesh)

