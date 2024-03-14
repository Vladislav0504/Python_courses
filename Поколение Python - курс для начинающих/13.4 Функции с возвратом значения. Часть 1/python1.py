"""Functions."""


def convert_to_miles(kilometers: int) -> float:
    """Convert kilometers to miles."""
    ratio = 0.6214
    return kilometers * ratio


def main():
    """My function."""
    num = int(input())
    print(convert_to_miles(num))


if __name__ == "__main__":
    main()
