"""Conditions."""


def main():
    """My function."""
    nums = [int(input()) for _ in range(3)]
    print(sum(num for num in nums if num > 0))


if __name__ == "__main__":
    main()
