"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import shift
n = 1

file = open('pelee.txt', 'r')
new_file = open('shift.txt', 'w')

string = file.read().rstrip()
estring = shift(string, n)
new_file.write(estring)

file.close()
new_file.close()
