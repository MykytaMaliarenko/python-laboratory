from python_helpers import helpers


def right(t: str, i: int):
    if len(t) == i:
        return t
    else:
        return right("." + t, i)


text = helpers.cycled_input("input string:\n", str, lambda v: len(v) > 0)
mod_length = helpers.cycled_input("input modification length:\n", int, lambda v: v >= len(text))

print("Res:\n{}".format(right(text, mod_length)))
