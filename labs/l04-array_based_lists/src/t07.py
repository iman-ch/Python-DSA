"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from utilities import list_test

# Constants
file = open("movies.txt", "r+")
source = read_movies(file)

file.close()
list_test(source)