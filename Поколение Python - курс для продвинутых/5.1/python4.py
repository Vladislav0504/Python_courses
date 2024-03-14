"""Exam."""


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(["."] * num_n for _ in range(num_n))
    for i in range(num_n):
        matrix[i][i] = "*"
        matrix[i][-1 - i] = "*"
        matrix[i][num_n >> 1] = "*"
        matrix[num_n >> 1][i] = "*"
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
