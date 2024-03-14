"""Fractions module."""
from fractions import Fraction


def main():
    """My function."""
    num_n = int(input())
    result = sum(Fraction(1, i**2) for i in range(1, num_n + 1))
    print(result)


if __name__ == "__main__":
    main()
