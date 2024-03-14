"""Exam."""
from sys import stdin


def is_latin(matrix: list[tuple[int]]) -> str:
    """Is square latin?."""
    numbers = set(range(1, len(matrix) + 1))
    for row in matrix:
        if set(row) != numbers:
            return "NO"
    for col in zip(*matrix):
        if set(col) != numbers:
            return "NO"
    return "YES"


def main():
    """My function."""
    input()
    matrix = [tuple(map(int, line.split())) for line in stdin]
    print(is_latin(matrix))


if __name__ == "__main__":
    main()
