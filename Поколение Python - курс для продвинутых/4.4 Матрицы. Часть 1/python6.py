"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    maximum = matrix[0][0]
    for i, row in enumerate(matrix):
        maximum = max(maximum, *row[:min(i + 1, num_n - i)])
        maximum = max(maximum, *row[max(i, num_n - 1 - i):])
    print(maximum)


if __name__ == "__main__":
    main()
