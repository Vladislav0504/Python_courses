"""Exam."""


def is_magic(date: str) -> bool:
    """Is date magic?."""
    day, month, year = date.split(".")
    return int(day) * int(month) == int(year[-2:])


def main():
    """My function."""
    date = input()
    print(is_magic(date))


if __name__ == "__main__":
    main()
