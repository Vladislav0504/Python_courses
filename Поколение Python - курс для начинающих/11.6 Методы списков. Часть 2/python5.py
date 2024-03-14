"""Lists."""


def main():
    """My function."""
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(*numbers)
    numbers.sort(reverse=True)
    print(*numbers)


if __name__ == "__main__":
    main()
