import random
import string
import time
from python_helpers import helpers


MAX_SEQ_LENGTH = 20
MAX_STR_LENGTH = 20


def generate_random_data(length=20):
    res = []
    while length > 0:
        res.append(generate_random_sequence(random.randint(2, MAX_SEQ_LENGTH)))
        length -= 1
    return res


def generate_random_sequence(length):
    seq = []
    while length > 0:
        seq.append(generate_random_string(random.randint(2, MAX_STR_LENGTH)))
        length -= 1
    return seq


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def first_version(lst: list) -> list:
    res = []
    for word in lst:
        for letter in word:
            res.append(letter)
    return res


def second_version(lst: list) -> list:
    res = []
    list(map(lambda v: list(map(lambda t: res.append(t), v)), lst))
    return res


def third_version(lst: list) -> list:
    res = []
    i = 0
    while i < len(lst):
        j = 0
        word = lst[i]
        while j < len(word):
            res.append(word[j])
            j += 1
        i += 1
    return res


def fourth_version(lst: list) -> list:
    res = []
    i = 0
    while i < len(lst):
        j = 0
        for letter in lst[j]:
            res.append(letter)
        i += 1
    return res


funcs = {
    "for": first_version,
    "reduce, map, lambda": second_version,
    "while": third_version,
    "while & for": fourth_version,
}


@helpers.cycled
def main():
    total_time = {}
    data = generate_random_data(1000)

    for k, v in funcs.items():
        if k not in total_time:
            total_time[k] = 0

        for t in data:
            millis = int(round(time.time() * 1000))
            v(t)
            total_time[k] += int(round(time.time() * 1000)) - millis

    print(total_time)


if __name__ == '__main__':
    main()
