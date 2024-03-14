"""Matrices."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(line.strip().split() for line in stdin)
    for i, row in enumerate(matrix):
        if any(row[j] != matrix[j][i] for j in range(i)):
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
