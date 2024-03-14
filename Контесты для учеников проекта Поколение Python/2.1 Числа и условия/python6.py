"""Contest."""


def main():
    """My function."""
    n_0 = int(input())
    result = ((1 + n_0) * n_0 >> 1) - sum(int(input()) for _ in range(n_0 - 1))
    print(result)


if __name__ == "__main__":
    main()
