"""Types."""
from math import tan, pi


def main():
    """My function."""
    num_n, num_a = int(input()), float(input())
    square = num_n * num_a**2 / (4 * tan(pi / num_n))
    print(square)


if __name__ == "__main__":
    main()
