"""
Видалити всі символи 'а' зі слів, довжина яких дорівнює обраної.
"""

"""
Видалити будь-які символи зі груп символів, розбитих за SEPARATOR, довжина яких дорівнює обраної.
"""

from python_helpers import helpers

SEPARATOR = " "
CHARS_TO_REMOVE = ["a"]


@helpers.cycled
def main():
    text = helpers.cycled_input("Enter text:", str, lambda v: len(v) > 0)
    word_length = helpers.input_int("Enter word length:", helpers.natural_only)

    words = text.split(SEPARATOR)
    for i in range(0, len(words)):
        if len(words[i]) == word_length:
            for char in CHARS_TO_REMOVE:
                words[i] = words[i].replace(char, "")

    print("Res:", SEPARATOR.join(words))
