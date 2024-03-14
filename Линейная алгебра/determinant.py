"""Determinant."""
from numpy import array, argmax, abs as np_abs, outer, ndarray


def determinant(matrix: ndarray[float], size: int) -> int:
    """Matrix determinant."""
    result = 1
    for row in range(size):
        j_max = argmax(np_abs(matrix[row:, row])) + row
        matrix[j_max], matrix[row] = matrix[row], matrix[j_max].copy()
        i = matrix[:, row] != 0
        i[:row + 1] = False
        matrix[i] -= outer(matrix[i, row] / matrix[row, row], matrix[row])
        if matrix[row, row] == 0:
            return 0
        result *= (-1)**(j_max != row) * matrix[row, row]
    return int(round(result))


def main():
    """My function."""
    num_n = int(input())
    matrix = array([list(map(float, input().split())) for _ in range(num_n)])
    print(determinant(matrix, num_n))


if __name__ == "__main__":
    main()
