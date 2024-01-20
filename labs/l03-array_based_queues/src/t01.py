"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-03"
-------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()
value = input("Value: ")
queue.insert(value)

print(len(queue))