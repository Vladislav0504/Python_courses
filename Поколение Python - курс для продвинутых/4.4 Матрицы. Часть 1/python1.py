"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n, num_m = int(input()), int(input())
    matrix = tuple(tuple(stdin.readline().strip() for _ in range(num_m))
                   for _ in range(num_n))
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
