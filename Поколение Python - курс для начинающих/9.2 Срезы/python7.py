"""Strings."""


def main():
    """My function."""
    string = input()
    print(string[2], string[-2], string[:5], string[:-2], sep="\n")
    print(string[::2], string[1::2], string[::-1], string[::-2], sep="\n")


if __name__ == "__main__":
    main()
