"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    print(*("*" * min(i + 1, num_n - i) for i in range(num_n)), sep="\n")


if __name__ == "__main__":
    main()
