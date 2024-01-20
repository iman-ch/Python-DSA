"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import matrix_transpose

a = [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]
b = matrix_transpose(a)

print(f'Matrix: {a} ')
print(f'Transposed Matrix: {b}')