"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
from functions import queue_combine
from Queue_array import Queue

target = Queue()

# create two source queues
source1 = Queue()
source2 = Queue()

# populate source queues with some data
for i in range(1, 6):
    source1.insert(i)
for j in range(6, 11):
    source2.insert(j)

# combine source queues into a target queue
target = queue_combine(source1, source2)

# print the contents of the target queue
while not target.is_empty():
    print(target.remove())



