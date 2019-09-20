import helpers


def input_cond(val):
    return val ** 2 + 4 * val + 5 != 0


x = helpers.cycled_input("x:\n", float(0), input_cond)
if x <= 2:
    print(x ** 2 + 4 * x + 5)
else:
    print(1 / (x ** 2 + 4 * x + 5))
