a = {1, 2, 'ee', 'a', 'd'}
b = {1, 'a', 'c', 'tt', 4, 3}

print(a.difference(b).intersection(a.symmetric_difference(b)))
