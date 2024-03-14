"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(line.strip().split() for line in stdin)
    matrix_2 = tuple(tuple(matrix[-1 - j][i] for j in range(num_n))
                     for i in range(num_n))
    for row in matrix_2:
        print(*row)


if __name__ == "__main__":
    main()
