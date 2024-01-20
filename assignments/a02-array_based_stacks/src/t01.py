"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
from Movie_utilities import get_by_year, read_movies

file = open('movies.txt', "r+")
movies = read_movies(file)
file.close()

year = int(input(f"Year: "))
ymovies = get_by_year(movies, year)

for movie in ymovies:
    print(movie)