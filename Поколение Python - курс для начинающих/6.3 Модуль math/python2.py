"""Types."""
from math import pi


def main():
    """My function."""
    radius = float(input())
    square, length = pi * radius**2, 2 * pi * radius
    print(square, length, sep="\n")


if __name__ == "__main__":
    main()
