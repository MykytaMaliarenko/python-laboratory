from python_helpers import helpers

SEPARATOR = " "


@helpers.cycled
def main():
    text = helpers.cycled_input("Enter text:", str, lambda v: len(v) > 0)
    word_length = helpers.cycled_input("Enter word length:", int, lambda v: v > 0)
    char_to_remove = helpers.cycled_input("Char to remove:", str, lambda v: len(v) == 1)

    words = text.split(SEPARATOR)
    for i in range(0, len(words)):
        if len(words[i]) == word_length:
            words[i] = words[i].replace(char_to_remove, "")

    print("Res:", SEPARATOR.join(words))


if __name__ == "__main__":
    main()
