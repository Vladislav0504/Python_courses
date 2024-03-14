"""Exam."""


def main():
    """My function."""
    print(*sorted(input().split(), key=str.lower))


if __name__ == "__main__":
    main()
