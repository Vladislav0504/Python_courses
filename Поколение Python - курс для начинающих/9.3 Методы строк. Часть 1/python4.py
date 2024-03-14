"""Strings."""


def main():
    """My function."""
    string = input()
    count = sum(char != char.upper() for char in string)
    print(count)


if __name__ == "__main__":
    main()
