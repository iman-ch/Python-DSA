"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
from Movie_utilities import get_by_rating, read_movies

file = open('movies.txt', "r+")
movies = read_movies(file)
file.close()

rating = float(input(f"Rating: "))
rmovies = get_by_rating(movies, rating)

for movie in rmovies:
    print(movie)