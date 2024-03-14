"""Exam."""


def main():
    """My function."""
    time = 17
    print("*" * time)
    print("*", "*", sep=" " * (time - 2))
    print("*", "*", sep=" " * (time - 2))
    print("*" * time)


if __name__ == "__main__":
    main()
