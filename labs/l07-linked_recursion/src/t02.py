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
lst = List()
other = List()
for i in [1, 2, 3, 4]:
    lst.append(i)
    other.append(i)
    
    
b = lst.is_identical_r(other)
print(b)
