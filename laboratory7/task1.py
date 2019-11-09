from python_helpers import helpers
import re


FILE_NAME = "data.txt"
FLOAT_REGEX_PATTERN = r"[+-]?([0-9]*[.])?[0-9]+"


@helpers.cycled
def main():
    data = []
    with open(FILE_NAME) as file:
        line = file.readline()

        while line:
            line = line.replace("\n", "")
            if bool(re.fullmatch(FLOAT_REGEX_PATTERN, line)):
                data.append(float(line))
            else:
                print("not a number:'{}'".format(line))
                data.append(0)

            line = file.readline()

    negatives = list(filter(lambda v: v < 0, data))
    if len(negatives) != 0:
        print("Avg. negative number:{}".format(sum(negatives) / len(negatives)))
    else:
        print("No negatives numbers in file")

    print("Max number:{}".format(max(data)))

    min_number = 0
    min_number_line = 0
    line = 0
    while line < len(data):
        if data[line] < min_number:
            min_number = data[line]
            min_number_line = line
        line += 1

    print("Min number: {}. On line: {}".format(min_number, min_number_line + 1))

    number_to_find = helpers.input_float("Which number you are looking for?\n")
    if number_to_find in data:
        print("Yes, we have it =)")
    else:
        print("We are sorry, but we don't have this number =(")


if __name__ == "__main__":
    main()
