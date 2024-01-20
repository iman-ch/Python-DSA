"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
#imports
from Letter import Letter
from BST_linked import BST
from functions import do_comparisons, comparison_total

#constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

#initialize bst
bst1 = BST()
bst2 = BST()
bst3 = BST()

#insert constants into bsts
for i in DATA1:
    l = Letter(i)
    bst1.insert(l)

for i in DATA2:
    l = Letter(i)
    bst2.insert(l)

for i in DATA3:
    l = Letter(i)
    bst3.insert(l)

#print bsts
#for v in bst1:
#    print(v, end=" ")
#print()
#for v in bst2:
#    print(v, end=" ")
#print()
#for v in bst3:
#    print(v, end=" ")
#print()

#bst1
file = open("gibbon.txt", "r+")
do_comparisons(file, bst1)
total = comparison_total(bst1)
file.close()
print("Comparing by order: ", DATA1)
print(f"Total comparisons: {total:,}")
print("----------------------------")

#bst2
file = open("gibbon.txt", "r+")
do_comparisons(file, bst2)
total = comparison_total(bst2)
file.close()
print("Comparing by order: ", DATA2)
print(f"Total comparisons: {total:,}")
print("----------------------------")

#bst3
file = open("gibbon.txt", "r+")
do_comparisons(file, bst3)
total = comparison_total(bst3)
file.close()
print("Comparing by order: ", DATA3)
print(f"Total comparisons: {total:,}")