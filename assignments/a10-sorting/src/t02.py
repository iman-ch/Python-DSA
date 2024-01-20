"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-04-09"
-------------------------------------------------------
"""
from List_linked import List
from Sorts_List_linked import Sorts
a = List()
arr = [99, 82, 53, 8, 18, 72]
for i in arr:
    a.append(i)
    
Sorts.radix_sort(a)

for i in a:
    print(i)

