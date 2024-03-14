"""Fractions module."""
from fractions import Fraction


def main():
    """My function."""
    num_n, result, factorial = int(input()), 0, 1
    for i in range(1, num_n + 1):
        factorial *= i
        result += Fraction(1, factorial)
    print(result)


if __name__ == "__main__":
    main()
