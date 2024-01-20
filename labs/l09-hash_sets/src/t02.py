"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

hs = Hash_Set(7)

for i in [1, 2, 3, 4]:
    hs.insert(i)
for value in hs:
    print(value)
print()
hs.remove(3)
for value in hs:
    print(value)


