"""Sets."""


def main():
    """My function."""
    nums_1 = set(map(int, input().split()))
    nums_2 = set(map(int, input().split()))
    intersection = nums_1 & nums_2
    print(len(intersection))


if __name__ == "__main__":
    main()
