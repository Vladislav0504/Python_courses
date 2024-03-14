"""Exam."""


def main():
    """My function."""
    numbers = input().split()
    result = sum(map(int, numbers))
    print("+".join(numbers), end=f"={result}")


if __name__ == "__main__":
    main()
