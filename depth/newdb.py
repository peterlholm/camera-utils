import numpy as np
from pathlib import Path

FILE = Path("data") / 'NEWbase.npy'

newdb = np.ones((160,160,30))

print (newdb.ndim)
print (newdb.shape)
print (newdb.dtype)

for x in range(0,160):
    for y in range(0,160):
        newdb[x,y] = y/2

print (newdb)

np.save(FILE, newdb)
