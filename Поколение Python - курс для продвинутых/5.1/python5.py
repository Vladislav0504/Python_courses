"""Exam."""
from sys import stdin


def main():
    """My function."""
    input()
    matrix = tuple(tuple(line.strip().split()) for line in stdin)
    for i, row in enumerate(matrix, 1):
        if any(row[j] != matrix[-j - 1][-i] for j in range(len(matrix) - i)):
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
