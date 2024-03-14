"""Repetition."""


def main():
    """My function."""
    nums = tuple(map(int, input().split()))
    count = 1 + sum(num_1 != num_2 for num_1, num_2 in zip(nums, nums[1:]))
    print(count)


if __name__ == "__main__":
    main()
