"""Dictionaries."""


def main():
    """My function."""
    dictionary = {}
    for word in input().lower().split():
        dictionary[word] = dictionary.get(word, 0) + 1
    print(*(f"{key} {value}" for key, value in dictionary.items()), sep="\n")


if __name__ == "__main__":
    main()
