"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
from BST_linked import BST

#balanced, valid
bst = BST()

for value in [3, 1, 5, 0, 2, 4, 6]:
    bst.insert(value)

print("Is the BST valid?: ")
print(bst.is_valid())

print()
print("Is the BST balanced?: ")
print(bst.is_balanced())


#eq, min, counts, order, remove
bst2 = BST()

for value in [11, 22, 33, 44]:
    bst2.insert(value)

print()
print("Are the BSTs equal?: ")
print(bst.__eq__(bst2))

print()
print("Minimum value in BST: ")
print(bst.min())

print()
print("Number of nodes with 0 children: ")
print(bst.leaf_count())

print()
print("Number of nodes with 1 child: ")
print(bst.one_child_count())

print()
print("Number of nodes with 2 children: ")
print(bst.two_child_count())

print()
print("Values in order from bst: ")
print(bst.inorder())

print()
print("Values in preorder from bst: ")
print(bst.preorder())

print()
print("Values in postorder from bst: ")
print(bst.postorder())

print()
print("Values in levelorder from bst: ")
print(bst.levelorder())

print()
print("Removed Value: ")
print(bst.remove(3))

print()
print("Printing Updated BST: ")
for value in bst:
    print(value)