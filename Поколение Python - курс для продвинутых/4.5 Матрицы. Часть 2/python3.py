"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n, _ = int(input()), int(input())
    matrix = tuple(stdin.readline().strip().split() for _ in range(num_n))
    num_i, num_j = map(int, input().split())
    for row in matrix:
        row[num_i], row[num_j] = row[num_j], row[num_i]
        print(*row)


if __name__ == "__main__":
    main()
