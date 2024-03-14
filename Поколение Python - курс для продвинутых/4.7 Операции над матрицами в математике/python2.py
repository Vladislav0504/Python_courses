"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n, _ = map(int, input().split())
    matrix_1 = tuple(tuple(map(int, stdin.readline().split()))
                     for _ in range(num_n))
    input()
    num_m, num_k = map(int, input().split())
    matrix_2 = tuple(tuple(map(int, line.split())) for line in stdin)
    matrix = tuple([0] * num_k for _ in range(num_n))
    for i, row in enumerate(matrix):
        for j in range(num_k):
            row[j] = sum(matrix_1[i][k] * matrix_2[k][j] for k in range(num_m))
        print(*row)


if __name__ == "__main__":
    main()
