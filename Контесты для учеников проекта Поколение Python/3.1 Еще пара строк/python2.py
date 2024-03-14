"""Contest."""


def main():
    """My function."""
    numbers = list(map(int, input().split()))
    index = 0
    for i, num in enumerate(numbers):
        if num:
            numbers[i] = 0
            numbers[index] = num
            index += 1
    print(*numbers)


if __name__ == "__main__":
    main()
