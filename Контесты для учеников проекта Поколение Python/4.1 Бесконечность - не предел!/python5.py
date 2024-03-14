"""Contest."""


def main():
    """My function."""
    string = input()
    result = ["" if char.isalpha() else char for char in string]
    index = len(result) - 1
    for char in string:
        while index != -1 and result[index]:
            index -= 1
        if char.isalpha():
            result[index] = char
            index -= 1
    print("".join(result))


if __name__ == "__main__":
    main()
