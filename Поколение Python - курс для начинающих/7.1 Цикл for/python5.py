"""Loops."""


def main():
    """My function."""
    string = input()
    print(*(f"{i} {string}" for i in range(10)), sep="\n")


if __name__ == "__main__":
    main()
