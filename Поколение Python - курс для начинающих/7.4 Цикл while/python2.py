"""Loops."""


def main():
    """My function."""
    string = input()
    while string not in ("КОНЕЦ", "конец"):
        print(string)
        string = input()


if __name__ == "__main__":
    main()
