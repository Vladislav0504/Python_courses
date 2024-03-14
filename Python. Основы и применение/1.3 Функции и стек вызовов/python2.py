"""Functions."""


def coefficient(num_n: int, num_k: int) -> int:
    """Binomial coefficient."""
    if num_n < num_k:
        return 0
    num_k = min(num_k, num_n - num_k)
    diff, result = num_n - num_k, 1
    for i in range(1, num_k + 1):
        result *= diff + i
        result //= i
    return result


def main():
    """My function."""
    num_n, num_k = map(int, input().split())
    print(coefficient(num_n, num_k))


if __name__ == "__main__":
    main()
