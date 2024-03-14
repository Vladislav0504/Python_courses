"""Fractions module."""
from fractions import Fraction


def main():
    """My function."""
    num_n = int(input())
    temp = num_n >> 1
    if num_n & 1:
        print(Fraction(temp, temp + 1))
    elif temp & 1:
        print(Fraction(temp - 2, temp + 2))
    else:
        print(Fraction(temp - 1, temp + 1))


if __name__ == "__main__":
    main()
