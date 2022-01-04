import numpy as np
from pathlib import Path

FILE = Path("data") / 'DDbase.npy'

db = np.load(FILE)

print (db.ndim)
print (db.shape)
print (db.dtype)
print (db)
