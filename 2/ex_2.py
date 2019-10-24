import helper

n = helper.cycled_input("n:\n", float, lambda v: v != 0)

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
