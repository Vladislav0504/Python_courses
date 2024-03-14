"""Exam."""
from sys import stdin


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(line.strip().split() for line in stdin)
    for i, row in enumerate(matrix):
        for j in range(i + 1, num_n):
            row[j], matrix[j][i] = matrix[j][i], row[j]
        print(*row)


if __name__ == "__main__":
    main()
