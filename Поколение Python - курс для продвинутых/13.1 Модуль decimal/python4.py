"""Decimal module."""
from decimal import Decimal


def main():
    """My function."""
    num_d = Decimal(input())
    result = sum(getattr(num_d, f)() for f in ("exp", "ln", "log10", "sqrt"))
    print(result)


if __name__ == "__main__":
    main()
