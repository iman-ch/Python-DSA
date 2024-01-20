"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
from Stack_array import Stack

source = Stack()
for i in range(1, 5):
    source.push(i)
target1, target2 = source.split_alt()

print("Target 1: ", end="")
while len(target1._values) > 0:
    print(target1._values.pop(), end=", ")
    
print("\n")

print("Target 2: ", end="")
while len(target2._values) > 0:
    print(target2._values.pop(), end=", ")