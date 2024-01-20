"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
from Queue_array import Queue

source1 = Queue()
source2 = Queue()

# add values to the source queues
for i in range(1, 6):
    source1.insert(i)
for j in range(6, 11):
    source2.insert(j)

# create a target queue and combine the source queues into it
target = Queue()
target.combine(source1, source2)

# print the contents of the target queue
while not target.is_empty():
    print(target.remove())