import sys
import open3d as o3d
import numpy as np

def mirror(pcloud):
    # mirror x axis
    for p in pcloud.points:
        p[0]= -p[0]
    return pcloud

def mirror_pcl(infile, outfile):
    pcd = o3d.io.read_point_cloud(str(infile))
    arr = np.asarray(pcd.points)
    print('xyz_load', arr)
    for p in arr:
        p[0] = -p[0]
    print('xyz_load', arr)
    opcd = o3d.geometry.PointCloud()
    opcd.points = o3d.utility.Vector3dVector(arr)
    o3d.io.write_point_cloud(outfile, opcd)



if __name__ == "__main__":
    #infile = sys.argv[1]
    infile = 'imaging/display/testdata/image8.ply'
    print (infile)
    #outfile = sys.argv[2]
    outfile = "ud.ply"
    mirror_pcl(infile,outfile)
    # pcd = o3d.io.read_point_cloud(str(infile))
    # outpcd = mirror(pcd)
    # o3d.io.write_point_cloud(outfile, outpcd)
    # o3d.io.write_point_cloud("test.ply", outpcd, write_ascii=True)
