"""Partition of number."""


def main():
    """My function."""
    nums, divider = list(map(int, input().split())), 12
    print(*((num**2 + 3) // divider for num in nums))


if __name__ == "__main__":
    main()
