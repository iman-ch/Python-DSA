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
source = List()
for i in [1, 2, 3, 4]:
    source.append(i)
    
source.reverse_r()
for i in source:
    print(i, end='-')