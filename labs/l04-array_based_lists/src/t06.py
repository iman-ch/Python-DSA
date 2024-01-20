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
from utilities import array_to_list, list_to_array

# Constants
llist = List()
source = [1, 2, 3, 4, 5]

array_to_list(llist, source)

print("LList: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("List: ")
for value in source:
    print(value)