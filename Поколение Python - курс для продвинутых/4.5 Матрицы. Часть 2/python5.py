"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(list(map(int, line.split())) for line in stdin)
    for i, line in enumerate(matrix):
        line[i], matrix[-i - 1][i] = matrix[-i - 1][i], line[i]
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
