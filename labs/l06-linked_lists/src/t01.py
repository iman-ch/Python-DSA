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

new_list.append(movies[0])

new_list.prepend(movies[1])

new_list.insert(1, movies[2])

for value in new_list:
    print(value)
    


    