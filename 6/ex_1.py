import random
from python_helpers import helpers

n = helpers.cycled_input("input n:", int, lambda v: v > 0)
arr = []
i = 0
while i < n:
    arr.append(helpers.cycled_input("{}:".format(i), float))
    i += 1

