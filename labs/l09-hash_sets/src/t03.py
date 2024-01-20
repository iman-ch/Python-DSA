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
hs.insert(movies[0])
hs.insert(movies[2])
hs.insert(movies[3])
hs.insert(movies[4])


hs.debug()