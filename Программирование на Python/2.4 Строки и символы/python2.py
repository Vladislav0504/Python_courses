"""Strings."""


def main():
    """My function."""
    string = f"{input()} "
    count, cur = 0, string[0]
    for char in string:
        if cur != char:
            print(f"{cur}{count}", end="")
            count, cur = 0, char
        count += 1


if __name__ == "__main__":
    main()
