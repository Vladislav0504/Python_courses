"""Functions."""
from functools import reduce


def evaluate(coefficients: list[int], num_x: int) -> int:
    """Evaluate value of polynomial."""
    return reduce(lambda prev, cur: prev * num_x + cur, coefficients, 0)


def main():
    """My function."""
    coefficients, num_x = list(map(int, input().split())), int(input())
    print(evaluate(coefficients, num_x))


if __name__ == "__main__":
    main()
