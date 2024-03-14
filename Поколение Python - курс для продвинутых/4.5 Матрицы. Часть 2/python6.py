"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = [tuple(map(int, line.split())) for line in stdin]
    matrix.reverse()
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
