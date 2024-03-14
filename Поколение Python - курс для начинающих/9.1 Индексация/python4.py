"""Strings."""


def main():
    """My function."""
    string = input()
    print(*string[::-1], sep="\n")


if __name__ == "__main__":
    main()
