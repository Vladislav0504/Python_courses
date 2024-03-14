"""Exam."""


def main():
    """My function."""
    nums = tuple(map(int, input().split()))
    print(len(nums) - len(set(nums)))


if __name__ == "__main__":
    main()
