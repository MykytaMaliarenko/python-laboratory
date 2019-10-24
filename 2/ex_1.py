import helper

x = helper.cycled_input("x:\n", float, None)
n = helper.cycled_input("n:\n", int, lambda v: v > 1)

res = 0
for i in range(1, n + 1):
    res += (1 / (x ** 2)) + i

print("res is:", res)
