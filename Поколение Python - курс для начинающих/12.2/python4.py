"""Exam."""


def main():
    """My function."""
    numbers = input().split("-")
    if numbers[0] == "7":
        numbers = numbers[1:]
    lengths = list(map(len, numbers))
    is_digits = all(num.isdigit() for num in numbers)
    print("YES" if lengths == [3, 3, 4] and is_digits else "NO")


if __name__ == "__main__":
    main()
