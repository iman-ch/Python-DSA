"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies


fh = open('movies.txt', 'r')
movies = read_movies(fh)
source2 = Sorted_List()



#
source = Sorted_List()
print("Contain Check...")
key = movies[2]
b = key in source

if b == True:
    print("Yes")
else:
    print("No")

print()

#
print("Finding item (__getitem__)...")
i = 2
value = movies[i]
print(value)

print()

#
source1 = Sorted_List()
source1.insert(movies[0])
source1.insert(movies[1])
source1.insert(movies[2])
source1.insert(movies[1])
source1.insert(movies[2])
source1.insert(movies[3])
source1.clean()

print("Cleaning Check...")

for x in source1:
    print(x)
    print("-")
print()

#
target = Sorted_List()
target.insert(movies[5])
target.insert(movies[5])
target.intersection(source1, source2)

print("Intersection check...")

for x in target:
    print(x)
    print("-")
print()

#
target1 = Sorted_List()
n = target1.index(movies[5])
print("Index check...")  # will be unchanged
print(n)
print()

#
b = target.__eq__(target)
print("Equal check...")

if b == True:
    print("True")
else:
    print("False")
print()

#
#value = target.remove_front()
print("Remove Front Check...")

for x in target:
    print(x)
print()

#
target2 = Sorted_List()
target2.insert(movies[1])
target2.insert(movies[2])
target2.insert(movies[1])
key = movies[2]
target2.remove_many(key)

print("Remove Many Check...")

for i in target2:
    print(i)
    print("-")
print()

#
target1, target2 = target.split()
print("Split Check...")
print()
print("Split1")
for x in target1:
    print(x)
    print("-")
print()
print("Split2")
for x in target2:
    print(x)
    print("-")
print()

#
target.insert(movies[1])
target.insert(movies[2])
target.insert(movies[3])
target.insert(movies[4])

target3, target4 = target.split_alt()

print("Alt Split Check...")
print("Split1")
for x in target3:
    print(x)
    print("-")
print()
print("Split2")
for x in target4:
    print(x)
    print("-")
print()

#
source1.insert(movies[7])
# source2 list is currently empty, source 1 had one element
target.union(source1, source2)
print("Union Check...")
for x in target:
    print(x)
    print("-")
print()

#
source3 = Sorted_List()
key = movies[3]
value = source3.find(key)
print("Find Check...")
print(value)
print()

#
key = movies[5]
value = target.count(key)
print("Count Check...")
print(value)
print()

#
value = target.remove(key)
print("Remove Check...")
print(value)
print()

#
value = target.peek()
print("Peek Check...")
print(value)
print()

#
value = target.min()
print("Min Check...")
print(value)
print()

#
value = target.max()
print("Max Check")
print(value)
print()

#
target.insert(movies[0])
target.insert(movies[1])
# split 1
target1, target2 = target.split_key(key)
print("Key Split Check...")
print("Split 1")
for x in target1:
    print(x)
    print("-")
print("Split 2")
for x in target2:
    print(x)
    print("-")
print()
