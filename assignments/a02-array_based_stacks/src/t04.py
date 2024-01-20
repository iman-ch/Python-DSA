"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genres, read_movies

file = open('movies.txt', 'r')

movies = read_movies(file)

genres = []

user_input = int(input("Enter a genre code (-1 TO QUIT): "))
while user_input != -1:
    genres.append(user_input)
    user_input = int(input("Enter a genre code (-1 TO QUIT): "))

gmovies = get_by_genres(movies, genres)

for movie in gmovies:
    print("===========================================")
    print(movie)