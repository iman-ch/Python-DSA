"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-08"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants
# Constants
source1 = List()
source2 = List()
for i in [1, 2, 3, 4]:
    source1.append(i)
for j in [4, 5, 6, 7]:
    source2.append(j)

target = List()   
target.intersection_r(source1, source2)

for k in target:
    print(k, end='-')