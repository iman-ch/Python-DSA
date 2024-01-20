"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Constants

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
     Hash     Slot Key
     -------- ---- --------------------
     1652346    3  Dark City, 1998
      848448    6  Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    slots = 7
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for i in values:
        code = hash(i)
        slot = code % slots
        print(f'{code:8d}{slot:5d}  {i.key()}')
    return
        