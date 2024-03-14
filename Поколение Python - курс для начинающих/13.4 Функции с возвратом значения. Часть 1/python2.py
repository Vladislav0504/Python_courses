"""Functions."""


def get_days(month: int) -> int:
    """Days in month."""
    days = (28, 31, 30)
    if month == 2:
        return days[0]
    if month & 1 and month < 8 or month & 1 == 0 and month > 7:
        return days[1]
    return days[2]


def main():
    """My function."""
    num = int(input())
    print(get_days(num))


if __name__ == "__main__":
    main()
