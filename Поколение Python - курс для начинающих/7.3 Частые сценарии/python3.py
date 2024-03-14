"""Loops."""
from math import log


def main():
    """My function."""
    num_n = int(input())
    print(sum(1 / i for i in range(1, num_n + 1)) - log(num_n))


if __name__ == "__main__":
    main()
