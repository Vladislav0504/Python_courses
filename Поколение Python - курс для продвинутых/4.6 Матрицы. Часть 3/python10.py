"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = tuple([0] * num_m for _ in range(num_n))
    i, j, diff_i, diff_j = 0, 0, 0, 1
    for k in range(1, num_n * num_m + 1):
        matrix[i][j] = k
        if matrix[(i + diff_i) % num_n][(j + diff_j) % num_m]:
            diff_i, diff_j = diff_j, -diff_i
        i += diff_i
        j += diff_j
    for row in matrix:
        print(*(x + " " * (3 - len(x)) for x in map(str, row)), sep="")


if __name__ == "__main__":
    main()
