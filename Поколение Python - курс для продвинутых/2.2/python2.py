"""Repetition."""


def main():
    """My function."""
    numbers = tuple(map(int, input().split()))
    count = sum(num_1 > num_2 for num_1, num_2 in zip(numbers[1:], numbers))
    print(count)


if __name__ == "__main__":
    main()
