"""Exam."""


def main():
    """My function."""
    string = input()
    index = string.find("f")
    print(-2 if index == -1 else string.find("f", index + 1))


if __name__ == "__main__":
    main()
