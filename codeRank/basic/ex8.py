"""
Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
El año es un año bisiesto (tiene 366 días).
El año no es un año bisiesto (tiene 365 días)
"""


def is_leap(year):
    return all([year % 4 == 0,any([year % 100 != 0,year % 400 == 0])])

year = int(input())
print(is_leap(year))