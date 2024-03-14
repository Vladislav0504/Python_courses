"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n, _ = map(int, input().split())
    matrix = tuple(list(map(int, stdin.readline().split()))
                   for _ in range(num_n))
    input()
    for i, line in enumerate(stdin):
        for j, num in enumerate(map(int, line.split())):
            matrix[i][j] += num
        print(*matrix[i])


if __name__ == "__main__":
    main()
