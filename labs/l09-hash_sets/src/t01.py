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
from functions import hash_table

fh = open('movies.txt', 'r+')
movies = read_movies(fh)


m1 = movies[1]
m2 = movies[2]
m3 = movies[3]
m4 = movies[4]

hash_table(7, [m1, m2, m3, m4])