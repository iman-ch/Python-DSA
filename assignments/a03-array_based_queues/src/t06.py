"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
from functions import is_mirror_stack
def main():
    string = "cmc"
    valid_chars = "abc"
    m = "m"
    mirror = is_mirror_stack(string, valid_chars, m)
    print(mirror)
main()