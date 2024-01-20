"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
from Stack_array import Stack

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = []
    target2 = []
    i = 1
    while not source.is_empty():
        if i % 2 != 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        i += 1
    return target1, target2
    
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    stack = Stack()
    reverse_index = len(string) - 1
    index = 0
    
    add = True
    while index < len(string) and reverse_index > 0 and palindrome :
        
        if string[index].isalpha() and add :
            stack.push(string[index].lower())
            
        elif string[reverse_index].isalpha() and add :
            reverse_index += 1
            
        else:
            add = True
        if reverse_index < len(string):
            if string[reverse_index].isalpha() :
                if (not stack.is_empty()):
                    if string[reverse_index].lower() != stack.pop() :
                        palindrome = False
            elif string[index].isalpha() :
                add = False
                index -= 1
                
        reverse_index -= 1
        index += 1
    
# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()
    for e in elements:
        if e not in OPERATORS:
            stack.push(e)
        else:
            top = float(stack.pop())
            second = float(stack.pop())
            if e=="+":
                stack.push(second+top)
            elif e == "-":
                stack.push(second-top)
            elif e =="*":
                stack.push(second*top)
            else:
                stack.push(second/top)
    answer = stack.pop()
    return answer
    
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    try:
        current = "Start"
        choices = maze[current]
        path = []
        if "X" in choices:
            path.append("X")
        stack = Stack()
        while "X" not in choices:
            for c in choices:
                stack.push(c)
            current = stack.pop()
            if maze[current]!=[]:
                path.append(current)          
            choices = maze[current]
            if "X" in choices:
                path.append("X")
    except:     
        path = None
    finally:
        return path
    
    

# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    L = []
    R = []
    pivot = False
    mirror = MIRRORED.NOT_MIRRORED

    for ch in string:
        if ch == m:
            pivot = True
        elif pivot:
            if ch not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
                break
            R.append(ch)
        else:
            if ch not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
                break
            L.append(ch)
    else:
        if not pivot:
            mirror = MIRRORED.NOT_MIRRORED
        elif len(L) > len(R):
            mirror = MIRRORED.TOO_MANY_LEFT
        elif len(R) > len(L):
            mirror = MIRRORED.TOO_MANY_RIGHT
        else:
            while L and R:
                if L.pop() != R.pop():
                    mirror = MIRRORED.MISMATCHED
                    break
            else:
                mirror = MIRRORED.IS_MIRRORED

    return mirror
    