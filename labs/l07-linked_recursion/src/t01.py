"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-08"
-------------------------------------------------------
"""
from List_linked import List

lst = List()

for value in [22, 44, 33, 55, 11]:
    lst.append(value)

p, c, i = lst._linear_search_r(33)

print(p._value)
print(c._value)
print(i)