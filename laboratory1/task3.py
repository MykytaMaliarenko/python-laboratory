"""
Обчислення конкретної функції, в залежності від введеного значення х
"""

from python_helpers import helpers


x = helpers.input_float("x:", lambda val: val ** 2 + 4 * val + 5 != 0)
if x <= 2:
    print(x ** 2 + 4 * x + 5)
else:
    print(1 / (x ** 2 + 4 * x + 5))
