"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import find_subs

string = str(input("String: "))
sub = str(input("Sub: "))

locations = find_subs(string, sub)

print(locations)