from python_helpers import helpers

x = helpers.input_float("x")
n = helpers.input_int("n:\n", lambda v: v > 1)

res = 0
for i in range(1, n + 1):
    res += (1 / (x ** 2)) + i

print("res is:", res)
