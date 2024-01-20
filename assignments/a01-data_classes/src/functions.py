"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_list = []
    index = 0
    while index < len(values):
        if values[index] not in temp_list:
            temp_list.append(values[index])
        else:
            values.pop(index)
            index -= 1
        index += 1
    return
    
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u, l, d, w, r = 0, 0, 0, 0, 0
    
    for line in fv:
        for character in line:
            if character.isspace():
                w += 1
            elif character.isupper():
                u += 1
            elif character.islower():
                l += 1
            elif character.isdigit():
                d += 1
            else:
                r += 1
                
    return u, l, d, w, r

def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    i = 0
    while i < len(string):
        i = string.find(sub, i)
        if i == -1:
            break
        else:
            locations.append(i)
            i += len(sub)
    return locations
    

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap_year = True
        
    else:
        leap_year = False
    return leap_year

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    for letter in name:
        if (not letter.isalpha() and not letter.isdigit() and letter != "_" ):
            valid = False
        elif name[0].isdigit():
            valid = False
        else:
            valid = True
    return valid

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    
    for index_list1 in range(len(a[0])):
        temp_list = []
        for index_main_list in range(len(a)):
            temp_list.append(a[index_main_list][index_list1])
        b.append(temp_list)
    return b

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    for i in a:
        
        c += [a[i - 1] * b[i - 1]] 
    return c

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', '0', 'U']
    pl = ""
    if word[0].lower() in VOWELS:
        pl = word + 'way'
    else:
        capital = False
        index = 0
        not_done = True
        temp_word = ""
        if word[0].isupper():
            capital = True
        while index < len(word) and not_done:
            if word[index] in VOWELS:
                not_done = False
            else:
                temp_word += word[index].lower()
                index += 1
        pl = word[index:] + temp_word + 'ay'
        if capital:
            pl = pl.capitalize()
    return pl

def shift(string, n): 
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            estring += chr((ord(char) + n - 65) % 26 + 65)
        else:
            estring += chr((ord(char) + n - 97) % 26 + 97)
    return estring.upper()
    







    