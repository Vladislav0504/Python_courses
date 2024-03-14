"""Loops."""


def main():
    """My function."""
    num_m, num_n = int(input()), int(input())
    print(*range(num_m - 1 + (num_m & 1), num_n - 1, -2), sep="\n")


if __name__ == "__main__":
    main()
