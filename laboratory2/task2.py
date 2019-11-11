"""
Скласти програму розкладання натурального числа n на прості множники.
"""

from python_helpers import helpers

n = helpers.input_float("n:\n", lambda v: v != 0)

res = []
if n == 1:
    res = [1]
else:
    x = 2
    while n != 1:
        if n % x == 0:
            res.append(x)
            n //= x
        else:
            x += 1

    if n > 1:
        res.append(int(n))

print(res)
