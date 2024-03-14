"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    trace = sum(row[i] for i, row in enumerate(matrix))
    print(trace)


if __name__ == "__main__":
    main()
