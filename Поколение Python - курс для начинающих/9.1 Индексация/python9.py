"""Strings."""


def main():
    """My function."""
    string = input()
    count = sum(ch_1 == ch_2 for ch_1, ch_2 in zip(string, string[1:]))
    print(count)


if __name__ == "__main__":
    main()
