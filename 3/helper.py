def cycled_input(text, input_type, valid_cond=None):
    input_type = input_type.__name__

    while True:
        try:
            if input_type == "int":
                user_input = int(input(text))
            elif input_type == "float":
                user_input = float(input(text))
            else:
                user_input = input(text)
        except ValueError:
            print("You entered wrong value. Let's try again.")
            continue

        if valid_cond is not None and valid_cond(user_input) is not True:
            print("input value is not valid.")
        else:
            return user_input
    return
