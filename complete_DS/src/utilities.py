"""
-------------------------------------------------------
Var. utilities
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-21"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # for i in range(len(source)-1, -1, -1):
    # stack.push(source[i])
    # source.pop()
    for i in source[::-1]:
        stack.push(i)
        source.pop()
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """   
    for i in stack:
        target.append(i)
        stack.pop()
    target.reverse()
    return
    

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    print("empty test: ")
    b = s.is_empty() #is_empty
    for i in s: #print stack
        print(i)
    print(b)
    
    s.push(1) #add movie to stack
    s.push(2)
    s.push(3)

    print()
    print("array_to_stack test: ")
    value = s.peek()
    for i in s:
        print(i)
    print(value)
    
    print()
    print("stack_test test: ")
    value = s.pop()
    for i in s:
        print(i)
    print(value)

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        queue.insert(i)
    
    source.clear()
    return
    

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue:
        i = queue.remove()
        target.append(i)
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("empty test: ")
    b = q.is_empty() #is_empty
    print(b)

    print()
    print("insert test: ")
    q.insert(1) 
    q.insert(2)
    q.insert(3)
    print(q._values)
    
    print()
    print("peek test: ")
    value = q.peek()
    print(value)
    
    print()
    print("remove test: ")
    value = q.remove()
    print(value)

    print()
    print("length test: ")
    n = len(q)
    print(n)
    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        pq.insert(i)
    source.clear()
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while pq:
        i = pq.remove()
        target.append(i)
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("empty test: ")
    b = pq.is_empty() #is_empty
    print(b)

    print()
    print("insert test: ")
    pq.insert(2) 
    pq.insert(1)
    pq.insert(3)
    print(pq._values)
    
    print()
    print("peek test: ")
    value = pq.peek()
    print(value)    
    
    print()
    print("remove test: ")
    value = pq.remove()
    print(value)

    print()
    print("length test: ")
    n = len(pq)
    print(n)
    return
    