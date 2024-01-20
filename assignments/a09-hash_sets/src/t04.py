"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
from BST_linked import BST

bst = BST()
for i in [3, 5, 13, 2, 7, 63, 34, 6, 19, 27, 53, 11, 1, 4]:
    bst.insert(i)

zero, one, two = bst.node_counts()
print('bst.node_counts() test...')
print(f'zero: {zero:1d}')
print(f'one: {one:2d}')
print(f'two: {two:2d}')
print()

b = bst.__contains__(7)
print('bst.__contains__(7) test...')
print(b)
print()

p = bst.parent(19)
print('bst.parent(19) test...')
print(p)
print()

pr = bst.parent_r(19)
print('bst.parent_r(19) test...')
print(pr)
print()
    


    