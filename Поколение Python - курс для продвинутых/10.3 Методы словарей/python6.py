"""Dictionaries."""


def main():
    """My function."""
    text, words = input(), {}
    my_text = text.lower()
    for char in ".,!?:;-":
        my_text = my_text.replace(char, " ")
    for word in my_text.split():
        words[word] = words.get(word, 0) + 1
    key, _ = min(words.items(), key=lambda pair: pair[::-1])
    print(key)


if __name__ == "__main__":
    main()
