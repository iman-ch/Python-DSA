"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-15"
-------------------------------------------------------
"""
from Movie_utilities import read_movies
from List_linked import List

file = open("movies.txt", "r+")

movies = read_movies(file)

file.close()

lst = List()

for value in movies:
    lst.append(value)

print("Printing the first item: ")
print(lst[0])

lst.prepend(movies[10])

print()
print("Printing first item: ")
print(lst[0])


print()
print("Printing count of each item: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst:
    print(f"{value.title:35} {lst.count(value):>5}")

lst.clean()

print()
print("Printing count of each item: ")
for value in lst:
    print(f"{value.title:35} {lst.count(value):>5}")

lst2 = List()

lst3 = List()

for value in range(10):
    lst2.append(movies[value])

lst3.combine(lst, lst2)

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.title:35} {lst3.count(value):>5}")


for value in range(1, 5):
    lst.append(movies[value])

lst2.intersection(lst, lst3)

print()
print("Printing count of each item in lst2: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst2:
    print(f"{value.title:35} {lst2.count(value):>5}")


print()
print("lst1 and lst2 are identical?: ")
print(lst.is_identical(lst2))

print()
print("Printing the removed value: ")
print(lst.remove_front())


print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.title:35} {lst3.count(value):>5}")


lst3.remove_many(movies[0])

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.title:35} {lst3.count(value):>5}")

target1, target2 = lst3.split()

print()
print("Printing count of each item in target1: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target1:
    print(f"{value.title:35} {target1.count(value):>5}")

print()
print("Printing count of each item in target2: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target2:
    print(f"{value.title:35} {target2.count(value):>5}")

target3, target4 = target1.split_alt()

print()
print("Printing count of each item in target3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target3:
    print(f"{value.title:35} {target3.count(value):>5}")

print()
print("Printing count of each item in target4: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target4:
    print(f"{value.title:35} {target4.count(value):>5}")

lst3.union(target3, target4)

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.title:35} {lst3.count(value):>5}")