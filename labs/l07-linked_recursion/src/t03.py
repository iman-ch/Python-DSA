"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-08"
-------------------------------------------------------
"""
from List_linked import List

source = List()

for value in [22, 44, 33, 55, 11]:
    source.append(value)

target1, target2 = source.split_alt_r()

print("Printing Target1: ")
for value in target1:
    print(value)

print()
print("Printing Target2: ")
for value in target2:
    print(value)
