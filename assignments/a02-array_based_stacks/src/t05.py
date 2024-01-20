"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
from Movie_utilities import genre_counts, read_movies

file = open('movies.txt', 'r+')
movies = read_movies(file)
counts = genre_counts(movies)

print("Counts: {}".format(counts))