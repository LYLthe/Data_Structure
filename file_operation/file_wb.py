"""
use pickle module write data
"""


import pickle
lys = [60, "a string object", 1997]
with open('item.dat', 'wb') as f:
    for item in lys:
        pickle.dump(item, f)
