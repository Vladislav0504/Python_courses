"""Exam."""


def main():
    """My function."""
    num = int(input())
    nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    print(nums[num - 1] if 1 <= num <= 10 else "ошибка")


if __name__ == "__main__":
    main()
