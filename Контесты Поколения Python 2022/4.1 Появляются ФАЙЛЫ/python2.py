"""Contest."""


def main():
    """My function."""
    nums = {}
    for num in map(int, input().split()):
        nums[num] = num in nums
    print(*sorted(k for k, v in nums.items() if v))


if __name__ == "__main__":
    main()
