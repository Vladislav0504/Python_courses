"""Fractions module."""
from fractions import Fraction


def main():
    """My function."""
    num_m, num_n = int(input()), int(input())
    fraction = Fraction(num_m, num_n)
    print(fraction)


if __name__ == "__main__":
    main()
