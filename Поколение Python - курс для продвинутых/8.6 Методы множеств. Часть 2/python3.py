"""Sets."""


def main():
    """My function."""
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    difference = sorted(nums_1 - nums_2)
    print(*difference)


if __name__ == "__main__":
    main()
