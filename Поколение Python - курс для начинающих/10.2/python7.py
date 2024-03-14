"""Exam."""


def main():
    """My function."""
    string = input()
    print(*(char for i, char in enumerate(string) if i % 3), sep="")


if __name__ == "__main__":
    main()
