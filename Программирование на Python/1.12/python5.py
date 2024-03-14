"""Problems."""


def main():
    """My function."""
    nums = sorted(int(input()) for _ in range(3))
    print(nums[2], nums[0], nums[1], sep="\n")


if __name__ == "__main__":
    main()
