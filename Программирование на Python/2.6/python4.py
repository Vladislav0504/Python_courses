"""Problems."""


def main():
    """My function."""
    mat, line = [], input()
    while line != "end":
        mat.append(tuple(map(int, line.split())))
        line = input()
    rows, cols = len(mat), len(mat[0])
    res = tuple([0] * cols for _ in range(rows))
    for i, row in enumerate(mat):
        for j in range(cols):
            res[i][j] = (mat[i - 1][j] + mat[i + 1 - rows][j]
                         + row[j - 1] + row[j + 1 - cols])
        print(*res[i])


if __name__ == "__main__":
    main()
