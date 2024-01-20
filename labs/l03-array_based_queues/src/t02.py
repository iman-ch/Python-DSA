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
insert_value = input("Value: ")
queue.insert(insert_value)
print(queue.peek())
value = queue.remove()

print(value)