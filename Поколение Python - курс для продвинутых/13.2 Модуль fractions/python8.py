"""Fractions module."""
from fractions import Fraction

from sys import stdout


def sorted_fractions(num_n: int) -> None:
    """Farey series."""
    fraction_1, fraction_2 = Fraction(0, 1), Fraction(1, num_n)
    while fraction_2.numerator != fraction_2.denominator:
        k = (num_n + fraction_1.denominator) // fraction_2.denominator
        numerator = k * fraction_2.numerator - fraction_1.numerator
        denominator = k * fraction_2.denominator - fraction_1.denominator
        fraction_1, fraction_2 = fraction_2, Fraction(numerator, denominator)
        stdout.write(f"{fraction_1}\n")


def main():
    """My function."""
    num_n = int(input())
    sorted_fractions(num_n)


if __name__ == "__main__":
    main()
