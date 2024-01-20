"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from Hash_Set_array import Hash_Set

fh = open('movies.txt', 'r+')
movies = read_movies(fh)

hs = Hash_Set(7)
i = 0
while i < 7:
    hs.insert(movies[i])
    i+=1
hs.debug()

print()
print("REHASHED SET...")
i += 1
hs.insert(movies[i])
hs._rehash()
hs.debug()
