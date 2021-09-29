import sys
import open3d as o3d

def mirror(pcloud):
    # mirror x axis
    for p in pcloud.points:
        p[0]= -p[0]
    return pcloud

if __name__ == "__main__":
    infile = sys.argv[1]
    print (infile)
    outfile = sys.argv[2]
    pcd = o3d.io.read_point_cloud(str(infile))
    outpcd = mirror(pcd)
    o3d.io.write_point_cloud(outfile, outpcd)
