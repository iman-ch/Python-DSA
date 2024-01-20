"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-15"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import DATA1, fill_letter_bst, encode_morse


bst = BST()

fill_letter_bst(bst, DATA1)

text = input("Enter a String: ")

print(encode_morse(bst, text))