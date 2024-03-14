"""Lists."""


def main():
    """My function."""
    numbers = {}
    for num in map(int, input().split()):
        numbers[num] = num in numbers
    print(*(key for key, value in numbers.items() if value), sep=" ")


if __name__ == "__main__":
    main()
