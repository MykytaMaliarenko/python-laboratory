import itertools

a = {1, 2, 'ee', 'a', 'd'}
b = {1, 'a', 'c', 'tt', 4, 3}
u = {1, 2, 3, 4, 'a', 'b', 'c', 'd', 'ee', 'tt', 'ww'}

print("union:", a.union(b))
print("intersection:", a.intersection(b))
print("A\\B:", a.difference(b))
print("A\\B:", b.difference(a))
print("A+B:", a.symmetric_difference(b))
print("!A:", u.difference(a))
print("!B:", u.difference(b))
print("AxB:", list(itertools.product(a, b)))
print("BxA:", list(itertools.product(b, a)))

print(a.difference(b).intersection(a.symmetric_difference(b)))
