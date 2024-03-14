"""Functions."""


def print_digit_sum(num: int) -> None:
    """Sum of number digits."""
    print(sum(map(int, str(num))))


def main():
    """My function."""
    num = int(input())
    print_digit_sum(num)


if __name__ == "__main__":
    main()
