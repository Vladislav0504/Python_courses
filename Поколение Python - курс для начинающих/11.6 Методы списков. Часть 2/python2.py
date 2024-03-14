"""Lists."""


def main():
    """My function."""
    nums = list(map(int, input().split()))
    index_1, index_2 = nums.index(min(nums)), nums.index(max(nums))
    nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
    print(*nums)


if __name__ == "__main__":
    main()
