import random
from python_helpers import helpers


@helpers.cycled
def main():
    n = helpers.cycled_input("input n:", int, lambda v: v > 0)
    arr = []
    i = 0
    while i < n:
        arr.append(helpers.cycled_input("{}:".format(i), float))
        i += 1

    i = 0
    while i < len(arr):
        if arr[i] == 0.0:
            arr = arr[:i] + arr[i+1:]
        else:
            i += 1

    print("res: {}", arr)


if __name__ == "__main__":
    main()
