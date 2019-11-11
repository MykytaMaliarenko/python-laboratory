import re
from python_helpers import helpers


def validate_user_input(inp: str) -> bool:
    return bool(re.match(r"\w+-([0-9]*[.])?[0-9]+$", inp))


def parse_user_input(inp: str) -> (str, float):
    name = inp[:inp.index("-")]
    price_raw = inp[inp.index("-") + 1:]
    return name, float(price_raw)


products = {}


@helpers.cycled
def get_user_input():
    raw_input = helpers.cycled_input("Let's see what you got(product - price):\n", str, validate_user_input)
    name, price = parse_user_input(raw_input)
    if name in products:
        products[name] += price
    else:
        products[name] = price


def main():
    get_user_input()

    unique_products = list(products.keys())
    print("You've bought: \n{}".format(unique_products))

    total_sum = sum(list(products.values()))
    print("Total sum: {}".format(total_sum))


if __name__ == "__main__":
    main()
