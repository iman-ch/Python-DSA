"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
#imports
from functions import is_palindrome_stack

#
string = input("Enter a string: ")
palindrome = is_palindrome_stack(string)

print(palindrome)