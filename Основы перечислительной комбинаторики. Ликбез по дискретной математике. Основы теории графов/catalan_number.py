"""Catalan number."""


def catalan_mod(num_n: int) -> int:
    """Catalan number modulo 1000000007."""
    result, prime = 1, 1000000007
    for i in range(1, num_n + 1):
        result = ((i << 2) - 2) * result * pow(i + 1, prime - 2, prime) % prime
    return result


def main():
    """My function."""
    num_n = int(input())
    print(catalan_mod(num_n))


if __name__ == "__main__":
    main()
