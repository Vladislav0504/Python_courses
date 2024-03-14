"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = tuple(["."] * num_m for _ in range(num_n))
    for i, row in enumerate(matrix):
        for j in range(i - 1 & 1, num_m, 2):
            row[j] = "*"
        print(*row)


if __name__ == "__main__":
    main()
