import re

PATTERNS = {
    int: r"^[-+]?[0-9]+$",
    float: r"[+-]?([0-9]*[.])?[0-9]+",
    str: r".+",
}


def cycled_input(text: str, input_type=str, valid_cond=None):
    if input_type in PATTERNS:
        while True:
            user_input = input(text)
            if bool(re.fullmatch(PATTERNS[input_type], user_input)):
                if (valid_cond is not None and valid_cond(input_type(user_input)) is True) or valid_cond is None:
                    return input_type(user_input)
                else:
                    print("input value is not valid.")
            else:
                print("You entered wrong value. Let's try again.")
    else:
        return None