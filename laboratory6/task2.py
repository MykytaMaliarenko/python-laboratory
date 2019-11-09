from python_helpers import helpers


def print_matrix(matrix: list):
    for row in matrix:
        row_text = ""
        for el in row:
            row_text += str(el) + "  "
        print(row_text)


@helpers.cycled
def main():
    n = helpers.input_int("n=", helpers.natural_only)
    m = helpers.input_int("m=", helpers.natural_only)

    matrix = []
    i = 0
    while i < n:
        num_of_neg = 0
        matrix.append([])
        j = 0
        while j < m:
            el = helpers.cycled_input("({};{})=".format(i, j), float)
            if el < 0:
                num_of_neg += 1
            matrix[i].append(el)
            j += 1

        matrix[i].append(num_of_neg)
        i += 1

    i = 0
    while i < m:
        num_of_neg = 0
        j = 0
        while j < n:
            if matrix[i][j] < 0:
                num_of_neg += 1
            j += 1
        matrix[i].append(num_of_neg)
        i += 1

    print_matrix(matrix)


if __name__ == "__main__":
    main()
