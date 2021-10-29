"Display depth"
#from pathlib import Path
import numpy as np
#import open3d as o3d
from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d

file = "depth/DDbase.npy"

db = np.load(file)

print("dtype", db.dtype)
print("shape", db.shape)
print("ndim", db.ndim)
#print(db)

xd = []
yd = []
zd = []
for x in range(0,160):
    for y in range (0,160):
        xd.append(x)
        yd.append(y)
        zd.append(db[x][y][1])

#print(xd)
#print(yd)
#print(zd)

# setting a custom style to use
style.use('ggplot')

# create a new figure for plotting
fig = plt.figure()

# create a new subplot on our figure
# and set projection as 3d
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

# defining x, y, z co-ordinate



ax1.scatter(xd, yd, zd, color = 'r', marker = 'o')

xd = []
yd = []
zd = []
for x in range(0,160):
    for y in range (0,160):
        xd.append(x)
        yd.append(y)
        zd.append(db[x][y][100])

ax1.scatter(xd, yd, zd, c = 'b', marker = 'o')

xd = []
yd = []
zd = []
for x in range(0,160):
    for y in range (0,160):
        xd.append(x)
        yd.append(y)
        zd.append(db[x][y][200])

ax1.scatter(xd, yd, zd, c = 'g', marker = 'o')
xd = []
yd = []
zd = []
for x in range(0,160):
    for y in range (0,160):
        xd.append(x)
        yd.append(y)
        zd.append(db[x][y][299])

ax1.scatter(xd, yd, zd, c = 'c', marker = 'o')
plt.show()
