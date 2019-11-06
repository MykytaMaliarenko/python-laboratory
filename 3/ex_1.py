from python_helpers import helpers

CHARS_TO_REMOVE = ["a", "а"]
SEPARATOR = " "


@helpers.cycled
def main():
    text = helpers.cycled_input("Enter text:\n", str, lambda v: len(v) > 0)
    word_length = helpers.cycled_input("Enter word length:\n", int, lambda v: v > 0)

    words = text.split(SEPARATOR)
    for i in range(0, len(words)):
        if len(words[i]) == word_length:
            for char in CHARS_TO_REMOVE:
                words[i] = words[i].replace(char, "")

    print("Res:\n", SEPARATOR.join(words))


if __name__ == "__main__":
    main()
