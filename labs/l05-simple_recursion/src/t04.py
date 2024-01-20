"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
from functions import to_power

base = float(input("Enter the base value: "))

power = int(input("Enter the power: "))

ans = to_power(base, power)

print(ans)