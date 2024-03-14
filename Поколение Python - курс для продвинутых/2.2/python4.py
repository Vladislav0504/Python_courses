"""Repetition."""


def main():
    """My function."""
    numbers = input().split()
    numbers.insert(0, numbers.pop())
    print(*numbers)


if __name__ == "__main__":
    main()
