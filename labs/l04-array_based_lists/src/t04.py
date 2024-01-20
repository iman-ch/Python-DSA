"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List

# Constants
list1 = List()
list1.append(0)
list1.append(1)
list1.append(2)
list1.append(-1)
list1.append(-2)

print(list1.index(-1))
print(list1.find(-1))

if 2 in list1:
    print("It is in list 1")
else:
    print("It is not in list 1")

print(list1.count(0))
print(list1.min())
print(list1.max())