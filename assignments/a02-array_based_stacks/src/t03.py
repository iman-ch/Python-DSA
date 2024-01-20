"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genre, read_movies

file = open('movies.txt', "r+")
movies = read_movies(file)
file.close()

genre = int(input(f"Genre number: "))
gmovies = get_by_genre(movies, genre)

for movie in gmovies:
    print(movie)