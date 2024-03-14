"""Strings."""


def main():
    """My function."""
    string = input()
    index_1, index_2 = string.find("h"), string.rfind("h")
    print(string[:index_1] + string[index_2 + 1:])


if __name__ == "__main__":
    main()
