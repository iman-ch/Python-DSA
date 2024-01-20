"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set
hash_set = Hash_Set(20)

fv = open("gibbon.txt", "r+")
insert_words(fv, hash_set)
fv.close()

total, max_word = comparison_total(hash_set)
print('Using array-based list Hash_Set')
print(f'Total Comparisons: {total:,}')
print(f"Word with maximum comparisons: '{max_word.word}': {max_word.comparisons:,}")
