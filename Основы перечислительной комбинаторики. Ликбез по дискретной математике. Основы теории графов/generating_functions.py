"""Generating functions."""
from numpy import array, dot, ndarray


def binary_power(matrix: ndarray[int], deg: int, mod: int) -> ndarray[int]:
    """Binary raising to power modulo mod."""
    result = array([[1, 0], [0, 1]])
    while deg:
        if deg & 1:
            result = dot(result, matrix) % mod
        matrix = dot(matrix, matrix) % mod
        deg >>= 1
    return result


def fibonacci(num_n: int, mod: int) -> int:
    """Fibonacci number modulo mod."""
    return binary_power(array([[0, 1], [1, 1]]), num_n, mod)[0][1]


def main():
    """My function."""
    num_n, prime = int(input()), 1000000007
    if num_n == 0:
        print(1)
    else:
        print(fibonacci(num_n << 1, prime))


if __name__ == "__main__":
    main()
