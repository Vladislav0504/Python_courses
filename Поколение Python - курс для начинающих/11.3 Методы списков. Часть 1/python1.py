"""Lists."""


def main():
    """My function."""
    numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10,
               8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1,
               2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
    nums = (5, 17)
    print(len(numbers), numbers[-1], numbers[::-1], sep="\n")
    print("YES" if nums[0] in numbers and nums[1] in numbers else "NO")
    print(numbers[1:-1])


if __name__ == "__main__":
    main()
