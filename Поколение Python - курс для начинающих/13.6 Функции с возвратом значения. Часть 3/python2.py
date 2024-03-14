"""Functions."""
from math import pi


def get_circle(radius: float) -> (float, float):
    """Length of circumference and square of circle."""
    return 2 * pi * radius, pi * radius**2


def main():
    """My function."""
    radius = float(input())
    length, square = get_circle(radius)
    print(length, square)


if __name__ == "__main__":
    main()
