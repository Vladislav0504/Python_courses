"""Strings."""


def main():
    """My function."""
    string = input()
    print(len(string), string * 3, string[0], string[:3], sep="\n")
    print(string[-3:], string[::-1], string[1:-1], sep="\n")


if __name__ == "__main__":
    main()
