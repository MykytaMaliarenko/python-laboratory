from python_helpers import helpers
import re


FILE_NAME = "data.txt"
FLOAT_REGEX_PATTERN = r"[+-]?([0-9]*[.])?[0-9]+"


@helpers.cycled
def main():
    number_to_find = helpers.input_float("Which number you are looking for?\n")
    is_found = False

    min_number = 0
    min_number_line = 0
    line_num = 0

    negatives_sum = 0
    num_of_negatives = 0
    max_number = 0
    with open(FILE_NAME) as file:
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

    if num_of_negatives != 0:
        print("Avg. negative number:{}".format(negatives_sum / num_of_negatives))
    else:
        print("No negatives numbers in file")

    print("Max number:{}".format(max_number))

    print("Min number: {}. On line: {}".format(min_number, min_number_line + 1))

    if is_found:
        print("Yes, we have it =)")
    else:
        print("We are sorry, but we don't have this number =(")


if __name__ == "__main__":
    main()
