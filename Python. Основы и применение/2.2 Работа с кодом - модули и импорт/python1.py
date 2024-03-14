"""Modules and import."""
from datetime import date, timedelta


def main():
    """My function."""
    year, month, day = map(int, input().split())
    data = date(year, month, day) + timedelta(days=int(input()))
    print(data.year, data.month, data.day)


if __name__ == "__main__":
    main()
