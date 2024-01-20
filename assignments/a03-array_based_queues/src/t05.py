"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
from functions import stack_maze
def main():
    maze = {'Start': ['A'], 'A':['C', 'B'], 
            'B':[], 'C':['D', 'X']}
    path = stack_maze(maze)
    print(path)
main()