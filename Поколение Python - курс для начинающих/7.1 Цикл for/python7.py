"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    print(*("*" * i for i in range(num_n, 0, -1)), sep="\n")


if __name__ == "__main__":
    main()
