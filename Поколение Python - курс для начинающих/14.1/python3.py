"""Exam."""
from math import factorial


def compute_binomial(num_n: int, num_k: int) -> int:
    """Binomial."""
    return factorial(num_n) // factorial(num_k) // factorial(num_n - num_k)


def main():
    """My function."""
    num_n, num_k = int(input()), int(input())
    print(compute_binomial(num_n, num_k))


if __name__ == "__main__":
    main()
