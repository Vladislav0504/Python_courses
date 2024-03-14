"""Matrices."""


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple([0] * num_n for _ in range(num_n))
    for i, row in enumerate(matrix):
        row[i] = 1
        row[-1 - i] = 1
        print(*row, sep="  ")


if __name__ == "__main__":
    main()
