"""Exam."""


def main():
    """My function."""
    print(sum(i for i in map(int, input()) if i & 1 == 0))


if __name__ == "__main__":
    main()
