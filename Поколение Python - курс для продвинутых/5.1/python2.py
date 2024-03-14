"""Exam."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    maximum = matrix[0][-1]
    for i, row in enumerate(matrix, 1):
        maximum = max(maximum, *row[-i:])
    print(maximum)


if __name__ == "__main__":
    main()
