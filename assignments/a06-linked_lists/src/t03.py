"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
from Deque_linked import Deque

queue = Deque()

print("Queue is empty: ")
print(queue.is_empty())

queue.insert_front(11)

queue.insert_rear(22)

print()
print("Length of queue: ")
print(len(queue))

print()
print("Value at Front: ")
print(queue.peek_front())

print()
print("Value at Rear: ")
print(queue.peek_rear())

print()
print("Value Removed: ")
print(queue.remove_front())

print()
print("Value Removed: ")
print(queue.remove_rear())

queue.insert_front(11)

queue.insert_rear(22)

queue.insert_rear(33)

queue.insert_rear(44)

queue._swap(queue._rear, queue._front)

print()
print("Values in queue: ")
for value in queue:
    print(value)