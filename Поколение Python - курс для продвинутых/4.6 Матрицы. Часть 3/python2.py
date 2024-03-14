"""Matrices."""


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple([0] * num_n for _ in range(num_n))
    for i, row in enumerate(matrix):
        row[-i - 1] = 1
        for j in range(num_n - i, num_n):
            row[j] = 2
        print(*row)


if __name__ == "__main__":
    main()
