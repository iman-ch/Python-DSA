"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-26"
-------------------------------------------------------
"""
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('gibbon.txt', 'r+')

do_comparisons(file, bst)

file.close()

letter_table(bst)