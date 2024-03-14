"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    maximum = max(max(row[:i + 1]) for i, row in enumerate(matrix))
    print(maximum)


if __name__ == "__main__":
    main()
