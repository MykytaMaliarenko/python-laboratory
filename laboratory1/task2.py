import helpers

a = helpers.cycled_input("a:\n", float(0), None)
b = helpers.cycled_input("b:\n", float(0), None)
c = helpers.cycled_input("c:\n", float(0), None)

numberOfPos = 0

if a > 0:
    numberOfPos += 1

if b > 0:
    numberOfPos += 1

if c > 0:
    numberOfPos += 1

print("numberOfPos: " + str(numberOfPos))
