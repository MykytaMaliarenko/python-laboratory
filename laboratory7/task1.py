from python_helpers import helpers
import re
import os


FLOAT_REGEX_PATTERN = r"[+-]?([0-9]*[.])?[0-9]+"


def input_file(file_name: str):
    with open(file_name, "x") as file:
        choice = "y"
        while choice == "y":
            user_input = helpers.input_string("Value: ")
            choice = helpers.input_string("Do you want to continue?(y/n)", lambda v: v == "y" or v == "n")
            if choice == "y":
                file.write(user_input + "\n")
            else:
                file.write(user_input)
        file.close()


@helpers.cycled
def main():
    file_name = helpers.input_string("File Name: ")
    if not os.path.isfile(file_name):
        choice = helpers.input_string("File not found. Do you want to create it?(y/n)", lambda v: v == "y" or v == "n")
        if choice == "n":
            print("see you.")
            return
        else:
            input_file(file_name)

    number_to_find = helpers.input_float("Which number you are looking for?\n")
    is_found = False

    min_number = 0
    min_number_line = 0
    line_num = 0

    negatives_sum = 0
    num_of_negatives = 0
    max_number = 0
    with open(file_name) as file:
        line = file.readline()

        while line:
            line = line.replace("\n", "")
            if bool(re.fullmatch(FLOAT_REGEX_PATTERN, line)):
                v = float(line)
                if v < min_number:
                    min_number = v
                    min_number_line = line_num

                if v < 0:
                    negatives_sum += v
                    num_of_negatives += 1

                if v > max_number:
                    max_number = v

                if number_to_find == v:
                    is_found = True

            line = file.readline()
            line_num += 1

    if is_found:
        print("Number is found =)")
    else:
        print("Number isn't found =(")

    if num_of_negatives != 0:
        print("Avg. negative number:{}".format(negatives_sum / num_of_negatives))
    else:
        print("No negatives numbers in file")

    print("Max number:{}".format(max_number))

    print("Min number: {}. On line: {}".format(min_number, min_number_line + 1))


if __name__ == "__main__":
    main()
