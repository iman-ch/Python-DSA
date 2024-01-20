"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-04-09"
-------------------------------------------------------
"""
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts
a = Deque()
arr = [99, 82, 53, 8, 18, 72]
for i in arr:
    a.insert_rear(i)


Sorts.gnome_sort(a)

for i in a:
    print(i)