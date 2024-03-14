"""Contest."""


def main():
    """My function."""
    numbers = map(int, input().split())
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    maximum = -1
    for key, value in frequency.items():
        if key == value and key > maximum:
            maximum = key
    print(maximum)


if __name__ == "__main__":
    main()
