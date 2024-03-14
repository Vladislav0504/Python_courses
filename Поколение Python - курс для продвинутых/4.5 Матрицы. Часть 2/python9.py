"""Matrices."""
from sys import stdin


def is_magic(matrix: list[list[int]], num: int) -> str:
    """Is square magic?."""
    total_1 = sum(row[i] for i, row in enumerate(matrix))
    total_2 = sum(row[-i - 1] for i, row in enumerate(matrix))
    if set(sum(matrix, [])) != set(range(1, num**2 + 1)) or total_1 != total_2:
        return "NO"
    for col in zip(*matrix):
        if total_1 != sum(col):
            return "NO"
    for row in matrix:
        if total_1 != sum(row):
            return "NO"
    return "YES"


def main():
    """My function."""
    num_n = int(input())
    matrix = [list(map(int, line.split())) for line in stdin]
    print(is_magic(matrix, num_n))


if __name__ == "__main__":
    main()
