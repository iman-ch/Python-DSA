"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import file_analyze

file = open('testing.txt', 'r+')
u, l, d, w, r = file_analyze(file)
file.close()

print(f"Uppercase Letters:    {u}")
print(f"Lowercase Letters:    {l}")
print(f"Digits:               {d}")
print(f"Whitespace Characters:{w}")
print(f"Remaining Characters: {r}")