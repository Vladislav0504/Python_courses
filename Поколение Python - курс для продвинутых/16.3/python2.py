"""Exam."""
from functools import reduce


def product_of_odds(data: list[int]) -> int:
    """Product of odds."""
    return reduce(lambda x, y: x * y, filter(lambda x: x & 1, data), 1)


def main():
    """My function."""
    assert product_of_odds([2, 3]) == 3


if __name__ == "__main__":
    main()
