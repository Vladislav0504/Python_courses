"""Matrices."""


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple([1] * num_n for _ in range(num_n))
    for i, row in enumerate(matrix):
        for j_1 in range(0, min(i, num_n - 1 - i)):
            row[j_1] = 0
        for j_2 in range(max(i + 1, num_n - i), num_n):
            row[j_2] = 0
        print(*row, sep="  ")


if __name__ == "__main__":
    main()
