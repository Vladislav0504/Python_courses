"""Conditions."""


def main():
    """My function."""
    num_1, num_2, num_3 = (int(input()) for _ in range(3))
    nums = sorted((num_1, num_2, num_3))
    print(nums[1])


if __name__ == "__main__":
    main()
