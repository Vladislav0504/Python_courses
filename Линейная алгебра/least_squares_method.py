"""Least squares method.

Good program.
"""
from numpy import (array, dot, concatenate, argmax, abs as np_abs, append,
                   outer, ndarray)
EPSILON = 1e-12


def change(matrix: ndarray[float], num_n: int, num_m: int) -> ndarray[int]:
    """Matrix change."""
    row, where = 0, array([-2] * num_m)
    for col in range(num_m):
        j_max = argmax(np_abs(matrix[row:, col])) + row
        if np_abs(matrix[j_max, col]) > EPSILON:
            matrix[j_max], matrix[row] = matrix[row], matrix[j_max].copy()
            i = matrix[:, col] != 0
            i[row] = False
            matrix[i] -= outer(matrix[i, col] / matrix[row, col], matrix[row])
            where[col] = row
            row += 1
            if row == num_n:
                break
    return where


def answer(matrix: ndarray[float],
           where: ndarray[int]) -> (str, ndarray[float]):
    """Answer."""
    result = array([0.0] * (matrix[0].size - 1))
    i = where != -2
    end = False
    result[i] = matrix[where[i], -1] / matrix[where[i], append(i, end)]
    if (np_abs(dot(matrix[:, :-1], result) - matrix[:, -1]) > EPSILON).any():
        return "NO", result
    if (where == -2).any():
        return "INF", result
    return "YES", result


def gauss(matrix: ndarray[float]) -> (str, ndarray[float]):
    """Gauss method to solve system of linear algebraic equations."""
    where = change(matrix, matrix.shape[0], matrix.shape[1] - 1)
    return answer(matrix, where)


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = array([list(map(float, input().split())) for _ in range(num_n)])
    matrix_x, vector_y = matrix[:, :num_m], matrix[:, num_m:]
    matrix_a, vector_b = dot(matrix_x.T, matrix_x), dot(matrix_x.T, vector_y)
    matrix = concatenate([matrix_a, vector_b], axis=1)
    print(*gauss(matrix)[1])


if __name__ == "__main__":
    main()
