"""Conditions."""


def main():
    """My function."""
    month, days = int(input()), (28, 31, 30)
    if month == 2:
        print(days[0])
    elif month & 1 and month < 8 or month & 1 == 0 and month > 7:
        print(days[1])
    else:
        print(days[2])


if __name__ == "__main__":
    main()
