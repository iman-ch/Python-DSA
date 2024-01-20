"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
from Queue_array import Queue

# Test equal queues
q1 = Queue()
q1.insert(1)
q1.insert(2)
q1.insert(3)

q2 = Queue()
q2.insert(1)
q2.insert(2)
q2.insert(3)

equals = q1 == q2
print(f"Equal Queues: {equals}")
assert equals