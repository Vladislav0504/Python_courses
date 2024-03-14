"""Fractions module."""
from fractions import Fraction


def main():
    """My function."""
    fraction_0, fraction_1 = input(), input()
    signs = ("+", "-", "*", "/")
    fraction = (Fraction(fraction_0), Fraction(fraction_1))
    results = (fraction[0] + fraction[1], fraction[0] - fraction[1],
               fraction[0] * fraction[1], fraction[0] / fraction[1])
    print(*(f"{fraction_0} {sign} {fraction_1} = {result}"
            for sign, result in zip(signs, results)), sep="\n")


if __name__ == "__main__":
    main()
