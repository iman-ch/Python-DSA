"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
from Movie_utilities import read_movie

line = 'Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8'
movie = read_movie(line)

print(movie)