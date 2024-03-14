"""Contest."""


def main():
    """My function."""
    string = input()
    alpha = sum(char.isalpha() for char in string)
    lower = sum(char.islower() for char in string)
    print(string.upper() if lower << 1 < alpha else string.lower())


if __name__ == "__main__":
    main()
