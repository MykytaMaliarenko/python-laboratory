from python_helpers import helpers


class MyList(list):

    def recursive_array_input(self, n: int):
        self.append(helpers.cycled_input("{}:".format(len(self)), float))
        if n != 1:
            self.recursive_array_input(n - 1)

    def remove_all_zero_elements(self, i: int = 0):
        if i != len(self):
            if self[i] == 0:
                self.pop(i)
            else:
                i += 1
            self.remove_all_zero_elements(i)


@helpers.cycled
def main():
    n = helpers.cycled_input("input n:", int, lambda v: v > 0)
    arr = MyList()
    arr.recursive_array_input(n)
    arr.remove_all_zero_elements()
    print("res: {}", arr)


if __name__ == "__main__":
    main()
