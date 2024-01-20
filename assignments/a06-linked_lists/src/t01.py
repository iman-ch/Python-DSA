"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants
sep = ("""
-----------------------------------------
""")
queue = Queue()


# is empty
b = queue.is_empty()
print("is_empty test ")
print(b)
print(sep)

# is full
b = queue.is_full()
print("is_full test ")
print(b)
print(sep)

# len
n = len(queue)
print("len test ")
print(n)
print(sep)

# insert
print("insert test ")
for i in [11, 22, 33, 44, 55]:
    queue.insert(i)
for val in queue:
    print(val)
print(sep)

# remove
print("remove test ")
value = queue.remove()
print(value)
print(sep)

# peek
print("peek test ")
value = queue.peek()
print(value)
print(sep)

# move front to rear
target = Queue()
source = Queue()

for i in [11, 22, 33, 44]:
    target.insert(i)
    
for j in [11, 22, 33, 44, 55]:
    source.insert(i)

print("move front to rear test ")
target._move_front_to_rear(source)
print("target values: ")
for val in target:
    print(val)
print("source values: ")
for val in source:
    print(val)
print(sep)

# append queue
print("append queue test ")
target._append_queue(source)
print("target values: ")
for val in target:
    print(val)
print(sep)
    
# combine
source1 = Queue()
source2 = Queue()
target0 = Queue()

for i in [11, 22]:
    source1.insert(i)
    
for j in [33, 44, 55]:
    source2.insert(i)

print("combine test ")
target.combine(source1, source2)
print("target values: ")
for val in target:
    print(val)



