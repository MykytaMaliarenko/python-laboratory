"""
Підрахувати кількість додатних серед чисел а, b, с (ввести з клавіатури).
"""

from python_helpers import helpers

a = helpers.input_float("a:\n")
b = helpers.input_float("b:\n")
c = helpers.input_float("c:\n")

numberOfPos = 0

if a > 0:
    numberOfPos += 1

if b > 0:
    numberOfPos += 1

if c > 0:
    numberOfPos += 1

print("numberOfPos: " + str(numberOfPos))
