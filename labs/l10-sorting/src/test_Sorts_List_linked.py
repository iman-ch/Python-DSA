"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-28"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    
    for i in range(SIZE):
        values.append(Number(i))
        
    return values  


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = create_sorted()
    
    values.reverse()
        
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = []
    rows = TESTS
    cols = SIZE
    
    for i in range(rows):
        row = List()
        for j in range(cols):
            val = random.randint(0, XRANGE)
            row.append(Number(val))
        lists.append(row)
    
    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    #In Order
    Number.comparisons = 0
    Sorts.swaps = 0
    values = create_sorted()
    func(values)
    in_order_total = round(Number.comparisons, 0)
    in_order_swaps = round(Sorts.swaps, 0)
    
    #Reverse Order
    Number.comparisons = 0
    Sorts.swaps = 0
    values = create_reversed()
    func(values)
    reverse_total = round(Number.comparisons, 0)
    reverse_swaps = round(Sorts.swaps, 0)
    
    #Random Order
    Number.comparisons = 0
    Sorts.swaps = 0
    array = create_randoms()
    for i in array:
        func(i)
    random_total = int((Number.comparisons) // TESTS)
    random_swaps = int((Sorts.swaps) // TESTS)
    
    print(f'{title:14} {in_order_total:>8} {reverse_total:>8} {random_total:>8} {in_order_swaps:>8} {reverse_swaps:>8} {random_swaps:>8}')
    return