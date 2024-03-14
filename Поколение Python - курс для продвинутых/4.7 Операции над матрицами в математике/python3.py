"""Matrices."""


def multiply(matrix_1: list[list[int]],
             matrix_2: list[list[int]]) -> list[list[int]]:
    """Matrix multiplication."""
    num_n, num_k, num_m = len(matrix_1), len(matrix_2), len(matrix_2[0])
    result = [[0] * num_m for _ in range(num_n)]
    for i, row in enumerate(result):
        for j in range(num_m):
            row[j] = sum(matrix_1[i][k] * matrix_2[k][j] for k in range(num_k))
    return result


def main():
    """My function."""
    num_n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num_n)]
    num_m = int(input())
    result = [[0] * num_n for _ in range(num_n)]
    for i, line in enumerate(result):
        line[i] = 1
    for _ in range(num_m):
        result = multiply(result, matrix)
    for row in result:
        print(*row)


if __name__ == "__main__":
    main()
