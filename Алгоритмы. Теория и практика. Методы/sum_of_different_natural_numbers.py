"""Greedy algorithms."""


def main():
    """My function."""
    num_n = int(input())
    num_k = int((1 + (num_n << 3))**0.5) - 1 >> 1
    print(num_k)
    print(*range(1, num_k), end=" ")
    print(num_n - (num_k * (num_k - 1) >> 1))


if __name__ == "__main__":
    main()
