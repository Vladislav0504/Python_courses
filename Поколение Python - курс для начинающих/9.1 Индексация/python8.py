"""Strings."""


def main():
    """My function."""
    string, count = input(), {"+": 0, "*": 0}
    for char in string:
        if char in "+*":
            count[char] += 1
    print(*(f"Символ {k} встречается {v} раз" for k, v in count.items()),
          sep="\n")


if __name__ == "__main__":
    main()
