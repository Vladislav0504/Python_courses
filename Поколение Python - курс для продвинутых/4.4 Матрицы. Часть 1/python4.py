"""Matrices."""
from sys import stdin, stdout


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    for row in matrix:
        mean = sum(row) / num_n
        count = sum(elem > mean for elem in row)
        stdout.write(f"{count}\n")


if __name__ == "__main__":
    main()
