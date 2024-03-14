"""Contest."""


def main():
    """My function."""
    num_k = int(input())
    num_n = int((1 + (num_k << 3))**0.5) + 1 >> 1
    print("".join(f"{i} " * i for i in range(1, num_n)), end="")
    print(f"{num_n} " * (num_k - (num_n * (num_n - 1) >> 1)))


if __name__ == "__main__":
    main()
