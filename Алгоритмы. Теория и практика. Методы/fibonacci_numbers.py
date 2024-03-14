"""Fibonacci numbers."""
from numpy import array, dot, ndarray


def binary_power(matrix: ndarray[int], deg: int) -> ndarray[int]:
    """Binary raising to power."""
    result = array([[1, 0], [0, 1]])
    while deg:
        if deg & 1:
            result = dot(result, matrix)
        matrix = dot(matrix, matrix)
        deg >>= 1
    return result


def fibonacci(num_n: int) -> int:
    """Fibonacci number."""
    return binary_power(array([[0, 1], [1, 1]]), num_n)[0][1]


def main():
    """My function."""
    num_n = int(input())
    print(fibonacci(num_n))


if __name__ == "__main__":
    main()
