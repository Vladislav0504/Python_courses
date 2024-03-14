"""Lists."""


def main():
    """My function."""
    numbers = {}
    for num in map(int, input().split()):
        numbers[num] = numbers.get(num, 0) + 1
    print(sum(k * (k - 1) for k in numbers.values()) >> 1)


if __name__ == "__main__":
    main()
