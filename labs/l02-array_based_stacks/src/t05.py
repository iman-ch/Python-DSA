"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
from Movie_utilities import read_movies
from utilities import stack_test

file = open('movies.txt', "r+")

movies = read_movies(file)

file.close()

stack_test(movies)