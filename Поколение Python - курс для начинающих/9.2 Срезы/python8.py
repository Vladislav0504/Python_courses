"""Strings."""


def main():
    """My function."""
    string = input()
    index = len(string) + 1 >> 1
    print(string[index:] + string[:index])


if __name__ == "__main__":
    main()
