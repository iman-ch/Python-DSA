"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
from functions import postfix
def main():
    string = "4 5.2 + "
    answer = postfix(string)
    print(answer)
main()