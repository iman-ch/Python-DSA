"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
from Movie_utilities import read_movies
from List_linked import List


file_variable = open("movies.txt", "r+")

movies = read_movies(file_variable)

file_variable.close()

new_list = List()

for value in movies:
    new_list.append(value)

print(new_list[5])

new_list[5] = movies[10]

print()
print(new_list[5])