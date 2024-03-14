"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    input()
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    max_i, max_j = 0, 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if matrix[max_i][max_j] < elem:
                max_i, max_j = i, j
    print(max_i, max_j)


if __name__ == "__main__":
    main()
