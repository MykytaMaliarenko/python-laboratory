import helper

CHARS_TO_REMOVE = ["a", "а"]

text = helper.cycled_input("Enter text:\n", str, lambda v: len(v) > 0)
word_length = helper.cycled_input("Enter word length:\n", int, lambda v: v > 0)

words = text.split()
for i in range(0, len(words)):
    if len(words[i]) == word_length:
        for char in CHARS_TO_REMOVE:
            words[i] = words[i].replace(char, "")

print("Res:\n", ' '.join(words))
