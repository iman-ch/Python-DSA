"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import clean_list

string_values = input('Enter values (separated by a comma): ').split(',')
values = []

for i in string_values:
    values.append(int(i))

clean_list(values)

print(f'Cleaned List: {values}')