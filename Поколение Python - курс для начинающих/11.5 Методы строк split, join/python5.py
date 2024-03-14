"""Lists."""


def main():
    """My function."""
    nums, limit = input().split("."), (0, 255)
    print("ДА" if all(limit[0] <= int(k) <= limit[1] for k in nums) else "НЕТ")


if __name__ == "__main__":
    main()
