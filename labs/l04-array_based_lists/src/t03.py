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
list1.append(100)
print(len(list1))

list1.insert(0, 200)
print(len(list1))

remove = list1.remove(200)
print(remove)