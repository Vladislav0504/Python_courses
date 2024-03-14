"""Contest."""


def main():
    """My function."""
    nums, num_n = list(map(int, input().split())), int(input())
    num_n %= len(nums)
    result = nums[-num_n:] + nums[:-num_n]
    print(*result)


if __name__ == "__main__":
    main()
