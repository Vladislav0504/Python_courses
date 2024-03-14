"""Types."""


def main():
    """My function."""
    fahrenheit, nums = float(input()), (5, 32, 9)
    print(nums[0] * (fahrenheit - nums[1]) / nums[2])


if __name__ == "__main__":
    main()
