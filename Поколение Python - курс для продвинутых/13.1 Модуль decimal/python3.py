"""Decimal module."""
from decimal import Decimal


def main():
    """My function."""
    num = Decimal(input())
    num_tuple = num.as_tuple()
    digits = list(num_tuple.digits)
    if len(digits) == -num_tuple.exponent:
        digits.append(0)
    print(max(digits) + min(digits))


if __name__ == "__main__":
    main()
