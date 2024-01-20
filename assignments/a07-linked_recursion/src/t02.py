"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-15"
-------------------------------------------------------
"""
from Movie_utilities import read_movies
from Sorted_List_linked import Sorted_List


file = open("movies.txt", "r+")

movies = read_movies(file)

file.close()

sl = Sorted_List()

for value in movies:
    sl.insert(value)

sl.insert(movies[10])

print("Printing count of each item: ")
print(f"title                                Count")
print(f"---------------------------------   -----")
for value in sl:
    print(f"{value.title:35} {sl.count(value):>5}")

sl.clean()

print("Printing count of each item: ")
print(f"title                                Count")
print(f"---------------------------------   -----")
for value in sl:
    print(f"{value.title:35} {sl.count(value):>5}")

print()
print(f"{movies[-4].title} in sl?: ")
print(movies[-4] in sl)

print()
print(f"Index of {movies[-4].title}: ")
print(sl.index(movies[-4]))

print()
print(f"{movies[-4].title} from sl: ")
print(sl.find(movies[-4]))

print()
print(f"Second item in sl: ")
print(sl[1])

print()
print(f"First item in sl: ")
print(sl.peek())

print()
print(f"Min value in sl: ")
print(sl.min())

print()
print(f"Max value in sl: ")
print(sl.max())

print()
print(f"Remove first value in sl: ")
print(sl.remove_front())

print()
print(f"Remove {movies[-4].title} from sl: ")
print(sl.remove(movies[-4]))

sl2 = Sorted_List()

sl3 = Sorted_List()

for value in range(10):
    sl2.insert(movies[value])

sl3.intersection(sl, sl2)

print()
print("Printing count of each item in sl3: ")
print(f"title                                Count")
print(f"---------------------------------   -----")
for value in sl3:
    print(f"{value.title:35} {sl3.count(value):>5}")

print()
print("sl2 and sl3 are identical?: ")
print(sl2.__eq__(sl3))

sl4 = Sorted_List()

sl4.union(sl2, sl3)

print()
print("Printing count of each item in sl4: ")
print(f"title                                Count")
print(f"---------------------------------   -----")
for value in sl4:
    print(f"{value.title:35} {sl4.count(value):>5}")
